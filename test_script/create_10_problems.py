#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser

def create_problems():
    """Create 10 test problems in the database"""
    try:
        # Get a teacher or admin user
        user = CustomUser.objects.filter(role__in=[2, 3]).first()
        
        if not user:
            print("No teacher or admin user found. Cannot create problems.")
            return
        
        # Define 10 problems
        problems = [
            {
                'title': 'Two Sum',
                'description': 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '算法',  # Algorithms
                'input_description': 'First line: an array of integers separated by spaces.\nSecond line: a target integer.',
                'output_description': 'Two indices (0-indexed) of the numbers that add up to the target.',
                'sample_input': '2 7 11 15\n9',
                'sample_output': '0 1',
                'hint': 'Consider using a hash map to store the values you\'ve seen so far.',
                'difficulty': 1,  # Easy
            },
            {
                'title': 'Reverse Linked List',
                'description': 'Given the head of a singly linked list, reverse the list, and return the reversed list.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '数据结构',  # Data Structures
                'input_description': 'A linked list represented as space-separated integers.',
                'output_description': 'The reversed linked list as space-separated integers.',
                'sample_input': '1 2 3 4 5',
                'sample_output': '5 4 3 2 1',
                'hint': 'You can use either iterative or recursive approach.',
                'difficulty': 1,  # Easy
            },
            {
                'title': 'Valid Parentheses',
                'description': 'Given a string s containing just the characters \'(\', \')\', \'{\', \'}\', \'[\' and \']\', determine if the input string is valid.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '栈',  # Stack
                'input_description': 'A string containing only parentheses.',
                'output_description': '"true" if the string is valid, "false" otherwise.',
                'sample_input': '()[]{}',
                'sample_output': 'true',
                'hint': 'Use a stack to keep track of opening brackets.',
                'difficulty': 1,  # Easy
            },
            {
                'title': 'Merge Two Sorted Lists',
                'description': 'Merge two sorted linked lists and return it as a sorted list.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '链表',  # Linked List
                'input_description': 'Two sorted linked lists represented as space-separated integers.',
                'output_description': 'The merged sorted linked list as space-separated integers.',
                'sample_input': '1 2 4\n1 3 4',
                'sample_output': '1 1 2 3 4 4',
                'hint': 'Compare the heads of both lists and choose the smaller one.',
                'difficulty': 1,  # Easy
            },
            {
                'title': 'Maximum Subarray',
                'description': 'Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '动态规划',  # Dynamic Programming
                'input_description': 'An array of integers separated by spaces.',
                'output_description': 'The sum of the contiguous subarray with the largest sum.',
                'sample_input': '-2 1 -3 4 -1 2 1 -5 4',
                'sample_output': '6',
                'hint': 'Consider using Kadane\'s algorithm.',
                'difficulty': 2,  # Medium
            },
            {
                'title': 'Longest Palindromic Substring',
                'description': 'Given a string s, return the longest palindromic substring in s.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '字符串',  # String
                'input_description': 'A string.',
                'output_description': 'The longest palindromic substring.',
                'sample_input': 'babad',
                'sample_output': 'bab',
                'hint': 'Consider expanding around center for each character.',
                'difficulty': 2,  # Medium
            },
            {
                'title': '3Sum',
                'description': 'Given an array nums of n integers, find all unique triplets in the array which gives the sum of zero.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '数组',  # Array
                'input_description': 'An array of integers separated by spaces.',
                'output_description': 'All unique triplets that sum to zero, each triplet on a new line.',
                'sample_input': '-1 0 1 2 -1 -4',
                'sample_output': '-1 -1 2\n-1 0 1',
                'hint': 'Sort the array first, then use two pointers technique.',
                'difficulty': 2,  # Medium
            },
            {
                'title': 'Binary Tree Level Order Traversal',
                'description': 'Given the root of a binary tree, return the level order traversal of its nodes\' values.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '树',  # Tree
                'input_description': 'A binary tree represented in level order (null nodes as "null").',
                'output_description': 'The level order traversal of the tree.',
                'sample_input': '3 9 20 null null 15 7',
                'sample_output': '3\n9 20\n15 7',
                'hint': 'Use a queue to perform breadth-first search.',
                'difficulty': 2,  # Medium
            },
            {
                'title': 'Trapping Rain Water',
                'description': 'Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '双指针',  # Two Pointers
                'input_description': 'An array of non-negative integers representing heights.',
                'output_description': 'The amount of water that can be trapped.',
                'sample_input': '0 1 0 2 1 0 1 3 2 1 2 1',
                'sample_output': '6',
                'hint': 'Consider using two pointers or dynamic programming approach.',
                'difficulty': 3,  # Hard
            },
            {
                'title': 'Median of Two Sorted Arrays',
                'description': 'Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.',
                'problem_type': 4,  # Programming problem
                'knowledge_point': '二分查找',  # Binary Search
                'input_description': 'Two sorted arrays of integers, each on a separate line.',
                'output_description': 'The median of the two sorted arrays.',
                'sample_input': '1 3\n2',
                'sample_output': '2.0',
                'hint': 'The problem can be converted to finding the k-th smallest element in the two sorted arrays.',
                'difficulty': 3,  # Hard
            },
        ]
        
        # Create each problem
        created_problems = []
        for problem_data in problems:
            problem = Problem(
                title=problem_data['title'],
                description=problem_data['description'],
                problem_type=problem_data['problem_type'],
                knowledge_point=problem_data['knowledge_point'],
                input_description=problem_data['input_description'],
                output_description=problem_data['output_description'],
                sample_input=problem_data['sample_input'],
                sample_output=problem_data['sample_output'],
                hint=problem_data['hint'],
                difficulty=problem_data['difficulty'],
                is_active=True,
                created_by=user
            )
            problem.save()
            created_problems.append(problem)
            print(f"Created problem: {problem.title} (ID: {problem.id})")
        
        print(f"\nSuccessfully created {len(created_problems)} problems!")
        
    except Exception as e:
        print(f"Error creating problems: {str(e)}")

if __name__ == "__main__":
    create_problems()