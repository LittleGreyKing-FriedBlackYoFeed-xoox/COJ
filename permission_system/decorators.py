# _*_ coding:utf-8 _*_
from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from own_models.custom_user_models import CustomUser

def permission_required(permission_codename):
    """
    权限检查装饰器
    
    参数:
    - permission_codename: 权限代码名称，如'view_users'
    
    用法:
    @permission_required('view_users')
    def my_view(request):
        # 视图代码
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # 检查用户是否已登录
            user_id = request.session.get('user_id')
            if not user_id:
                return redirect('user:login')
            
            try:
                user = CustomUser.objects.get(id=user_id)
                
                # 检查用户角色
                # 管理员角色自动拥有所有权限
                if user.is_admin():
                    return view_func(request, *args, **kwargs)
                
                # 基于角色的权限检查
                if permission_codename.startswith('view_') and (user.is_student() or user.is_teacher()):
                    return view_func(request, *args, **kwargs)
                elif permission_codename.startswith('add_') and user.is_teacher():
                    return view_func(request, *args, **kwargs)
                elif permission_codename.startswith('change_') and user.is_teacher():
                    return view_func(request, *args, **kwargs)
                
                # 如果没有权限，返回403错误
                return HttpResponseForbidden("权限不足，无法访问此页面")
            except CustomUser.DoesNotExist:
                return redirect('user:login')
        
        return _wrapped_view
    return decorator

def admin_required(view_func):
    """
    管理员权限检查装饰器
    
    用法:
    @admin_required
    def my_view(request):
        # 视图代码
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # 检查用户是否已登录
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('user:login')
        
        try:
            user = CustomUser.objects.get(id=user_id)
            
            # 检查用户是否是管理员
            if user.is_admin():
                return view_func(request, *args, **kwargs)
            
            # 如果不是管理员，返回403错误
            return HttpResponseForbidden("权限不足，无法访问此页面")
        except CustomUser.DoesNotExist:
            return redirect('user:login')
    
    return _wrapped_view

def teacher_required(view_func):
    """
    教师权限检查装饰器
    
    用法:
    @teacher_required
    def my_view(request):
        # 视图代码
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # 检查用户是否已登录
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('user:login')
        
        try:
            user = CustomUser.objects.get(id=user_id)
            
            # 检查用户是否是教师或管理员
            if user.is_teacher() or user.is_admin():
                return view_func(request, *args, **kwargs)
            
            # 如果不是教师或管理员，返回403错误
            return HttpResponseForbidden("权限不足，无法访问此页面")
        except CustomUser.DoesNotExist:
            return redirect('user:login')
    
    return _wrapped_view