from django.db import models
from django.conf import settings
from own_models.problem_models import Problem

class ManualReviewRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('reviewed', 'Reviewed'),
        ('rejected', 'Rejected'),
    ]
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manual_review_requests')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='manual_reviews')
    review_time = models.DateTimeField(null=True, blank=True)
    review_comment = models.TextField(blank=True, default='')
    annotated_code = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Manual Review Request'
        verbose_name_plural = 'Manual Review Requests'
        ordering = ['-request_time']

    def __str__(self):
        return f"{self.student} - {self.problem} - {self.status}"