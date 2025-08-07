# _*_ coding:utf-8 _*_
from django.shortcuts import render, redirect
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from own_models.ranking_system_models import RankingSystem
from own_models.custom_user_models import CustomUser

def ranking_list(request):
    """
    Display the ranking list of all users based on problems completed and attempts
    """
    # Update all rankings before displaying
    RankingSystem.update_all_rankings()
    
    # Get all rankings ordered by rank position
    all_rankings = RankingSystem.objects.select_related('user').order_by('rank_position')
    
    # Pagination
    per_page = request.GET.get('per_page', 10)  # Default 10 items per page
    paginator = Paginator(all_rankings, per_page)
    page = request.GET.get('page', 1)
    
    try:
        rankings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        rankings = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        rankings = paginator.page(paginator.num_pages)
    
    # Find the current user's ranking if user is logged in
    user_rank = None
    if hasattr(request, 'user') and request.user:
        try:
            user_ranking = RankingSystem.objects.get(user=request.user)
            user_rank = user_ranking.rank_position
        except RankingSystem.DoesNotExist:
            user_rank = None
    
    context = {
        'rankings': rankings,
        'user_rank': user_rank,
    }
    
    return render(request, 'ranking_system/ranking_list.html', context)

def update_rankings(request):
    """
    Manually trigger an update of all user rankings
    """
    # Create rankings for users who don't have one yet
    users_without_ranking = CustomUser.objects.filter(ranking__isnull=True)
    for user in users_without_ranking:
        RankingSystem.objects.create(user=user)
    
    # Update metrics for all users
    for ranking in RankingSystem.objects.all():
        ranking.update_metrics()
    
    # Update the ranking positions
    RankingSystem.update_all_rankings()
    
    # Redirect to the ranking list
    return redirect('ranking_system:ranking_list')
