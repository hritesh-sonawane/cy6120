import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def validate_calendly_token(api_token):
    url = "https://api.calendly.com/users/me"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Token is valid.")
        user_info = response.json()
        print("User Information:")
        print(f"Name: {user_info['resource']['name']}")
        print(f"Email: {user_info['resource']['email']}")
        print(f"Scheduling URL: {user_info['resource']['scheduling_url']}")
        print(f"Timezone: {user_info['resource']['timezone']}")
    else:
        print("Token is invalid.")
        print("Response Code:", response.status_code)
        print("Response Body:", response.json())

# API token from the environment variable
api_token = os.getenv('CALENDLY_API_TOKEN')

if api_token:
    validate_calendly_token(api_token)
else:
    print("API token not found in the .env file.")