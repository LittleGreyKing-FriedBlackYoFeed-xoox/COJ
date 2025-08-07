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

def create_unique_problems():
    """Create 100 unique test problems in the database"""
    try:
        # Get a teacher or admin user
        user = CustomUser.objects.filter(role__in=[2, 3]).first()
        
        if not user:
            print("No teacher or admin user found. Cannot create problems.")
            return
        
        # Get existing problem titles to avoid duplicates
        existing_titles = set(Problem.objects.values_list('title', flat=True))
        
        # Define knowledge points
        knowledge_points = [
            "Algorithms", "Data Structures", "Arrays", "Strings", "Linked Lists",
            "Trees", "Graphs", "Dynamic Programming", "Greedy", "Backtracking",
            "Recursion", "Binary Search", "Hash Tables", "Heaps", "Stacks",
            "Queues", "Sorting", "Searching", "Math", "Bit Manipulation",
            "Divide and Conquer", "Trie", "Union Find", "Sliding Window", "Two Pointers",
            "BFS", "DFS", "Topological Sort", "Segment Tree", "Binary Indexed Tree",
            "Game Theory", "Minimax", "Geometry", "Combinatorics", "Probability",
            "Number Theory", "Randomized Algorithms", "Computational Geometry", "Network Flow",
            "Bipartite Matching"
        ]
        
        # Define problem templates
        problem_templates = [
            # New unique problem templates
            {
                'title_template': "Implement {algorithm}",
                'description_template': "Write a function to implement the {algorithm} algorithm for {purpose}.",
                'difficulty': 2,
                'variables': {
                    'algorithm': [
                        "Dijkstra's Algorithm", "A* Search", "Kruskal's Algorithm", "Prim's Algorithm",
                        "Bellman-Ford Algorithm", "Floyd-Warshall Algorithm", "Topological Sort",
                        "Tarjan's Algorithm", "Kosaraju's Algorithm", "Kahn's Algorithm"
                    ],
                    'purpose': [
                        "finding the shortest path in a weighted graph",
                        "finding the minimum spanning tree",
                        "detecting cycles in a directed graph",
                        "finding strongly connected components",
                        "sorting vertices in a directed acyclic graph"
                    ]
                }
            },
            {
                'title_template': "Design a {data_structure}",
                'description_template': "Implement a {data_structure} with the following operations: {operations}.",
                'difficulty': 2,
                'variables': {
                    'data_structure': [
                        "Hash Map", "LRU Cache", "Trie", "Segment Tree", "Binary Indexed Tree",
                        "Min Stack", "Min Queue", "Priority Queue", "Disjoint Set Union",
                        "Bloom Filter"
                    ],
                    'operations': [
                        "insert, delete, search, and update",
                        "get, put, and remove with O(1) time complexity",
                        "add, remove, contains, and get minimum",
                        "query range sum, update element, and find minimum in range",
                        "union, find, and path compression"
                    ]
                }
            },
            {
                'title_template': "Solve the {puzzle_type} Puzzle",
                'description_template': "Write an algorithm to solve the {puzzle_type} puzzle with the following constraints: {constraints}.",
                'difficulty': 3,
                'variables': {
                    'puzzle_type': [
                        "N-Queens", "Sudoku", "Knight's Tour", "Word Search", "Tower of Hanoi",
                        "Coin Change", "Knapsack", "Traveling Salesman", "Longest Increasing Subsequence",
                        "Longest Common Subsequence"
                    ],
                    'constraints': [
                        "optimal time complexity and minimal space usage",
                        "handling edge cases and invalid inputs",
                        "using only O(n) extra space",
                        "solving it in O(n log n) time",
                        "using dynamic programming approach"
                    ]
                }
            },
            {
                'title_template': "Optimize {system} Performance",
                'description_template': "Design an optimized {system} that can handle {operations} efficiently with {constraints}.",
                'difficulty': 3,
                'variables': {
                    'system': [
                        "Database Query Processor", "Web Cache", "Task Scheduler", "Memory Allocator",
                        "File System", "Load Balancer", "Rate Limiter", "Message Queue",
                        "Distributed Lock Manager", "Connection Pool"
                    ],
                    'operations': [
                        "high-frequency read and write operations",
                        "concurrent access from multiple users",
                        "real-time data processing and analytics",
                        "fault tolerance and recovery mechanisms",
                        "horizontal scaling across multiple nodes"
                    ],
                    'constraints': [
                        "minimal latency and maximum throughput",
                        "limited memory and CPU resources",
                        "network bandwidth constraints",
                        "consistency guarantees in distributed settings",
                        "handling system failures gracefully"
                    ]
                }
            },
            {
                'title_template': "Implement a {pattern} Design Pattern",
                'description_template': "Create a {language} implementation of the {pattern} design pattern to solve {problem}.",
                'difficulty': 2,
                'variables': {
                    'pattern': [
                        "Singleton", "Factory", "Observer", "Strategy", "Decorator",
                        "Adapter", "Command", "Iterator", "Composite", "Proxy"
                    ],
                    'language': [
                        "Python", "Java", "C++", "JavaScript", "TypeScript"
                    ],
                    'problem': [
                        "managing shared resources efficiently",
                        "creating objects without specifying their concrete classes",
                        "notifying multiple objects about state changes",
                        "selecting algorithms at runtime",
                        "adding responsibilities to objects dynamically"
                    ]
                }
            },
            {
                'title_template': "Develop a {application_type} Application",
                'description_template': "Design and implement a {application_type} application that supports {features} with {requirements}.",
                'difficulty': 3,
                'variables': {
                    'application_type': [
                        "Chat", "E-commerce", "Social Media", "Content Management", "Task Management",
                        "File Sharing", "Video Streaming", "Music Recommendation", "Weather Forecast",
                        "Stock Trading"
                    ],
                    'features': [
                        "user authentication and authorization",
                        "real-time notifications and updates",
                        "data persistence and synchronization",
                        "search and filtering capabilities",
                        "analytics and reporting"
                    ],
                    'requirements': [
                        "responsive UI and efficient backend",
                        "scalability and performance optimization",
                        "security and privacy protection",
                        "offline functionality and data caching",
                        "cross-platform compatibility"
                    ]
                }
            },
            {
                'title_template': "Implement {algorithm} for {domain}",
                'description_template': "Develop an implementation of {algorithm} specifically optimized for {domain} applications.",
                'difficulty': 2,
                'variables': {
                    'algorithm': [
                        "Machine Learning", "Natural Language Processing", "Computer Vision", "Recommendation System",
                        "Genetic Algorithm", "Neural Network", "Clustering", "Classification",
                        "Regression", "Reinforcement Learning"
                    ],
                    'domain': [
                        "healthcare data analysis",
                        "financial market prediction",
                        "social network analysis",
                        "image and video processing",
                        "autonomous vehicle navigation",
                        "smart home automation",
                        "cybersecurity threat detection",
                        "e-commerce product recommendation",
                        "natural language understanding",
                        "game playing and simulation"
                    ]
                }
            },
            {
                'title_template': "Build a {component} for {platform}",
                'description_template': "Create a {component} that can be integrated into {platform} with {features}.",
                'difficulty': 2,
                'variables': {
                    'component': [
                        "Authentication Service", "Payment Gateway", "Notification System", "Search Engine",
                        "Analytics Dashboard", "Content Delivery Network", "API Gateway", "Message Broker",
                        "Caching Layer", "Rate Limiter"
                    ],
                    'platform': [
                        "Web Applications", "Mobile Apps", "IoT Devices", "Cloud Services",
                        "Microservices Architecture", "Serverless Computing", "Edge Computing",
                        "Blockchain Networks", "Distributed Systems", "Real-time Processing Frameworks"
                    ],
                    'features': [
                        "high availability and fault tolerance",
                        "low latency and high throughput",
                        "security and compliance with regulations",
                        "scalability and resource efficiency",
                        "monitoring and observability"
                    ]
                }
            },
            {
                'title_template': "Create a {type} Parser",
                'description_template': "Implement a parser for {type} that can handle {features} and produce {output}.",
                'difficulty': 2,
                'variables': {
                    'type': [
                        "JSON", "XML", "CSV", "Markdown", "YAML",
                        "Regular Expression", "SQL Query", "GraphQL", "Protocol Buffer", "HTML"
                    ],
                    'features': [
                        "nested structures and complex data types",
                        "error handling and validation",
                        "streaming large files efficiently",
                        "custom extensions and annotations",
                        "backward compatibility with older formats"
                    ],
                    'output': [
                        "an abstract syntax tree",
                        "a structured object representation",
                        "a normalized data format",
                        "a queryable database",
                        "a visual rendering"
                    ]
                }
            },
            {
                'title_template': "Implement a {protocol} Protocol",
                'description_template': "Develop an implementation of the {protocol} protocol that supports {features} with {constraints}.",
                'difficulty': 3,
                'variables': {
                    'protocol': [
                        "HTTP/3", "WebSocket", "MQTT", "gRPC", "GraphQL",
                        "OAuth 2.0", "SMTP", "FTP", "DNS", "Blockchain"
                    ],
                    'features': [
                        "secure communication and encryption",
                        "connection pooling and multiplexing",
                        "compression and binary encoding",
                        "request/response pipelining",
                        "pub/sub messaging patterns"
                    ],
                    'constraints': [
                        "minimal overhead and bandwidth usage",
                        "reliability over unreliable networks",
                        "backward compatibility with older versions",
                        "cross-platform interoperability",
                        "compliance with industry standards"
                    ]
                }
            }
        ]
        
        # Generate 100 problems
        created_problems = []
        problem_count = 0
        
        while problem_count < 100:
            # Select a random template
            template = random.choice(problem_templates)
            
            # Fill in the template variables
            variables = {}
            for var_name, var_values in template['variables'].items():
                variables[var_name] = random.choice(var_values)
            
            title = template['title_template'].format(**variables)
            
            # Add a unique identifier to ensure uniqueness
            unique_id = problem_count + 1
            title = f"{title} #{unique_id}"
            
            # Skip if title already exists
            if title in existing_titles:
                continue
            
            description = template['description_template'].format(**variables)
            
            # Select a random knowledge point
            knowledge_point = random.choice(knowledge_points)
            
            # Generate input/output descriptions and samples based on the problem type
            if "algorithm" in title.lower() or "implement" in title.lower():
                input_description = "Input format will depend on the specific algorithm implementation. Typically includes parameters required by the algorithm."
                output_description = "Output should be the result of applying the algorithm to the input data."
                sample_input = "Example input parameters for the algorithm"
                sample_output = "Expected output after algorithm execution"
            elif "data structure" in title.lower() or "design" in title.lower():
                input_description = "A series of operations to perform on the data structure, one operation per line."
                output_description = "The result of each operation, one result per line."
                sample_input = "insert 5\ninsert 10\nget 1\ndelete 5\nget 0"
                sample_output = "null\nnull\n10\nnull\n10"
            elif "parser" in title.lower() or "protocol" in title.lower():
                input_description = "A string representing the content to be parsed or the protocol message."
                output_description = "The parsed representation or protocol response."
                sample_input = "Sample input string to parse"
                sample_output = "Structured output after parsing"
            elif "application" in title.lower() or "system" in title.lower():
                input_description = "System configuration parameters and user interactions."
                output_description = "System responses and state changes."
                sample_input = "Configuration parameters and sample user actions"
                sample_output = "Expected system behavior and responses"
            else:
                input_description = "Input format will depend on the specific problem requirements."
                output_description = "Output format will depend on the specific problem requirements."
                sample_input = "Sample input based on problem description"
                sample_output = "Expected output for the sample input"
            
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
            existing_titles.add(title)  # Add to existing titles to avoid duplicates
            problem_count += 1
            print(f"Created problem {problem_count}/100: {problem.title} (ID: {problem.id})")
        
        print(f"\nSuccessfully created {len(created_problems)} unique problems!")
        
    except Exception as e:
        print(f"Error creating problems: {str(e)}")

if __name__ == "__main__":
    create_unique_problems()