# _*_ coding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import Permission, Group
from own_models.custom_user_models import CustomUser

# 我们使用Django内置的权限模型，不需要自定义模型
# 这个文件主要用于导入必要的模型，以便Django能够正确识别它们

# 用户-组关联模型（使用Django内置的）
# User.groups = ManyToManyField(Group)

# 组-权限关联模型（使用Django内置的）
# Group.permissions = ManyToManyField(Permission)

# 用户-权限关联模型（使用Django内置的）
# User.user_permissions = ManyToManyField(Permission)