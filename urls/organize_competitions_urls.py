from django.urls import path
from views import organize_competitions_views

app_name = 'organize_competitions'

urlpatterns = [
    path('competition_list/', organize_competitions_views.competition_list, name='competition_list'),
    path('create/', organize_competitions_views.competition_create, name='create'),
    path('competition/<int:competition_id>/papers/', organize_competitions_views.paper_list, name='paper_list'),
    path('paper/<int:paper_id>/', organize_competitions_views.paper_detail, name='paper_detail'),
    path('student_papers/', organize_competitions_views.student_paper_list, name='student_paper_list'),
    path('student_paper/<int:paper_id>/', organize_competitions_views.student_paper_detail, name='student_paper_detail'),
]