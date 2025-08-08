from django.db import models
from own_models.student_practice import Submission

class CodeDuplicationCheck(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='duplication_checks')
    similarity_score = models.FloatField()
    duplication_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Duplication check for submission {self.submission.id}"