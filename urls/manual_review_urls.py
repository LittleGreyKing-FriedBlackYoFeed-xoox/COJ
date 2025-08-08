from django.urls import path
from views import manual_review_views

app_name = 'manual_review'

urlpatterns = [
    path('request/', manual_review_views.request_manual_review, name='request_manual_review'),
    path('list/', manual_review_views.teacher_review_list, name='teacher_review_list'),
    path('review/<int:review_id>/', manual_review_views.review_detail, name='review_detail'),
    path('result/<int:review_id>/', manual_review_views.student_review_result, name='student_review_result'),
]