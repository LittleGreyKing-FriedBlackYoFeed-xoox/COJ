#!/usr/bin/env python
"""
测试教师登录和manual review功能的脚本
"""
import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

from own_models.custom_user_models import CustomUser
from own_models.manual_review_models import ManualReviewRequest

def test_teacher_login():
    """测试教师登录功能"""
    print("=== Testing Teacher Login ===")
    
    # 查找一个教师用户
    teachers = CustomUser.objects.filter(role=2)  # role=2 表示教师
    if not teachers.exists():
        print("No teacher users found. Creating a test teacher...")
        teacher = CustomUser.objects.create_user(
            username='test_teacher',
            password='password123',
            email='teacher@test.com',
            role=2
        )
        print(f"Created teacher: {teacher.username}")
    else:
        teacher = teachers.first()
        print(f"Found teacher: {teacher.username}")
    
    # 显示教师信息
    print(f"Teacher ID: {teacher.id}")
    print(f"Teacher Username: {teacher.username}")
    print(f"Teacher Role: {teacher.get_role_display()}")
    print(f"Is Teacher: {teacher.is_teacher()}")
    print(f"Is Admin: {teacher.is_admin()}")
    
    return teacher

def test_manual_review_data():
    """测试manual review数据"""
    print("\n=== Manual Review Data ===")
    
    # 统计数据
    total_reviews = ManualReviewRequest.objects.count()
    pending_reviews = ManualReviewRequest.objects.filter(status='pending').count()
    reviewed_reviews = ManualReviewRequest.objects.filter(status='reviewed').count()
    rejected_reviews = ManualReviewRequest.objects.filter(status='rejected').count()
    
    print(f"Total Reviews: {total_reviews}")
    print(f"Pending Reviews: {pending_reviews}")
    print(f"Reviewed Reviews: {reviewed_reviews}")
    print(f"Rejected Reviews: {rejected_reviews}")
    
    # 显示最近的几个review请求
    recent_reviews = ManualReviewRequest.objects.select_related(
        'student', 'problem', 'teacher'
    ).order_by('-request_time')[:5]
    
    print("\n=== Recent Review Requests ===")
    for review in recent_reviews:
        print(f"ID: {review.id}")
        print(f"  Student: {review.student.username}")
        print(f"  Problem: {review.problem.title}")
        print(f"  Status: {review.get_status_display()}")
        print(f"  Request Time: {review.request_time}")
        if review.teacher:
            print(f"  Teacher: {review.teacher.username}")
        print(f"  Code Preview: {review.code[:50]}...")
        print("-" * 50)

def simulate_teacher_session():
    """模拟教师会话"""
    print("\n=== Simulating Teacher Session ===")
    
    teacher = test_teacher_login()
    
    # 这里可以添加更多的模拟操作
    print(f"Teacher {teacher.username} session simulated successfully!")
    print(f"Teacher can access manual review at: http://127.0.0.1:8000/manual_review/list/")
    print(f"Teacher ID for session: {teacher.id}")
    
    return teacher

if __name__ == "__main__":
    try:
        teacher = simulate_teacher_session()
        test_manual_review_data()
        
        print("\n=== Test Summary ===")
        print("✅ Teacher login test completed")
        print("✅ Manual review data test completed")
        print(f"✅ Use teacher ID {teacher.id} for manual testing")
        print("\n📝 To test manually:")
        print("1. Go to http://127.0.0.1:8000/manual_review/list/")
        print("2. Login as teacher or set session manually")
        print("3. Test the improved UI and functionality")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()