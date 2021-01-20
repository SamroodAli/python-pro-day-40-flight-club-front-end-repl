import os
import requests

# Sheety API authentication and endpoint
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
endpoint = os.getenv("ENDPOINT")

# Update Google Sheets Data using Sheety API
def update_sheets(first_name,last_name,email):
    new_user = {
        "user": {
        "first":first_name,
        "last":last_name,
        "email":email
        }
    }
    response = requests.post(url=endpoint, auth=(username,password), json=new_user)
    response.raise_for_status()
    if response.status_code == 200:
        print("Thank you. You are now in the Club. Check your email for future cheap flights")