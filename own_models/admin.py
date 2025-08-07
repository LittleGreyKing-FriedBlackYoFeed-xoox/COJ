from django.contrib import admin
from own_models.ranking_system_models import RankingSystem
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance

@admin.register(RankingSystem)
class RankingSystemAdmin(admin.ModelAdmin):
    list_display = ('user', 'problems_completed', 'total_attempts', 'rank_position', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ('user__username', 'user__email')
    ordering = ('rank_position',)
    readonly_fields = ('rank_position', 'last_updated')


@admin.register(LearningFeedback)
class LearningFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'success_rate', 'average_completion_time', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('last_updated',)


@admin.register(KnowledgePointPerformance)
class KnowledgePointPerformanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'knowledge_point', 'problems_attempted', 'problems_solved', 'average_attempts', 'average_time')
    list_filter = ('knowledge_point', 'last_updated')
    search_fields = ('user__username', 'user__email', 'knowledge_point')
    readonly_fields = ('last_updated',)

