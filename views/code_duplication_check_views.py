from django.shortcuts import render, redirect
from own_models.problem_models import Problem
from own_models.student_practice import Submission
from own_models.code_duplication_check_models import CodeDuplicationCheck
import difflib
import json

def code_duplication_check(request):
    if request.method == 'POST':
        problem_id = request.POST.get('problem_id')
        submissions = Submission.objects.filter(problem_id=problem_id)
        
        # Clear previous checks for this problem
        submission_ids = submissions.values_list('id', flat=True)
        CodeDuplicationCheck.objects.filter(submission_id__in=submission_ids).delete()

        for i in range(len(submissions)):
            for j in range(i + 1, len(submissions)):
                submission1 = submissions[i]
                submission2 = submissions[j]
                
                sm = difflib.SequenceMatcher(None, submission1.code, submission2.code)
                similarity = sm.ratio()
                
                if similarity > 0.8:
                    # Generate HTML diff
                    d = difflib.HtmlDiff()
                    diff_html = d.make_table(submission1.code.splitlines(), submission2.code.splitlines(), context=True)

                    # Create or update duplication check records
                    # Convert similarity to percentage (0-100)
                    similarity_percentage = similarity * 100
                    CodeDuplicationCheck.objects.update_or_create(
                        submission=submission1,
                        defaults={
                            'similarity_score': similarity_percentage,
                            'duplication_details': json.dumps({'similar_to': submission2.id, 'diff': diff_html})
                        }
                    )
        return redirect('code_duplication_check:code_duplication_check')

    problems = Problem.objects.all()
    checks = CodeDuplicationCheck.objects.all().order_by('-similarity_score')
    return render(request, 'code_duplication_check/code_duplication_check.html', {'problems': problems, 'checks': checks})

from django.http import HttpResponse

# duplication_details 视图用于展示查重详情
from django.shortcuts import get_object_or_404

def duplication_details(request, check_id):
    check = get_object_or_404(CodeDuplicationCheck, id=check_id)
    details = json.loads(check.duplication_details)
    similar_submission = Submission.objects.get(id=details['similar_to'])
    return render(request, 'code_duplication_check/duplication_details.html', {
        'check': check,
        'details': details,
        'similar_submission': similar_submission
    })

def download_report(request, check_id):
    check = CodeDuplicationCheck.objects.get(id=check_id)
    details = json.loads(check.duplication_details)
    similar_submission = Submission.objects.get(id=details['similar_to'])

    report_content = f"""
Code Duplication Report
=======================

Original Submission
-------------------
Submission ID: {check.submission.id}
User: {check.submission.user.username}
Time: {check.submission.created_at}

Similar Submission
------------------
Submission ID: {similar_submission.id}
User: {similar_submission.user.username}
Time: {similar_submission.created_at}

Similarity Score: {check.similarity_score:.2%}

Code Difference
---------------
{details['diff']}
"""

    response = HttpResponse(report_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="duplication_report_{check.id}.txt"'
    return response