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
from django.db.models import Avg, Count, Q
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem
from own_models.student_practice import Submission, StudentStatistics
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance

def quick_populate_dashboard():
    """Quickly populate the dashboard with essential data"""
    try:
        # Get the first student user
        user = CustomUser.objects.filter(role=1).first()
        
        if not user:
            print("No student users found. Please create at least one student user first.")
            return
        
        print(f"Populating dashboard data for user: {user.username}")
        
        # Create or update learning feedback
        feedback, created = LearningFeedback.objects.get_or_create(user=user)
        feedback.success_rate = 75.5
        feedback.average_completion_time = 245.8
        feedback.strengths = "You demonstrate excellent understanding of algorithm concepts. Your problem-solving skills in data structures are impressive. You consistently perform well in programming language related problems."
        feedback.weaknesses = "You may benefit from more practice with database problems. Consider reviewing fundamental concepts in networking."
        feedback.recommendations = "Focus on practicing more database problems to strengthen your skills.\nReview the core concepts of networking and try applying them to different problems.\nContinue building on your strength in algorithms by tackling more advanced problems.\nMaintain a consistent practice schedule to improve your overall problem-solving skills."
        feedback.last_updated = timezone.now()
        feedback.save()
        
        # Create or update student statistics
        stats, created = StudentStatistics.objects.get_or_create(user=user)
        stats.total_submissions = 150
        stats.accepted_submissions = 113
        stats.total_problems_attempted = 75
        stats.total_problems_solved = 60
        stats.easy_problems_solved = 30
        stats.medium_problems_solved = 20
        stats.hard_problems_solved = 10
        stats.last_updated = timezone.now()
        stats.save()
        
        # Create knowledge point performances
        knowledge_points = [
            'algorithm', 'data_structure', 'programming_language', 
            'database', 'network', 'operating_system',
            'frontend', 'backend', 'computer_basics'
        ]
        
        # Clear existing performances
        KnowledgePointPerformance.objects.filter(user=user).delete()
        
        # Create new performances with realistic data
        for i, kp in enumerate(knowledge_points):
            # Vary the data to make it look realistic
            if kp in ['algorithm', 'data_structure', 'programming_language']:
                # Strong areas
                problems_attempted = random.randint(15, 25)
                success_rate = random.uniform(0.75, 0.95)
            elif kp in ['database', 'network']:
                # Weak areas
                problems_attempted = random.randint(5, 15)
                success_rate = random.uniform(0.4, 0.6)
            else:
                # Average areas
                problems_attempted = random.randint(8, 20)
                success_rate = random.uniform(0.6, 0.8)
            
            problems_solved = int(problems_attempted * success_rate)
            average_attempts = random.uniform(1.0, 3.0)
            average_time = random.uniform(100, 400)
            
            performance = KnowledgePointPerformance(
                user=user,
                knowledge_point=kp,
                problems_attempted=problems_attempted,
                problems_solved=problems_solved,
                average_attempts=average_attempts,
                average_time=average_time,
                last_updated=timezone.now()
            )
            performance.save()
            print(f"Created performance data for {kp}: {problems_solved}/{problems_attempted} problems solved")
        
        print(f"Successfully populated dashboard data for {user.username}")
        print("You can now view the learning feedback dashboard at http://127.0.0.1:8000/student/dashboard/")
        
    except Exception as e:
        print(f"Error populating dashboard data: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Starting to populate dashboard data...")
    quick_populate_dashboard()
    print("Done!")