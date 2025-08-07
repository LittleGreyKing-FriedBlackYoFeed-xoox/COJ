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
from own_models.custom_user_models import CustomUser
from own_models.ranking_system_models import RankingSystem
from own_models.problem_models import Problem
from own_models.student_practice import Submission, StudentStatistics

def create_realistic_submissions(user, problems):
    """Create realistic submission data for a user"""
    print(f"Creating submission data for user: {user.username}")
    
    # Define programming languages
    languages = ['python', 'java', 'cpp', 'c', 'javascript']
    
    # Define possible submission statuses with weighted probabilities
    statuses = {
        'accepted': 0.6,  # 60% chance of acceptance
        'wrong_answer': 0.2,  # 20% chance of wrong answer
        'time_limit_exceeded': 0.1,  # 10% chance of time limit exceeded
        'runtime_error': 0.05,  # 5% chance of runtime error
        'compile_error': 0.05,  # 5% chance of compile error
    }
    
    # Determine how many problems this user will attempt
    # More active users will attempt more problems
    activity_level = random.random()  # Random value between 0 and 1
    
    if activity_level > 0.8:  # Very active users (20%)
        num_problems_to_attempt = int(len(problems) * random.uniform(0.7, 0.9))
    elif activity_level > 0.5:  # Moderately active users (30%)
        num_problems_to_attempt = int(len(problems) * random.uniform(0.4, 0.7))
    elif activity_level > 0.2:  # Somewhat active users (30%)
        num_problems_to_attempt = int(len(problems) * random.uniform(0.2, 0.4))
    else:  # Less active users (20%)
        num_problems_to_attempt = int(len(problems) * random.uniform(0.05, 0.2))
    
    # Ensure at least 1 problem is attempted
    num_problems_to_attempt = max(1, num_problems_to_attempt)
    
    # Randomly select problems to attempt
    problems_to_attempt = random.sample(list(problems), min(num_problems_to_attempt, len(problems)))
    
    # Track which problems were solved
    solved_problems = set()
    total_submissions = 0
    
    # For each problem, create submissions
    for problem in problems_to_attempt:
        # Determine how many submissions for this problem
        # Some problems might need multiple attempts
        num_submissions = random.randint(1, 5)
        
        # Last submission has higher chance of being accepted
        for i in range(num_submissions):
            # Choose a random language
            language = random.choice(languages)
            
            # Determine submission status
            if i == num_submissions - 1:  # Last submission has higher chance of success
                status = random.choices(
                    list(statuses.keys()),
                    weights=[0.8, 0.1, 0.05, 0.03, 0.02],  # Higher chance of acceptance
                    k=1
                )[0]
            else:
                status = random.choices(
                    list(statuses.keys()),
                    weights=list(statuses.values()),
                    k=1
                )[0]
            
            # Create submission
            submission = Submission(
                user=user,
                problem=problem,
                code=f"// Sample code for {problem.title}\n// Submission {i+1} for this problem",
                language=language,
                status=status,
                execution_time=random.randint(10, 500),  # Random execution time between 10ms and 500ms
                memory_used=random.randint(1000, 10000),  # Random memory usage between 1MB and 10MB
                created_at=timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23)),
                updated_at=timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
            )
            
            if status == 'accepted':
                solved_problems.add(problem.id)
                
            submission.save()
            total_submissions += 1
            
            print(f"  Created submission for problem '{problem.title}': {status}")
    
    # Update or create student statistics
    try:
        stats = StudentStatistics.objects.get(user=user)
    except StudentStatistics.DoesNotExist:
        stats = StudentStatistics(user=user)
    
    stats.total_submissions = total_submissions
    stats.accepted_submissions = Submission.objects.filter(user=user, status='accepted').count()
    stats.total_problems_attempted = len(problems_to_attempt)
    stats.total_problems_solved = len(solved_problems)
    
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
    
    stats.save()
    
    print(f"  Updated statistics for {user.username}: {stats.total_problems_solved} problems solved, {stats.total_submissions} submissions")
    
    return len(solved_problems), total_submissions

def update_ranking_data(clear=False):
    """
    Update ranking data with realistic submission and completion statistics
    
    Args:
        clear (bool): Whether to clear existing submission data before creating new data
    """
    print('Starting to update ranking data with realistic statistics...')
    
    # Get all users
    users = CustomUser.objects.all()
    user_count = users.count()
    
    if user_count == 0:
        print('No users found in the system.')
        return
        
    print(f'Found {user_count} users.')
    
    # Get all problems
    problems = Problem.objects.all()
    problem_count = problems.count()
    
    if problem_count == 0:
        print('No problems found in the system. Creating sample problems...')
        # Create some sample problems if none exist
        difficulties = [1, 2, 3]  # Easy, Medium, Hard
        problem_types = [1, 2, 3, 4, 5]  # Using the PROBLEM_TYPE_CHOICES from the model
        knowledge_points = ['data_structure', 'algorithm', 'database', 'network', 'operating_system', 
                           'frontend', 'backend', 'computer_basics', 'programming_language']
        
        for i in range(1, 31):  # Create 30 sample problems
            difficulty = random.choice(difficulties)
            problem_type = random.choice(problem_types)
            knowledge_point = random.choice(knowledge_points)
            
            problem = Problem(
                title=f"Sample Problem {i}",
                description=f"This is a sample problem {i} for testing purposes.",
                difficulty=difficulty,
                problem_type=problem_type,
                knowledge_point=knowledge_point,
                created_by=users.first(),  # Assign to the first user
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            problem.save()
            
            print(f"Created sample problem: {problem.title}")
        
        problems = Problem.objects.all()
        problem_count = problems.count()
    
    print(f'Found {problem_count} problems.')
    
    # Clear existing submission data if requested
    if clear:
        print("Clearing existing submission data...")
        Submission.objects.all().delete()
        StudentStatistics.objects.all().delete()
        print("Existing data cleared.")
    
    # Create or update ranking data for each user
    for user in users:
        # Create realistic submission data
        problems_completed, total_attempts = create_realistic_submissions(user, problems)
        
        # Create or update ranking record
        ranking, created = RankingSystem.objects.get_or_create(user=user)
        ranking.problems_completed = problems_completed
        ranking.total_attempts = total_attempts
        ranking.last_updated = timezone.now()
        ranking.save()
        
        action = "Created" if created else "Updated"
        print(f'{action} ranking for {user.username}: {problems_completed} problems completed, {total_attempts} total attempts')
    
    # Update all rankings to recalculate positions
    RankingSystem.update_all_rankings()
    print('Successfully updated ranking data for all users!')

def main():
    """
    Script to update ranking data
    
    Usage:
        python update_ranking_data.py [--clear]
        
    Arguments:
        --clear (optional): Clear existing submission data before creating new data
    """
    import sys
    
    clear = False
    if len(sys.argv) > 1 and sys.argv[1] == '--clear':
        clear = True
        print("Will clear existing data before updating")
    
    update_ranking_data(clear)

if __name__ == "__main__":
    main()