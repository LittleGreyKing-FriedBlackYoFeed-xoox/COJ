import os
import sys
import django
import random
from datetime import timedelta

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

from django.utils import timezone
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem
from own_models.student_practice import Submission, StudentStatistics
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance
from own_models.update_learning_feedback import update_learning_feedback_for_user

def generate_sample_problems(num_problems=100):
    """Generate sample problems if not enough exist"""
    existing_problems = Problem.objects.count()
    if existing_problems >= num_problems:
        print(f"Already have {existing_problems} problems, no need to generate more.")
        return Problem.objects.all()
    
    print(f"Generating {num_problems - existing_problems} sample problems...")
    
    # Define problem attributes
    difficulties = [1, 2, 3]  # Easy, Medium, Hard
    problem_types = [1, 2, 3, 4, 5]  # Using the PROBLEM_TYPE_CHOICES from the model
    knowledge_points = [
        'data_structure', 'algorithm', 'database', 'network', 'operating_system',
        'frontend', 'backend', 'computer_basics', 'programming_language',
        'machine_learning', 'artificial_intelligence', 'security', 'distributed_systems',
        'mobile_development', 'cloud_computing', 'web_development', 'game_development'
    ]
    
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
    try:
        creator = CustomUser.objects.first()
    except:
        print("No users found. Please create at least one user first.")
        return Problem.objects.all()
    
    # Generate problems
    for i in range(existing_problems + 1, num_problems + 1):
        difficulty = random.choice(difficulties)
        problem_type = random.choice(problem_types)
        knowledge_point = random.choice(knowledge_points)
        
        # Generate a more realistic title and description
        topic = random.choice(topics)
        description_template = random.choice(descriptions)
        title = f"{topic.title()} {['Challenge', 'Problem', 'Exercise', 'Task', 'Quiz'][random.randint(0, 4)]} {i}"
        description = description_template.format(topic, knowledge_point)
        
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
        print(f"Created problem: {problem.title} ({problem.knowledge_point})")
    
    return Problem.objects.all()

def generate_sample_submissions(user, problems, num_submissions=200):
    """Generate sample submissions for a user"""
    print(f"Generating {num_submissions} sample submissions for user {user.username}...")
    
    # Define submission attributes
    languages = ['python', 'java', 'cpp', 'c', 'javascript']
    statuses = ['accepted', 'wrong_answer', 'time_limit_exceeded', 'runtime_error', 'compile_error']
    status_weights = [0.7, 0.15, 0.08, 0.04, 0.03]  # Increased success rate for better visuals
    
    # Track statistics
    problems_attempted = set()
    problems_solved = set()
    
    # Generate submissions
    for _ in range(num_submissions):
        # Select a random problem
        problem = random.choice(problems)
        problems_attempted.add(problem.id)
        
        # Determine submission attributes
        language = random.choice(languages)
        status = random.choices(statuses, weights=status_weights, k=1)[0]
        execution_time = random.randint(10, 500)  # 10ms to 500ms
        memory_used = random.randint(1000, 10000)  # 1MB to 10MB
        
        # Create submission with a random date in the past 90 days for better trend data
        submission_date = timezone.now() - timedelta(
            days=random.randint(0, 90),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        
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
        
        if status == 'accepted':
            problems_solved.add(problem.id)
    
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
    
    return len(problems_attempted), len(problems_solved)

def generate_realistic_feedback_text(strengths, weaknesses):
    """Generate realistic feedback text based on strengths and weaknesses"""
    
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
    
    return {
        'strengths': ", ".join(strength_feedback),
        'weaknesses': ", ".join(weakness_feedback),
        'recommendations': "\n".join(recommendations)
    }

def generate_learning_feedback_data():
    """Generate learning feedback data for all student users"""
    # Get all student users
    students = CustomUser.objects.filter(role=1)
    
    if not students:
        print("No student users found. Please create at least one student user first.")
        return
    
    print(f"Found {students.count()} student users.")
    
    # Generate sample problems
    problems = generate_sample_problems(num_problems=100)
    
    # For each student, generate submissions and update learning feedback
    for student in students:
        print(f"\nProcessing student: {student.username}")
        
        # Generate sample submissions
        problems_attempted, problems_solved = generate_sample_submissions(
            user=student,
            problems=problems,
            num_submissions=random.randint(100, 300)  # More submissions for better data
        )
        
        # Update learning feedback
        print(f"Updating learning feedback for {student.username}...")
        update_learning_feedback_for_user(student.id)
        
        # Enhance the feedback with more realistic text
        feedback = LearningFeedback.objects.get(user=student)
        
        # Get knowledge point performances to identify strengths and weaknesses
        performances = KnowledgePointPerformance.objects.filter(user=student).order_by('-problems_solved')
        
        # Identify strengths (high success rate)
        strengths = []
        for perf in performances:
            if perf.problems_attempted > 0 and perf.problems_solved / perf.problems_attempted >= 0.7:
                strengths.append(perf.knowledge_point)
        
        # Identify weaknesses (low success rate but multiple attempts)
        weaknesses = []
        for perf in performances:
            if perf.problems_attempted >= 3 and perf.problems_solved / perf.problems_attempted <= 0.5:
                weaknesses.append(perf.knowledge_point)
        
        # Generate realistic feedback text
        if strengths or weaknesses:
            realistic_feedback = generate_realistic_feedback_text(strengths, weaknesses)
            
            # Update the feedback with realistic text
            feedback.strengths = realistic_feedback['strengths']
            feedback.weaknesses = realistic_feedback['weaknesses']
            feedback.recommendations = realistic_feedback['recommendations']
            feedback.save()
        
        # Verify learning feedback was created
        feedback = LearningFeedback.objects.get(user=student)
        print(f"Learning feedback created/updated for {student.username}")
        print(f"Success rate: {feedback.success_rate:.1f}%")
        print(f"Average completion time: {feedback.average_completion_time:.1f}ms")
        
        # Verify knowledge point performances were created
        kp_count = KnowledgePointPerformance.objects.filter(user=student).count()
        print(f"Created {kp_count} knowledge point performance records")

if __name__ == "__main__":
    print("Starting to generate learning feedback data...")
    generate_learning_feedback_data()
    print("\nLearning feedback data generation completed!")