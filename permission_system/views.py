# _*_ coding:utf-8 _*_
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from own_models.custom_user_models import CustomUser
from .decorators import admin_required

# 权限管理仪表板
@admin_required
def dashboard(request):
    """权限管理系统仪表板"""
    # 统计数据
    permission_count = Permission.objects.count()
    group_count = Group.objects.count()
    user_count = CustomUser.objects.count()
    
    context = {
        'permission_count': permission_count,
        'group_count': group_count,
        'user_count': user_count,
    }
    
    return render(request, 'permission_system/dashboard.html', context)

# 权限管理
@admin_required
def permission_list(request):
    """权限列表"""
    permissions = Permission.objects.all().order_by('content_type__app_label', 'codename')
    
    context = {
        'permissions': permissions,
    }
    
    return render(request, 'permission_system/permission_list.html', context)

@admin_required
def permission_list_data(request):
    """权限列表数据（用于AJAX请求）"""
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')
    
    # 查询权限
    permissions = Permission.objects.all()
    
    # 搜索
    if search_value:
        permissions = permissions.filter(
            Q(name__icontains=search_value) | 
            Q(codename__icontains=search_value) |
            Q(content_type__app_label__icontains=search_value)
        )
    
    # 总记录数
    total = permissions.count()
    
    # 排序
    permissions = permissions.order_by('content_type__app_label', 'codename')
    
    # 分页
    permissions = permissions[start:start+length]
    
    # 构造返回数据
    data = []
    for permission in permissions:
        data.append({
            'id': permission.id,
            'name': permission.name,
            'codename': permission.codename,
            'app_label': permission.content_type.app_label,
            'model': permission.content_type.model,
        })
    
    return JsonResponse({
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,
        'data': data,
    })

@admin_required
def permission_create(request):
    """创建权限"""
    if request.method == 'POST':
        name = request.POST.get('name')
        codename = request.POST.get('codename')
        app_label = request.POST.get('app_label')
        model = request.POST.get('model')
        
        # 获取或创建内容类型
        content_type, created = ContentType.objects.get_or_create(
            app_label=app_label,
            model=model
        )
        
        # 创建权限
        permission, created = Permission.objects.get_or_create(
            name=name,
            codename=codename,
            content_type=content_type
        )
        
        if created:
            return redirect('permission_system:permission_list')
        else:
            return render(request, 'permission_system/permission_create.html', {
                'error': '权限已存在',
                'content_types': ContentType.objects.all(),
            })
    
    # GET请求
    content_types = ContentType.objects.all()
    
    context = {
        'content_types': content_types,
    }
    
    return render(request, 'permission_system/permission_create.html', context)

# 用户组管理
@admin_required
def group_list(request):
    """用户组列表"""
    groups = Group.objects.all()
    
    context = {
        'groups': groups,
    }
    
    return render(request, 'permission_system/group_list.html', context)

@admin_required
def group_list_data(request):
    """用户组列表数据（用于AJAX请求）"""
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')
    
    # 查询用户组
    groups = Group.objects.all()
    
    # 搜索
    if search_value:
        groups = groups.filter(name__icontains=search_value)
    
    # 总记录数
    total = groups.count()
    
    # 排序
    groups = groups.order_by('name')
    
    # 分页
    groups = groups[start:start+length]
    
    # 构造返回数据
    data = []
    for group in groups:
        data.append({
            'id': group.id,
            'name': group.name,
            'permissions_count': group.permissions.count(),
            'user_count': group.user_set.count(),
        })
    
    return JsonResponse({
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,
        'data': data,
    })

@admin_required
def group_create(request):
    """创建用户组"""
    if request.method == 'POST':
        name = request.POST.get('name')
        permissions = request.POST.getlist('permissions')
        
        # 创建用户组
        group, created = Group.objects.get_or_create(name=name)
        
        # 分配权限
        group.permissions.clear()
        for permission_id in permissions:
            try:
                permission = Permission.objects.get(id=permission_id)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                pass
        
        return redirect('permission_system:group_list')
    
    # GET请求
    permissions = Permission.objects.all().order_by('content_type__app_label', 'codename')
    
    context = {
        'permissions': permissions,
    }
    
    return render(request, 'permission_system/group_create.html', context)

@admin_required
def group_edit(request, group_id):
    """编辑用户组"""
    group = get_object_or_404(Group, id=group_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        permissions = request.POST.getlist('permissions')
        
        # 更新用户组
        group.name = name
        group.save()
        
        # 分配权限
        group.permissions.clear()
        for permission_id in permissions:
            try:
                permission = Permission.objects.get(id=permission_id)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                pass
        
        return redirect('permission_system:group_list')
    
    # GET请求
    permissions = Permission.objects.all().order_by('content_type__app_label', 'codename')
    group_permissions = group.permissions.all()
    
    context = {
        'group': group,
        'permissions': permissions,
        'group_permissions': group_permissions,
    }
    
    return render(request, 'permission_system/group_edit.html', context)

# 用户权限管理
@admin_required
def user_list(request):
    """用户列表"""
    users = CustomUser.objects.all()
    
    context = {
        'users': users,
    }
    
    return render(request, 'permission_system/user_list.html', context)

@admin_required
def user_list_data(request):
    """用户列表数据（用于AJAX请求）"""
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '')
    
    # 查询用户
    users = CustomUser.objects.all()
    
    # 搜索
    if search_value:
        users = users.filter(
            Q(username__icontains=search_value) | 
            Q(email__icontains=search_value) |
            Q(real_name__icontains=search_value)
        )
    
    # 总记录数
    total = users.count()
    
    # 排序
    users = users.order_by('username')
    
    # 分页
    users = users[start:start+length]
    
    # 构造返回数据
    data = []
    for user in users:
        role_display = "未知"
        if user.role == 1:
            role_display = "学生"
        elif user.role == 2:
            role_display = "教师"
        elif user.role == 3:
            role_display = "管理员"
            
        data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'role_display': role_display,
            'is_active': user.is_active,
            'date_joined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S') if user.date_joined else '',
            'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else '',
        })
    
    return JsonResponse({
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': total,
        'data': data,
    })

@admin_required
def user_permissions(request):
    """用户权限管理"""
    user_id = request.GET.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        role = request.POST.get('role')
        groups = request.POST.getlist('groups')
        
        # 更新用户角色
        user.role = int(role)
        user.save()
        
        # 分配用户组
        user.groups.clear()
        for group_id in groups:
            try:
                group = Group.objects.get(id=group_id)
                user.groups.add(group)
            except Group.DoesNotExist:
                pass
        
        return redirect('permission_system:user_list')
    
    # GET请求
    groups = Group.objects.all()
    user_groups = user.groups.all()
    
    context = {
        'user': user,
        'groups': groups,
        'user_groups': user_groups,
    }
    
    return render(request, 'permission_system/user_permissions.html', context)

# 初始化权限系统
@admin_required
def init_permissions(request):
    """初始化权限系统"""
    from django.core.management import call_command
    
    # 调用初始化命令
    call_command('init_permissions')
    
    return redirect('permission_system:dashboard')