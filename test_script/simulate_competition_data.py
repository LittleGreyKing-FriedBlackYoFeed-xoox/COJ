#!/usr/bin/env python
import os
import django
import random
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.organize_competitions_models import Competition, Paper, PaperAssignment
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser
from django.utils import timezone

def create_test_competitions_and_papers():
    """创建测试竞赛和试卷数据"""
    print("=== 创建竞赛答题模拟数据 ===\n")
    
    # 1. 获取或创建教师用户
    teacher_users = CustomUser.objects.filter(user_type='teacher')
    if not teacher_users:
        print("❌ 没有找到教师用户，请先创建教师用户")
        return
    
    teacher = teacher_users.first()
    print(f"✅ 使用教师用户: {teacher.username}")
    
    # 2. 获取学生用户
    student_users = CustomUser.objects.filter(user_type='student')
    if student_users.count() < 10:
        print(f"⚠️  学生用户数量不足 ({student_users.count()}个)，建议至少10个学生用户")
    
    students = list(student_users[:20])  # 最多取20个学生
    print(f"✅ 找到 {len(students)} 个学生用户")
    
    # 3. 获取题目
    problems = list(Problem.objects.all()[:10])  # 取前10个题目
    if len(problems) < 5:
        print(f"❌ 题目数量不足 ({len(problems)}个)，请先创建更多题目")
        return
    
    print(f"✅ 找到 {len(problems)} 个题目")
    
    # 4. 创建竞赛和试卷
    competitions_data = [
        {
            'name': 'Python编程基础竞赛',
            'description': '面向初学者的Python编程竞赛，包含基础语法和算法题目',
            'papers': [
                {'name': 'Python基础试卷A', 'problems': problems[:5]},
                {'name': 'Python基础试卷B', 'problems': problems[2:7]},
            ]
        },
        {
            'name': '算法设计与分析竞赛',
            'description': '中级算法竞赛，考查数据结构和算法设计能力',
            'papers': [
                {'name': '算法设计试卷A', 'problems': problems[3:8]},
                {'name': '算法设计试卷B', 'problems': problems[5:10]},
            ]
        }
    ]
    
    created_papers = []
    
    for comp_data in competitions_data:
        # 检查竞赛是否已存在
        competition, created = Competition.objects.get_or_create(
            name=comp_data['name'],
            creator=teacher,
            defaults={'description': comp_data['description']}
        )
        
        if created:
            print(f"✅ 创建竞赛: {competition.name}")
        else:
            print(f"📋 竞赛已存在: {competition.name}")
        
        for paper_data in comp_data['papers']:
            # 检查试卷是否已存在
            paper, created = Paper.objects.get_or_create(
                name=paper_data['name'],
                competition=competition,
                defaults={}
            )
            
            if created:
                paper.problems.set(paper_data['problems'])
                print(f"✅ 创建试卷: {paper.name}")
            else:
                print(f"📋 试卷已存在: {paper.name}")
            
            created_papers.append(paper)
    
    # 5. 为试卷分配学生并模拟答题数据
    print("\n=== 模拟学生答题数据 ===")
    
    for paper in created_papers:
        print(f"\n📝 处理试卷: {paper.name}")
        
        # 为每个试卷随机分配15-25个学生
        num_students = min(random.randint(15, 25), len(students))
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
                simulate_student_progress(assignment)
                print(f"  ✅ 分配给学生: {student.username}")
    
    print(f"\n=== 数据创建完成 ===")
    print(f"📊 创建的试卷ID: {[paper.id for paper in created_papers]}")
    print(f"🌐 测试URL: http://127.0.0.1:8000/teacher/competitions/paper/{created_papers[0].id}/")
    
    return created_papers

def simulate_student_progress(assignment):
    """模拟学生答题进度"""
    # 随机生成答题状态
    completion_scenarios = [
        {'is_completed': True, 'progress': 100, 'rate': random.randint(80, 100)},  # 已完成
        {'is_completed': False, 'progress': random.randint(60, 99), 'rate': random.randint(60, 90)},  # 进行中
        {'is_completed': False, 'progress': random.randint(20, 59), 'rate': random.randint(40, 70)},  # 刚开始
        {'is_completed': False, 'progress': 0, 'rate': 0},  # 未开始
    ]
    
    # 权重：已完成30%，进行中40%，刚开始25%，未开始5%
    scenario = random.choices(
        completion_scenarios,
        weights=[30, 40, 25, 5],
        k=1
    )[0]
    
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

def add_model_fields():
    """为PaperAssignment模型添加缺失的字段"""
    print("\n=== 检查模型字段 ===")
    
    # 检查PaperAssignment模型是否有需要的字段
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA table_info(own_models_paperassignment)")
        columns = [row[1] for row in cursor.fetchall()]
        
        missing_fields = []
        required_fields = [
            'completion_progress', 'completion_rate', 'total_duration_minutes', 'first_login_time'
        ]
        
        for field in required_fields:
            if field not in columns:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"⚠️  模型缺少字段: {missing_fields}")
            print("建议在 organize_competitions_models.py 中添加这些字段")
        else:
            print("✅ 模型字段完整")

if __name__ == "__main__":
    try:
        add_model_fields()
        papers = create_test_competitions_and_papers()
        
        print("\n=== 测试建议 ===")
        print("1. 启动开发服务器: python manage.py runserver")
        if papers:
            print(f"2. 访问试卷详情页面: http://127.0.0.1:8000/teacher/competitions/paper/{papers[0].id}/")
        print("3. 检查分页和题目链接功能")
        print("4. 验证用户答题数据显示")
        
    except Exception as e:
        print(f"❌ 执行出错: {e}")
        import traceback
        traceback.print_exc()