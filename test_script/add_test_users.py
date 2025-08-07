#!/usr/bin/env python
import os
import sys
import random
import string
import django
import datetime

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.custom_user_models import CustomUser
from django.utils import timezone

# Define roles with their numeric values and weights
# We'll make students more common, then teachers, then admins
ROLES = [
    (1, "student", 70),  # 70% chance for students
    (2, "teacher", 25),  # 25% chance for teachers
    (3, "admin", 5)      # 5% chance for admins
]

# First names and last names for generating realistic user data
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

# Generate random user data
def generate_random_user(index):
    # Select random role based on weights
    role_weights = [weight for _, _, weight in ROLES]
    role_ids = [role_id for role_id, _, _ in ROLES]
    role_id = random.choices(role_ids, weights=role_weights, k=1)[0]
    role_name = next(name for id, name, _ in ROLES if id == role_id)
    
    # Generate basic user info
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    username = f"{first_name.lower()}{last_name.lower()}{random.randint(1, 999)}"
    email = f"{username}@example.com"
    password = "password123"  # Simple password for test users
    
    # Generate role-specific data
    usercode = ""
    remark = ""
    
    if role_id == 1:  # Student
        usercode = f"S{100000 + index}"
        colleges = ["Information College", "Medical College", "Literature College", 
                   "Science College", "Engineering College", "Business College", 
                   "Law College", "Art College"]
        remark = random.choice(colleges)
    elif role_id == 2:  # Teacher
        usercode = f"T{200000 + index}"
        titles = ["Teaching Assistant", "Lecturer", "Associate Professor", "Professor"]
        remark = random.choice(titles)
    elif role_id == 3:  # Admin
        usercode = f"A{300000 + index}"
        remark = "System Administrator"
    
    # Generate a random date within the last year for date_joined
    days_ago = random.randint(1, 365)
    date_joined = timezone.now() - datetime.timedelta(days=days_ago)
    
    return {
        'username': username,
        'email': email,
        'password': password,
        'role': role_id,
        'usercode': usercode,
        'remark': remark,
        'is_active': random.random() > 0.05,  # 95% of users are active
        'date_joined': date_joined,
        'real_name': f"{first_name} {last_name}",
        'gender': random.choice(['M', 'F'])
    }

# Create 100 users
def create_test_users():
    created_users = []
    
    for i in range(1, 101):
        user_data = generate_random_user(i)
        
        try:
            # Check if user already exists
            if CustomUser.objects.filter(username=user_data['username']).exists():
                print(f"User {user_data['username']} already exists, skipping...")
                continue
                
            user = CustomUser(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                role=user_data['role'],
                usercode=user_data['usercode'],
                remark=user_data['remark'],
                is_active=user_data['is_active'],
                date_joined=user_data['date_joined'],
                real_name=user_data['real_name'],
                gender=user_data['gender']
            )
            user.save()
            
            created_users.append(user)
            print(f"Created user: {user.username} with role: {ROLES[user.role-1][1]}")
        except Exception as e:
            print(f"Error creating user {user_data['username']}: {str(e)}")
    
    return created_users

if __name__ == "__main__":
    print("Creating 100 test users...")
    users = create_test_users()
    print(f"Successfully created {len(users)} test users")
