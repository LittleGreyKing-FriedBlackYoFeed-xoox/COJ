# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from .custom_user_models import CustomUser
from .problem_models import Problem, Tag

class LearningFeedback(models.Model):
    """
    Learning Feedback model for providing personalized feedback to students
    based on their problem-solving performance
    """
    class Meta:
        db_table = "own_models_learning_feedback"
        verbose_name = "Learning Feedback"
        verbose_name_plural = "Learning Feedbacks"
    
    # User relationship
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="learning_feedback", verbose_name="User")
    
    # Feedback content
    strengths = models.TextField("Strengths", blank=True, help_text="Knowledge points the student is strong in")
    weaknesses = models.TextField("Weaknesses", blank=True, help_text="Knowledge points the student needs to improve")
    recommendations = models.TextField("Recommendations", blank=True, help_text="Recommended problems or topics to practice")
    
    # Performance metrics
    average_completion_time = models.FloatField("Average Completion Time (ms)", default=0)
    success_rate = models.FloatField("Success Rate (%)", default=0)
    
    # Metadata
    last_updated = models.DateTimeField("Last Updated", auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Learning Feedback"
    
    @property
    def strengths_list(self):
        """Return strengths as a list"""
        if not self.strengths or self.strengths == "No specific strengths identified yet.":
            return []
        return [s.strip() for s in self.strengths.split(',')]
    
    @property
    def weaknesses_list(self):
        """Return weaknesses as a list"""
        if not self.weaknesses or self.weaknesses == "No specific weaknesses identified yet.":
            return []
        return [w.strip() for w in self.weaknesses.split(',')]
    
    @property
    def recommendations_list(self):
        """Return recommendations as a list"""
        if not self.recommendations or self.recommendations == "Try to solve more problems to get personalized recommendations.":
            return []
        return self.recommendations.split('\n')
    
    def update_feedback(self):
        """
        Update the learning feedback based on the user's submission history
        """
        from .student_practice import Submission
        from django.db.models import Avg, Count, Q
        
        # Get all user submissions
        submissions = Submission.objects.filter(user=self.user)
        
        # Calculate success rate
        total_submissions = submissions.count()
        if total_submissions > 0:
            accepted_submissions = submissions.filter(status='accepted').count()
            self.success_rate = (accepted_submissions / total_submissions) * 100
        else:
            self.success_rate = 0
        
        # Calculate average completion time for accepted submissions
        avg_time = submissions.filter(status='accepted').aggregate(avg_time=Avg('execution_time'))
        self.average_completion_time = avg_time['avg_time'] if avg_time['avg_time'] else 0
        
        # Analyze strengths (problems solved with good performance)
        # 原有 ORM 写法不支持跨表 avg 聚合，改为仅统计 accepted 数量最多的知识点
        strength_submissions = submissions.filter(
            status='accepted'
        ).values('problem__knowledge_point').annotate(count=Count('id')).order_by('-count')[:5]
        
        strengths = []
        for item in strength_submissions:
            if item['problem__knowledge_point']:
                strengths.append(item['problem__knowledge_point'])
        
        self.strengths = ", ".join(strengths) if strengths else "No specific strengths identified yet."
        
        # Analyze weaknesses (problems with multiple failed attempts)
        weakness_problems = Problem.objects.filter(
            submissions__user=self.user
        ).annotate(
            attempts=Count('submissions', filter=Q(submissions__user=self.user)),
            accepted=Count('submissions', filter=Q(submissions__user=self.user, submissions__status='accepted'))
        ).filter(
            attempts__gt=3,
            accepted=0
        ).values('knowledge_point').annotate(count=Count('id')).order_by('-count')[:5]
        
        weaknesses = []
        for item in weakness_problems:
            if item['knowledge_point']:
                weaknesses.append(item['knowledge_point'])
        
        self.weaknesses = ", ".join(weaknesses) if weaknesses else "No specific weaknesses identified yet."
        
        # Generate recommendations based on weaknesses
        if weaknesses:
            # Find problems related to weak knowledge points that the user hasn't attempted yet
            recommended_problems = Problem.objects.filter(
                knowledge_point__in=weaknesses
            ).exclude(
                submissions__user=self.user
            ).order_by('difficulty')[:5]
            
            recommendations = []
            for problem in recommended_problems:
                recommendations.append(f"Problem #{problem.id}: {problem.title} ({problem.get_difficulty_display()})")
            
            self.recommendations = "\n".join(recommendations) if recommendations else "Continue practicing problems across different knowledge areas."
        else:
            self.recommendations = "Try to solve more problems to get personalized recommendations."
        
        # Save the updated feedback
        self.save()

class KnowledgePointPerformance(models.Model):
    """
    Model to track student performance on specific knowledge points
    """
    class Meta:
        db_table = "own_models_knowledge_point_performance"
        verbose_name = "Knowledge Point Performance"
        verbose_name_plural = "Knowledge Point Performances"
        unique_together = ('user', 'knowledge_point')
    
    # Relationships
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="knowledge_performances", verbose_name="User")
    knowledge_point = models.CharField("Knowledge Point", max_length=100)
    
    # Performance metrics
    problems_attempted = models.IntegerField("Problems Attempted", default=0)
    problems_solved = models.IntegerField("Problems Solved", default=0)
    average_attempts = models.FloatField("Average Attempts per Problem", default=0)
    average_time = models.FloatField("Average Time (ms)", default=0)
    
    # Metadata
    last_updated = models.DateTimeField("Last Updated", auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.knowledge_point} Performance"
    
    @property
    def success_rate(self):
        """Calculate success rate"""
        if self.problems_attempted > 0:
            return (self.problems_solved / self.problems_attempted) * 100
        return 0
    
    @staticmethod
    def update_all_performances(user):
        """
        Update performance metrics for all knowledge points for a specific user
        """
        from .student_practice import Submission
        from django.db.models import Count, Avg, F, Q
        
        # Get all knowledge points from user's submissions
        knowledge_points = Problem.objects.filter(
            submissions__user=user
        ).values_list('knowledge_point', flat=True).distinct()
        
        for kp in knowledge_points:
            if not kp:  # Skip empty knowledge points
                continue
                
            # Get problems with this knowledge point
            problems = Problem.objects.filter(knowledge_point=kp)
            problem_ids = problems.values_list('id', flat=True)
            
            # Get user's submissions for these problems
            submissions = Submission.objects.filter(user=user, problem_id__in=problem_ids)
            
            # Calculate metrics
            problems_attempted = submissions.values('problem').distinct().count()
            problems_solved = submissions.filter(status='accepted').values('problem').distinct().count()
            
            # Calculate average attempts per problem
            if problems_attempted > 0:
                total_attempts = submissions.count()
                average_attempts = total_attempts / problems_attempted
            else:
                average_attempts = 0
                
            # Calculate average time for accepted submissions
            avg_time_data = submissions.filter(status='accepted').aggregate(avg_time=Avg('execution_time'))
            average_time = avg_time_data['avg_time'] if avg_time_data['avg_time'] else 0
            
            # Update or create the performance record
            performance, created = KnowledgePointPerformance.objects.update_or_create(
                user=user,
                knowledge_point=kp,
                defaults={
                    'problems_attempted': problems_attempted,
                    'problems_solved': problems_solved,
                    'average_attempts': average_attempts,
                    'average_time': average_time
                }
            )