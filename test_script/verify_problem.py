#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem

def verify_problem():
    """Verify that our problem exists in the database"""
    try:
        # Get the problem we just created
        problem = Problem.objects.get(title='Binary Search Implementation')
        
        print("Problem found in database:")
        print(f"ID: {problem.id}")
        print(f"Title: {problem.title}")
        print(f"Type: {problem.get_problem_type_display()}")
        print(f"Difficulty: {problem.get_difficulty_display()}")
        print(f"Knowledge Point: {problem.knowledge_point}")
        print(f"Created by: {problem.created_by.username}")
        print(f"Is Active: {problem.is_active}")
        
    except Problem.DoesNotExist:
        print("Problem not found in database.")
    except Exception as e:
        print(f"Error verifying problem: {str(e)}")

if __name__ == "__main__":
    verify_problem()