from django.urls import path
from views.problemViews import (
    problemList, get_problems_json, addProblem, editProblem, 
    viewProblem, deleteProblem, toggleProblemStatus
)

app_name = 'problem'

urlpatterns = [
    # 题目管理相关URL
    path("problemList/", problemList, name="problemList"),
    path("addProblem/", addProblem, name="addProblem"),
    path("editProblem/<int:problem_id>/", editProblem, name="editProblem"),
    path("viewProblem/<int:problem_id>/", viewProblem, name="viewProblem"),
    path("deleteProblem/<int:problem_id>/", deleteProblem, name="deleteProblem"),
    path("toggleProblemStatus/<int:problem_id>/", toggleProblemStatus, name="toggleProblemStatus"),
    path("api/problems/", get_problems_json, name="get_problems_json"),
]