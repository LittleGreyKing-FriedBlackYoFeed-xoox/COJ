#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

from own_models.manual_review_models import ManualReviewRequest
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem

print('=== Manual Review System Status ===')
print(f'Total review requests: {ManualReviewRequest.objects.count()}')
print(f'Pending reviews: {ManualReviewRequest.objects.filter(status="pending").count()}')
print(f'Reviewed: {ManualReviewRequest.objects.filter(status="reviewed").count()}')
print(f'Rejected: {ManualReviewRequest.objects.filter(status="rejected").count()}')

# 检查是否有教师用户 (role=2)
teachers = CustomUser.objects.filter(role=2)
print(f'Teachers: {teachers.count()}')
if teachers.exists():
    print(f'Teacher usernames: {[t.username for t in teachers[:5]]}')

# 检查是否有学生用户 (role=1)
students = CustomUser.objects.filter(role=1)
print(f'Students: {students.count()}')
if students.exists():
    print(f'Student usernames: {[s.username for s in students[:5]]}')

# 检查是否有问题
problems = Problem.objects.all()
print(f'Problems: {problems.count()}')
if problems.exists():
    print(f'Problem titles: {[p.title for p in problems[:5]]}')

# 如果没有测试数据，创建一些
if ManualReviewRequest.objects.count() == 0 and students.exists() and problems.exists():
    print('\n=== Creating test data ===')
    
    # 创建一些测试的复核请求
    test_codes = [
        "def hello():\n    print('Hello World')",
        "for i in range(10):\n    print(i)",
        "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)",
        "x = input('Enter a number: ')\nprint(int(x) * 2)",
        "def is_prime(n):\n    for i in range(2, n):\n        if n % i == 0:\n            return False\n    return True"
    ]
    
    for i, code in enumerate(test_codes):
        if i < len(students) and i < len(problems):
            student = students[i % len(students)]
            problem = problems[i % len(problems)]
            
            review_request = ManualReviewRequest.objects.create(
                student=student,
                problem=problem,
                code=code,
                status='pending'
            )
            print(f'Created review request {review_request.id} for {student.username} - {problem.title}')
    
    print(f'Created {len(test_codes)} test review requests')

print('\n=== Current Review Requests ===')
for review in ManualReviewRequest.objects.all()[:10]:
    print(f'ID: {review.id}, Student: {review.student.username}, Problem: {review.problem.title}, Status: {review.status}')