from django.urls import path
from views import notification_views as views

app_name = 'notification'

urlpatterns = [
    path('send_notification/', views.send_notification, name='send_notification'),
    path('get_notifications/', views.get_notifications, name='get_notifications'),
    path('mark_as_read/', views.mark_as_read, name='mark_as_read'),
]