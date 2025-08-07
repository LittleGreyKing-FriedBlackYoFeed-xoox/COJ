#!/usr/bin/env python
import os
import sys
import django
from collections import Counter

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
django.setup()

# Import models after Django setup
from own_models.custom_user_models import CustomUser

def check_chinese_characters(text):
    """Check if text contains any Chinese characters"""
    if not text:
        return False
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def analyze_users():
    # Get all users
    users = CustomUser.objects.all()
    total_users = users.count()
    
    # Initialize counters
    chinese_found = 0
    english_only = 0
    role_counts = Counter()
    chinese_fields = Counter()
    
    print(f"Total users in system: {total_users}")
    
    # Check each user
    for user in users:
        role_counts[user.role] += 1
        
        # Check for Chinese characters in various fields
        has_chinese = False
        
        if check_chinese_characters(user.username):
            has_chinese = True
            chinese_fields['username'] += 1
        
        if check_chinese_characters(user.real_name):
            has_chinese = True
            chinese_fields['real_name'] += 1
        
        if check_chinese_characters(user.remark):
            has_chinese = True
            chinese_fields['remark'] += 1
        
        if has_chinese:
            chinese_found += 1
        else:
            english_only += 1
    
    # Print results
    print("\n=== Translation Results ===")
    print(f"Users with English-only information: {english_only} ({english_only/total_users*100:.1f}%)")
    print(f"Users with Chinese characters remaining: {chinese_found} ({chinese_found/total_users*100:.1f}%)")
    
    print("\n=== Role Distribution ===")
    print(f"Students (role 1): {role_counts[1]} ({role_counts[1]/total_users*100:.1f}%)")
    print(f"Teachers (role 2): {role_counts[2]} ({role_counts[2]/total_users*100:.1f}%)")
    print(f"Admins (role 3): {role_counts[3]} ({role_counts[3]/total_users*100:.1f}%)")
    
    if chinese_found > 0:
        print("\n=== Fields with Chinese Characters ===")
        for field, count in chinese_fields.items():
            print(f"{field}: {count} users")
    
    return english_only, chinese_found, role_counts

if __name__ == "__main__":
    print("Analyzing user translation results...")
    english_only, chinese_found, role_counts = analyze_users()
    
    if chinese_found > 0:
        print("\nWarning: Some users still have Chinese characters in their information.")
        print("You may want to run the translation script again.")
    else:
        print("\nSuccess! All users now have English-only information.")