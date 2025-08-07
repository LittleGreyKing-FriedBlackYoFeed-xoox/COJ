#!/usr/bin/env python
import os
import sys
import django
import random
import time

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.custom_user_models import CustomUser
from django.utils import timezone
from django.db import connection, transaction
from django.db.utils import OperationalError, InterfaceError

# Translation mappings for common Chinese terms
COLLEGE_TRANSLATIONS = {
    "信息学院": "Information College",
    "医学院": "Medical College",
    "文学院": "Literature College",
    "理学院": "Science College",
    "工学院": "Engineering College",
    "商学院": "Business College",
    "法学院": "Law College",
    "艺术学院": "Art College"
}

TITLE_TRANSLATIONS = {
    "未定级": "Unclassified",
    "助教": "Teaching Assistant",
    "讲师": "Lecturer",
    "副教授": "Associate Professor",
    "教授": "Professor"
}

ROLE_TRANSLATIONS = {
    "学生": "Student",
    "教师": "Teacher",
    "管理员": "Admin",
    "系统管理员": "System Administrator"
}

# English names for random assignment
FIRST_NAMES = [
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles",
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth",
    "Emily", "Emma", "Madison", "Olivia", "Hannah", "Abigail", "Isabella", "Samantha", "Elizabeth", "Ashley"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
    "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
    "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter"
]

# Colleges for students
COLLEGES = [
    "Information College", "Medical College", "Literature College", "Science College",
    "Engineering College", "Business College", "Law College", "Art College"
]

# Titles for teachers
TITLES = [
    "Unclassified", "Teaching Assistant", "Lecturer", "Associate Professor", "Professor"
]

# Function to check if text contains Chinese characters
def contains_chinese(text):
    if not text:
        return False
    return any('\u4e00' <= char <= '\u9fff' for char in text)

# Function to reset database connection
def reset_db_connection():
    try:
        connection.close()
        connection.connect()
        return True
    except Exception as e:
        print(f"Error resetting database connection: {str(e)}")
        return False

# Function to update a single user
def update_user(user):
    updated = False
    
    try:
        # 1. Ensure username is English
        if contains_chinese(user.username) or not user.username:
            first_name = random.choice(FIRST_NAMES).lower()
            last_name = random.choice(LAST_NAMES).lower()
            new_username = f"{first_name}{last_name}{random.randint(1, 999)}"
            
            # Make sure username is unique
            while CustomUser.objects.filter(username=new_username).exists():
                new_username = f"{first_name}{last_name}{random.randint(1, 999)}"
                
            user.username = new_username
            updated = True
            print(f"Updated username for user {user.id}: {new_username}")
        
        # 2. Ensure real_name is English
        if contains_chinese(user.real_name) or not user.real_name:
            first_name = random.choice(FIRST_NAMES)
            last_name = random.choice(LAST_NAMES)
            user.real_name = f"{first_name} {last_name}"
            updated = True
            print(f"Updated real_name for user {user.username}: {user.real_name}")
        
        # 3. Ensure remark is English based on role
        if user.role == 1:  # Student
            if contains_chinese(user.remark) or not user.remark or user.remark not in COLLEGES:
                user.remark = random.choice(COLLEGES)
                updated = True
                print(f"Updated student college for {user.username}: {user.remark}")
        elif user.role == 2:  # Teacher
            if contains_chinese(user.remark) or not user.remark or user.remark not in TITLES:
                user.remark = random.choice(TITLES)
                updated = True
                print(f"Updated teacher title for {user.username}: {user.remark}")
        elif user.role == 3:  # Admin
            if contains_chinese(user.remark) or not user.remark or user.remark != "System Administrator":
                user.remark = "System Administrator"
                updated = True
                print(f"Updated admin remark for {user.username}: {user.remark}")
        
        # 4. Ensure email is set
        if not user.email:
            user.email = f"{user.username}@example.com"
            updated = True
            print(f"Updated email for {user.username}: {user.email}")
        
        # 5. Ensure is_active is a boolean
        if not isinstance(user.is_active, bool):
            user.is_active = True  # Default to active
            updated = True
            print(f"Fixed is_active field for {user.username}")
        
        # Save changes if any updates were made
        if updated:
            user.save()
            return True
    except Exception as e:
        print(f"Error updating user {user.id}: {str(e)}")
        # Try to fix specific issues
        try:
            if "value must be either True or False" in str(e):
                print(f"Attempting to fix boolean field issue for user {user.id}")
                user.is_active = True  # Set to default value
                user.save(update_fields=['is_active'])
                print(f"Fixed is_active field for user {user.id}")
                return True
        except Exception as fix_error:
            print(f"Failed to fix user {user.id}: {str(fix_error)}")
    
    return False

# Function to ensure all user information is in English
def ensure_english_information():
    # Get total user count
    try:
        total_users = CustomUser.objects.count()
        print(f"Found {total_users} users in the system.")
    except (OperationalError, InterfaceError) as e:
        print(f"Database connection error: {str(e)}")
        print("Attempting to reset connection...")
        if reset_db_connection():
            try:
                total_users = CustomUser.objects.count()
                print(f"Connection reset. Found {total_users} users in the system.")
            except Exception as e:
                print(f"Failed to reconnect to database: {str(e)}")
                return 0
        else:
            print("Failed to reset database connection.")
            return 0
    
    print("Starting to ensure all user information is in English...")
    updated_count = 0
    batch_size = 10  # Process users in smaller batches
    
    # Process users in batches to avoid timeouts
    for offset in range(0, total_users, batch_size):
        try:
            # Get a batch of users
            users_batch = CustomUser.objects.all()[offset:offset+batch_size]
            print(f"Processing batch {offset//batch_size + 1} (users {offset+1} to {min(offset+batch_size, total_users)})")
            
            # Process each user in the batch
            for user in users_batch:
                if update_user(user):
                    updated_count += 1
            
            # Close and reopen connection between batches to avoid timeouts
            connection.close()
            connection.connect()
            
            # Small delay between batches
            time.sleep(0.5)
            
        except (OperationalError, InterfaceError) as e:
            print(f"Database error during batch processing: {str(e)}")
            print("Attempting to reset connection...")
            if reset_db_connection():
                print("Connection reset successfully. Continuing with next batch.")
            else:
                print("Failed to reset connection. Skipping to next batch.")
    
    print(f"Update complete. Modified {updated_count} out of {total_users} users.")
    return updated_count

if __name__ == "__main__":
    print("Starting comprehensive user information translation process...")
    try:
        updated = ensure_english_information()
        print(f"Successfully updated {updated} users to English information.")
    except Exception as e:
        print(f"An error occurred during the translation process: {str(e)}")
