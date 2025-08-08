from django.http import JsonResponse
from django.views.decorators.http import require_POST
from own_models.notification_models import Notification
from own_models.custom_user_models import CustomUser
from own_models.code_duplication_check_models import CodeDuplicationCheck
import json

@require_POST
def send_notification(request):
    try:
        data = json.loads(request.body)
        check_id = data.get('check_id')
        check = CodeDuplicationCheck.objects.get(id=check_id)
        student = check.submission.user
        
        title = "Code Duplication Detected"
        message = f"A potential code duplication has been detected in your submission for problem '{check.submission.problem.title}'. Please review the details."
        
        Notification.objects.create(
            user=student,
            title=title,
            message=message
        )
        return JsonResponse({'status': 'success', 'message': 'Notification sent successfully.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def get_notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        return JsonResponse({'notifications': list(notifications.values())})
    return JsonResponse({'notifications': []})

@require_POST
def mark_as_read(request):
    try:
        data = json.loads(request.body)
        notification_id = data.get('notification_id')
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})