import os
import sys
import django
import random

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

from own_models.problem_models import Problem
from own_models.student_practice import Submission
from django.contrib.auth import get_user_model

User = get_user_model()

def create_submissions_for_problem(problem_id, num_submissions=5):
    try:
        problem = Problem.objects.get(id=problem_id)
        users = User.objects.all()
        if not users.exists():
            print("No users found. Please create some users first.")
            return

        # Base code with some variations
        base_code = ["""def solve():
    a = int(input())
    b = int(input())
    print(a + b)
""",
                     """def solution():
    x = int(input())
    y = int(input())
    print(x + y)
""",
                     """# Add two numbers
num1 = int(input())
num2 = int(input())
sum = num1 + num2
print(sum)
""",
                     """# A different approach
import sys
lines = sys.stdin.readlines()
a = int(lines[0])
b = int(lines[1])
print(a+b)
""",
                     """# Unique solution
print(sum(map(int, __import__('sys').stdin)))
"""]

        for i in range(num_submissions):
            user = random.choice(users)
            code = random.choice(base_code)
            # Add some random comments to make code slightly different
            code += f"\n# Submission by {user.username}"

            Submission.objects.create(
                user=user,
                problem=problem,
                code=code,
                language='python',
                status='accepted'
            )
            print(f"Created submission for problem {problem.title} by {user.username}")

    except Problem.DoesNotExist:
        print(f"Problem with id {problem_id} does not exist.")

if __name__ == '__main__':
    # Assuming a problem with ID 1 exists. Change if necessary.
    problem_id_to_test = 1
    create_submissions_for_problem(problem_id_to_test, 10)