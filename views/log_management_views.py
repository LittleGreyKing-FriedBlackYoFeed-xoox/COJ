# _*_ coding:utf-8 _*_
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils import timezone
from datetime import datetime, timedelta
from permission_system.decorators import admin_required
from own_models.log_management_models import SystemLog, UserOperationLog, ErrorLog, LoginLog
from own_models.custom_user_models import CustomUser
import json


@admin_required
def log_dashboard(request):
    """日志管理主页"""
    # 统计数据
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    week_ago = today - timedelta(days=7)
    
    # 今日统计
    today_system_logs = SystemLog.objects.filter(created_time__date=today).count()
    today_user_operations = UserOperationLog.objects.filter(operation_time__date=today).count()
    today_errors = ErrorLog.objects.filter(error_time__date=today).count()
    today_logins = LoginLog.objects.filter(login_time__date=today).count()
    
    # 昨日统计
    yesterday_system_logs = SystemLog.objects.filter(created_time__date=yesterday).count()
    yesterday_user_operations = UserOperationLog.objects.filter(operation_time__date=yesterday).count()
    yesterday_errors = ErrorLog.objects.filter(error_time__date=yesterday).count()
    yesterday_logins = LoginLog.objects.filter(login_time__date=yesterday).count()
    
    # 本周统计
    week_system_logs = SystemLog.objects.filter(created_time__date__gte=week_ago).count()
    week_user_operations = UserOperationLog.objects.filter(operation_time__date__gte=week_ago).count()
    week_errors = ErrorLog.objects.filter(error_time__date__gte=week_ago).count()
    week_logins = LoginLog.objects.filter(login_time__date__gte=week_ago).count()
    
    # 错误统计
    unresolved_errors = ErrorLog.objects.filter(is_resolved=False).count()
    critical_errors = ErrorLog.objects.filter(error_type='SYSTEM_ERROR', error_time__date__gte=week_ago).count()
    
    # 最近的日志
    recent_system_logs = SystemLog.objects.all()[:5]
    recent_errors = ErrorLog.objects.filter(is_resolved=False)[:5]
    recent_logins = LoginLog.objects.all()[:5]
    
    context = {
        'today_stats': {
            'system_logs': today_system_logs,
            'user_operations': today_user_operations,
            'errors': today_errors,
            'logins': today_logins,
        },
        'yesterday_stats': {
            'system_logs': yesterday_system_logs,
            'user_operations': yesterday_user_operations,
            'errors': yesterday_errors,
            'logins': yesterday_logins,
        },
        'week_stats': {
            'system_logs': week_system_logs,
            'user_operations': week_user_operations,
            'errors': week_errors,
            'logins': week_logins,
        },
        'error_stats': {
            'unresolved': unresolved_errors,
            'critical': critical_errors,
        },
        'recent_system_logs': recent_system_logs,
        'recent_errors': recent_errors,
        'recent_logins': recent_logins,
    }
    
    return render(request, 'log_management/dashboard.html', context)


@admin_required
def system_logs(request):
    """系统日志列表"""
    return render(request, 'log_management/system_logs.html')


@admin_required
def system_logs_data(request):
    """系统日志数据接口"""
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    
    # 搜索条件
    search = request.GET.get('search', '')
    log_type = request.GET.get('log_type', '')
    level = request.GET.get('level', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    # 构建查询条件
    queryset = SystemLog.objects.all()
    
    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) | 
            Q(message__icontains=search) |
            Q(user__username__icontains=search)
        )
    
    if log_type:
        queryset = queryset.filter(log_type=log_type)
    
    if level:
        queryset = queryset.filter(level=level)
    
    if start_date:
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        queryset = queryset.filter(created_time__gte=start_datetime)
    
    if end_date:
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        queryset = queryset.filter(created_time__lt=end_datetime)
    
    # 分页
    paginator = Paginator(queryset, limit)
    logs = paginator.get_page(page)
    
    # 构建返回数据
    data = []
    for log in logs:
        data.append({
            'id': log.id,
            'log_type': log.get_log_type_display(),
            'level': log.level,
            'title': log.title,
            'message': log.message[:100] + '...' if len(log.message) > 100 else log.message,
            'user': log.user.username if log.user else '系统',
            'user_ip': log.user_ip or '-',
            'request_method': log.request_method or '-',
            'request_url': log.request_url or '-',
            'response_status': log.response_status or '-',
            'created_time': log.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        })
    
    return JsonResponse({
        'code': 0,
        'msg': '',
        'count': paginator.count,
        'data': data
    })


@admin_required
def system_log_detail(request, log_id):
    """系统日志详情"""
    log = get_object_or_404(SystemLog, id=log_id)
    
    if request.method == 'GET':
        return render(request, 'log_management/system_log_detail.html', {'log': log})


@admin_required
def user_operations(request):
    """用户操作日志列表"""
    return render(request, 'log_management/user_operations.html')


@admin_required
def user_operations_data(request):
    """用户操作日志数据接口"""
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    
    # 搜索条件
    search = request.GET.get('search', '')
    operation = request.GET.get('operation', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    # 构建查询条件
    queryset = UserOperationLog.objects.select_related('user').all()
    
    if search:
        queryset = queryset.filter(
            Q(user__username__icontains=search) | 
            Q(operation_desc__icontains=search) |
            Q(target_model__icontains=search)
        )
    
    if operation:
        queryset = queryset.filter(operation=operation)
    
    if start_date:
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        queryset = queryset.filter(operation_time__gte=start_datetime)
    
    if end_date:
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        queryset = queryset.filter(operation_time__lt=end_datetime)
    
    # 分页
    paginator = Paginator(queryset, limit)
    logs = paginator.get_page(page)
    
    # 构建返回数据
    data = []
    for log in logs:
        data.append({
            'id': log.id,
            'user': log.user.username,
            'user_ip': log.user_ip,
            'operation': log.get_operation_display(),
            'operation_desc': log.operation_desc,
            'target_model': log.target_model or '-',
            'target_id': log.target_id or '-',
            'request_method': log.request_method,
            'request_url': log.request_url,
            'is_success': '成功' if log.is_success else '失败',
            'operation_time': log.operation_time.strftime('%Y-%m-%d %H:%M:%S'),
        })
    
    return JsonResponse({
        'code': 0,
        'msg': '',
        'count': paginator.count,
        'data': data
    })


@admin_required
def error_logs(request):
    """错误日志列表"""
    return render(request, 'log_management/error_logs.html')


@admin_required
def error_logs_data(request):
    """错误日志数据接口"""
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    
    # 搜索条件
    search = request.GET.get('search', '')
    error_type = request.GET.get('error_type', '')
    is_resolved = request.GET.get('is_resolved', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    # 构建查询条件
    queryset = ErrorLog.objects.select_related('user', 'resolved_by').all()
    
    if search:
        queryset = queryset.filter(
            Q(error_message__icontains=search) | 
            Q(error_code__icontains=search) |
            Q(module_name__icontains=search)
        )
    
    if error_type:
        queryset = queryset.filter(error_type=error_type)
    
    if is_resolved:
        queryset = queryset.filter(is_resolved=is_resolved == 'true')
    
    if start_date:
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        queryset = queryset.filter(error_time__gte=start_datetime)
    
    if end_date:
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        queryset = queryset.filter(error_time__lt=end_datetime)
    
    # 分页
    paginator = Paginator(queryset, limit)
    logs = paginator.get_page(page)
    
    # 构建返回数据
    data = []
    for log in logs:
        data.append({
            'id': log.id,
            'error_type': log.get_error_type_display(),
            'error_code': log.error_code or '-',
            'error_message': log.error_message[:100] + '...' if len(log.error_message) > 100 else log.error_message,
            'user': log.user.username if log.user else '-',
            'user_ip': log.user_ip or '-',
            'module_name': log.module_name or '-',
            'is_resolved': '已解决' if log.is_resolved else '未解决',
            'resolved_by': log.resolved_by.username if log.resolved_by else '-',
            'error_time': log.error_time.strftime('%Y-%m-%d %H:%M:%S'),
        })
    
    return JsonResponse({
        'code': 0,
        'msg': '',
        'count': paginator.count,
        'data': data
    })


@admin_required
def error_log_detail(request, log_id):
    """错误日志详情"""
    log = get_object_or_404(ErrorLog, id=log_id)
    
    if request.method == 'GET':
        return render(request, 'log_management/error_log_detail.html', {'log': log})
    
    elif request.method == 'POST':
        # 标记错误为已解决
        user_id = request.session.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id)
        
        log.is_resolved = True
        log.resolved_time = timezone.now()
        log.resolved_by = user
        log.resolution_note = request.POST.get('resolution_note', '')
        log.save()
        
        return JsonResponse({'code': 0, 'msg': '错误已标记为已解决'})


@admin_required
def login_logs(request):
    """登录日志列表"""
    return render(request, 'log_management/login_logs.html')


@admin_required
def login_logs_data(request):
    """登录日志数据接口"""
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    
    # 搜索条件
    search = request.GET.get('search', '')
    login_status = request.GET.get('login_status', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    # 构建查询条件
    queryset = LoginLog.objects.select_related('user').all()
    
    if search:
        queryset = queryset.filter(
            Q(username__icontains=search) | 
            Q(login_ip__icontains=search) |
            Q(city__icontains=search)
        )
    
    if login_status:
        queryset = queryset.filter(login_status=login_status)
    
    if start_date:
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        queryset = queryset.filter(login_time__gte=start_datetime)
    
    if end_date:
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        queryset = queryset.filter(login_time__lt=end_datetime)
    
    # 分页
    paginator = Paginator(queryset, limit)
    logs = paginator.get_page(page)
    
    # 构建返回数据
    data = []
    for log in logs:
        data.append({
            'id': log.id,
            'username': log.username,
            'login_status': log.get_login_status_display(),
            'login_ip': log.login_ip,
            'country': log.country or '-',
            'region': log.region or '-',
            'city': log.city or '-',
            'failure_reason': log.failure_reason or '-',
            'login_time': log.login_time.strftime('%Y-%m-%d %H:%M:%S'),
            'logout_time': log.logout_time.strftime('%Y-%m-%d %H:%M:%S') if log.logout_time else '-',
            'session_duration': str(log.session_duration) if log.session_duration else '-',
        })
    
    return JsonResponse({
        'code': 0,
        'msg': '',
        'count': paginator.count,
        'data': data
    })


@admin_required
def log_statistics(request):
    """日志统计"""
    # 获取时间范围
    days = int(request.GET.get('days', 7))
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=days-1)
    
    # 按日期统计
    date_stats = []
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        system_count = SystemLog.objects.filter(created_time__date=current_date).count()
        operation_count = UserOperationLog.objects.filter(operation_time__date=current_date).count()
        error_count = ErrorLog.objects.filter(error_time__date=current_date).count()
        login_count = LoginLog.objects.filter(login_time__date=current_date).count()
        
        date_stats.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'system_logs': system_count,
            'user_operations': operation_count,
            'errors': error_count,
            'logins': login_count,
        })
    
    # 按类型统计
    log_type_stats = SystemLog.objects.values('log_type').annotate(count=Count('id'))
    operation_stats = UserOperationLog.objects.values('operation').annotate(count=Count('id'))
    error_type_stats = ErrorLog.objects.values('error_type').annotate(count=Count('id'))
    login_status_stats = LoginLog.objects.values('login_status').annotate(count=Count('id'))
    
    return JsonResponse({
        'code': 0,
        'data': {
            'date_stats': date_stats,
            'log_type_stats': list(log_type_stats),
            'operation_stats': list(operation_stats),
            'error_type_stats': list(error_type_stats),
            'login_status_stats': list(login_status_stats),
        }
    })


@admin_required
def clear_logs(request):
    """清理日志"""
    if request.method == 'POST':
        log_type = request.POST.get('log_type')
        days = int(request.POST.get('days', 30))
        
        cutoff_date = timezone.now() - timedelta(days=days)
        
        deleted_count = 0
        if log_type == 'system':
            deleted_count = SystemLog.objects.filter(created_time__lt=cutoff_date).delete()[0]
        elif log_type == 'operation':
            deleted_count = UserOperationLog.objects.filter(operation_time__lt=cutoff_date).delete()[0]
        elif log_type == 'error':
            deleted_count = ErrorLog.objects.filter(error_time__lt=cutoff_date, is_resolved=True).delete()[0]
        elif log_type == 'login':
            deleted_count = LoginLog.objects.filter(login_time__lt=cutoff_date).delete()[0]
        elif log_type == 'all':
            system_count = SystemLog.objects.filter(created_time__lt=cutoff_date).delete()[0]
            operation_count = UserOperationLog.objects.filter(operation_time__lt=cutoff_date).delete()[0]
            error_count = ErrorLog.objects.filter(error_time__lt=cutoff_date, is_resolved=True).delete()[0]
            login_count = LoginLog.objects.filter(login_time__lt=cutoff_date).delete()[0]
            deleted_count = system_count + operation_count + error_count + login_count
        
        return JsonResponse({
            'code': 0,
            'msg': f'成功清理 {deleted_count} 条日志记录'
        })
    
    return JsonResponse({'code': 1, 'msg': '请求方法错误'})