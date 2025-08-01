from django.contrib import admin
from .models import CustomUser, Problem
from .student_practice import Submission, TestCase, TestCaseResult, StudentStatistics

# Register the CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

# Register the Problem model
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'problem_type', 'difficulty', 'created_by', 'submission_count', 'accepted_count', 'is_active')
    list_filter = ('problem_type', 'difficulty', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('id',)

# Register the Submission model
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'language', 'status', 'execution_time', 'memory_used', 'created_at')
    list_filter = ('status', 'language')
    search_fields = ('user__username', 'problem__title')
    ordering = ('-created_at',)

# Register the TestCase model
@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem', 'is_sample')
    list_filter = ('is_sample',)
    search_fields = ('problem__title',)

# Register the TestCaseResult model
@admin.register(TestCaseResult)
class TestCaseResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'submission', 'test_case', 'status', 'execution_time', 'memory_used')
    list_filter = ('status',)
    search_fields = ('submission__id', 'test_case__id')

# Register the StudentStatistics model
@admin.register(StudentStatistics)
class StudentStatisticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_submissions', 'accepted_submissions', 'total_problems_attempted', 'total_problems_solved')
    search_fields = ('user__username',)