#!/usr/bin/env python
import os
import django
import random
import string

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.problem_models import Problem
from own_models.custom_user_models import CustomUser

def create_unique_problems():
    """Create 200 unique test problems in the database"""
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
            "Bipartite Matching", "Suffix Array", "KMP Algorithm", "Rabin-Karp Algorithm",
            "Manacher's Algorithm", "Convex Hull", "Line Sweep", "Interval Tree",
            "Bloom Filter", "Skip List", "B-Tree", "Red-Black Tree", "AVL Tree",
            "Splay Tree", "Treap", "Fibonacci Heap", "Disjoint Set", "Sparse Table",
            "Lowest Common Ancestor", "Heavy-Light Decomposition", "Centroid Decomposition",
            "Mo's Algorithm", "Persistent Data Structures", "Sqrt Decomposition"
        ]
        
        # Define problem templates
        problem_templates = [
            # Algorithm Implementation Problems
            {
                'title_template': "Implement {algorithm}",
                'description_template': "Write a function to implement the {algorithm} algorithm for {purpose}.",
                'difficulty': 2,
                'variables': {
                    'algorithm': [
                        "Dijkstra's Algorithm", "A* Search", "Kruskal's Algorithm", "Prim's Algorithm",
                        "Bellman-Ford Algorithm", "Floyd-Warshall Algorithm", "Topological Sort",
                        "Tarjan's Algorithm", "Kosaraju's Algorithm", "Kahn's Algorithm",
                        "Edmonds-Karp Algorithm", "Ford-Fulkerson Algorithm", "Johnson's Algorithm",
                        "Boruvka's Algorithm", "Hierholzer's Algorithm", "Kadane's Algorithm",
                        "Boyer-Moore Algorithm", "Z Algorithm", "Aho-Corasick Algorithm",
                        "Knuth-Morris-Pratt Algorithm"
                    ],
                    'purpose': [
                        "finding the shortest path in a weighted graph",
                        "finding the minimum spanning tree",
                        "detecting cycles in a directed graph",
                        "finding strongly connected components",
                        "sorting vertices in a directed acyclic graph",
                        "finding the maximum flow in a flow network",
                        "finding all pairs shortest paths",
                        "finding Euler paths and circuits",
                        "finding the maximum subarray sum",
                        "efficient string pattern matching",
                        "finding articulation points and bridges",
                        "solving the traveling salesman problem approximately",
                        "finding the longest increasing subsequence",
                        "detecting negative cycles in a graph",
                        "finding the diameter of a tree"
                    ]
                }
            },
            # Data Structure Design Problems
            {
                'title_template': "Design a {data_structure}",
                'description_template': "Implement a {data_structure} with the following operations: {operations}.",
                'difficulty': 2,
                'variables': {
                    'data_structure': [
                        "Hash Map", "LRU Cache", "Trie", "Segment Tree", "Binary Indexed Tree",
                        "Min Stack", "Min Queue", "Priority Queue", "Disjoint Set Union",
                        "Bloom Filter", "Skip List", "B-Tree", "Red-Black Tree", "AVL Tree",
                        "Splay Tree", "Treap", "Fibonacci Heap", "Sparse Table", "Suffix Array",
                        "Suffix Tree", "Interval Tree", "Quad Tree", "K-d Tree", "Persistent Array",
                        "Persistent Segment Tree", "Wavelet Tree", "Rope", "Cartesian Tree"
                    ],
                    'operations': [
                        "insert, delete, search, and update",
                        "get, put, and remove with O(1) time complexity",
                        "add, remove, contains, and get minimum",
                        "query range sum, update element, and find minimum in range",
                        "union, find, and path compression",
                        "efficient prefix matching and wildcard search",
                        "range minimum/maximum query and point update",
                        "efficient nearest neighbor search",
                        "efficient interval overlap queries",
                        "efficient substring search and pattern matching",
                        "efficient range updates and range queries",
                        "efficient persistence with path copying",
                        "efficient string concatenation and splitting",
                        "efficient 2D range queries"
                    ]
                }
            },
            # Puzzle Problems
            {
                'title_template': "Solve the {puzzle_type} Puzzle",
                'description_template': "Write an algorithm to solve the {puzzle_type} puzzle with the following constraints: {constraints}.",
                'difficulty': 3,
                'variables': {
                    'puzzle_type': [
                        "N-Queens", "Sudoku", "Knight's Tour", "Word Search", "Tower of Hanoi",
                        "Coin Change", "Knapsack", "Traveling Salesman", "Longest Increasing Subsequence",
                        "Longest Common Subsequence", "Edit Distance", "Regular Expression Matching",
                        "Wildcard Matching", "Palindrome Partitioning", "Word Break",
                        "Combination Sum", "Permutations", "Subsets", "Sliding Puzzle",
                        "Rubik's Cube", "15 Puzzle", "Lights Out", "Minesweeper", "Tetris",
                        "Sokoban", "Rush Hour", "Nonogram", "Kakuro", "Slitherlink"
                    ],
                    'constraints': [
                        "optimal time complexity and minimal space usage",
                        "handling edge cases and invalid inputs",
                        "using only O(n) extra space",
                        "solving it in O(n log n) time",
                        "using dynamic programming approach",
                        "using backtracking with pruning",
                        "using A* search with an admissible heuristic",
                        "using iterative deepening depth-first search",
                        "using branch and bound techniques",
                        "using greedy approach with proof of optimality",
                        "using divide and conquer strategy",
                        "using bit manipulation for space efficiency",
                        "using memoization to avoid redundant calculations",
                        "using two pointers or sliding window technique",
                        "using monotonic stack or queue"
                    ]
                }
            },
            # System Design Problems
            {
                'title_template': "Optimize {system} Performance",
                'description_template': "Design an optimized {system} that can handle {operations} efficiently with {constraints}.",
                'difficulty': 3,
                'variables': {
                    'system': [
                        "Database Query Processor", "Web Cache", "Task Scheduler", "Memory Allocator",
                        "File System", "Load Balancer", "Rate Limiter", "Message Queue",
                        "Distributed Lock Manager", "Connection Pool", "Object Pool", "Thread Pool",
                        "Garbage Collector", "Log Structured Merge Tree", "B-tree Index",
                        "Inverted Index", "Full-Text Search Engine", "Recommendation System",
                        "Content Delivery Network", "Distributed Hash Table", "Consensus Algorithm",
                        "Distributed Transaction Manager", "Sharded Database", "Time Series Database",
                        "Graph Database", "Document Store", "Key-Value Store", "Column-Family Store"
                    ],
                    'operations': [
                        "high-frequency read and write operations",
                        "concurrent access from multiple users",
                        "real-time data processing and analytics",
                        "fault tolerance and recovery mechanisms",
                        "horizontal scaling across multiple nodes",
                        "low-latency queries and updates",
                        "batch processing of large datasets",
                        "streaming data ingestion and processing",
                        "complex join operations across multiple tables",
                        "graph traversal and pattern matching",
                        "geospatial indexing and querying",
                        "time-based windowing and aggregation",
                        "full-text search with relevance ranking",
                        "multi-dimensional range queries",
                        "versioning and conflict resolution"
                    ],
                    'constraints': [
                        "minimal latency and maximum throughput",
                        "limited memory and CPU resources",
                        "network bandwidth constraints",
                        "consistency guarantees in distributed settings",
                        "handling system failures gracefully",
                        "supporting both read and write-heavy workloads",
                        "maintaining data integrity during concurrent updates",
                        "ensuring data durability across system restarts",
                        "providing isolation between concurrent transactions",
                        "supporting both point queries and range scans",
                        "minimizing storage overhead and fragmentation",
                        "supporting efficient incremental backups",
                        "handling skewed data distributions",
                        "supporting multi-tenancy with resource isolation",
                        "ensuring predictable performance under varying load"
                    ]
                }
            },
            # Design Pattern Problems
            {
                'title_template': "Implement a {pattern} Design Pattern",
                'description_template': "Create a {language} implementation of the {pattern} design pattern to solve {problem}.",
                'difficulty': 2,
                'variables': {
                    'pattern': [
                        "Singleton", "Factory", "Abstract Factory", "Builder", "Prototype",
                        "Adapter", "Bridge", "Composite", "Decorator", "Facade",
                        "Flyweight", "Proxy", "Chain of Responsibility", "Command", "Interpreter",
                        "Iterator", "Mediator", "Memento", "Observer", "State",
                        "Strategy", "Template Method", "Visitor", "Module", "Dependency Injection"
                    ],
                    'language': [
                        "Python", "Java", "C++", "JavaScript", "TypeScript",
                        "C#", "Go", "Rust", "Swift", "Kotlin"
                    ],
                    'problem': [
                        "managing shared resources efficiently",
                        "creating objects without specifying their concrete classes",
                        "notifying multiple objects about state changes",
                        "selecting algorithms at runtime",
                        "adding responsibilities to objects dynamically",
                        "providing a unified interface to a set of interfaces",
                        "decoupling an abstraction from its implementation",
                        "composing objects into tree structures",
                        "encapsulating a request as an object",
                        "representing and interpreting a language grammar",
                        "accessing elements of a collection without exposing its structure",
                        "defining a skeleton of an algorithm with customizable steps",
                        "representing operations to be performed on objects",
                        "capturing and restoring an object's internal state",
                        "allowing an object to alter its behavior when its state changes"
                    ]
                }
            },
            # Application Development Problems
            {
                'title_template': "Develop a {application_type} Application",
                'description_template': "Design and implement a {application_type} application that supports {features} with {requirements}.",
                'difficulty': 3,
                'variables': {
                    'application_type': [
                        "Chat", "E-commerce", "Social Media", "Content Management", "Task Management",
                        "File Sharing", "Video Streaming", "Music Recommendation", "Weather Forecast",
                        "Stock Trading", "Email Client", "Calendar", "Note Taking", "Password Manager",
                        "Photo Gallery", "Recipe Manager", "Fitness Tracker", "Budget Planner",
                        "Travel Planner", "Job Board", "Learning Management", "Project Management",
                        "Customer Relationship Management", "Inventory Management", "Point of Sale"
                    ],
                    'features': [
                        "user authentication and authorization",
                        "real-time notifications and updates",
                        "data persistence and synchronization",
                        "search and filtering capabilities",
                        "analytics and reporting",
                        "social sharing and collaboration",
                        "content moderation and flagging",
                        "recommendation and personalization",
                        "payment processing and subscriptions",
                        "file upload and management",
                        "commenting and discussion threads",
                        "tagging and categorization",
                        "version history and rollback",
                        "export and import functionality",
                        "multi-language support and localization"
                    ],
                    'requirements': [
                        "responsive UI and efficient backend",
                        "scalability and performance optimization",
                        "security and privacy protection",
                        "offline functionality and data caching",
                        "cross-platform compatibility",
                        "accessibility compliance",
                        "mobile-first design approach",
                        "low bandwidth usage for developing regions",
                        "integration with third-party services",
                        "comprehensive test coverage",
                        "detailed documentation and user guides",
                        "continuous integration and deployment",
                        "monitoring and error reporting",
                        "data backup and disaster recovery",
                        "compliance with relevant regulations"
                    ]
                }
            },
            # Machine Learning Problems
            {
                'title_template': "Implement {algorithm} for {domain}",
                'description_template': "Develop an implementation of {algorithm} specifically optimized for {domain} applications.",
                'difficulty': 3,
                'variables': {
                    'algorithm': [
                        "Linear Regression", "Logistic Regression", "Decision Trees", "Random Forests",
                        "Support Vector Machines", "K-Means Clustering", "Hierarchical Clustering",
                        "Principal Component Analysis", "Neural Networks", "Convolutional Neural Networks",
                        "Recurrent Neural Networks", "Long Short-Term Memory Networks", "Transformers",
                        "Generative Adversarial Networks", "Reinforcement Learning", "Q-Learning",
                        "Naive Bayes", "K-Nearest Neighbors", "Gradient Boosting", "AdaBoost",
                        "Hidden Markov Models", "Latent Dirichlet Allocation", "Word2Vec",
                        "BERT", "GPT", "YOLO", "ResNet", "U-Net", "Autoencoder", "Variational Autoencoder"
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
                        "game playing and simulation",
                        "speech recognition and synthesis",
                        "anomaly detection in time series",
                        "sentiment analysis in text",
                        "fraud detection in transactions",
                        "predictive maintenance for equipment",
                        "customer churn prediction",
                        "drug discovery and development",
                        "genomic sequence analysis",
                        "climate modeling and prediction",
                        "personalized education and learning"
                    ]
                }
            },
            # Component Development Problems
            {
                'title_template': "Build a {component} for {platform}",
                'description_template': "Create a {component} that can be integrated into {platform} with {features}.",
                'difficulty': 2,
                'variables': {
                    'component': [
                        "Authentication Service", "Payment Gateway", "Notification System", "Search Engine",
                        "Analytics Dashboard", "Content Delivery Network", "API Gateway", "Message Broker",
                        "Caching Layer", "Rate Limiter", "Load Balancer", "Service Discovery",
                        "Configuration Management", "Circuit Breaker", "Feature Flag System",
                        "Logging Framework", "Monitoring Service", "Tracing System", "Identity Provider",
                        "Authorization Service", "Data Pipeline", "ETL Process", "Recommendation Engine",
                        "Full-Text Search", "Geospatial Index", "Time Series Database", "Graph Database",
                        "Document Store", "Key-Value Store", "Object Storage"
                    ],
                    'platform': [
                        "Web Applications", "Mobile Apps", "IoT Devices", "Cloud Services",
                        "Microservices Architecture", "Serverless Computing", "Edge Computing",
                        "Blockchain Networks", "Distributed Systems", "Real-time Processing Frameworks",
                        "Big Data Platforms", "Container Orchestration", "DevOps Pipelines",
                        "Continuous Integration/Deployment", "Hybrid Cloud Environments",
                        "Multi-Cloud Deployments", "Embedded Systems", "Gaming Platforms",
                        "Augmented Reality Applications", "Virtual Reality Environments",
                        "Smart City Infrastructure", "Industrial IoT", "Healthcare Systems",
                        "Financial Trading Platforms", "E-commerce Marketplaces"
                    ],
                    'features': [
                        "high availability and fault tolerance",
                        "low latency and high throughput",
                        "security and compliance with regulations",
                        "scalability and resource efficiency",
                        "monitoring and observability",
                        "automated testing and validation",
                        "comprehensive documentation",
                        "backward compatibility guarantees",
                        "graceful degradation under load",
                        "efficient resource utilization",
                        "minimal dependencies and coupling",
                        "clear separation of concerns",
                        "extensibility through plugins",
                        "configurable behavior without code changes",
                        "comprehensive metrics and logging"
                    ]
                }
            },
            # Parser Development Problems
            {
                'title_template': "Create a {type} Parser",
                'description_template': "Implement a parser for {type} that can handle {features} and produce {output}.",
                'difficulty': 2,
                'variables': {
                    'type': [
                        "JSON", "XML", "CSV", "Markdown", "YAML",
                        "Regular Expression", "SQL Query", "GraphQL", "Protocol Buffer", "HTML",
                        "CSS", "JavaScript", "Python", "Java", "C++",
                        "Assembly", "Binary Format", "Network Protocol", "Log Format", "Configuration File",
                        "Domain-Specific Language", "Query Language", "Template Language", "Markup Language",
                        "Serialization Format", "Data Exchange Format", "Schema Definition", "Grammar Specification",
                        "Command Line Arguments", "URL Format"
                    ],
                    'features': [
                        "nested structures and complex data types",
                        "error handling and validation",
                        "streaming large files efficiently",
                        "custom extensions and annotations",
                        "backward compatibility with older formats",
                        "forward compatibility with newer formats",
                        "incremental parsing for large inputs",
                        "handling malformed or incomplete input",
                        "preserving comments and formatting",
                        "supporting multiple encodings",
                        "handling circular references",
                        "supporting schema validation",
                        "efficient memory usage for large files",
                        "parallel processing of independent sections",
                        "handling ambiguous grammar constructs"
                    ],
                    'output': [
                        "an abstract syntax tree",
                        "a structured object representation",
                        "a normalized data format",
                        "a queryable database",
                        "a visual rendering",
                        "an optimized binary format",
                        "a semantic model",
                        "an executable representation",
                        "a transformed document",
                        "a validated data structure",
                        "an indexed and searchable collection",
                        "a memory-efficient representation",
                        "a stream of events",
                        "a set of transformation instructions",
                        "a canonical form for comparison"
                    ]
                }
            },
            # Protocol Implementation Problems
            {
                'title_template': "Implement a {protocol} Protocol",
                'description_template': "Develop an implementation of the {protocol} protocol that supports {features} with {constraints}.",
                'difficulty': 3,
                'variables': {
                    'protocol': [
                        "HTTP/3", "WebSocket", "MQTT", "gRPC", "GraphQL",
                        "OAuth 2.0", "SMTP", "FTP", "DNS", "Blockchain",
                        "AMQP", "STOMP", "XMPP", "SIP", "RTMP",
                        "SSH", "TLS", "QUIC", "CoAP", "LDAP",
                        "Kerberos", "SAML", "OpenID Connect", "DHCP", "NTP",
                        "BGP", "OSPF", "SNMP", "RADIUS", "DIAMETER"
                    ],
                    'features': [
                        "secure communication and encryption",
                        "connection pooling and multiplexing",
                        "compression and binary encoding",
                        "request/response pipelining",
                        "pub/sub messaging patterns",
                        "flow control and congestion avoidance",
                        "authentication and authorization",
                        "session management and persistence",
                        "error handling and recovery",
                        "monitoring and metrics collection",
                        "backward compatibility with older versions",
                        "extensibility through custom headers",
                        "support for proxying and intermediaries",
                        "caching and conditional requests",
                        "content negotiation and transformation"
                    ],
                    'constraints': [
                        "minimal overhead and bandwidth usage",
                        "reliability over unreliable networks",
                        "backward compatibility with older versions",
                        "cross-platform interoperability",
                        "compliance with industry standards",
                        "minimal latency for real-time applications",
                        "support for resource-constrained devices",
                        "handling network partitions gracefully",
                        "efficient use of system resources",
                        "support for both synchronous and asynchronous operations",
                        "handling high concurrency efficiently",
                        "maintaining security across trust boundaries",
                        "supporting various quality of service levels",
                        "operating within limited memory constraints",
                        "supporting both client and server implementations"
                    ]
                }
            },
            # Security Problems
            {
                'title_template': "Implement {security_feature} for {application_type}",
                'description_template': "Design and implement a {security_feature} system for {application_type} applications that protects against {threats}.",
                'difficulty': 3,
                'variables': {
                    'security_feature': [
                        "Authentication", "Authorization", "Encryption", "Access Control",
                        "Secure Communication", "Intrusion Detection", "Vulnerability Scanning",
                        "Secure Coding Practices", "Security Auditing", "Penetration Testing",
                        "Data Loss Prevention", "Security Monitoring", "Threat Modeling",
                        "Security Incident Response", "Security Compliance", "Key Management",
                        "Certificate Management", "Password Management", "Multi-factor Authentication",
                        "Single Sign-On", "Security Token Service", "Secure Boot", "Secure Storage",
                        "Secure Deletion", "Secure Backup", "Security Policy Enforcement",
                        "Security Awareness Training", "Security Risk Assessment", "Security Hardening",
                        "Security Patching"
                    ],
                    'application_type': [
                        "Web", "Mobile", "Desktop", "IoT", "Cloud",
                        "Microservices", "Serverless", "Distributed", "Real-time", "Big Data",
                        "Machine Learning", "Blockchain", "Financial", "Healthcare", "E-commerce",
                        "Social Media", "Gaming", "Streaming", "Enterprise", "Government",
                        "Critical Infrastructure", "Industrial Control Systems", "Automotive",
                        "Aviation", "Maritime", "Space", "Military", "Telecommunications",
                        "Energy", "Transportation"
                    ],
                    'threats': [
                        "SQL injection attacks",
                        "cross-site scripting (XSS)",
                        "cross-site request forgery (CSRF)",
                        "man-in-the-middle attacks",
                        "denial of service attacks",
                        "buffer overflow vulnerabilities",
                        "memory leaks and resource exhaustion",
                        "insecure deserialization",
                        "broken authentication and session management",
                        "sensitive data exposure",
                        "XML external entity (XXE) attacks",
                        "broken access control",
                        "security misconfiguration",
                        "using components with known vulnerabilities",
                        "insufficient logging and monitoring",
                        "server-side request forgery (SSRF)",
                        "race conditions",
                        "timing attacks",
                        "side-channel attacks",
                        "social engineering attacks"
                    ]
                }
            }
        ]
        
        # Generate 200 problems
        created_problems = []
        problem_count = 0
        
        while problem_count < 200:
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
            elif "security" in title.lower() or "authentication" in title.lower():
                input_description = "Security-related inputs such as credentials, tokens, or data to be protected."
                output_description = "Security outcomes such as authentication results, encrypted data, or security logs."
                sample_input = "username=user123&password=securepass&token=abc123"
                sample_output = "Authentication successful: true\nSession token: xyz789\nExpiration: 3600s"
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
            print(f"Created problem {problem_count}/200: {problem.title} (ID: {problem.id})")
        
        print(f"\nSuccessfully created {len(created_problems)} unique problems!")
        
    except Exception as e:
        print(f"Error creating problems: {str(e)}")

if __name__ == "__main__":
    create_unique_problems()