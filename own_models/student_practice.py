# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from .custom_user_models import CustomUser
from .problem_models import Problem

class Submission(models.Model):
    """
    学生提交的代码模型
    """
    class Meta:
        db_table = "own_models_submission"
        verbose_name = "提交记录"
        verbose_name_plural = "提交记录"
    
    STATUS_CHOICES = (
        ('pending', '评测中'),
        ('accepted', '通过'),
        ('wrong_answer', '答案错误'),
        ('time_limit_exceeded', '超时'),
        ('memory_limit_exceeded', '内存超限'),
        ('runtime_error', '运行时错误'),
        ('compile_error', '编译错误'),
        ('system_error', '系统错误'),
    )
    
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('c', 'C'),
        ('javascript', 'JavaScript'),
    )
    
    # 关联信息
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="submissions", verbose_name="提交用户")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="submissions", verbose_name="题目")
    
    # 提交内容
    code = models.TextField("代码")
    language = models.CharField("编程语言", max_length=20, choices=LANGUAGE_CHOICES)
    
    # 评测结果
    status = models.CharField("状态", max_length=30, choices=STATUS_CHOICES, default='pending')
    execution_time = models.IntegerField("执行时间(ms)", default=0)
    memory_used = models.IntegerField("内存使用(KB)", default=0)
    error_message = models.TextField("错误信息", blank=True, null=True)
    
    # 元数据
    created_at = models.DateTimeField("提交时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.get_status_display()}"

class TestCase(models.Model):
    """
    测试用例模型
    """
    class Meta:
        db_table = "own_models_testcase"
        verbose_name = "测试用例"
        verbose_name_plural = "测试用例"
    
    # 关联信息
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="test_cases", verbose_name="题目")
    
    # 测试用例内容
    input_data = models.TextField("输入数据")
    expected_output = models.TextField("期望输出")
    is_sample = models.BooleanField("是否为样例", default=False)
    
    # 元数据
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    
    def __str__(self):
        return f"测试用例 {self.id} - 题目 {self.problem.id}"

class TestCaseResult(models.Model):
    """
    测试用例结果模型
    """
    class Meta:
        db_table = "own_models_testcase_result"
        verbose_name = "测试用例结果"
        verbose_name_plural = "测试用例结果"
    
    STATUS_CHOICES = (
        ('passed', '通过'),
        ('failed', '失败'),
    )
    
    # 关联信息
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="test_results", verbose_name="提交记录")
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name="results", verbose_name="测试用例")
    
    # 结果信息
    status = models.CharField("状态", max_length=10, choices=STATUS_CHOICES)
    execution_time = models.IntegerField("执行时间(ms)", default=0)
    memory_used = models.IntegerField("内存使用(KB)", default=0)
    error_message = models.TextField("错误信息", blank=True, null=True)
    
    # 元数据
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    
    def __str__(self):
        return f"提交 {self.submission.id} - 测试用例 {self.test_case.id} - {self.get_status_display()}"

class StudentStatistics(models.Model):
    """
    学生统计数据模型
    """
    class Meta:
        db_table = "own_models_student_statistics"
        verbose_name = "学生统计"
        verbose_name_plural = "学生统计"
    
    # 关联信息
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="statistics", verbose_name="用户")
    
    # 统计数据
    total_submissions = models.IntegerField("总提交次数", default=0)
    accepted_submissions = models.IntegerField("通过提交次数", default=0)
    total_problems_attempted = models.IntegerField("尝试题目数", default=0)
    total_problems_solved = models.IntegerField("解决题目数", default=0)
    
    # 难度统计
    easy_problems_solved = models.IntegerField("简单题解决数", default=0)
    medium_problems_solved = models.IntegerField("中等题解决数", default=0)
    hard_problems_solved = models.IntegerField("困难题解决数", default=0)
    
    # 元数据
    last_updated = models.DateTimeField("最后更新时间", auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} 的统计数据"
    
    def update_statistics(self):
        """更新统计数据"""
        from django.db.models import Count, Q
        
        # 获取用户的所有提交
        submissions = Submission.objects.filter(user=self.user)
        
        # 更新提交统计
        self.total_submissions = submissions.count()
        self.accepted_submissions = submissions.filter(status='accepted').count()
        
        # 获取尝试过的题目和解决的题目
        attempted_problems = submissions.values('problem').annotate(count=Count('problem')).count()
        solved_problems = submissions.filter(status='accepted').values('problem').annotate(count=Count('problem')).count()
        
        self.total_problems_attempted = attempted_problems
        self.total_problems_solved = solved_problems
        
        # 更新难度统计
        self.easy_problems_solved = submissions.filter(
            status='accepted', 
            problem__difficulty=1  # 使用数字1代表简单
        ).values('problem').annotate(count=Count('problem')).count()
        
        self.medium_problems_solved = submissions.filter(
            status='accepted', 
            problem__difficulty=2  # 使用数字2代表中等
        ).values('problem').annotate(count=Count('problem')).count()
        
        self.hard_problems_solved = submissions.filter(
            status='accepted', 
            problem__difficulty=3  # 使用数字3代表困难
        ).values('problem').annotate(count=Count('problem')).count()
        
        # 保存更新
        self.save()