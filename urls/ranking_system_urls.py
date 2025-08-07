from django.urls import path
from views.ranking_system_views import ranking_list, update_rankings

app_name = 'ranking_system'

urlpatterns = [
    path('rankings/', ranking_list, name='ranking_list'),
    path('update-rankings/', update_rankings, name='update_rankings'),
]