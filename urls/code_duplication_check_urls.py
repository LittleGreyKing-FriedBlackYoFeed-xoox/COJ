from django.urls import path
from views import code_duplication_check_views

app_name = 'code_duplication_check'

urlpatterns = [
    path('', code_duplication_check_views.code_duplication_check, name='code_duplication_check'),
    path('details/<int:check_id>/', code_duplication_check_views.duplication_details, name='duplication_details'),
    path('details/<int:check_id>/download/', code_duplication_check_views.download_report, name='download_report'),
]