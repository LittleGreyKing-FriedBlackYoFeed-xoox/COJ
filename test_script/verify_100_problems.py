#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem

def verify_problems():
    """Verify that all problems were created successfully"""
    try:
        # Get all problems
        problems = Problem.objects.all().order_by('-id')
        
        # Count problems
        total_count = problems.count()
        print(f"Total problems in database: {total_count}")
        
        # Count by difficulty
        easy_count = Problem.objects.filter(difficulty=1).count()
        medium_count = Problem.objects.filter(difficulty=2).count()
        hard_count = Problem.objects.filter(difficulty=3).count()
        
        print(f"\nDifficulty distribution:")
        print(f"Easy: {easy_count} ({easy_count/total_count*100:.1f}%)")
        print(f"Medium: {medium_count} ({medium_count/total_count*100:.1f}%)")
        print(f"Hard: {hard_count} ({hard_count/total_count*100:.1f}%)")
        
        # Count by knowledge point
        knowledge_points = {}
        for problem in problems:
            kp = problem.knowledge_point
            if kp in knowledge_points:
                knowledge_points[kp] += 1
            else:
                knowledge_points[kp] = 1
        
        print(f"\nKnowledge point distribution:")
        for kp, count in sorted(knowledge_points.items(), key=lambda x: x[1], reverse=True):
            print(f"{kp}: {count} ({count/total_count*100:.1f}%)")
        
        # List the 10 most recent problems
        print(f"\n10 most recent problems:")
        for i, problem in enumerate(problems[:10], 1):
            print(f"\n--- Problem {i} ---")
            print(f"ID: {problem.id}")
            print(f"Title: {problem.title}")
            print(f"Type: {problem.get_problem_type_display()}")
            print(f"Difficulty: {problem.get_difficulty_display()}")
            print(f"Knowledge Point: {problem.knowledge_point}")
        
    except Exception as e:
        print(f"Error verifying problems: {str(e)}")

if __name__ == "__main__":
    verify_problems()