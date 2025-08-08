from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random

from own_models.organize_competitions_models import Competition, Paper, PaperAssignment
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser


class Command(BaseCommand):
    help = '创建竞赛和答题模拟数据'

    def handle(self, *args, **options):
        self.stdout.write("=== 创建竞赛答题模拟数据 ===\n")
        
        # 1. 获取或创建教师用户 (role=2)
        teacher_users = CustomUser.objects.filter(role=2)
        if not teacher_users:
            self.stdout.write(self.style.ERROR("❌ 没有找到教师用户，请先创建教师用户"))
            return
        
        teacher = teacher_users.first()
        self.stdout.write(f"✅ 使用教师用户: {teacher.username}")
        
        # 2. 获取学生用户 (role=1)
        student_users = CustomUser.objects.filter(role=1)
        if student_users.count() < 5:
            self.stdout.write(self.style.WARNING(f"⚠️  学生用户数量不足 ({student_users.count()}个)，建议至少5个学生用户"))
        
        students = list(student_users[:30])  # 最多取30个学生
        self.stdout.write(f"✅ 找到 {len(students)} 个学生用户")
        
        # 3. 获取题目
        problems = list(Problem.objects.all()[:10])  # 取前10个题目
        if len(problems) < 5:
            self.stdout.write(self.style.ERROR(f"❌ 题目数量不足 ({len(problems)}个)，请先创建更多题目"))
            return
        
        self.stdout.write(f"✅ 找到 {len(problems)} 个题目")
        
        # 4. 创建竞赛和试卷
        competition, created = Competition.objects.get_or_create(
            name='Python编程基础竞赛',
            creator=teacher,
            defaults={'description': '面向初学者的Python编程竞赛，包含基础语法和算法题目'}
        )
        
        if created:
            self.stdout.write(f"✅ 创建竞赛: {competition.name}")
        else:
            self.stdout.write(f"📋 竞赛已存在: {competition.name}")
        
        # 创建试卷
        paper, created = Paper.objects.get_or_create(
            name='Python基础试卷A',
            competition=competition,
            defaults={}
        )
        
        if created:
            paper.problems.set(problems[:5])
            self.stdout.write(f"✅ 创建试卷: {paper.name}")
        else:
            self.stdout.write(f"📋 试卷已存在: {paper.name}")
        
        # 5. 为试卷分配学生并模拟答题数据
        self.stdout.write(f"\n📝 处理试卷: {paper.name}")
        
        # 为试卷随机分配20-30个学生
        num_students = min(random.randint(20, 30), len(students))
        assigned_students = random.sample(students, num_students)
        
        for student in assigned_students:
            # 检查是否已经分配
            assignment, created = PaperAssignment.objects.get_or_create(
                paper=paper,
                user=student,
                defaults={
                    'assigned_at': timezone.now() - timedelta(days=random.randint(1, 30))
                }
            )
            
            if created:
                # 模拟答题状态
                self.simulate_progress(assignment)
                self.stdout.write(f"  ✅ 分配给学生: {student.username}")
        
        self.stdout.write(f"\n=== 数据创建完成 ===")
        self.stdout.write(f"📊 创建的试卷ID: {paper.id}")
        self.stdout.write(self.style.SUCCESS(f"🌐 测试URL: http://127.0.0.1:8000/teacher/competitions/paper/{paper.id}/"))

    def simulate_progress(self, assignment):
        """模拟学生答题进度"""
        # 随机生成答题状态
        scenarios = [
            {'is_completed': True, 'progress': 100, 'rate': random.randint(80, 100)},  # 已完成
            {'is_completed': False, 'progress': random.randint(60, 99), 'rate': random.randint(60, 90)},  # 进行中
            {'is_completed': False, 'progress': random.randint(20, 59), 'rate': random.randint(40, 70)},  # 刚开始
            {'is_completed': False, 'progress': 0, 'rate': 0},  # 未开始
        ]
        
        # 权重：已完成30%，进行中40%，刚开始25%，未开始5%
        scenario = random.choices(scenarios, weights=[30, 40, 25, 5], k=1)[0]
        
        # 更新分配记录
        assignment.is_completed = scenario['is_completed']
        assignment.completion_progress = scenario['progress']
        assignment.completion_rate = scenario['rate']
        
        # 设置答题时长
        if scenario['progress'] > 0:
            assignment.total_duration_minutes = random.randint(30, 180)
            assignment.first_login_time = assignment.assigned_at + timedelta(
                hours=random.randint(0, 24)
            )
        else:
            assignment.total_duration_minutes = 0
            assignment.first_login_time = None
        
        if scenario['is_completed']:
            assignment.completed_at = assignment.assigned_at + timedelta(
                hours=random.randint(1, 72)
            )
        
        assignment.save()