import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_t.settings')
django.setup()

from own_models.update_learning_feedback import update_learning_feedback_for_user

def main():
    """
    Script to update learning feedback data for all students or a specific student
    
    Usage:
        python update_learning_feedback.py [user_id]
        
    Arguments:
        user_id (optional): ID of the specific user to update
    """
    import sys
    
    user_id = None
    if len(sys.argv) > 1:
        try:
            user_id = int(sys.argv[1])
            print(f"Updating learning feedback for user ID: {user_id}")
        except ValueError:
            print("Error: user_id must be an integer")
            return
    else:
        print("Updating learning feedback for all students")
    
    updated_count, error_count = update_learning_feedback_for_user(user_id)
    
    print(f"Update completed. Updated: {updated_count}, Errors: {error_count}")

if __name__ == "__main__":
    main()