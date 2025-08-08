from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
from django.urls import path, include
from views.userViews import index

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),
    path("", index, name="home"),  # 首页
    path('code_duplication_check/', include('urls.code_duplication_check_urls')),
    path('notification/', include('urls.notification_urls')),
    path("admin/", admin.site.urls),
    
    # 用户相关URL
    path("", include("urls.user_urls")),
    
    # 题目管理相关URL
    path("", include("urls.problem_urls")),
    
    # COJ系统相关URL
    path("", include("urls.coj_urls")),
    
    # 学生题目练习相关URL
    path("student/", include("urls.student_practice_urls")),
    
    # 权限管理系统URL
    path("permissions/", include("permission_system.urls")),
    
    # 排名系统URL
    path("student/", include("urls.ranking_system_urls")),
    
    # 学习反馈系统URL
    path("student/", include("urls.learning_feedback_urls")),
    
    # 组织竞赛相关URL
    path("teacher/competitions/", include("urls.organize_competitions_urls")),
    # 人工复核系统URL
    path("manual_review/", include(("urls.manual_review_urls", "manual_review"), namespace="manual_review")),
    
    # 日志管理系统URL
    path("log_management/", include(("urls.log_management_urls", "log_management"), namespace="log_management")),
]
