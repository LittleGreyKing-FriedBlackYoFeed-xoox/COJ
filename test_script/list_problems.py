#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem

def list_all_problems():
    """List all problems in the database"""
    try:
        problems = Problem.objects.all().order_by('-id')
        
        print(f"Total problems in database: {problems.count()}")
        print("\nRecent problems:")
        
        for i, problem in enumerate(problems[:5], 1):
            print(f"\n--- Problem {i} ---")
            print(f"ID: {problem.id}")
            print(f"Title: {problem.title}")
            print(f"Type: {problem.problem_type}")
            print(f"Difficulty: {problem.difficulty}")
            print(f"Knowledge Point: {problem.knowledge_point}")
            print(f"Created by: {problem.created_by.username}")
            
    except Exception as e:
        print(f"Error listing problems: {str(e)}")

if __name__ == "__main__":
    list_all_problems()