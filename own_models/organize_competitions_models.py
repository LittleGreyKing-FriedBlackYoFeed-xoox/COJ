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
    
    # 新增字段用于更详细的答题数据
    completion_progress = models.IntegerField(default=0, help_text="完成进度百分比 (0-100)")
    completion_rate = models.IntegerField(default=0, help_text="正确率百分比 (0-100)")
    total_duration_minutes = models.IntegerField(default=0, help_text="总答题时长(分钟)")
    first_login_time = models.DateTimeField(null=True, blank=True, help_text="首次登录答题时间")
    
    class Meta:
        unique_together = ('paper', 'user')
    
    def get_status_display(self):
        """获取状态显示文本"""
        if self.is_completed:
            return "已完成"
        elif self.completion_progress > 0:
            return "进行中"
        else:
            return "未开始"
    
    def get_progress_color(self):
        """获取进度条颜色"""
        if self.completion_progress >= 80:
            return "layui-bg-green"
        elif self.completion_progress >= 50:
            return "layui-bg-orange"
        else:
            return "layui-bg-red"

# 假设题目模型已在 own_models.problem_models.py 中定义为 Problem