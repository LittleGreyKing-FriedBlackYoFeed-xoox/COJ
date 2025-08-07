import os
import sys
import django
import random
from datetime import timedelta

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

from django.utils import timezone
from django.db import transaction
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem
from own_models.student_practice import Submission, StudentStatistics
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance

def generate_sample_data_for_current_user():
    """Generate sample data for the currently logged-in user"""
    try:
        # Get the first student user (assuming this is the logged-in user)
        user = CustomUser.objects.filter(role=1).first()
        
        if not user:
            print("No student users found. Please create at least one student user first.")
            return
        
        print(f"Generating sample data for user: {user.username}")
        
        # Get or create some problems
        problems = Problem.objects.all()
        if problems.count() < 20:
            print("Not enough problems found. Creating some sample problems...")
            problems = create_sample_problems(20)
        
        # Generate submissions
        with transaction.atomic():
            generate_submissions_for_user(user, problems, 50)
        
        # Update learning feedback
        update_learning_feedback(user)
        
        print(f"Successfully generated sample data for {user.username}")
        print("You can now view the learning feedback dashboard at http://127.0.0.1:8000/student/dashboard/")
        
    except Exception as e:
        print(f"Error generating sample data: {str(e)}")

def create_sample_problems(num_problems=20):
    """Create a small number of sample problems"""
    print(f"Creating {num_problems} sample problems...")
    
    # Define problem attributes
    difficulties = [1, 2, 3]  # Easy, Medium, Hard
    problem_types = [1, 2, 3, 4, 5]  # Using the PROBLEM_TYPE_CHOICES from the model
    knowledge_points = [
        'data_structure', 'algorithm', 'database', 'network', 'operating_system',
        'frontend', 'backend', 'computer_basics', 'programming_language'
    ]
    
    # Get a user to be the creator
    creator = CustomUser.objects.first()
    
    problems = []
    for i in range(1, num_problems + 1):
        difficulty = random.choice(difficulties)
        problem_type = random.choice(problem_types)
        knowledge_point = random.choice(knowledge_points)
        
        problem = Problem(
            title=f"Sample Problem {i}",
            description=f"This is a sample problem {i} for testing purposes. It covers concepts in {knowledge_point}.",
            difficulty=difficulty,
            problem_type=problem_type,
            knowledge_point=knowledge_point,
            created_by=creator,
            created_at=timezone.now() - timedelta(days=random.randint(1, 30)),
            updated_at=timezone.now() - timedelta(days=random.randint(0, 15))
        )
        problem.save()
        problems.append(problem)
        print(f"Created problem: {problem.title}")
    
    return problems

def generate_submissions_for_user(user, problems, num_submissions=50):
    """Generate a reasonable number of submissions for a user"""
    print(f"Generating {num_submissions} submissions for {user.username}...")
    
    # Define submission attributes
    languages = ['python', 'java', 'cpp', 'c', 'javascript']
    statuses = ['accepted', 'wrong_answer', 'time_limit_exceeded', 'runtime_error', 'compile_error']
    status_weights = [0.7, 0.15, 0.08, 0.04, 0.03]  # Higher success rate for better visuals
    
    # Track statistics
    problems_attempted = set()
    problems_solved = set()
    
    # Generate submissions
    for _ in range(num_submissions):
        # Select a random problem
        problem = random.choice(problems)
        problems_attempted.add(problem.id)
        
        # Determine submission attributes
        language = random.choice(languages)
        status = random.choices(statuses, weights=status_weights, k=1)[0]
        execution_time = random.randint(10, 500)  # 10ms to 500ms
        memory_used = random.randint(1000, 10000)  # 1MB to 10MB
        
        # Create submission with a random date in the past 30 days
        submission_date = timezone.now() - timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        
        submission = Submission(
            user=user,
            problem=problem,
            code=f"// Sample code for {problem.title}\n// This is a {status} submission",
            language=language,
            status=status,
            execution_time=execution_time,
            memory_used=memory_used,
            created_at=submission_date,
            updated_at=submission_date
        )
        submission.save()
        
        if status == 'accepted':
            problems_solved.add(problem.id)
    
    print(f"Generated {num_submissions} submissions")
    print(f"Problems attempted: {len(problems_attempted)}, Problems solved: {len(problems_solved)}")
    
    # Update student statistics
    try:
        stats = StudentStatistics.objects.get(user=user)
    except StudentStatistics.DoesNotExist:
        stats = StudentStatistics(user=user)
    
    stats.total_submissions = Submission.objects.filter(user=user).count()
    stats.accepted_submissions = Submission.objects.filter(user=user, status='accepted').count()
    stats.total_problems_attempted = len(problems_attempted)
    stats.total_problems_solved = len(problems_solved)
    
    # Update difficulty statistics
    stats.easy_problems_solved = Submission.objects.filter(
        user=user, status='accepted', problem__difficulty=1
    ).values('problem').distinct().count()
    
    stats.medium_problems_solved = Submission.objects.filter(
        user=user, status='accepted', problem__difficulty=2
    ).values('problem').distinct().count()
    
    stats.hard_problems_solved = Submission.objects.filter(
        user=user, status='accepted', problem__difficulty=3
    ).values('problem').distinct().count()
    
    stats.last_updated = timezone.now()
    stats.save()

def update_learning_feedback(user):
    """Update learning feedback for a user"""
    print(f"Updating learning feedback for {user.username}...")
    
    # Get or create learning feedback
    feedback, created = LearningFeedback.objects.get_or_create(user=user)
    
    # Update feedback
    feedback.update_feedback()
    
    # Generate realistic feedback text
    strengths = ["algorithm", "data_structure", "programming_language"]
    weaknesses = ["database", "network"]
    
    strength_text = [
        "You demonstrate excellent understanding of algorithm concepts.",
        "Your problem-solving skills in data structures are impressive.",
        "You consistently perform well in programming language related problems."
    ]
    
    weakness_text = [
        "You may benefit from more practice with database problems.",
        "Consider reviewing fundamental concepts in networking."
    ]
    
    recommendation_text = [
        "Focus on practicing more database problems to strengthen your skills.",
        "Review the core concepts of networking and try applying them to different problems.",
        "Continue building on your strength in algorithms by tackling more advanced problems.",
        "Maintain a consistent practice schedule to improve your overall problem-solving skills."
    ]
    
    feedback.strengths = ". ".join(strength_text)
    feedback.weaknesses = ". ".join(weakness_text)
    feedback.recommendations = "\n".join(recommendation_text)
    feedback.last_updated = timezone.now()
    feedback.save()
    
    # Update knowledge point performances
    KnowledgePointPerformance.update_all_performances(user)
    
    print(f"Learning feedback updated for {user.username}")

if __name__ == "__main__":
    print("Starting to generate minimal learning feedback data...")
    generate_sample_data_for_current_user()
    print("Done!")