# _*_ coding:utf-8 _*_
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count, Q, Avg
from django.utils import timezone
from django.core.cache import cache
import json
import datetime

from own_models.custom_user_models import CustomUser
from own_models.problem_models import Problem
from own_models.student_practice import Submission, StudentStatistics
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance
from own_models.update_learning_feedback import update_learning_feedback_for_user

def learning_feedback_dashboard(request):
    """
    Display the learning feedback dashboard for a student
    """
    # Check if user is logged in and is a student or admin
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    # Get current user
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # Try to get cached feedback data
    cache_key = f'learning_feedback_{user.id}'
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return render(request, 'learning_feedback/dashboard.html', cached_data)
    
    # Get or create learning feedback
    feedback, created = LearningFeedback.objects.get_or_create(user=user)
    
    # Update feedback if it's new or hasn't been updated recently
    if created or not feedback.last_updated or (timezone.now() - feedback.last_updated).days > 0:
        update_learning_feedback_for_user(user.id)
    
    # Get knowledge point performances
    knowledge_performances = KnowledgePointPerformance.objects.filter(user=user).order_by('-problems_solved')
    
    # Get student statistics
    stats, _ = StudentStatistics.objects.get_or_create(user=user)
    if not stats.last_updated or (timezone.now() - stats.last_updated).days > 0:
        stats.update_statistics()
    
    # Get recent submissions
    recent_submissions = Submission.objects.filter(user=user).select_related('problem').order_by('-created_at')[:10]
    
    # Calculate performance trends
    performance_trends = calculate_performance_trends(user)
    
    # Prepare data for charts
    knowledge_point_data = {
        'labels': [kp.knowledge_point for kp in knowledge_performances[:5]],
        'attempted': [kp.problems_attempted for kp in knowledge_performances[:5]],
        'solved': [kp.problems_solved for kp in knowledge_performances[:5]]
    }
    
    # Prepare context
    context = {
        'feedback': feedback,
        'knowledge_performances': knowledge_performances,
        'stats': stats,
        'recent_submissions': recent_submissions,
        'performance_trends': {
            'weeks': json.dumps(performance_trends['weeks']),
            'success_rates': json.dumps(performance_trends['success_rates']),
            'avg_times': json.dumps(performance_trends['avg_times'])
        },
        'knowledge_point_data': json.dumps(knowledge_point_data)
    }
    
    # Cache the data for 30 minutes
    cache.set(cache_key, context, 60 * 30)
    
    return render(request, 'learning_feedback/dashboard.html', context)

def calculate_performance_trends(user):
    """
    Calculate performance trends over time for the user
    """
    # Get submissions from the last 30 days
    end_date = timezone.now().date()
    start_date = end_date - datetime.timedelta(days=29)
    
    submissions = Submission.objects.filter(
        user=user,
        created_at__date__gte=start_date,
        created_at__date__lte=end_date
    )
    
    # Group by week and calculate metrics
    weekly_data = {}
    for submission in submissions:
        # Get the week number
        week_number = submission.created_at.isocalendar()[1]
        year = submission.created_at.year
        week_key = f"{year}-W{week_number}"
        
        if week_key not in weekly_data:
            weekly_data[week_key] = {
                'total': 0,
                'accepted': 0,
                'avg_time': 0,
                'time_sum': 0
            }
        
        weekly_data[week_key]['total'] += 1
        if submission.status == 'accepted':
            weekly_data[week_key]['accepted'] += 1
            weekly_data[week_key]['time_sum'] += submission.execution_time
    
    # Calculate averages
    for week, data in weekly_data.items():
        if data['accepted'] > 0:
            data['avg_time'] = data['time_sum'] / data['accepted']
        if data['total'] > 0:
            data['success_rate'] = (data['accepted'] / data['total']) * 100
        else:
            data['success_rate'] = 0
    
    # Sort by week
    sorted_weeks = sorted(weekly_data.items())
    
    # Prepare trend data
    trends = {
        'weeks': [week for week, _ in sorted_weeks],
        'success_rates': [data['success_rate'] for _, data in sorted_weeks],
        'avg_times': [data['avg_time'] for _, data in sorted_weeks]
    }
    
    return trends

def knowledge_point_detail(request, knowledge_point):
    """
    Display detailed performance for a specific knowledge point
    """
    # Check if user is logged in and is a student or admin
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    # Get current user
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # Get performance for this knowledge point
    performance = get_object_or_404(KnowledgePointPerformance, user=user, knowledge_point=knowledge_point)
    
    # Get problems with this knowledge point
    problems = Problem.objects.filter(knowledge_point=knowledge_point)
    
    # Get user's submissions for these problems
    problem_ids = problems.values_list('id', flat=True)
    submissions = Submission.objects.filter(user=user, problem_id__in=problem_ids)
    
    # Group submissions by problem
    problem_submissions = {}
    for problem in problems:
        problem_subs = submissions.filter(problem=problem).order_by('-created_at')
        problem_submissions[problem.id] = {
            'problem': problem,
            'submissions': problem_subs,
            'attempts': problem_subs.count(),
            'solved': problem_subs.filter(status='accepted').exists()
        }
    
    # Get recommended problems for this knowledge point that user hasn't attempted
    recommended_problems = Problem.objects.filter(
        knowledge_point=knowledge_point
    ).exclude(
        id__in=submissions.values_list('problem_id', flat=True)
    ).order_by('difficulty')[:5]
    
    context = {
        'performance': performance,
        'knowledge_point': knowledge_point,
        'problem_submissions': problem_submissions,
        'recommended_problems': recommended_problems
    }
    
    return render(request, 'learning_feedback/knowledge_point_detail.html', context)

def generate_learning_path(request):
    """
    Generate a personalized learning path based on user's performance
    """
    # Check if user is logged in and is a student or admin
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return redirect('index')
    
    # Get current user
    user_id = request.session.get('user_id')
    user = CustomUser.objects.get(id=user_id)
    
    # Get user's feedback
    feedback, created = LearningFeedback.objects.get_or_create(user=user)
    if created or not feedback.last_updated or (timezone.now() - feedback.last_updated).days > 0:
        feedback.update_feedback()
    
    # Get knowledge performances
    performances = KnowledgePointPerformance.objects.filter(user=user).order_by('problems_solved')
    
    # Identify weak knowledge points (low solve rate)
    weak_points = [p.knowledge_point for p in performances if p.problems_solved / max(p.problems_attempted, 1) < 0.5]
    
    # Get problems for weak knowledge points, starting with easier ones
    weak_point_problems = Problem.objects.filter(
        knowledge_point__in=weak_points,
        difficulty__lte=2  # Easy to medium difficulty
    ).exclude(
        submissions__user=user,
        submissions__status='accepted'
    ).order_by('difficulty')[:10]
    
    # Get some problems from knowledge points user hasn't tried yet
    unexplored_problems = Problem.objects.exclude(
        knowledge_point__in=performances.values_list('knowledge_point', flat=True)
    ).order_by('difficulty')[:5]
    
    # Get some challenging problems from strong knowledge points for growth
    strong_points = [p.knowledge_point for p in performances if p.problems_solved / max(p.problems_attempted, 1) > 0.8]
    challenge_problems = Problem.objects.filter(
        knowledge_point__in=strong_points,
        difficulty=3  # Hard difficulty
    ).exclude(
        submissions__user=user
    ).order_by('?')[:3]  # Random selection
    
    context = {
        'feedback': feedback,
        'weak_point_problems': weak_point_problems,
        'unexplored_problems': unexplored_problems,
        'challenge_problems': challenge_problems
    }
    
    return render(request, 'learning_feedback/learning_path.html', context)

def refresh_feedback(request):
    """
    Manually refresh the learning feedback
    """
    # Check if user is logged in and is a student or admin
    if 'user_id' not in request.session or request.session.get('user_role') not in [1, 3]:
        return JsonResponse({'success': False, 'message': 'Authentication required'})
    
    # Get current user
    user_id = request.session.get('user_id')
    
    try:
        # Update feedback using the centralized function
        updated_count, error_count = update_learning_feedback_for_user(user_id)
        
        if updated_count > 0:
            # Get the updated feedback
            user = CustomUser.objects.get(id=user_id)
            feedback = LearningFeedback.objects.get(user=user)
            
            # Clear cache
            cache_key = f'learning_feedback_{user_id}'
            cache.delete(cache_key)
            
            return JsonResponse({
                'success': True, 
                'message': 'Feedback refreshed successfully',
                'last_updated': feedback.last_updated.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return JsonResponse({'success': False, 'message': f'Error refreshing feedback: No updates performed'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error refreshing feedback: {str(e)}'})
