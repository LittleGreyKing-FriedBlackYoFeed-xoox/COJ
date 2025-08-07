from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Q
from django.utils import timezone
from django.core.cache import cache
import json
import datetime
import random

from own_models.models import Problem, CustomUser
from own_models.student_practice import Submission, TestCase, TestCaseResult, StudentStatistics
from django.views.decorators.cache import cache_page

# Student problem list page
@cache_page(60 * 5)  # 缓存5分钟
def student_problem_list(request):
    # 检查用户是否已登录且是学生或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    # 获取当前用户
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # 获取查询参数
    problem_type = request.GET.get('problem_type', '')
    difficulty = request.GET.get('difficulty', '')
    status = request.GET.get('status', '')
    search = request.GET.get('search', '')
    
    # 尝试从缓存获取题目列表
    # 添加时间戳确保每次都获取最新数据
    import time
    cache_key = f'problems_list_{problem_type}_{difficulty}_{search}_{int(time.time()/300)}'
    problems = cache.get(cache_key)
    
    if problems is None:
        # 缓存未命中，从数据库获取
        problems = Problem.objects.all().select_related('created_by')
        
        # 应用筛选条件
        if problem_type:
            problems = problems.filter(problem_type=problem_type)
        
        if difficulty:
            problems = problems.filter(difficulty=difficulty)
        
        if search:
            problems = problems.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        
        # 缓存结果，有效期30分钟
        cache.set(cache_key, problems, 60 * 30)
    
    # 获取用户的提交记录来确定题目状态 - 这部分不缓存，因为它是用户特定的
    user_submissions = Submission.objects.filter(user=user).values('problem_id', 'status')
    
    # 使用字典推导式优化
    submission_status = {}
    for sub in user_submissions:
        problem_id = sub['problem_id']
        current_status = submission_status.get(problem_id, 'attempted')
        if sub['status'] == 'accepted' or current_status == 'solved':
            submission_status[problem_id] = 'solved'
        else:
            submission_status[problem_id] = 'attempted'
    
    # 为每个题目添加状态信息 - 使用列表推导式优化
    problem_list = [{
        'id': problem.id,
        'title': problem.title,
        'problem_type': problem.problem_type,
        'difficulty': problem.difficulty,
        'submission_count': problem.submission_count,
        'accepted_count': problem.accepted_count,
        'status': submission_status.get(problem.id, 'unsolved')
    } for problem in problems]
    
    # 根据状态筛选
    if status:
        problem_list = [p for p in problem_list if p['status'] == status]
    
    # 分页
    paginator = Paginator(problem_list, 20)
    page_number = request.GET.get('page')
    problems_page = paginator.get_page(page_number)
    
    # 获取用户统计数据 - 使用缓存
    stats_cache_key = f'user_stats_{user.id}'
    user_stats = cache.get(stats_cache_key)
    
    if user_stats is None:
        user_stats, created = StudentStatistics.objects.get_or_create(user=user)
        if created or not user_stats.last_updated or (timezone.now() - user_stats.last_updated).days > 0:
            user_stats.update_statistics()
        cache.set(stats_cache_key, user_stats, 60 * 15)  # 缓存15分钟
    
    # 计算未解决的题目数量
    total_problems = len(problem_list)
    unsolved_count = total_problems - user_stats.total_problems_solved
    
    # 计算百分比统计
    if total_problems > 0:
        solved_percentage = round((user_stats.total_problems_solved / total_problems) * 100, 1)
        attempted_percentage = round((user_stats.total_problems_attempted / total_problems) * 100, 1)
        unsolved_percentage = round((unsolved_count / total_problems) * 100, 1)
    else:
        solved_percentage = attempted_percentage = unsolved_percentage = 0
    
    return render(request, 'student_practice/problem_list.html', {
        'problems': problems_page,
        'request': request,
        'user_stats': user_stats,
        'unsolved_count': unsolved_count,
        'solved_percentage': solved_percentage,
        'attempted_percentage': attempted_percentage,
        'unsolved_percentage': unsolved_percentage
    })

# 学生题目详情页面
def student_problem_detail(request, problem_id):
    # 检查用户是否已登录且是学生或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    try:
        # 获取题目 - 使用缓存
        cache_key = f'problem_detail_{problem_id}'
        problem = cache.get(cache_key)
        
        if problem is None:
            problem = get_object_or_404(Problem, id=problem_id, is_active=True)
            cache.set(cache_key, problem, 60 * 30)  # 缓存30分钟
        
        # 获取当前用户
        user_id = request.session.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        
        # 获取用户对该题目的提交记录 - 使用缓存减少数据库查询
        submissions_cache_key = f'user_{user_id}_problem_{problem_id}_submissions'
        submissions = cache.get(submissions_cache_key)
        
        if submissions is None:
            try:
                # 使用select_related减少数据库查询
                submissions = list(Submission.objects.filter(
                    user=user, 
                    problem=problem
                ).order_by('-created_at')[:20])  # 只获取最近20条记录并转换为列表
                
                # 缓存结果5分钟
                cache.set(submissions_cache_key, submissions, 60 * 5)
            except Exception as e:
                # 如果查询失败，使用空列表
                submissions = []
                print(f"Error fetching submissions: {str(e)}")
        
        # 获取最后一次提交的代码
        last_code = ""
        if submissions and len(submissions) > 0:
            last_code = submissions[0].code
        
        # 使用缓存获取统计数据
        stats_cache_key = f'user_{user_id}_problem_{problem_id}_stats'
        submission_stats = cache.get(stats_cache_key)
        
        if submission_stats is None:
            try:
                # 使用聚合查询优化计算
                submission_stats = Submission.objects.filter(
                    user=user,
                    problem=problem
                ).aggregate(
                    total=Count('id'),
                    accepted=Count('id', filter=Q(status='accepted'))
                )
                
                # 缓存结果10分钟
                cache.set(stats_cache_key, submission_stats, 60 * 10)
            except Exception as e:
                # 如果查询失败，使用默认值
                submission_stats = {'total': 0, 'accepted': 0}
                print(f"Error fetching submission stats: {str(e)}")
        
        total_submissions = submission_stats.get('total', 0)
        accepted_count = submission_stats.get('accepted', 0)
        
        # 计算通过率
        if problem.submission_count > 0:
            problem_pass_rate = (problem.accepted_count / problem.submission_count) * 100
        else:
            problem_pass_rate = 0
        
        # 计算用户对该题目的通过率
        user_pass_rate = 0
        if total_submissions > 0:
            user_pass_rate = (accepted_count / total_submissions) * 100
        
        # 添加英文题型文本属性
        problem_type_map = {
            1: 'Multiple Choice',
            2: 'Fill in the Blank',
            3: 'True/False',
            4: 'Programming',
            5: 'Short Answer'
        }
        setattr(problem, 'problem_type_text', problem_type_map.get(problem.problem_type, 'Unknown'))
        return render(request, 'student_practice/problem_detail.html', {
            'problem': problem,
            'submissions': submissions,
            'last_code': last_code,
            'accepted_count': accepted_count,
            'problem_pass_rate': problem_pass_rate,
            'user_pass_rate': user_pass_rate
        })
    
    except Exception as e:
        # Log error and return friendly error page
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in student_problem_detail: {str(e)}")
        
        # 返回错误页面
        return render(request, 'error.html', {
            'error_message': 'Error loading problem details, please try again later.',
            'error_details': str(e) if DEBUG else None
        })

# Student code submission
def student_submit_solution(request, problem_id):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
    # 检查用户是否已登录且是学生或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return JsonResponse({'success': False, 'message': 'User not logged in or insufficient permissions'})
    
    # 获取题目
    problem = get_object_or_404(Problem, id=problem_id, is_active=True)
    
    # 获取当前用户
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # 获取提交数据
    code = request.POST.get('code', '').strip()
    language = request.POST.get('language', '')
    
    # 验证数据
    if not code:
        return JsonResponse({'success': False, 'message': 'Code cannot be empty'})
    
    if not language:
        return JsonResponse({'success': False, 'message': 'Please select a programming language'})
    
    try:
        with transaction.atomic():
            # 创建提交记录
            submission = Submission.objects.create(
                user=user,
                problem=problem,
                code=code,
                language=language,
                status='pending'
            )
            
            # Simulate code evaluation (in a real project, this should call an actual evaluation system)
            # Here we randomly generate evaluation results for demonstration
            import time
            time.sleep(1)  # Simulate evaluation time
            
            # Randomly generate evaluation results
            statuses = ['accepted', 'wrong_answer', 'time_limit_exceeded', 'runtime_error']
            weights = [0.6, 0.25, 0.1, 0.05]  # 60% pass rate
            result_status = random.choices(statuses, weights=weights)[0]
            
            # 更新提交结果
            submission.status = result_status
            submission.execution_time = random.randint(50, 2000)
            submission.memory_used = random.randint(1024, 65536)
            
            if result_status != 'accepted':
                error_messages = {
                    'wrong_answer': 'Wrong Answer: Output does not match expected result',
                    'time_limit_exceeded': 'Time Limit Exceeded: Program execution time exceeds limit',
                    'runtime_error': 'Runtime Error: Exception occurred during program execution'
                }
                submission.error_message = error_messages.get(result_status, '未知错误')
            
            submission.save()
            
            # 更新题目统计
            problem.submission_count += 1
            if result_status == 'accepted':
                problem.accepted_count += 1
            problem.save()
            
            # 更新用户统计
            stats, created = StudentStatistics.objects.get_or_create(user=user)
            stats.update_statistics()
            
            return JsonResponse({
                'success': True,
                'message': 'Code submitted successfully',
                'status': result_status,
                'submission_id': submission.id,
                'execution_time': submission.execution_time,
                'memory_used': submission.memory_used,
                'error_message': submission.error_message
            })
            
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Submission failed: {str(e)}'})

# Student submission detail page
def student_submission_detail(request, submission_id):
    # 检查用户是否已登录且是学生或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    # 获取当前用户
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # 获取提交记录（只能查看自己的提交）
    submission = get_object_or_404(Submission, id=submission_id, user=user)
    
    # 获取测试用例结果
    test_results = TestCaseResult.objects.filter(submission=submission)
    
    return render(request, 'student_practice/submission_detail.html', {
        'submission': submission,
        'test_results': test_results
    })


# Student statistics page
@cache_page(60 * 10)  # 缓存10分钟
def student_statistics(request):
    # 检查用户是否已登录且是学生或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    # 获取当前用户
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # 使用缓存获取统计数据
    cache_key = f'user_statistics_{user.id}'
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return render(request, 'student_practice/statistics.html', cached_data)
    
    # 缓存未命中，计算统计数据
    # 获取或创建统计数据
    stats, created = StudentStatistics.objects.get_or_create(user=user)
    if created or not stats.last_updated or (timezone.now() - stats.last_updated).days > 0:
        stats.update_statistics()
    
    # 获取最近的提交记录 - 限制查询数量并包含更多相关数据
    recent_submissions = Submission.objects.filter(user=user).select_related('problem').order_by('-created_at')[:15]
    
    # 使用单个查询获取难度分布数据
    difficulty_stats = Submission.objects.filter(
        user=user,
        status='accepted'
    ).values('problem__difficulty').annotate(count=Count('problem', distinct=True))
    
    difficulty_data = {'easy': 0, 'medium': 0, 'hard': 0}
    for item in difficulty_stats:
        if item['problem__difficulty'] == 1:
            difficulty_data['easy'] = item['count']
        elif item['problem__difficulty'] == 2:
            difficulty_data['medium'] = item['count']
        elif item['problem__difficulty'] == 3:
            difficulty_data['hard'] = item['count']
    
    # Ensure difficulty data has at least some values for chart display
    if difficulty_data['easy'] == 0 and difficulty_data['medium'] == 0 and difficulty_data['hard'] == 0:
        difficulty_data = {'easy': 3, 'medium': 2, 'hard': 1}
    
    # Daily submission data (last 30 days) - optimized date processing
    from datetime import datetime, timedelta
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=29)
    
    # 使用单个查询获取日期统计
    submissions_by_date = Submission.objects.filter(
        user=user,
        created_at__date__gte=start_date,
        created_at__date__lte=end_date
    ).extra({'date': "date(created_at)"}).values('date').annotate(
        total_count=Count('id'),
        accepted_count=Count('id', filter=Q(status='accepted'))
    )
    
    # 初始化日期数据
    daily_submissions = {(start_date + timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(30)}
    daily_accepted = daily_submissions.copy()
    
    # 填充实际数据
    for item in submissions_by_date:
        date_str = item['date'].strftime('%Y-%m-%d')
        daily_submissions[date_str] = item['total_count']
        daily_accepted[date_str] = item['accepted_count']
    
    # Ensure there is some submission data for chart display
    has_data = False
    for value in daily_submissions.values():
        if value > 0:
            has_data = True
            break
    
    if not has_data:
        # Add some sample data
        today = end_date.strftime('%Y-%m-%d')
        yesterday = (end_date - timedelta(days=1)).strftime('%Y-%m-%d')
        two_days_ago = (end_date - timedelta(days=2)).strftime('%Y-%m-%d')
        
        daily_submissions[today] = 5
        daily_submissions[yesterday] = 3
        daily_submissions[two_days_ago] = 4
        
        daily_accepted[today] = 3
        daily_accepted[yesterday] = 2
        daily_accepted[two_days_ago] = 2
    
    # Problem type distribution data - single query retrieval
    problem_type_data = Submission.objects.filter(
        user=user,
        status='accepted'
    ).values('problem__problem_type').annotate(count=Count('problem', distinct=True))
    
    type_distribution = {}
    type_names = dict(Problem.PROBLEM_TYPE_CHOICES)
    for item in problem_type_data:
        problem_type = item['problem__problem_type']
        if problem_type:
            type_distribution[type_names.get(problem_type, str(problem_type))] = item['count']
    
    # If no problem type data, add some sample data for chart display
    if not type_distribution:
        type_distribution = {
            "算法": 5,
            "数据结构": 3,
            "数学": 2,
            "字符串": 4,
            "动态规划": 1
        }
    
    # Calculate success rate
    success_rate = 0
    if stats.total_submissions > 0:
        success_rate = round((stats.accepted_submissions / stats.total_submissions) * 100, 1)
    
    # 使用缓存获取总题目数
    total_problems_cache_key = 'total_active_problems'
    total_problems = cache.get(total_problems_cache_key)
    if total_problems is None:
        total_problems = Problem.objects.filter(is_active=True).count()
        cache.set(total_problems_cache_key, total_problems, 60 * 60)  # 缓存1小时
    
    # Calculate number of untried problems
    untried_problems = total_problems - stats.total_problems_attempted
    
    # Tag distribution data - temporarily using empty dictionary as there is no corresponding table in the database
    tag_distribution = {}
    # Future tag query logic can be added here when the database table is created
    
    # Get consecutive submission days
    consecutive_days = 0
    current_date = end_date
    while current_date >= start_date:
        date_str = current_date.strftime('%Y-%m-%d')
        if daily_submissions.get(date_str, 0) > 0:
            consecutive_days += 1
            current_date -= timedelta(days=1)
        else:
            break
    
    # Get best consecutive submission streak
    best_streak = 0
    current_streak = 0
    for i in range(30):
        date_str = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        if daily_submissions.get(date_str, 0) > 0:
            current_streak += 1
            best_streak = max(best_streak, current_streak)
        else:
            current_streak = 0
    
    context = {
        'stats': {
            'total_problems': total_problems,
            'solved_problems': stats.total_problems_solved,
            'attempted_problems': stats.total_problems_attempted,
            'untried_problems': untried_problems,
            'success_rate': success_rate,
            'total_submissions': stats.total_submissions,
            'accepted_submissions': stats.accepted_submissions,
            'consecutive_days': consecutive_days,
            'best_streak': best_streak,
            'easy_solved': stats.easy_problems_solved,
            'medium_solved': stats.medium_problems_solved,
            'hard_solved': stats.hard_problems_solved
        },
        'recent_submissions': recent_submissions,
        'difficulty_data': json.dumps(difficulty_data),
        'daily_submissions': json.dumps(daily_submissions),
        'daily_accepted': json.dumps(daily_accepted),
        'type_distribution': json.dumps(type_distribution),
        'tag_distribution': json.dumps(tag_distribution)
    }
    
    # 缓存计算结果
    cache.set(cache_key, context, 60 * 5)  # 缓存5分钟
    
    return render(request, 'student_practice/statistics.html', context)


# Return code editing page
def code_editing(request):
    return render(request, 'student_practice/code_editing.html')