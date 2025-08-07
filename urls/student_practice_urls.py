from django.urls import path
from views.student_practice import (
    student_problem_list, student_problem_detail, student_submit_solution,
    student_submission_detail, student_statistics,code_editing
)


app_name = 'student_practice'

urlpatterns = [
    path('problems/', student_problem_list, name='problem_list'),
    path('problem/<int:problem_id>/', student_problem_detail, name='problem_detail'),
    path('problem/<int:problem_id>/submit/', student_submit_solution, name='submit_solution'),
    path('submission/<int:submission_id>/', student_submission_detail, name='submission_detail'),
    path('statistics/', student_statistics, name='statistics'),
    # Code editing page
    path('code_editing/', code_editing, name='code_editing'),
]