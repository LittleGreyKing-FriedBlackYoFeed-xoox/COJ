import requests
import json
from bs4 import BeautifulSoup

def add_test_problem():
    """
    Script to add a test problem to the database by simulating a POST request
    to the /addProblem/ endpoint.
    """
    # URL for the addProblem endpoint
    url = "http://127.0.0.1:8000/addProblem/"
    
    # First, get the CSRF token from the page
    session = requests.Session()
    response = session.get(url)
    
    # Parse the HTML to extract the CSRF token
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')
    
    # Prepare the problem data
    problem_data = {
        'title': 'Find the Maximum Number',
        'description': 'Write a function to find the maximum number in an array of integers.',
        'problem_type': '4',  # Programming problem
        'knowledge_point': '算法',  # Algorithms
        'input_description': 'An array of integers separated by spaces.',
        'output_description': 'The maximum integer in the array.',
        'sample_input': '5 3 9 1 7',
        'sample_output': '9',
        'hint': 'You can solve this by initializing a variable to the first element and then comparing it with each element in the array.',
        'difficulty': '2',  # Medium difficulty
        'is_active': 'on',  # Enable the problem
    }
    
    # Add the CSRF token to the data
    problem_data['csrfmiddlewaretoken'] = csrf_token
    
    # Send the POST request
    headers = {
        'Referer': url,
        'X-CSRFToken': csrf_token
    }
    
    response = session.post(url, data=problem_data, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            result = response.json()
            if result.get('success'):
                print("Problem added successfully!")
            else:
                print(f"Failed to add problem: {result.get('message')}")
        except json.JSONDecodeError:
            print("Received non-JSON response. The problem might have been added, but couldn't confirm.")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    add_test_problem()