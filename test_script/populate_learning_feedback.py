import os
import sys
import django
import random
from datetime import timedelta, datetime

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

from django.utils import timezone
from django.db import transaction
from django.db.models import Avg, Count, Q
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem, Tag
from own_models.student_practice import Submission, StudentStatistics, TestCase, TestCaseResult
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance

# Configuration
NUM_PROBLEMS = 100
NUM_SUBMISSIONS = 300
KNOWLEDGE_POINTS = [
    'data_structure', 'algorithm', 'database', 'network', 'operating_system',
    'frontend', 'backend', 'computer_basics', 'programming_language',
    'machine_learning', 'artificial_intelligence', 'security', 'distributed_systems',
    'mobile_development', 'cloud_computing', 'web_development', 'game_development'
]

def create_sample_problems(num_problems=NUM_PROBLEMS):
    """Create a diverse set of sample problems"""
    print(f"Creating {num_problems} sample problems...")
    
    # Define problem attributes
    difficulties = [1, 2, 3]  # Easy, Medium, Hard
    problem_types = [1, 2, 3, 4, 5]  # Using the PROBLEM_TYPE_CHOICES from the model
    
    # Create more detailed problem descriptions
    descriptions = [
        "Implement a solution to solve the {0} problem efficiently using {1} techniques.",
        "Design an algorithm that optimizes {0} operations with a focus on {1} principles.",
        "Create a {0} system that handles multiple {1} operations simultaneously.",
        "Develop a {0} solution that addresses common {1} challenges in real-world applications.",
        "Build a robust {0} implementation that follows best practices in {1}.",
        "Optimize a {0} algorithm to improve performance in {1} scenarios.",
        "Debug and fix issues in a {0} implementation related to {1} concepts.",
        "Analyze the complexity of a {0} solution in the context of {1}.",
        "Implement a {0} data structure that efficiently supports {1} operations.",
        "Design a {0} system architecture that scales well for {1} workloads."
    ]
    
    # Create problem topics
    topics = [
        "sorting", "searching", "graph traversal", "dynamic programming", "greedy algorithms",
        "backtracking", "divide and conquer", "tree traversal", "hashing", "string matching",
        "bit manipulation", "recursion", "linked lists", "stacks", "queues", "heaps",
        "binary search trees", "balanced trees", "trie", "segment trees", "union-find",
        "sliding window", "two pointers", "breadth-first search", "depth-first search",
        "topological sort", "minimum spanning tree", "shortest path", "network flow"
    ]
    
    # Get a user to be the creator
    creator = CustomUser.objects.first()
    
    # Check existing problems
    existing_count = Problem.objects.count()
    if existing_count >= num_problems:
        print(f"Already have {existing_count} problems, no need to create more.")
        return Problem.objects.all()
    
    problems_to_create = num_problems - existing_count
    problems = list(Problem.objects.all())
    
    # Create new problems
    for i in range(existing_count + 1, num_problems + 1):
        # Generate a more realistic title and description
        topic = random.choice(topics)
        knowledge_point = random.choice(KNOWLEDGE_POINTS)
        description_template = random.choice(descriptions)
        title = f"{topic.title()} {['Challenge', 'Problem', 'Exercise', 'Task', 'Quiz'][random.randint(0, 4)]} {i}"
        description = description_template.format(topic, knowledge_point)
        
        difficulty = random.choice(difficulties)
        problem_type = random.choice(problem_types)
        
        problem = Problem(
            title=title,
            description=description,
            difficulty=difficulty,
            problem_type=problem_type,
            knowledge_point=knowledge_point,
            created_by=creator,
            created_at=timezone.now() - timedelta(days=random.randint(1, 60)),
            updated_at=timezone.now() - timedelta(days=random.randint(0, 30))
        )
        problem.save()
        problems.append(problem)
        print(f"Created problem: {problem.title} ({problem.knowledge_point})")
    
    # Create tags for problems
    tags = ["Array", "String", "Hash Table", "Dynamic Programming", "Math", 
            "Greedy", "Sorting", "Depth-First Search", "Binary Search", "Tree",
            "Breadth-First Search", "Graph", "Stack", "Backtracking", "Design",
            "Bit Manipulation", "Heap", "Sliding Window", "Divide and Conquer",
            "Recursion", "Linked List", "Binary Tree", "Queue", "Trie", "Geometry"]
    
    for tag_name in tags:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        if created:
            print(f"Created tag: {tag_name}")
    
    # Assign tags to problems
    all_tags = Tag.objects.all()
    for problem in problems:
        # Assign 2-4 random tags to each problem
        num_tags = random.randint(2, 4)
        selected_tags = random.sample(list(all_tags), num_tags)
        for tag in selected_tags:
            problem.tags.add(tag)
        print(f"Added {num_tags} tags to problem: {problem.title}")
    
    return problems

def generate_realistic_submissions(user, problems, num_submissions=NUM_SUBMISSIONS):
    """Generate realistic submission data for a user"""
    print(f"Generating {num_submissions} submissions for user {user.username}...")
    
    # Define submission attributes
    languages = ['python', 'java', 'cpp', 'c', 'javascript']
    statuses = ['accepted', 'wrong_answer', 'time_limit_exceeded', 'runtime_error', 'compile_error']
    status_weights = [0.7, 0.15, 0.08, 0.04, 0.03]  # Higher success rate for better visuals
    
    # Track statistics
    problems_attempted = set()
    problems_solved = set()
    knowledge_points_data = {}
    
    # Create a distribution of submissions over time (more recent = more submissions)
    date_ranges = [
        (90, 61, 0.1),  # 10% of submissions from 90-61 days ago
        (60, 31, 0.2),  # 20% of submissions from 60-31 days ago
        (30, 8, 0.3),   # 30% of submissions from 30-8 days ago
        (7, 0, 0.4),    # 40% of submissions from last 7 days
    ]
    
    # Distribute submissions across knowledge points
    knowledge_point_weights = {}
    for kp in KNOWLEDGE_POINTS:
        knowledge_point_weights[kp] = random.uniform(0.2, 1.0)
    
    # Normalize weights
    total_weight = sum(knowledge_point_weights.values())
    for kp in knowledge_point_weights:
        knowledge_point_weights[kp] /= total_weight
    
    # Generate submissions
    with transaction.atomic():
        for _ in range(num_submissions):
            # Determine submission date based on distribution
            range_choice = random.choices(
                date_ranges, 
                weights=[r[2] for r in date_ranges], 
                k=1
            )[0]
            
            days_ago = random.randint(range_choice[1], range_choice[0])
            hours_ago = random.randint(0, 23)
            minutes_ago = random.randint(0, 59)
            
            submission_date = timezone.now() - timedelta(
                days=days_ago,
                hours=hours_ago,
                minutes=minutes_ago
            )
            
            # Select a problem with bias towards certain knowledge points
            filtered_problems = [p for p in problems if hasattr(p, 'knowledge_point') and p.knowledge_point]
            if not filtered_problems:
                filtered_problems = problems
                
            weights = [knowledge_point_weights.get(getattr(p, 'knowledge_point', ''), 0.5) for p in filtered_problems]
            problem = random.choices(filtered_problems, weights=weights, k=1)[0]
            
            # Track knowledge point data
            kp = getattr(problem, 'knowledge_point', 'unknown')
            if kp not in knowledge_points_data:
                knowledge_points_data[kp] = {'attempted': 0, 'solved': 0}
            knowledge_points_data[kp]['attempted'] += 1
            
            problems_attempted.add(problem.id)
            
            # Choose a random language with bias towards python and javascript
            language_weights = [0.4, 0.2, 0.2, 0.1, 0.1]  # python, java, cpp, c, javascript
            language = random.choices(languages, weights=language_weights, k=1)[0]
            
            # Determine submission status with bias based on:
            # 1. More recent submissions have higher success rate
            # 2. Easier problems have higher success rate
            # 3. Some knowledge points have higher success rate
            
            base_success_rate = status_weights[0]  # Base rate for 'accepted'
            
            # Adjust for recency (more recent = higher success)
            recency_bonus = (90 - days_ago) / 90 * 0.1  # Up to 10% bonus for recent submissions
            
            # Adjust for difficulty (easier = higher success)
            difficulty_factor = 0.1 if problem.difficulty == 1 else (0.0 if problem.difficulty == 2 else -0.1)
            
            # Adjust for knowledge point (some areas are stronger)
            kp_factor = 0.1 if kp in ['algorithm', 'data_structure', 'programming_language'] else 0
            
            # Calculate final success probability
            success_prob = min(0.9, max(0.3, base_success_rate + recency_bonus + difficulty_factor + kp_factor))
            
            # Determine status
            if random.random() < success_prob:
                status = 'accepted'
                knowledge_points_data[kp]['solved'] += 1
                problems_solved.add(problem.id)
                execution_time = random.randint(10, 300)  # Faster execution for accepted solutions
            else:
                status = random.choices(statuses[1:], weights=status_weights[1:], k=1)[0]
                execution_time = random.randint(100, 500)  # Slower execution for failed solutions
            
            memory_used = random.randint(1000, 10000)  # 1MB to 10MB
            
            # Create submission
            submission = Submission(
                user=user,
                problem=problem,
                code=f"// Sample code for {problem.title}\n// This is a {status} submission",
                language=language,
                status=status,
                execution_time=execution_time,
                memory_used=memory_used,
                created_at=submission_date,
                updated_at=submission_date
            )
            submission.save()
            
            # Create test case results for this submission
            create_test_case_results(submission, problem, status)
    
    print(f"Generated {num_submissions} submissions for {user.username}")
    print(f"Problems attempted: {len(problems_attempted)}, Problems solved: {len(problems_solved)}")
    
    # Update student statistics
    try:
        stats = StudentStatistics.objects.get(user=user)
    except StudentStatistics.DoesNotExist:
        stats = StudentStatistics(user=user)
    
    stats.total_submissions = Submission.objects.filter(user=user).count()
    stats.accepted_submissions = Submission.objects.filter(user=user, status='accepted').count()
    stats.total_problems_attempted = len(problems_attempted)
    stats.total_problems_solved = len(problems_solved)
    
    # Update difficulty statistics
    stats.easy_problems_solved = Submission.objects.filter(
        user=user, status='accepted', problem__difficulty=1
    ).values('problem').distinct().count()
    
    stats.medium_problems_solved = Submission.objects.filter(
        user=user, status='accepted', problem__difficulty=2
    ).values('problem').distinct().count()
    
    stats.hard_problems_solved = Submission.objects.filter(
        user=user, status='accepted', problem__difficulty=3
    ).values('problem').distinct().count()
    
    stats.last_updated = timezone.now()
    stats.save()
    
    return knowledge_points_data

def create_test_case_results(submission, problem, status):
    """Create test case results for a submission"""
    # Create or get test cases for the problem
    test_cases = TestCase.objects.filter(problem=problem)
    if not test_cases:
        # Create 3-5 test cases for this problem
        num_test_cases = random.randint(3, 5)
        test_cases = []
        for i in range(1, num_test_cases + 1):
            test_case = TestCase(
                problem=problem,
                input_data=f"Test input {i} for problem {problem.id}",
                expected_output=f"Expected output {i} for problem {problem.id}",
                is_sample=(i == 1),  # First test case is a sample
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            test_case.save()
            test_cases.append(test_case)
    
    # Create test case results
    for test_case in test_cases:
        # If submission was accepted, all test cases passed
        # Otherwise, some test cases might have failed
        if status == 'accepted':
            result_status = 'passed'
            output = test_case.expected_output
        elif status == 'wrong_answer':
            # For wrong answer, some test cases might pass, but at least one fails
            if random.random() < 0.3 and test_case != test_cases[-1]:
                result_status = 'passed'
                output = test_case.expected_output
            else:
                result_status = 'failed'
                output = f"Wrong output for test case {test_case.id}"
        elif status == 'time_limit_exceeded':
            result_status = 'timeout'
            output = "Time limit exceeded"
        elif status == 'runtime_error':
            result_status = 'error'
            output = "Runtime error occurred"
        else:  # compile_error
            result_status = 'error'
            output = "Compilation failed"
        
        # Create the test case result
        test_result = TestCaseResult(
            submission=submission,
            test_case=test_case,
            status=result_status,
            output=output,
            execution_time=random.randint(10, 500),
            memory_used=random.randint(1000, 5000)
        )
        test_result.save()

def generate_realistic_feedback(user, knowledge_points_data):
    """Generate realistic learning feedback based on submission data"""
    print(f"Generating realistic learning feedback for {user.username}...")
    
    # Get or create learning feedback
    feedback, created = LearningFeedback.objects.get_or_create(user=user)
    
    # Calculate overall statistics
    submissions = Submission.objects.filter(user=user)
    total_submissions = submissions.count()
    accepted_submissions = submissions.filter(status='accepted').count()
    
    if total_submissions > 0:
        success_rate = (accepted_submissions / total_submissions) * 100
    else:
        success_rate = 0
    
    avg_time = submissions.filter(status='accepted').aggregate(avg_time=Avg('execution_time'))['avg_time'] or 0
    
    # Update feedback model
    feedback.success_rate = success_rate
    feedback.average_completion_time = avg_time
    
    # Identify strengths and weaknesses
    strengths = []
    weaknesses = []
    
    for kp, data in knowledge_points_data.items():
        if data['attempted'] > 0:
            success_rate = (data['solved'] / data['attempted']) * 100
            if success_rate >= 70 and data['attempted'] >= 5:
                strengths.append(kp)
            elif success_rate <= 50 and data['attempted'] >= 3:
                weaknesses.append(kp)
    
    # Generate personalized feedback text
    strength_templates = [
        "You demonstrate excellent understanding of {0} concepts.",
        "Your problem-solving skills in {0} are impressive.",
        "You consistently perform well in {0} related problems.",
        "You show strong proficiency in applying {0} techniques.",
        "Your solutions to {0} problems are efficient and elegant."
    ]
    
    weakness_templates = [
        "You may benefit from more practice with {0} problems.",
        "Consider reviewing fundamental concepts in {0}.",
        "Your solutions to {0} problems could be more efficient.",
        "You sometimes struggle with complex {0} scenarios.",
        "More practice with {0} would help improve your problem-solving speed."
    ]
    
    recommendation_templates = [
        "Focus on practicing more {0} problems to strengthen your skills.",
        "Review the core concepts of {0} and try applying them to different problems.",
        "Work on optimizing your solutions for {0} problems to improve efficiency.",
        "Try solving {0} problems with different approaches to expand your toolkit.",
        "Consider studying advanced {0} techniques to tackle more complex problems."
    ]
    
    # Generate personalized strengths feedback
    strength_feedback = []
    for strength in strengths[:3]:  # Use top 3 strengths
        template = random.choice(strength_templates)
        strength_feedback.append(template.format(strength))
    
    # Generate personalized weaknesses feedback
    weakness_feedback = []
    for weakness in weaknesses[:3]:  # Use top 3 weaknesses
        template = random.choice(weakness_templates)
        weakness_feedback.append(template.format(weakness))
    
    # Generate personalized recommendations
    recommendations = []
    for weakness in weaknesses[:2]:  # Focus recommendations on top weaknesses
        template = random.choice(recommendation_templates)
        recommendations.append(template.format(weakness))
    
    # Add a strength-based recommendation
    if strengths:
        recommendations.append(f"Continue building on your strength in {strengths[0]} by tackling more advanced problems.")
    
    # Add a general recommendation
    recommendations.append("Maintain a consistent practice schedule to improve your overall problem-solving skills.")
    
    # Update feedback text
    feedback.strengths = ". ".join(strength_feedback) if strength_feedback else "Keep practicing to identify your strengths."
    feedback.weaknesses = ". ".join(weakness_feedback) if weakness_feedback else "Keep practicing to identify areas for improvement."
    feedback.recommendations = "\n".join(recommendations)
    feedback.last_updated = timezone.now()
    feedback.save()
    
    print(f"Generated learning feedback for {user.username}")
    
    # Update knowledge point performances
    for kp, data in knowledge_points_data.items():
        performance, created = KnowledgePointPerformance.objects.get_or_create(
            user=user,
            knowledge_point=kp
        )
        
        performance.problems_attempted = data['attempted']
        performance.problems_solved = data['solved']
        
        # Calculate average attempts per problem
        if data['attempted'] > 0:
            avg_attempts = Submission.objects.filter(
                user=user,
                problem__knowledge_point=kp
            ).values('problem').annotate(
                attempt_count=Count('id')
            ).aggregate(
                avg_attempts=Avg('attempt_count')
            )['avg_attempts'] or 1
            
            performance.average_attempts = avg_attempts
        else:
            performance.average_attempts = 0
        
        # Calculate average time
        avg_time = Submission.objects.filter(
            user=user,
            problem__knowledge_point=kp,
            status='accepted'
        ).aggregate(
            avg_time=Avg('execution_time')
        )['avg_time'] or 0
        
        performance.average_time = avg_time
        performance.last_updated = timezone.now()
        performance.save()
    
    print(f"Updated knowledge point performances for {user.username}")

def populate_learning_feedback_data():
    """Main function to populate learning feedback data"""
    try:
        # Get the first student user (assuming this is the logged-in user)
        user = CustomUser.objects.filter(role=1).first()
        
        if not user:
            print("No student users found. Please create at least one student user first.")
            return
        
        print(f"Populating learning feedback data for user: {user.username}")
        
        # Create sample problems
        problems = create_sample_problems(NUM_PROBLEMS)
        
        # Generate submissions
        knowledge_points_data = generate_realistic_submissions(user, problems, NUM_SUBMISSIONS)
        
        # Generate learning feedback
        generate_realistic_feedback(user, knowledge_points_data)
        
        print(f"Successfully populated learning feedback data for {user.username}")
        print("You can now view the learning feedback dashboard at http://127.0.0.1:8000/student/dashboard/")
        
    except Exception as e:
        print(f"Error populating learning feedback data: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Starting to populate learning feedback data...")
    populate_learning_feedback_data()
    print("Done!")