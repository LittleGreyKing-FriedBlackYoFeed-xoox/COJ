from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import transaction
from own_models.models import Problem, CustomUser
from django.core.cache import cache

# 获取所有不重复的知识点
def get_knowledge_points():
    # 获取所有不为空的知识点，并去重
    knowledge_points = Problem.objects.exclude(knowledge_point='').values_list('knowledge_point', flat=True).distinct()
    # 转换为列表并排序
    return sorted(list(knowledge_points))

# 题目列表页面
def problemList(request):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
        return redirect('index')
    
    # 获取所有不重复的知识点
    knowledge_points = get_knowledge_points()
    
    return render(request, "problem/problemList.html", {"knowledge_points": knowledge_points})

# 获取题目列表（JSON格式）
def get_problems_json(request):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
        return JsonResponse({"code": 0, "msg": "Insufficient permissions", "count": 0, "data": []})
    
    try:
        # 获取查询参数
        title = request.GET.get('title', '')
        problem_type = request.GET.get('problem_type', '')
        knowledge_point = request.GET.get('knowledge_point', '')
        difficulty = request.GET.get('difficulty', '')
        is_active = request.GET.get('is_active', '')
        
        # 获取分页参数
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        
        # 获取题目列表
        problems = Problem.objects.all().select_related('created_by')
        
        # 应用过滤条件
        if title:
            problems = problems.filter(title__icontains=title)
        
        if problem_type:
            problems = problems.filter(problem_type=int(problem_type))
        
        if knowledge_point:
            problems = problems.filter(knowledge_point=knowledge_point)
        
        if difficulty:
            problems = problems.filter(difficulty=int(difficulty))
        
        if is_active == 'true':
            problems = problems.filter(is_active=True)
        elif is_active == 'false':
            problems = problems.filter(is_active=False)
        
        # 计算总数
        total_count = problems.count()
        
        # 分页
        start = (page - 1) * limit
        end = page * limit
        problems = problems[start:end]
        
        problem_list = []
        
        for problem in problems:
            # 获取难度文本
            difficulty_text = "Unknown"
            if problem.difficulty == 1:
                difficulty_text = "Easy"
            elif problem.difficulty == 2:
                difficulty_text = "Medium"
            elif problem.difficulty == 3:
                difficulty_text = "Hard"
            
            # 获取题型文本
            problem_type_text = ""
            if problem.problem_type == 1:
                problem_type_text = "Multiple Choice"
            elif problem.problem_type == 2:
                problem_type_text = "Fill in the Blank"
            elif problem.problem_type == 3:
                problem_type_text = "True/False"
            elif problem.problem_type == 4:
                problem_type_text = "Programming"
            elif problem.problem_type == 5:
                problem_type_text = "Short Answer"
            
            # 构建题目数据
            problem_data = {
                "id": problem.id,
                "title": problem.title,
                "problem_type": problem.problem_type,
                "problem_type_text": problem_type_text,
                "difficulty": problem.difficulty,
                "difficulty_text": difficulty_text,
                "knowledge_point": problem.knowledge_point or "General",
                "submission_count": problem.submission_count,
                "accepted_count": problem.accepted_count,
                "created_by": problem.created_by.username,
                "created_at": problem.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": problem.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                "is_active": problem.is_active
            }
            
            problem_list.append(problem_data)
        
        # 返回符合Layui表格要求的数据格式
        return JsonResponse({
            "code": 0,  # Layui要求成功状态码为0
            "msg": "",
            "count": total_count,
            "data": problem_list
        })
    except Exception as e:
        return JsonResponse({
            "code": 1,  # 错误状态码
            "msg": str(e),
            "count": 0,
            "data": []
        })

# 添加题目
def addProblem(request):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
        return redirect('index')
    
    # 获取所有不重复的知识点
    knowledge_points = get_knowledge_points()
    
    if request.method == "POST":
        try:
            # 获取基本信息
            title = request.POST.get("title")
            description = request.POST.get("description")
            problem_type = int(request.POST.get("problem_type", 1))
            input_description = request.POST.get("input_description", "")
            output_description = request.POST.get("output_description", "")
            sample_input = request.POST.get("sample_input", "")
            sample_output = request.POST.get("sample_output", "")
            hint = request.POST.get("hint", "")
            difficulty = int(request.POST.get("difficulty", 1))
            knowledge_point = request.POST.get("knowledge_point", "")
            is_active = request.POST.get("is_active") == "on"
            
            # 获取当前用户
            user_id = request.session.get('user_id')
            user = CustomUser.objects.get(id=user_id)
            
            # 创建题目
            with transaction.atomic():
                problem = Problem(
                    title=title,
                    description=description,
                    problem_type=problem_type,
                    input_description=input_description,
                    output_description=output_description,
                    sample_input=sample_input,
                    sample_output=sample_output,
                    hint=hint,
                    difficulty=difficulty,
                    knowledge_point=knowledge_point,
                    is_active=is_active,
                    created_by=user
                )
                problem.save()
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return render(request, "problem/addProblem.html")

# 编辑题目
def editProblem(request, problem_id):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
        return redirect('index')
    
    # 尝试从缓存获取题目信息
    cache_key = f"problem_detail_{problem_id}"
    problem = cache.get(cache_key)
    
    if not problem:
        # 缓存中没有，从数据库查询
        problem = get_object_or_404(Problem, id=problem_id)
        # 将题目信息存入缓存，有效期10分钟
        cache.set(cache_key, problem, 60 * 10)
    
    if request.method == "POST":
        try:
            # 获取基本信息
            title = request.POST.get("title")
            description = request.POST.get("description")
            problem_type = int(request.POST.get("problem_type", 1))
            input_description = request.POST.get("input_description", "")
            output_description = request.POST.get("output_description", "")
            sample_input = request.POST.get("sample_input", "")
            sample_output = request.POST.get("sample_output", "")
            hint = request.POST.get("hint", "")
            difficulty = int(request.POST.get("difficulty", 1))
            knowledge_point = request.POST.get("knowledge_point", "")
            is_active = request.POST.get("is_active") == "on"
            
            # 更新题目信息
            with transaction.atomic():
                problem.title = title
                problem.description = description
                problem.problem_type = problem_type
                problem.input_description = input_description
                problem.output_description = output_description
                problem.sample_input = sample_input
                problem.sample_output = sample_output
                problem.hint = hint
                problem.difficulty = difficulty
                problem.knowledge_point = knowledge_point
                problem.is_active = is_active
                problem.save()
                
                # 清除缓存
                cache.delete(cache_key)
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    # 准备题目数据
    difficulty_text = "Unknown"
    if problem.difficulty == 1:
        difficulty_text = "Easy"
    elif problem.difficulty == 2:
        difficulty_text = "Medium"
    elif problem.difficulty == 3:
        difficulty_text = "Hard"
    
    problem_data = {
        'id': problem.id,
        'title': problem.title,
        'description': problem.description,
        'input_description': problem.input_description,
        'output_description': problem.output_description,
        'sample_input': problem.sample_input,
        'sample_output': problem.sample_output,
        'hint': problem.hint,
        'difficulty': problem.difficulty,
        'difficulty_text': difficulty_text,
        'knowledge_point': problem.knowledge_point or "",
        'is_active': problem.is_active,
        'created_by': problem.created_by.username,
        'created_at': problem.created_at,
        'updated_at': problem.updated_at
    }
    
    return render(request, "problem/editProblem.html", {"problem": problem_data})

# 查看题目详情
def viewProblem(request, problem_id):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
        return redirect('index')
    
    # 尝试从缓存获取题目信息
    cache_key = f"problem_detail_{problem_id}"
    problem = cache.get(cache_key)
    
    if not problem:
        # 缓存中没有，从数据库查询
        problem = get_object_or_404(Problem, id=problem_id)
        # 将题目信息存入缓存，有效期10分钟
        cache.set(cache_key, problem, 60 * 10)
    
    # 准备题目数据
    difficulty_text = "未知"
    if problem.difficulty == 1:
        difficulty_text = "简单"
    elif problem.difficulty == 2:
        difficulty_text = "中等"
    elif problem.difficulty == 3:
        difficulty_text = "困难"
    
    problem_data = {
        'id': problem.id,
        'title': problem.title,
        'description': problem.description,
        'input_description': problem.input_description,
        'output_description': problem.output_description,
        'sample_input': problem.sample_input,
        'sample_output': problem.sample_output,
        'hint': problem.hint,
        'difficulty': problem.difficulty,
        'difficulty_text': difficulty_text,
        'knowledge_point': problem.knowledge_point or "General",
        'submission_count': problem.submission_count,
        'accepted_count': problem.accepted_count,
        'is_active': problem.is_active,
        'created_by': problem.created_by.username,
        'created_at': problem.created_at,
        'updated_at': problem.updated_at
    }
    
    return render(request, "problem/problemDetail.html", {"problem": problem_data})

# 删除题目
def deleteProblem(request, problem_id):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
            return JsonResponse({"success": False, "message": "Insufficient permissions"})
    
    if request.method == "POST":
        try:
            # 尝试从缓存获取题目信息
            cache_key = f"problem_detail_{problem_id}"
            problem = cache.get(cache_key)
            
            if not problem:
                # 缓存中没有，从数据库查询
                problem = get_object_or_404(Problem, id=problem_id)
            
            # 使用事务保证数据一致性
            with transaction.atomic():
                # 删除题目
                problem.delete()
                
                # 清除相关缓存
                cache.delete(cache_key)
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return JsonResponse({"success": False, "message": "Request method not allowed"})

# 切换题目状态（启用/禁用）
def toggleProblemStatus(request, problem_id):
    # 检查用户是否已登录且是教师或管理员
    if 'user_id' not in request.session or request.session.get('user_role') not in [2, 3]:
        return JsonResponse({"success": False, "message": "权限不足"})
    
    if request.method == "POST":
        try:
            # 尝试从缓存获取题目信息
            cache_key = f"problem_detail_{problem_id}"
            problem = cache.get(cache_key)
            
            if not problem:
                # 缓存中没有，从数据库查询
                problem = get_object_or_404(Problem, id=problem_id)
            
            # 使用事务保证数据一致性
            with transaction.atomic():
                # 更新状态
                problem.is_active = request.POST.get("is_active") == "true"
                problem.save(update_fields=['is_active'])
                
                # 清除相关缓存
                cache.delete(cache_key)
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return JsonResponse({"success": False, "message": "请求方法不允许"})