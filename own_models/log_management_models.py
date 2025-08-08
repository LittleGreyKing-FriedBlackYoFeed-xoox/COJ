# _*_ coding:utf-8 _*_
from django.db import models
from own_models.custom_user_models import CustomUser
from django.utils import timezone

class SystemLog(models.Model):
    """系统日志模型"""
    
    LOG_LEVEL_CHOICES = (
        ('DEBUG', 'Debug'),
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
        ('CRITICAL', 'Critical'),
    )
    
    LOG_TYPE_CHOICES = (
        ('SYSTEM', '系统日志'),
        ('USER', '用户操作'),
        ('SECURITY', '安全日志'),
        ('DATABASE', '数据库操作'),
        ('API', 'API调用'),
        ('ERROR', '错误日志'),
    )
    
    class Meta:
        db_table = "log_management_system_log"
        verbose_name = "系统日志"
        verbose_name_plural = "系统日志"
        ordering = ['-created_time']
    
    # 基本信息
    log_type = models.CharField("日志类型", max_length=20, choices=LOG_TYPE_CHOICES, default='SYSTEM')
    level = models.CharField("日志级别", max_length=10, choices=LOG_LEVEL_CHOICES, default='INFO')
    title = models.CharField("日志标题", max_length=200)
    message = models.TextField("日志内容")
    
    # 用户信息
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="操作用户")
    user_ip = models.GenericIPAddressField("用户IP", null=True, blank=True)
    user_agent = models.TextField("用户代理", blank=True)
    
    # 请求信息
    request_method = models.CharField("请求方法", max_length=10, blank=True)
    request_url = models.URLField("请求URL", max_length=500, blank=True)
    request_params = models.TextField("请求参数", blank=True)
    
    # 响应信息
    response_status = models.IntegerField("响应状态码", null=True, blank=True)
    response_time = models.FloatField("响应时间(ms)", null=True, blank=True)
    
    # 时间信息
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    
    # 额外信息
    module = models.CharField("模块名称", max_length=100, blank=True)
    function = models.CharField("函数名称", max_length=100, blank=True)
    extra_data = models.JSONField("额外数据", default=dict, blank=True)
    
    def __str__(self):
        return f"[{self.level}] {self.title} - {self.created_time}"


class UserOperationLog(models.Model):
    """用户操作日志模型"""
    
    OPERATION_CHOICES = (
        ('LOGIN', '登录'),
        ('LOGOUT', '登出'),
        ('CREATE', '创建'),
        ('UPDATE', '更新'),
        ('DELETE', '删除'),
        ('VIEW', '查看'),
        ('DOWNLOAD', '下载'),
        ('UPLOAD', '上传'),
        ('SUBMIT', '提交'),
        ('APPROVE', '审批'),
        ('REJECT', '拒绝'),
        ('OTHER', '其他'),
    )
    
    class Meta:
        db_table = "log_management_user_operation"
        verbose_name = "用户操作日志"
        verbose_name_plural = "用户操作日志"
        ordering = ['-operation_time']
    
    # 用户信息
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="操作用户")
    user_ip = models.GenericIPAddressField("用户IP")
    user_agent = models.TextField("用户代理", blank=True)
    
    # 操作信息
    operation = models.CharField("操作类型", max_length=20, choices=OPERATION_CHOICES)
    operation_desc = models.CharField("操作描述", max_length=200)
    target_model = models.CharField("目标模型", max_length=100, blank=True)
    target_id = models.CharField("目标ID", max_length=100, blank=True)
    
    # 请求信息
    request_method = models.CharField("请求方法", max_length=10)
    request_url = models.URLField("请求URL", max_length=500)
    request_data = models.TextField("请求数据", blank=True)
    
    # 结果信息
    is_success = models.BooleanField("是否成功", default=True)
    result_message = models.TextField("结果信息", blank=True)
    
    # 时间信息
    operation_time = models.DateTimeField("操作时间", auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.operation_desc} - {self.operation_time}"


class ErrorLog(models.Model):
    """错误日志模型"""
    
    ERROR_TYPE_CHOICES = (
        ('SYSTEM_ERROR', '系统错误'),
        ('DATABASE_ERROR', '数据库错误'),
        ('NETWORK_ERROR', '网络错误'),
        ('PERMISSION_ERROR', '权限错误'),
        ('VALIDATION_ERROR', '验证错误'),
        ('BUSINESS_ERROR', '业务错误'),
        ('UNKNOWN_ERROR', '未知错误'),
    )
    
    class Meta:
        db_table = "log_management_error_log"
        verbose_name = "错误日志"
        verbose_name_plural = "错误日志"
        ordering = ['-error_time']
    
    # 错误信息
    error_type = models.CharField("错误类型", max_length=20, choices=ERROR_TYPE_CHOICES, default='UNKNOWN_ERROR')
    error_code = models.CharField("错误代码", max_length=50, blank=True)
    error_message = models.TextField("错误信息")
    error_traceback = models.TextField("错误堆栈", blank=True)
    
    # 用户信息
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="相关用户")
    user_ip = models.GenericIPAddressField("用户IP", null=True, blank=True)
    
    # 请求信息
    request_method = models.CharField("请求方法", max_length=10, blank=True)
    request_url = models.URLField("请求URL", max_length=500, blank=True)
    request_data = models.TextField("请求数据", blank=True)
    
    # 环境信息
    server_name = models.CharField("服务器名称", max_length=100, blank=True)
    module_name = models.CharField("模块名称", max_length=100, blank=True)
    function_name = models.CharField("函数名称", max_length=100, blank=True)
    
    # 状态信息
    is_resolved = models.BooleanField("是否已解决", default=False)
    resolved_time = models.DateTimeField("解决时间", null=True, blank=True)
    resolved_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, 
                                   related_name='resolved_errors', verbose_name="解决人")
    resolution_note = models.TextField("解决说明", blank=True)
    
    # 时间信息
    error_time = models.DateTimeField("错误时间", auto_now_add=True)
    
    def __str__(self):
        return f"[{self.error_type}] {self.error_message[:50]} - {self.error_time}"


class LoginLog(models.Model):
    """登录日志模型"""
    
    LOGIN_STATUS_CHOICES = (
        ('SUCCESS', '成功'),
        ('FAILED', '失败'),
        ('BLOCKED', '被阻止'),
    )
    
    class Meta:
        db_table = "log_management_login_log"
        verbose_name = "登录日志"
        verbose_name_plural = "登录日志"
        ordering = ['-login_time']
    
    # 用户信息
    username = models.CharField("用户名", max_length=150)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    
    # 登录信息
    login_status = models.CharField("登录状态", max_length=10, choices=LOGIN_STATUS_CHOICES)
    login_ip = models.GenericIPAddressField("登录IP")
    user_agent = models.TextField("用户代理", blank=True)
    
    # 地理位置信息
    country = models.CharField("国家", max_length=100, blank=True)
    region = models.CharField("地区", max_length=100, blank=True)
    city = models.CharField("城市", max_length=100, blank=True)
    
    # 失败原因
    failure_reason = models.CharField("失败原因", max_length=200, blank=True)
    
    # 时间信息
    login_time = models.DateTimeField("登录时间", auto_now_add=True)
    logout_time = models.DateTimeField("登出时间", null=True, blank=True)
    session_duration = models.DurationField("会话时长", null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} - {self.login_status} - {self.login_time}"