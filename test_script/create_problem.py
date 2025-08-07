#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser

def create_test_problem():
    """Create a test problem in the database"""
    try:
        # Get a teacher or admin user
        user = CustomUser.objects.filter(role__in=[2, 3]).first()
        
        if not user:
            print("No teacher or admin user found. Cannot create problem.")
            return
        
        # Create a new problem
        problem = Problem(
            title='Binary Search Implementation',
            description='Implement a binary search algorithm to find a target value in a sorted array.',
            problem_type=4,  # Programming problem
            knowledge_point='算法',  # Algorithms
            input_description='First line: a sorted array of integers separated by spaces.\nSecond line: a target integer to find.',
            output_description='The index of the target in the array (0-indexed), or -1 if not found.',
            sample_input='1 3 5 7 9\n5',
            sample_output='2',
            hint='Binary search works by repeatedly dividing the search interval in half.',
            difficulty=2,  # Medium difficulty
            is_active=True,
            created_by=user
        )
        
        # Save the problem to the database
        problem.save()
        
        print(f"Problem successfully created with ID: {problem.id}")
        print(f"Title: {problem.title}")
        print(f"Created by: {problem.created_by.username}")
        
    except Exception as e:
        print(f"Error creating problem: {str(e)}")

if __name__ == "__main__":
    create_test_problem()