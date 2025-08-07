#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem

def verify_new_problems():
    """Verify that all new problems were created successfully"""
    try:
        # Get all problems
        problems = Problem.objects.all().order_by('-id')
        
        # Count problems
        total_count = problems.count()
        print(f"Total problems in database: {total_count}")
        
        # Get the 100 most recent problems
        recent_problems = problems[:100]
        
        # Count by difficulty
        easy_count = sum(1 for p in recent_problems if p.difficulty == 1)
        medium_count = sum(1 for p in recent_problems if p.difficulty == 2)
        hard_count = sum(1 for p in recent_problems if p.difficulty == 3)
        
        print(f"\nDifficulty distribution of 100 newest problems:")
        print(f"Easy: {easy_count} ({easy_count/100*100:.1f}%)")
        print(f"Medium: {medium_count} ({medium_count/100*100:.1f}%)")
        print(f"Hard: {hard_count} ({hard_count/100*100:.1f}%)")
        
        # Count by knowledge point
        knowledge_points = {}
        for problem in recent_problems:
            kp = problem.knowledge_point
            if kp in knowledge_points:
                knowledge_points[kp] += 1
            else:
                knowledge_points[kp] = 1
        
        print(f"\nKnowledge point distribution of 100 newest problems:")
        for kp, count in sorted(knowledge_points.items(), key=lambda x: x[1], reverse=True):
            print(f"{kp}: {count} ({count/100*100:.1f}%)")
        
        # List the 10 most recent problems
        print(f"\n10 most recent problems:")
        for i, problem in enumerate(recent_problems[:10], 1):
            print(f"\n--- Problem {i} ---")
            print(f"ID: {problem.id}")
            print(f"Title: {problem.title}")
            print(f"Type: {problem.get_problem_type_display()}")
            print(f"Difficulty: {problem.get_difficulty_display()}")
            print(f"Knowledge Point: {problem.knowledge_point}")
        
        # Verify all problems are in English
        non_english_count = 0
        for problem in recent_problems:
            # Simple check for Chinese characters
            if any('\u4e00' <= char <= '\u9fff' for char in problem.title + problem.description):
                non_english_count += 1
                print(f"Problem {problem.id} may contain non-English characters: {problem.title}")
        
        if non_english_count == 0:
            print("\nAll 100 newest problems are in English.")
        else:
            print(f"\n{non_english_count} problems may contain non-English characters.")
        
    except Exception as e:
        print(f"Error verifying problems: {str(e)}")

if __name__ == "__main__":
    verify_new_problems()