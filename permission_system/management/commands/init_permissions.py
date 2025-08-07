# _*_ coding:utf-8 _*_
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from own_models.custom_user_models import CustomUser

class Command(BaseCommand):
    help = '初始化权限系统，创建默认的权限和用户组'
    
    def handle(self, *args, **options):
        self.stdout.write('开始初始化权限系统...')
        
        # 创建内容类型
        content_type, created = ContentType.objects.get_or_create(
            app_label='own_models',
            model='customuser'
        )
        
        # 创建基本权限
        permissions = [
            ('view_users', '查看用户列表'),
            ('add_user', '添加用户'),
            ('change_user', '修改用户'),
            ('delete_user', '删除用户'),
            ('view_reports', '查看报表'),
            ('export_data', '导出数据'),
            ('manage_system', '管理系统'),
        ]
        
        created_permissions = []
        for codename, name in permissions:
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type
            )
            created_permissions.append(permission)
            if created:
                self.stdout.write(f'创建权限: {name}')
            else:
                self.stdout.write(f'权限已存在: {name}')
        
        # 创建用户组
        # 学生组
        student_group, created = Group.objects.get_or_create(name='学生')
        if created:
            self.stdout.write('创建用户组: 学生')
        else:
            self.stdout.write('用户组已存在: 学生')
        
        # 为学生组分配权限
        student_permissions = Permission.objects.filter(codename='view_users')
        student_group.permissions.set(student_permissions)
        self.stdout.write('为学生组分配权限: 查看用户列表')
        
        # 教师组
        teacher_group, created = Group.objects.get_or_create(name='教师')
        if created:
            self.stdout.write('创建用户组: 教师')
        else:
            self.stdout.write('用户组已存在: 教师')
        
        # 为教师组分配权限
        teacher_permissions = Permission.objects.filter(
            codename__in=['view_users', 'add_user', 'change_user', 'view_reports']
        )
        teacher_group.permissions.set(teacher_permissions)
        self.stdout.write('为教师组分配权限: 查看用户列表, 添加用户, 修改用户, 查看报表')
        
        # 管理员组
        admin_group, created = Group.objects.get_or_create(name='管理员')
        if created:
            self.stdout.write('创建用户组: 管理员')
        else:
            self.stdout.write('用户组已存在: 管理员')
        
        # 为管理员组分配所有权限
        admin_group.permissions.set(Permission.objects.all())
        self.stdout.write('为管理员组分配所有权限')
        
        # 为现有用户分配用户组
        for user in CustomUser.objects.all():
            if user.role == 1:  # 学生
                user.groups.add(student_group)
                self.stdout.write(f'将用户 {user.username} 添加到学生组')
            elif user.role == 2:  # 教师
                user.groups.add(teacher_group)
                self.stdout.write(f'将用户 {user.username} 添加到教师组')
            elif user.role == 3:  # 管理员
                user.groups.add(admin_group)
                self.stdout.write(f'将用户 {user.username} 添加到管理员组')
        
        self.stdout.write(self.style.SUCCESS('权限系统初始化完成!'))