import os
import sys
import django

# 初始化Django环境
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()
from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem
from own_models.student_practice import Submission
from test_script.populate_learning_feedback import generate_realistic_submissions

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

if __name__ == "__main__":
    # 每批处理5个未有提交记录的学生
    BATCH_SIZE = 5
    NUM_SUBMISSIONS = 50  # 每个用户生成的提交数，可根据需要调整
    # 获取所有未有提交记录的学生用户
    users = CustomUser.objects.filter(role=1).exclude(id__in=Submission.objects.values('user_id').distinct())[:BATCH_SIZE]
    if not users:
        print("没有更多未生成数据的学生用户。")
        sys.exit(0)
    problems = list(Problem.objects.all())
    if not problems:
        print("题库为空，请先生成题目。")
        sys.exit(1)
    for user in users:
        print(f"为用户 {user.username} (ID: {user.id}) 生成题目完成与提交数据...")
        try:
            generate_realistic_submissions(user, problems, NUM_SUBMISSIONS)
            print(f"用户 {user.username} 数据生成完成。\n")
        except Exception as e:
            print(f"用户 {user.username} 数据生成失败: {str(e)}\n")
    print(f"本批次处理完毕，共处理 {len(users)} 位学生。请检查效果后再运行下一批。")