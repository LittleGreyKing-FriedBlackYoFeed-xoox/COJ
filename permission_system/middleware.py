# _*_ coding:utf-8 _*_
from django.shortcuts import redirect
from django.urls import resolve
from own_models.custom_user_models import CustomUser

class PermissionMiddleware:
    """
    权限检查中间件
    用于在请求处理过程中检查用户权限
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
        # 不需要权限检查的URL名称列表
        self.public_urls = [
            'login',
            'register',
            'home',
            'index',
        ]
        
        # 需要管理员权限的URL名称列表
        self.admin_urls = [
            'permission_system:dashboard',
            'permission_system:permission_list',
            'permission_system:permission_create',
            'permission_system:group_list',
            'permission_system:group_create',
            'permission_system:group_edit',
            'permission_system:user_list',
            'permission_system:user_permissions',
        ]
    
    def __call__(self, request):
        # 获取当前URL的名称
        url_name = resolve(request.path_info).url_name
        namespace = resolve(request.path_info).namespace
        
        if namespace:
            full_url_name = f"{namespace}:{url_name}"
        else:
            full_url_name = url_name
        
        # 如果是公共URL，直接放行
        if url_name in self.public_urls:
            return self.get_response(request)
        
        # 检查用户是否已登录
        user_id = request.session.get('user_id')
        if not user_id:
            # 如果用户未登录，重定向到登录页面
            return redirect('user:login')
        
        try:
            user = CustomUser.objects.get(id=user_id)
            
            # 如果是管理员URL，检查用户是否是管理员
            if full_url_name in self.admin_urls and not user.is_admin():
                # 如果用户不是管理员，重定向到首页
                return redirect('index')
            
            # 将用户对象添加到请求中，方便视图函数使用
            request.user = user
            
            # 继续处理请求
            return self.get_response(request)
        except CustomUser.DoesNotExist:
            # 如果用户不存在，重定向到登录页面
            return redirect('user:login')