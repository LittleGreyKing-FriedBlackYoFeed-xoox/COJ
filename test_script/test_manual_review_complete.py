#!/usr/bin/env python
import os
import django
import requests
import json

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.manual_review_models import ManualReviewRequest
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser

def test_manual_review_system():
    """Test the complete manual review system"""
    
    print("=== Manual Review System Test ===\n")
    
    # 1. Check if we have test data
    print("1. Checking test data...")
    
    # Check for problems
    problems = Problem.objects.all()[:5]
    if not problems:
        print("❌ No problems found. Please create some problems first.")
        return
    print(f"✅ Found {problems.count()} problems")
    
    # Check for users
    students = CustomUser.objects.filter(user_type='student')[:3]
    teachers = CustomUser.objects.filter(user_type='teacher')[:3]
    
    if not students:
        print("❌ No student users found. Please create some student users first.")
        return
    if not teachers:
        print("❌ No teacher users found. Please create some teacher users first.")
        return
        
    print(f"✅ Found {students.count()} students and {teachers.count()} teachers")
    
    # 2. Create test manual review requests
    print("\n2. Creating test manual review requests...")
    
    test_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# This is a recursive solution but not optimized
print(fibonacci(10))
"""
    
    # Create review requests for testing
    for i, student in enumerate(students):
        for j, problem in enumerate(problems[:2]):  # 2 problems per student
            # Check if request already exists
            existing = ManualReviewRequest.objects.filter(
                student=student,
                problem=problem,
                status='pending'
            ).first()
            
            if not existing:
                review_request = ManualReviewRequest.objects.create(
                    student=student,
                    problem=problem,
                    submitted_code=test_code + f"\n# Student: {student.username}, Problem: {problem.title}"
                )
                print(f"✅ Created review request {review_request.id} for {student.username} - {problem.title}")
    
    # 3. Display current status
    print("\n3. Current Manual Review Status:")
    
    pending_reviews = ManualReviewRequest.objects.filter(status='pending')
    reviewed_reviews = ManualReviewRequest.objects.filter(status='reviewed')
    rejected_reviews = ManualReviewRequest.objects.filter(status='rejected')
    
    print(f"📋 Pending reviews: {pending_reviews.count()}")
    print(f"✅ Reviewed: {reviewed_reviews.count()}")
    print(f"❌ Rejected: {rejected_reviews.count()}")
    
    # 4. Test URLs and endpoints
    print("\n4. Testing URL endpoints...")
    
    base_url = "http://localhost:8000"
    
    # Test URLs to check
    test_urls = [
        "/manual_review/list/",
        "/manual_review/request/",
    ]
    
    # Add specific review URLs
    if pending_reviews:
        test_urls.append(f"/manual_review/review/{pending_reviews.first().id}/")
        test_urls.append(f"/manual_review/result/{pending_reviews.first().id}/")
    
    print("📝 URL endpoints to test:")
    for url in test_urls:
        print(f"   {base_url}{url}")
    
    # 5. Display sample data for manual testing
    print("\n5. Sample data for manual testing:")
    
    if pending_reviews:
        sample_review = pending_reviews.first()
        print(f"📄 Sample Review Request ID: {sample_review.id}")
        print(f"   Student: {sample_review.student.username}")
        print(f"   Problem: {sample_review.problem.title}")
        print(f"   Status: {sample_review.status}")
        print(f"   Submitted: {sample_review.request_time}")
    
    # 6. Test data for AJAX requests
    print("\n6. Test data for AJAX requests:")
    
    if problems:
        sample_problem = problems.first()
        print(f"📝 Sample AJAX request data:")
        print(f"   URL: {base_url}/manual_review/request/")
        print(f"   Method: POST")
        print(f"   Data: {{")
        print(f"     'problem_id': {sample_problem.id},")
        print(f"     'code': 'def hello(): return \"Hello World\"',")
        print(f"     'csrfmiddlewaretoken': '[CSRF_TOKEN]'")
        print(f"   }}")
    
    print("\n=== Test Complete ===")
    print("\n📋 Next Steps:")
    print("1. Start the Django development server: python manage.py runserver")
    print("2. Visit the teacher review list: http://localhost:8000/manual_review/list/")
    print("3. Test student submission from problem detail pages")
    print("4. Test teacher review and rejection functionality")
    print("5. Check student review results")

if __name__ == "__main__":
    test_manual_review_system()