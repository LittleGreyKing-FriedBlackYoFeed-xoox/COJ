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
from django.db import transaction
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem
from own_models.student_practice import Submission

# 获取所有学生用户
users = list(CustomUser.objects.filter(role=1))
if not users:
    print('No student users found.')
    sys.exit(1)

# 获取所有未被提交过的题目
submitted_problem_ids = set(Submission.objects.values_list('problem_id', flat=True))
all_problems = list(Problem.objects.all())
unsubmitted_problems = [p for p in all_problems if p.id not in submitted_problem_ids]

if not unsubmitted_problems:
    print('All problems have at least one submission.')
    sys.exit(0)

print(f'Found {len(unsubmitted_problems)} unsubmitted problems. Simulating submissions...')

languages = ['python', 'java', 'cpp', 'c', 'javascript']
statuses = ['accepted', 'wrong_answer', 'time_limit_exceeded', 'runtime_error', 'compile_error']
status_weights = [0.7, 0.15, 0.08, 0.04, 0.03]

with transaction.atomic():
    for problem in unsubmitted_problems:
        user = random.choice(users)
        language = random.choice(languages)
        status = random.choices(statuses, weights=status_weights, k=1)[0]
        execution_time = random.randint(10, 500)
        memory_used = random.randint(1000, 10000)
        submission_date = timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        code = f'# Solution for problem {problem.id}\nprint("Hello World")'
        submission = Submission(
            user=user,
            problem=problem,
            code=code,
            language=language,
            status=status,
            execution_time=execution_time,
            memory_used=memory_used,
            error_message='' if status == 'accepted' else 'Simulated error',
            created_at=submission_date,
            updated_at=submission_date
        )
        submission.save()
        print(f'Simulated submission for problem {problem.id} by user {user.username}')

print('Simulation complete.')