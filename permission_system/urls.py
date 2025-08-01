# _*_ coding:utf-8 _*_
from django.urls import path
from . import views

app_name = 'permission_system'

urlpatterns = [
    # 权限管理仪表板
    path('', views.dashboard, name='dashboard'),
    
    # 权限管理
    path('permissions/', views.permission_list, name='permission_list'),
    path('permissions/data/', views.permission_list_data, name='permission_list_data'),
    path('permissions/create/', views.permission_create, name='permission_create'),
    
    # 用户组管理
    path('groups/', views.group_list, name='group_list'),
    path('groups/data/', views.group_list_data, name='group_list_data'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:group_id>/edit/', views.group_edit, name='group_edit'),
    
    # 用户权限管理
    path('users/', views.user_list, name='user_list'),
    path('users/data/', views.user_list_data, name='user_list_data'),
    path('users/permissions/', views.user_permissions, name='user_permissions'),
    
    # 初始化权限系统
    path('init/', views.init_permissions, name='init_permissions'),
]