# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

# 从自定义模型文件导入模型
from .custom_user_models import CustomUser
from .problem_models import Problem
from .student_practice import Submission, TestCase, TestCaseResult, StudentStatistics
from .ranking_system_models import RankingSystem
from .learning_feedback_models import LearningFeedback, KnowledgePointPerformance

# 这个文件现在只是一个导入点，实际模型定义在各个模型文件中
# 这样做是为了保持与Django的约定兼容，Django默认会在每个应用的models.py中查找模型

