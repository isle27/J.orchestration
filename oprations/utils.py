# Helper functions (random choice, delays, logging)
import requests
from config import BASE_URL


def login(email,password):
    url = f"{BASE_URL}/update-user/login"
    payload = {
    "email": email,
    "password": password
    }
    response = requests.post(url, json=payload)
    if response.ok:
        print("Login successful")
        return response.json()  # usually contains token
    else:
        print("Login failed:", response.status_code, response.text)
        return None
    

