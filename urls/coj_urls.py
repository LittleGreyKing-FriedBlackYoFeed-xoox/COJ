from django.urls import path
from views.cojView import requestIndex, learningData, get_learning_data

app_name = 'coj'

urlpatterns = [
    path("requestIndex/", requestIndex, name="requestIndex"),
    path("learningData/", learningData, name="learningData"),
    path("api/learning-data/", get_learning_data, name="learning_data_api"),
]