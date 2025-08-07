# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from .custom_user_models import CustomUser

class Tag(models.Model):
    """
    题目标签模型
    """
    class Meta:
        db_table = "own_models_tag"  # 指定明确的表名
        verbose_name = "标签"
        verbose_name_plural = "标签"
    
    name = models.CharField(("标签名称"), max_length=50, unique=True)
    description = models.TextField(("标签描述"), blank=True, null=True)
    created_at = models.DateTimeField(("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(("更新时间"), auto_now=True)
    
    def __str__(self):
        return self.name

class Problem(models.Model):
    """
    题目模型
    """
    class Meta:
        db_table = "own_models_problem"  # 指定明确的表名
        verbose_name = "题目"
        verbose_name_plural = "题目"
    
    DIFFICULTY_CHOICES = (
        (1, "简单"),
        (2, "中等"),
        (3, "困难"),
    )
    
    PROBLEM_TYPE_CHOICES = (
        (1, "选择题"),
        (2, "填空题"),
        (3, "判断题"),
        (4, "编程题"),
        (5, "简答题"),
    )
    
    # 题目基本信息
    title = models.CharField(("题目标题"), max_length=200)
    description = models.TextField(("题目描述"))
    problem_type = models.PositiveSmallIntegerField(("题目类型"), choices=PROBLEM_TYPE_CHOICES, default=1)
    knowledge_point = models.CharField(("知识点"), max_length=100, blank=True, null=True, help_text="例如：判断、循环、函数、模块等")
    input_description = models.TextField(("输入描述"), blank=True)
    output_description = models.TextField(("输出描述"), blank=True)
    sample_input = models.TextField(("样例输入"), blank=True)
    sample_output = models.TextField(("样例输出"), blank=True)
    hint = models.TextField(("提示"), blank=True, null=True)
    difficulty = models.PositiveSmallIntegerField(("难度"), choices=DIFFICULTY_CHOICES, default=1)
    
    # 题目元数据
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_problems", verbose_name=("创建者"))
    created_at = models.DateTimeField(("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(("更新时间"), auto_now=True)
    is_active = models.BooleanField(("是否激活"), default=True)
    
    # 题目统计信息
    submission_count = models.IntegerField(("提交次数"), default=0)
    accepted_count = models.IntegerField(("通过次数"), default=0)
    
    # 添加与Tag的多对多关系
    tags = models.ManyToManyField(Tag, verbose_name=("标签"), blank=True, related_name="problems")
    
    def __str__(self):
        return self.title