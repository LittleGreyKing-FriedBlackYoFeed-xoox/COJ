from django.urls import path
from views.learning_feedback_views import (
    learning_feedback_dashboard, knowledge_point_detail,
    generate_learning_path, refresh_feedback
)

app_name = 'learning_feedback'

urlpatterns = [
    path('dashboard/', learning_feedback_dashboard, name='dashboard'),
    path('knowledge-point/<str:knowledge_point>/', knowledge_point_detail, name='knowledge_point_detail'),
    path('learning-path/', generate_learning_path, name='learning_path'),
    path('refresh/', refresh_feedback, name='refresh_feedback'),
]