# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models

"""
更新字段后，执行命令：

1. python manage.py makemigrations own_models
2. python manage.py sqlmigrate own_models 0001  # 查看将执行的SQL
3. python manage.py migrate / python manage.py migrate own_models --fake-initial
"""

# 普通用户模型（不用于认证），models.Model ，如果带权限认证，需要继承自AbstractBaseUser
# class User(AbstractBaseUser):
class CustomUser(models.Model):
    """
    自定义用户模型
    角色说明：
    - 1: 学生
    - 2: 教师
    - 3: 管理员
    """

    class Meta:
        db_table = "own_models_custom_user"  # 指定明确的表名
        verbose_name = "自定义用户"
        verbose_name_plural = "自定义用户"

    ROLE_CHOICES = (
        (1, "学生"),
        (2, "教师"),
        (3, "管理员"),
    )

    # 用户基本信息
    username = models.CharField(("用户名"), max_length=150, unique=True)
    password = models.CharField(("密码"), max_length=128)
    email = models.EmailField(("邮箱"), blank=True)
    is_active = models.BooleanField(("是否激活"), default=True)
    is_staff = models.BooleanField(("是否职员"), default=False) # 新增 is_staff 字段
    date_joined = models.DateTimeField(("注册时间"), auto_now_add=True)
    last_login = models.DateTimeField(("最后登录"), blank=True, null=True)
    
    # 自定义字段
    usercode = models.CharField(("用户编码"), max_length=120)
    mobile = models.CharField(("手机号"), max_length=20, blank=True, null=True)
    role = models.PositiveSmallIntegerField(("角色"), choices=ROLE_CHOICES, default=1)
    real_name = models.CharField(("真实姓名"), max_length=50, blank=True)
    avatar = models.ImageField(("头像"), upload_to="avatars/", blank=True, null=True)
    gender = models.CharField(
        ("性别"), max_length=10, choices=(("M", "男"), ("F", "女")), blank=True
    )
    birth_date = models.DateField(("出生日期"), blank=True, null=True)
    remark = models.TextField(("备注"), blank=True, null=True)
    
    # 角色相关方法
    def is_student(self):
        return self.role == 1

    def is_teacher(self):
        return self.role == 2

    def is_admin(self):
        return self.role == 3
    
        
    def __str__(self):
        return self.username
