from django.db import models
from django.conf import settings

class Competition(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey('own_models.CustomUser', on_delete=models.CASCADE, related_name='created_competitions')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

class Paper(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='papers')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    problems = models.ManyToManyField('own_models.Problem', related_name='papers')
    assigned_users = models.ManyToManyField('own_models.CustomUser', through='PaperAssignment', related_name='assigned_papers')

class PaperAssignment(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    user = models.ForeignKey('own_models.CustomUser', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

# 假设题目模型已在 own_models.problem_models.py 中定义为 Problem