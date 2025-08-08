from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from own_models.organize_competitions_models import Competition, Paper, PaperAssignment
from own_models.problem_models import Problem
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

@login_required
def competition_list(request):
    competitions = Competition.objects.filter(creator=request.user)
    return render(request, 'organize_competitions/competition_list.html', {'competitions': competitions})

@login_required
def competition_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        problem_ids = request.POST.getlist('problems')
        user_ids = request.POST.getlist('users')
        competition = Competition.objects.create(name=name, creator=request.user, description=description)
        paper = Paper.objects.create(competition=competition, name=name)
        paper.problems.set(Problem.objects.filter(id__in=problem_ids))
        paper.save()
        for uid in user_ids:
            user = User.objects.get(id=uid)
            PaperAssignment.objects.create(paper=paper, user=user)
        return redirect('organize_competitions:competition_list')
    problems = Problem.objects.all()
    users = User.objects.all()
    return render(request, 'organize_competitions/competition_create.html', {'problems': problems, 'users': users})

@login_required
def paper_detail(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    problems = paper.problems.all()
    user_papers = PaperAssignment.objects.filter(paper=paper)
    return render(request, 'organize_competitions/paper_detail.html', {'paper': paper, 'problems': problems, 'user_papers': user_papers})

@login_required
def student_paper_list(request):
    assignments = PaperAssignment.objects.filter(user=request.user, is_completed=False)
    return render(request, 'organize_competitions/student_paper_list.html', {'assignments': assignments})

@login_required
def student_paper_detail(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)
    assignment = get_object_or_404(PaperAssignment, paper=paper, user=request.user)
    if request.method == 'POST':
        # 这里只做简单标记完成，实际可扩展为保存答案等
        assignment.is_completed = True
        assignment.completed_at = timezone.now()
        assignment.save()
        return redirect('organize_competitions:student_paper_list')
    return render(request, 'organize_competitions/student_paper_detail.html', {'paper': paper})

@login_required
def paper_list(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id, creator=request.user)
    papers = Paper.objects.filter(competition=competition)
    return render(request, 'organize_competitions/paper_list.html', {'competition': competition, 'papers': papers})