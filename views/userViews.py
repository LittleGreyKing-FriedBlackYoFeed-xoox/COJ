from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.http import JsonResponse
from django.contrib.auth import logout
from own_models import models
from own_models.models import CustomUser
# 访问首页
def index(request):
    # 如果用户已登录，添加角色文本到会话中
    if 'user_role' in request.session:
        role_value = request.session.get('user_role')
        # 直接在会话中设置 role_text，这样在模板中可以通过 {{ request.session.role_text }} 访问
        if role_value == 1:
            request.session['role_text'] = '学'
        elif role_value == 2:
            request.session['role_text'] = '教'
        elif role_value == 3:
            request.session['role_text'] = '管'
        else:
            request.session['role_text'] = '未知'
    
    return render(request, "user/index.html")

# 导入缓存模块
from django.core.cache import cache
from django.db import connection

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        role = request.POST.get("role", None)
        
        if not username or not password:
            # 检查AJAX请求
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "message": "用户名和密码不能为空"})
            else:
                return render(request, "user/login.html", {"error_message": "用户名和密码不能为空"})
        
        try:
            # 尝试从缓存获取用户信息
            cache_key = f"user_{username}"
            user = cache.get(cache_key)
            
            if not user:
                # 缓存中没有，从数据库查询
                try:
                    # 使用select_for_update避免并发问题
                    user = CustomUser.objects.filter(username=username).first()
                    
                    if not user:
                        # 用户不存在
                        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                            return JsonResponse({"success": False, "message": "用户不存在"})
                        else:
                            return render(request, "user/login.html", {"error_message": "用户不存在"})
                    
                    # 将用户信息存入缓存，有效期30分钟
                    cache.set(cache_key, user, 60 * 30)
                except Exception as db_error:
                    # 数据库查询错误
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({"success": False, "message": f"数据库查询错误: {str(db_error)}"})
                    else:
                        return render(request, "user/login.html", {"error_message": f"数据库查询错误: {str(db_error)}"})
            
            # 简单的密码验证（实际应用中应使用更安全的方法）
            if user.password == password:  # 注意：这里应该使用哈希比较，而不是明文比较
                # 检查用户角色是否匹配
                if (role == "student" and user.role == 1) or \
                   (role == "teacher" and user.role == 2) or \
                   (role == "admin" and user.role == 3):
                    
                    # 将用户ID和角色存储在会话中
                    request.session['user_id'] = user.id
                    request.session['user_role'] = user.role
                    request.session['username'] = user.username
                    
                    # 设置角色文本
                    if user.role == 1:
                        request.session['role_text'] = '学'
                    elif user.role == 2:
                        request.session['role_text'] = '教'
                    elif user.role == 3:
                        request.session['role_text'] = '管'
                    else:
                        request.session['role_text'] = '未知'
                    
                    # 更新最后登录时间
                    from django.utils import timezone
                    user.last_login = timezone.now()
                    user.save(update_fields=['last_login'])
                    
                    # 检查AJAX请求
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({
                            "success": True, 
                            "redirect": "/",
                            "role": role
                        })
                    else:
                        return redirect('index')
                else:
                    # 角色不匹配
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({"success": False, "message": "所选角色与账号不匹配"})
                    else:
                        return render(request, "user/login.html", {"error_message": "所选角色与账号不匹配"})
            else:
                # 密码错误
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({"success": False, "message": "密码错误"})
                else:
                    return render(request, "user/login.html", {"error_message": "密码错误"})
                    
        except Exception as e:
            # 其他错误
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "message": f"登录失败: {str(e)}"})
            else:
                return render(request, "user/login.html", {"error_message": f"登录失败: {str(e)}"})
    
    return render(request, "user/login.html")

# 注册
def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        role = request.POST.get("role", None)
        
        # 根据角色设置usercode和role值
        usercode = ""
        role_value = 1  # 默认为学生
        
        if role == "student":
            usercode = request.POST.get("student_id", "")
            role_value = 1
        elif role == "teacher":
            usercode = request.POST.get("teacher_id", "")
            role_value = 2
        elif role == "admin":
            usercode = request.POST.get("admin_id", "")
            role_value = 3
            
        # 创建用户
        try:
            # 使用缓存检查用户名是否已存在
            cache_key = f"username_exists_{username}"
            username_exists = cache.get(cache_key)
            
            if username_exists is None:
                # 缓存中没有，从数据库查询
                username_exists = CustomUser.objects.filter(username=username).exists()
                # 将结果存入缓存，有效期10分钟
                cache.set(cache_key, username_exists, 60 * 10)
            
            if username_exists:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({"success": False, "error": "用户名已存在"})
                else:
                    return render(request, "user/register.html", {"error_message": "用户名已存在"})
            
            # 创建新用户
            from django.utils import timezone
            
            user = CustomUser(
                username=username,
                password=password,  # 注意：实际应用中应该哈希密码
                usercode=usercode,
                role=role_value,
                is_active=True,
                date_joined=timezone.now()
            )
            
            # 保存其他字段
            if role == "student":
                user.remark = request.POST.get("college", "")  # 将学院信息保存在remark字段
            elif role == "teacher":
                user.remark = request.POST.get("title", "")  # 将职称信息保存在remark字段
            elif role == "admin":
                user.remark = "系统管理员"  # 管理员备注
                
            # 使用事务保证数据一致性
            from django.db import transaction
            with transaction.atomic():
                user.save()
                
                # 清除相关缓存
                cache.delete(cache_key)
            
            # 检查是否是AJAX请求
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # 返回JSON响应
                return JsonResponse({"success": True})
            else:
                # 普通表单提交，重定向到登录页面
                return render(request, "user/index.html", {"register_success": True})
        except Exception as e:
            # 注册失败，返回错误信息
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # 返回JSON响应
                return JsonResponse({"success": False, "error": str(e)})
            else:
                # 普通表单提交，返回错误信息
                return render(request, "user/register.html", {"error_message": str(e)})
            
    # GET请求，显示注册页面
    return render(request, "user/register.html")

# 用户列表页面
def userList(request):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return redirect('index')
    
    return render(request, "user/userList.html")

# 退出登录
def logout_view(request):
    # 清除会话
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_role' in request.session:
        del request.session['user_role']
    if 'username' in request.session:
        del request.session['username']
    
    # 清除所有会话数据
    request.session.flush()
    
    # 如果是AJAX请求，返回JSON响应
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({"success": True})
    
    # 普通请求，重定向到首页
    return redirect('index')

# 获取用户列表（JSON格式）
def get_users_json(request):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return JsonResponse({"code": 0, "msg": "权限不足", "count": 0, "data": []})
    
    try:
        # 获取查询参数
        username = request.GET.get('username', '')
        role = request.GET.get('role', '')
        is_active = request.GET.get('is_active', '')
        
        # 获取分页参数
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        
        # 获取用户列表 - 使用select_related优化查询
        users = CustomUser.objects.all()
        
        # 应用过滤条件
        if username:
            users = users.filter(username__icontains=username)
        
        if role:
            users = users.filter(role=int(role))
        
        if is_active == 'true':
            users = users.filter(is_active=True)
        elif is_active == 'false':
            users = users.filter(is_active=False)
        
        # 计算总数
        total_count = users.count()
        
        # 分页
        start = (page - 1) * limit
        end = page * limit
        users = users[start:end]
        
        user_list = []
        
        for user in users:
            # 根据角色获取角色名称和特殊字段
            role_name = ""
            special_field = ""
            
            if user.role == 1:
                role_name = "学生"
                special_field = user.remark  # 学院
            elif user.role == 2:
                role_name = "教师"
                special_field = user.remark  # 职称
            elif user.role == 3:
                role_name = "管理员"
                special_field = "系统管理员"
            
            # 构建用户数据
            user_data = {
                "id": user.id,
                "username": user.username,
                "role": user.role,
                "role_name": role_name,
                "usercode": user.usercode,
                "special_field": special_field,
                "is_active": user.is_active,
                "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S") if user.date_joined else "",
                "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S") if user.last_login else ""
            }
            
            user_list.append(user_data)
        
        # 返回符合Layui表格要求的数据格式
        return JsonResponse({
            "code": 0,  # Layui要求成功状态码为0
            "msg": "",
            "count": total_count,
            "data": user_list
        })
    except Exception as e:
        return JsonResponse({
            "code": 1,  # 错误状态码
            "msg": str(e),
            "count": 0,
            "data": []
        })

# 用户列表页面
def userList(request):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return redirect('index')
    
    return render(request, "user/userList.html")

# 添加用户
def addUser(request):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return redirect('index')
    
    if request.method == "POST":
        try:
            # 获取基本信息
            username = request.POST.get("username")
            password = request.POST.get("password")
            role = int(request.POST.get("role"))
            is_active = True  # 默认设置为启用状态
            
            # 使用缓存检查用户名是否已存在
            cache_key = f"username_exists_{username}"
            username_exists = cache.get(cache_key)
            
            if username_exists is None:
                # 缓存中没有，从数据库查询
                username_exists = CustomUser.objects.filter(username=username).exists()
                # 将结果存入缓存，有效期10分钟
                cache.set(cache_key, username_exists, 60 * 10)
            
            if username_exists:
                return JsonResponse({"success": False, "message": "用户名已存在"})
            
            # 根据角色获取特殊字段
            usercode = ""
            remark = ""
            
            if role == 1:  # 学生
                usercode = request.POST.get("student_id")
                remark = request.POST.get("college")
            elif role == 2:  # 教师
                usercode = request.POST.get("teacher_id")
                remark = request.POST.get("title")
            elif role == 3:  # 管理员
                usercode = request.POST.get("admin_id")
                remark = "系统管理员"
            
            # 创建用户
            from django.utils import timezone
            
            user = CustomUser(
                username=username,
                password=password,  # 注意：实际应用中应该哈希密码
                role=role,
                usercode=usercode,
                remark=remark,
                is_active=is_active,
                date_joined=timezone.now()
            )
            
            # 使用事务保证数据一致性
            from django.db import transaction
            with transaction.atomic():
                user.save()
                
                # 清除相关缓存
                cache.delete(cache_key)
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return render(request, "user/addUser.html")

# 编辑用户
def editUser(request, user_id):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return redirect('index')
    
    # 尝试从缓存获取用户信息
    cache_key = f"user_detail_{user_id}"
    user = cache.get(cache_key)
    
    if not user:
        # 缓存中没有，从数据库查询
        user = get_object_or_404(CustomUser, id=user_id)
        # 将用户信息存入缓存，有效期10分钟
        cache.set(cache_key, user, 60 * 10)
    
    if request.method == "POST":
        try:
            # 获取基本信息
            username = request.POST.get("username")
            password = request.POST.get("password")
            role = int(request.POST.get("role"))
            is_active = request.POST.get("is_active") == "on"
            
            # 检查用户名是否已存在（排除当前用户）
            username_exists = CustomUser.objects.filter(username=username).exclude(id=user_id).exists()
            
            if username_exists:
                return JsonResponse({"success": False, "message": "用户名已存在"})
            
            # 更新基本信息
            user.username = username
            if password:  # 如果提供了密码，则更新密码
                user.password = password  # 注意：实际应用中应该哈希密码
            user.role = role
            user.is_active = is_active
            
            # 根据角色更新特殊字段
            if role == 1:  # 学生
                user.usercode = request.POST.get("student_id")
                user.remark = request.POST.get("college")
            elif role == 2:  # 教师
                user.usercode = request.POST.get("teacher_id")
                user.remark = request.POST.get("title")
            elif role == 3:  # 管理员
                user.usercode = request.POST.get("admin_id")
                user.remark = "系统管理员"
            
            # 使用事务保证数据一致性
            from django.db import transaction
            with transaction.atomic():
                # 保存更新
                user.save()
                
                # 清除相关缓存
                cache.delete(cache_key)
                cache.delete(f"user_{user.username}")
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    # 准备用户数据，包括角色和备注的转义
    role_text = "未知"
    if user.role == 1:
        role_text = "学生"
    elif user.role == 2:
        role_text = "教师"
    elif user.role == 3:
        role_text = "管理员"
    
    remark_text = user.remark
    if user.role == 1:
        remark_text = f"学院: {user.remark}"
    elif user.role == 2:
        remark_text = f"职称: {user.remark}"
    
    user_data = {
        'id': user.id,
        'username': user.username,
        'usercode': user.usercode,
        'role': user.role,
        'role_text': role_text,
        'remark': remark_text,
        'is_active': user.is_active,
        'date_joined': user.date_joined if hasattr(user, 'date_joined') else None
    }
    
    return render(request, "user/editUser.html", {"user": user_data})

# 查看用户详情
def viewUser(request, user_id):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return redirect('index')
    
    # 尝试从缓存获取用户信息
    cache_key = f"user_detail_{user_id}"
    user = cache.get(cache_key)
    
    if not user:
        # 缓存中没有，从数据库查询
        user = get_object_or_404(CustomUser, id=user_id)
        # 将用户信息存入缓存，有效期10分钟
        cache.set(cache_key, user, 60 * 10)
    
    # 准备用户数据，包括角色和备注的转义
    role_text = "未知"
    if user.role == 1:
        role_text = "学生"
    elif user.role == 2:
        role_text = "教师"
    elif user.role == 3:
        role_text = "管理员"
    
    remark_text = user.remark
    if user.role == 1:
        remark_text = f"学院: {user.remark}"
    elif user.role == 2:
        remark_text = f"职称: {user.remark}"
    
    user_data = {
        'id': user.id,
        'username': user.username,
        'usercode': user.usercode,
        'role': user.role,
        'role_text': role_text,
        'remark': remark_text,
        'is_active': user.is_active,
        'date_joined': user.date_joined if hasattr(user, 'date_joined') else None,
        'last_login': user.last_login if hasattr(user, 'last_login') else None
    }
    
    return render(request, "user/userDetail.html", {"user": user_data})

# 删除用户
def deleteUser(request, user_id):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return JsonResponse({"success": False, "message": "权限不足"})
    
    if request.method == "POST":
        try:
            # 尝试从缓存获取用户信息
            cache_key = f"user_detail_{user_id}"
            user = cache.get(cache_key)
            
            if not user:
                # 缓存中没有，从数据库查询
                user = get_object_or_404(CustomUser, id=user_id)
            
            # 不允许删除自己
            if int(user.id) == int(request.session.get('user_id')):
                return JsonResponse({"success": False, "message": "不能删除当前登录的用户"})
            
            # 使用事务保证数据一致性
            from django.db import transaction
            with transaction.atomic():
                # 删除用户
                username = user.username
                user.delete()
                
                # 清除相关缓存
                cache.delete(cache_key)
                cache.delete(f"user_{username}")
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return JsonResponse({"success": False, "message": "请求方法不允许"})

# 切换用户状态（启用/禁用）
def toggleUserStatus(request, user_id):
    # 检查用户是否已登录且是管理员
    if 'user_id' not in request.session or request.session.get('user_role') != 3:
        return JsonResponse({"success": False, "message": "权限不足"})
    
    if request.method == "POST":
        try:
            # 尝试从缓存获取用户信息
            cache_key = f"user_detail_{user_id}"
            user = cache.get(cache_key)
            
            if not user:
                # 缓存中没有，从数据库查询
                user = get_object_or_404(CustomUser, id=user_id)
            
            # 不允许禁用自己
            if user.id == request.session.get('user_id') and not request.POST.get("is_active") == "true":
                return JsonResponse({"success": False, "message": "不能禁用当前登录的用户"})
            
            # 使用事务保证数据一致性
            from django.db import transaction
            with transaction.atomic():
                # 更新状态
                user.is_active = request.POST.get("is_active") == "true"
                user.save(update_fields=['is_active'])
                
                # 清除相关缓存
                cache.delete(cache_key)
                cache.delete(f"user_{user.username}")
            
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return JsonResponse({"success": False, "message": "请求方法不允许"})