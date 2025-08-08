# _*_ coding:utf-8 _*_
from django.urls import path
from views import log_management_views

app_name = 'log_management'

urlpatterns = [
    # 日志管理主页
    path('', log_management_views.log_dashboard, name='dashboard'),
    
    # 系统日志
    path('system/', log_management_views.system_logs, name='system_logs'),
    path('system/data/', log_management_views.system_logs_data, name='system_logs_data'),
    path('system/<int:log_id>/', log_management_views.system_log_detail, name='system_log_detail'),
    
    # 用户操作日志
    path('operations/', log_management_views.user_operations, name='user_operations'),
    path('operations/data/', log_management_views.user_operations_data, name='user_operations_data'),
    
    # 错误日志
    path('errors/', log_management_views.error_logs, name='error_logs'),
    path('errors/data/', log_management_views.error_logs_data, name='error_logs_data'),
    path('errors/<int:log_id>/', log_management_views.error_log_detail, name='error_log_detail'),
    
    # 登录日志
    path('logins/', log_management_views.login_logs, name='login_logs'),
    path('logins/data/', log_management_views.login_logs_data, name='login_logs_data'),
    
    # 统计和管理
    path('statistics/', log_management_views.log_statistics, name='statistics'),
    path('clear/', log_management_views.clear_logs, name='clear_logs'),
]