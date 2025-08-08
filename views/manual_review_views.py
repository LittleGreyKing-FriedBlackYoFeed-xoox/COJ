from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from own_models.manual_review_models import ManualReviewRequest
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser

# 工具函数：获取当前登录用户
def get_current_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    try:
        return CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return None

# 学生请求人工复核
@csrf_exempt
def request_manual_review(request):
    user = get_current_user(request)
    if not user:
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    
    if request.method == 'POST':
        problem_id = request.POST.get('problem_id')
        code = request.POST.get('code', '').strip()
        
        # 验证必填字段
        if not problem_id or not code:
            return JsonResponse({'error': 'Missing problem_id or code'}, status=400)
        
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return JsonResponse({'error': 'Problem not found'}, status=404)
        
        # 检查是否已有待处理的复核请求
        existing_request = ManualReviewRequest.objects.filter(
            student=user,
            problem=problem,
            status='pending'
        ).first()
        
        if existing_request:
            return JsonResponse({
                'error': 'You already have a pending review request for this problem',
                'existing_review_id': existing_request.id
            }, status=400)
        
        # 创建新的复核请求
        review_request = ManualReviewRequest.objects.create(
            student=user,
            problem=problem,
            submitted_code=code
        )
        
        return JsonResponse({
            'success': True, 
            'review_id': review_request.id,
            'message': 'Manual review request submitted successfully'
        }, status=201)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# 教师复核列表
def teacher_review_list(request):
    user = get_current_user(request)
    if not user:
        return redirect('user:login')
    
    # 权限检查：只有教师和管理员可以访问
    if not (user.is_teacher() or user.is_admin()):
        return redirect('user:login')
    
    # 获取状态过滤参数
    status_filter = request.GET.get('status', 'pending')
    if status_filter not in ['pending', 'reviewed', 'rejected', 'all']:
        status_filter = 'pending'
    
    # 根据状态过滤
    if status_filter == 'all':
        reviews = ManualReviewRequest.objects.all()
    else:
        reviews = ManualReviewRequest.objects.filter(status=status_filter)
    
    # 按请求时间倒序排列
    reviews = reviews.order_by('-request_time')
    
    # 分页处理
    from django.core.paginator import Paginator
    paginator = Paginator(reviews, 10)  # 每页显示10条记录
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'reviews': page_obj,
        'current_status': status_filter,
        'status_choices': ManualReviewRequest.STATUS_CHOICES,
    }
    
    return render(request, 'manual_review/teacher_review_list.html', context)

# 复核详情与提交
@csrf_exempt
def review_detail(request, review_id):
    user = get_current_user(request)
    if not user:
        return redirect('user:login')
    
    # 权限检查：只有教师和管理员可以访问
    if not (user.is_teacher() or user.is_admin()):
        return JsonResponse({'error': 'Permission denied'}, status=403)
    
    review = get_object_or_404(ManualReviewRequest, id=review_id)
    
    if request.method == 'POST':
        action = request.POST.get('action', 'review')
        
        if action == 'reject':
            # 拒绝复核请求
            review.status = 'rejected'
            review.teacher = user
            review.review_time = timezone.now()
            review.save()
            return JsonResponse({'success': True, 'message': 'Review request rejected'}, status=200)
        else:
            # 正常复核流程
            review_comment = request.POST.get('review_comment', '').strip()
            annotated_code = request.POST.get('annotated_code', '').strip()
            
            # 验证必填字段
            if not review_comment and not annotated_code:
                return JsonResponse({'error': 'Please provide either review comment or annotated code'}, status=400)
            
            review.review_comment = review_comment
            review.annotated_code = annotated_code
            review.status = 'reviewed'
            review.teacher = user
            review.review_time = timezone.now()
            review.save()
            return JsonResponse({'success': True, 'message': 'Review submitted successfully'}, status=200)
    
    return render(request, 'manual_review/review_detail.html', {'review': review})

# 学生查看复核结果
def student_review_result(request, review_id):
    user = get_current_user(request)
    if not user:
        return redirect('user:login')
    review = get_object_or_404(ManualReviewRequest, id=review_id, student=user)
    return render(request, 'manual_review/student_review_result.html', {'review': review})