#!/usr/bin/env python
import os
import django
import random

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser

def create_problems():
    """Create 100 test problems in the database"""
    try:
        # Get a teacher or admin user
        user = CustomUser.objects.filter(role__in=[2, 3]).first()
        
        if not user:
            print("No teacher or admin user found. Cannot create problems.")
            return
        
        # Define knowledge points
        knowledge_points = [
            "Algorithms", "Data Structures", "Arrays", "Strings", "Linked Lists",
            "Trees", "Graphs", "Dynamic Programming", "Greedy", "Backtracking",
            "Recursion", "Binary Search", "Hash Tables", "Heaps", "Stacks",
            "Queues", "Sorting", "Searching", "Math", "Bit Manipulation"
        ]
        
        # Define problem templates for different types
        problem_templates = [
            # Easy problems
            {
                'title_template': "Find the {nth} {element} in {collection}",
                'description_template': "Write a function to find the {nth} {element} in a given {collection}.",
                'difficulty': 1,
                'variables': {
                    'nth': ["smallest", "largest", "missing", "duplicate", "unique"],
                    'element': ["number", "character", "element", "item", "value"],
                    'collection': ["array", "list", "string", "sequence", "collection"]
                }
            },
            {
                'title_template': "{action} {collection}",
                'description_template': "Implement a function to {action} a given {collection}.",
                'difficulty': 1,
                'variables': {
                    'action': ["reverse", "sort", "rotate", "shuffle", "filter"],
                    'collection': ["array", "linked list", "string", "matrix", "binary tree"]
                }
            },
            # Medium problems
            {
                'title_template': "{algorithm} Implementation",
                'description_template': "Implement the {algorithm} algorithm to solve the following problem: {problem_description}",
                'difficulty': 2,
                'variables': {
                    'algorithm': ["Binary Search", "Merge Sort", "Quick Sort", "Breadth-First Search", "Depth-First Search"],
                    'problem_description': [
                        "find a target value in a sorted array",
                        "sort an array of integers efficiently",
                        "traverse a graph and find the shortest path",
                        "detect cycles in a directed graph",
                        "find all connected components in an undirected graph"
                    ]
                }
            },
            {
                'title_template': "{problem_type} Problem",
                'description_template': "Solve the following {problem_type} problem: {specific_problem}",
                'difficulty': 2,
                'variables': {
                    'problem_type': ["Dynamic Programming", "Greedy", "Backtracking", "Two Pointers", "Sliding Window"],
                    'specific_problem': [
                        "find the maximum sum subarray",
                        "find the minimum number of coins to make change",
                        "generate all valid combinations of parentheses",
                        "find all pairs in an array that sum to a target",
                        "find the longest substring without repeating characters"
                    ]
                }
            },
            # Hard problems
            {
                'title_template': "Advanced {topic} Challenge",
                'description_template': "Solve this advanced {topic} challenge: {challenge_description}",
                'difficulty': 3,
                'variables': {
                    'topic': ["Graph Theory", "Dynamic Programming", "Computational Geometry", "Advanced Data Structures", "Algorithm Design"],
                    'challenge_description': [
                        "find the shortest path that visits all nodes in a graph exactly once",
                        "partition an array into k subsets with equal sum",
                        "find the convex hull of a set of points in 2D space",
                        "implement a self-balancing binary search tree",
                        "design an algorithm to solve the n-queens problem efficiently"
                    ]
                }
            },
            {
                'title_template': "Optimize {system} for {criteria}",
                'description_template': "Design and implement an optimized {system} that satisfies the following {criteria}.",
                'difficulty': 3,
                'variables': {
                    'system': ["database", "cache", "scheduler", "memory allocator", "file system"],
                    'criteria': [
                        "minimum latency and maximum throughput",
                        "efficient space utilization and fast lookup",
                        "fair resource allocation and minimal waiting time",
                        "minimal fragmentation and fast allocation/deallocation",
                        "consistency guarantees and fault tolerance"
                    ]
                }
            }
        ]
        
        # Generate 100 problems
        created_problems = []
        for i in range(1, 101):
            # Select a random template based on desired difficulty distribution
            # 40% Easy, 40% Medium, 20% Hard
            rand = random.random()
            if rand < 0.4:
                template_indices = [0, 1]  # Easy templates
            elif rand < 0.8:
                template_indices = [2, 3]  # Medium templates
            else:
                template_indices = [4, 5]  # Hard templates
                
            template = problem_templates[random.choice(template_indices)]
            
            # Fill in the template variables
            variables = {}
            for var_name, var_values in template['variables'].items():
                variables[var_name] = random.choice(var_values)
            
            title = template['title_template'].format(**variables)
            description = template['description_template'].format(**variables)
            
            # Add a number to ensure uniqueness
            title = f"{title} #{i}"
            
            # Select a random knowledge point
            knowledge_point = random.choice(knowledge_points)
            
            # Generate input/output descriptions and samples based on the problem type
            if "array" in description.lower() or "list" in description.lower():
                input_description = "An array of integers separated by spaces."
                output_description = "The result based on the problem requirements."
                sample_input = "1 3 5 7 9"
                sample_output = "9"  # Assuming the largest element
            elif "string" in description.lower():
                input_description = "A string."
                output_description = "The result based on the problem requirements."
                sample_input = "abcdefg"
                sample_output = "gfedcba"  # Assuming reversed
            elif "graph" in description.lower():
                input_description = "First line: number of nodes (n) and edges (m).\nNext m lines: pairs of nodes representing edges."
                output_description = "The result based on the problem requirements."
                sample_input = "5 6\n1 2\n1 3\n2 3\n2 4\n3 5\n4 5"
                sample_output = "1 2 3 5 4"  # Assuming a path
            elif "tree" in description.lower():
                input_description = "A binary tree represented in level order (null nodes as 'null')."
                output_description = "The result based on the problem requirements."
                sample_input = "3 9 20 null null 15 7"
                sample_output = "3 9 20 15 7"  # Assuming level order traversal
            else:
                input_description = "Input format depends on the specific problem."
                output_description = "Output format depends on the specific problem."
                sample_input = "Sample input"
                sample_output = "Sample output"
            
            # Generate a hint based on the knowledge point
            hints = {
                "Algorithms": "Consider the time and space complexity of your solution.",
                "Data Structures": "Choose the appropriate data structure for efficient operations.",
                "Arrays": "Consider edge cases like empty arrays or arrays with a single element.",
                "Strings": "Be careful with string manipulation operations and their efficiency.",
                "Linked Lists": "Consider using dummy nodes or fast/slow pointers.",
                "Trees": "Consider recursive and iterative approaches for tree traversal.",
                "Graphs": "Consider using adjacency lists or matrices for graph representation.",
                "Dynamic Programming": "Break down the problem into overlapping subproblems.",
                "Greedy": "Make locally optimal choices at each step.",
                "Backtracking": "Explore all possible solutions and backtrack when necessary.",
                "Recursion": "Define the base case and recursive case clearly.",
                "Binary Search": "Ensure the array is sorted before applying binary search.",
                "Hash Tables": "Use hashing for O(1) average time complexity for lookups.",
                "Heaps": "Use priority queues for efficient minimum/maximum element access.",
                "Stacks": "Use LIFO (Last In, First Out) principle for solving the problem.",
                "Queues": "Use FIFO (First In, First Out) principle for solving the problem.",
                "Sorting": "Choose the appropriate sorting algorithm based on the requirements.",
                "Searching": "Consider the efficiency of different search algorithms.",
                "Math": "Look for mathematical patterns or formulas that can simplify the problem.",
                "Bit Manipulation": "Use bitwise operations for efficient solutions."
            }
            hint = hints.get(knowledge_point, "Think about the problem carefully and consider different approaches.")
            
            # Create the problem
            problem = Problem(
                title=title,
                description=description,
                problem_type=4,  # Programming problem
                knowledge_point=knowledge_point,
                input_description=input_description,
                output_description=output_description,
                sample_input=sample_input,
                sample_output=sample_output,
                hint=hint,
                difficulty=template['difficulty'],
                is_active=True,
                created_by=user
            )
            problem.save()
            created_problems.append(problem)
            print(f"Created problem {i}/100: {problem.title} (ID: {problem.id})")
        
        print(f"\nSuccessfully created {len(created_problems)} problems!")
        
    except Exception as e:
        print(f"Error creating problems: {str(e)}")

if __name__ == "__main__":
    create_problems()