# This is a sample file that mimics production code.
import requests
import json

# Sample API URL (assuming a fictional service)
API_URL = "https://api.example.com/data"

# Example of a hardcoded token - this is a VALID token
TOKEN = "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzI3NzI0MTk5LCJqdGkiOiJiYmMxZTM5MC02NWY4LTRhNTUtODI5MS1mZmM5NDI3MTMwYzgiLCJ1c2VyX3V1aWQiOiJhODk3ZDFjMC00ZjA5LTQ5NTAtOWQyNS1lNGQ1YTBiZjdiODYifQ.s8ormtTmtuPtypOkIK-YDlo-3OcVLEnHepN1lHd7tBdf8F9zoctC_O_1TIcqXFtKg6TlhCUn1h82iHd00Blc0g"

def fetch_data():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()

        # Process the response JSON
        data = response.json()
        print("Data fetched successfully:", json.dumps(data, indent=4))
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    print("🚀 Starting the data fetch process...")
    fetch_data()