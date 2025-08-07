# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from .custom_user_models import CustomUser

class RankingSystem(models.Model):
    """
    Ranking System model for tracking user rankings based on problem completion and attempts
    """
    class Meta:
        db_table = "own_models_ranking_system"
        verbose_name = "Ranking System"
        verbose_name_plural = "Ranking Systems"
    
    # User relationship
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="ranking", verbose_name="User")
    
    # Ranking metrics
    problems_completed = models.IntegerField("Problems Completed", default=0)
    total_attempts = models.IntegerField("Total Attempts", default=0)
    
    # Ranking position (calculated field)
    rank_position = models.IntegerField("Rank Position", default=0)
    
    # Metadata
    last_updated = models.DateTimeField("Last Updated", auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Ranking - Position: {self.rank_position}"
    
    @staticmethod
    def update_all_rankings():
        """
        Update rankings for all users based on problems completed and total attempts
        """
        # Get all ranking records ordered by problems_completed (desc) and total_attempts (asc)
        rankings = RankingSystem.objects.all().order_by('-problems_completed', 'total_attempts')
        
        # Update rank positions
        for index, ranking in enumerate(rankings, 1):
            ranking.rank_position = index
            ranking.save(update_fields=['rank_position'])
    
    def update_metrics(self):
        """
        Update the metrics for this user's ranking
        """
        from .student_practice import Submission
        from django.db.models import Count
        
        # Count unique problems completed
        completed_problems = Submission.objects.filter(
            user=self.user, 
            status='accepted'
        ).values('problem').distinct().count()
        
        # Count total submission attempts
        total_attempts = Submission.objects.filter(user=self.user).count()
        
        # Update the metrics
        self.problems_completed = completed_problems
        self.total_attempts = total_attempts
        self.save(update_fields=['problems_completed', 'total_attempts', 'last_updated'])