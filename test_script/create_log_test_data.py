#!/usr/bin/env python
import os
import sys
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

from own_models.log_management_models import SystemLog, UserOperationLog, ErrorLog, LoginLog
from own_models.custom_user_models import CustomUser

def create_test_data():
    """创建日志管理测试数据"""
    
    # 获取所有用户
    users = list(CustomUser.objects.all())
    if not users:
        print("没有找到用户，请先创建用户")
        return
    
    print(f"找到 {len(users)} 个用户，开始创建测试数据...")
    
    # 创建系统日志
    print("创建系统日志...")
    system_log_types = ['SYSTEM_START', 'SYSTEM_STOP', 'DATABASE_BACKUP', 'CACHE_CLEAR', 'CONFIG_UPDATE', 'MAINTENANCE', 'SECURITY_SCAN', 'OTHER']
    log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    
    for i in range(100):
        log_time = timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        user = random.choice(users) if random.random() > 0.3 else None
        log_type = random.choice(system_log_types)
        level = random.choice(log_levels)
        
        log = SystemLog.objects.create(
            log_type='SYSTEM',
            level=level,
            title=f"{log_type.replace('_', ' ').title()} - {level}",
            message=f"系统日志消息 #{i+1}: {log_type} 操作执行",
            user=user,
            user_ip=f"192.168.1.{random.randint(1, 254)}",
            request_method=random.choice(['GET', 'POST', 'PUT', 'DELETE']),
            request_url=f"/api/system/{log_type.lower()}",
            response_status=random.choice([200, 201, 400, 404, 500]),
            extra_data={"request_id": f"{random.randint(1000, 9999)}", "duration": random.randint(10, 1000)}
        )
        # 手动设置创建时间
        log.created_time = log_time
        log.save()
    
    # 创建用户操作日志
    print("创建用户操作日志...")
    operations = ['LOGIN', 'LOGOUT', 'CREATE', 'UPDATE', 'DELETE', 'VIEW', 'DOWNLOAD', 'UPLOAD', 'SUBMIT', 'APPROVE', 'REJECT', 'OTHER']
    target_models = ['Problem', 'Submission', 'User', 'Competition', 'TestCase']
    
    for i in range(150):
        log_time = timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        user = random.choice(users)
        operation = random.choice(operations)
        target_model = random.choice(target_models)
        
        op_log = UserOperationLog.objects.create(
            user=user,
            operation=operation,
            operation_desc=f"用户 {user.username} 执行了 {operation} 操作",
            target_model=target_model,
            target_id=str(random.randint(1, 100)),
            user_ip=f"192.168.1.{random.randint(1, 254)}",
            request_method=random.choice(['GET', 'POST', 'PUT', 'DELETE']),
            request_url=f"/api/{target_model.lower()}/{random.randint(1, 100)}",
            is_success=random.choice([True, False])
        )
        # 手动设置操作时间
        op_log.operation_time = log_time
        op_log.save()
    
    # 创建错误日志
    print("创建错误日志...")
    error_levels = ['ERROR', 'CRITICAL', 'WARNING']
    exception_types = ['ValueError', 'TypeError', 'AttributeError', 'KeyError', 'IndexError', 'DatabaseError', 'ValidationError', 'PermissionError']
    
    for i in range(80):
        log_time = timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        user = random.choice(users) if random.random() > 0.4 else None
        level = random.choice(error_levels)
        exception_type = random.choice(exception_types)
        
        error_log = ErrorLog.objects.create(
            error_type=random.choice(['SYSTEM_ERROR', 'DATABASE_ERROR', 'NETWORK_ERROR', 'PERMISSION_ERROR', 'VALIDATION_ERROR', 'BUSINESS_ERROR', 'UNKNOWN_ERROR']),
            error_message=f"{exception_type}: 错误消息 #{i+1} - 这是一个模拟的错误信息",
            error_traceback=f"Traceback (most recent call last):\n  File \"views.py\", line {random.randint(10, 200)}, in function_name\n    raise {exception_type}(\"错误详情\")\n{exception_type}: 错误详情",
            user=user,
            user_ip=f"192.168.1.{random.randint(1, 254)}",
            request_method=random.choice(['GET', 'POST', 'PUT', 'DELETE']),
            request_url=f"/api/error/{random.randint(1, 100)}",
            is_resolved=random.choice([True, False])
        )
        # 手动设置错误时间
        error_log.error_time = log_time
        error_log.save()
    
    # 创建登录日志
    print("创建登录日志...")
    statuses = ['SUCCESS', 'FAILED']
    failure_reasons = ['密码错误', '用户不存在', '账户被锁定', '验证码错误', '网络超时']
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    ]
    locations = ['北京市', '上海市', '广州市', '深圳市', '杭州市', '南京市', '武汉市', '成都市', '西安市', '重庆市']
    
    for i in range(200):
        login_time = timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        user = random.choice(users)
        status = random.choice(statuses)
        
        logout_time = None
        session_duration = None
        if status == 'SUCCESS' and random.random() > 0.3:
            logout_time = login_time + timedelta(hours=random.randint(1, 8), minutes=random.randint(0, 59))
            session_duration = str(logout_time - login_time)
        
        login_log = LoginLog.objects.create(
            username=user.username,
            user=user,
            login_ip=f"192.168.1.{random.randint(1, 254)}",
            city=random.choice(locations),
            user_agent=random.choice(user_agents),
            login_status=status,
            failure_reason=random.choice(failure_reasons) if status == 'FAILED' else '',
            logout_time=logout_time
        )
        # 手动设置登录时间
        login_log.login_time = login_time
        login_log.save()
    
    print("测试数据创建完成！")
    print(f"系统日志: {SystemLog.objects.count()} 条")
    print(f"用户操作日志: {UserOperationLog.objects.count()} 条")
    print(f"错误日志: {ErrorLog.objects.count()} 条")
    print(f"登录日志: {LoginLog.objects.count()} 条")

if __name__ == "__main__":
    create_test_data()