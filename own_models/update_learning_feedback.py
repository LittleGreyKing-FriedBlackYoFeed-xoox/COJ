from django.utils import timezone
from django.db.models import Avg, Count, Q
from own_models.custom_user_models import CustomUser
from own_models.learning_feedback_models import LearningFeedback, KnowledgePointPerformance
from own_models.student_practice import Submission
import logging

logger = logging.getLogger(__name__)

def update_learning_feedback_for_user(user_id=None):
    """
    Update learning feedback data for a specific user or all students
    
    Args:
        user_id (int, optional): ID of the specific user to update. If None, updates all students.
    
    Returns:
        tuple: (updated_count, error_count) - Number of users updated and number of errors encountered
    """
    start_time = timezone.now()
    logger.info(f"Starting learning feedback update at {start_time}")
    
    try:
        # Get all student users (role=1)
        if user_id:
            users = CustomUser.objects.filter(id=user_id, role=1)
            logger.info(f"Updating learning feedback for user ID: {user_id}")
        else:
            users = CustomUser.objects.filter(role=1)
            logger.info(f"Updating learning feedback for all {users.count()} students")
        
        updated_count = 0
        error_count = 0
        
        # Update feedback for each user
        for user in users:
            try:
                # Get or create learning feedback
                feedback, created = LearningFeedback.objects.get_or_create(user=user)
                
                # Update feedback
                feedback.update_feedback()
                
                # Update knowledge point performances
                KnowledgePointPerformance.update_all_performances(user)
                
                updated_count += 1
                if updated_count % 10 == 0:
                    logger.info(f"Updated {updated_count} users so far...")
                    
            except Exception as e:
                error_count += 1
                logger.error(f"Error updating learning feedback for user {user.id}: {str(e)}")
        
        end_time = timezone.now()
        duration = end_time - start_time
        
        logger.info(
            f"Learning feedback update completed at {end_time}. "
            f"Duration: {duration.total_seconds():.2f} seconds. "
            f"Updated: {updated_count}, Errors: {error_count}"
        )
        
        return updated_count, error_count
        
    except Exception as e:
        logger.error(f"Error in update_learning_feedback function: {str(e)}")
        return 0, 1