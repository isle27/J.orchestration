# Helper functions (random choice, delays, logging)
import requests
import random
from oprations.config import BASE_URL


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
    

def get_random_int(z,y):
    pass

def generate_random(x):
    words = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon"
    ]
    data=""
    if x=="sentence":
        for i in range(random.randint(5, 16)):
            data= data+random.choice(words)+ " "
    
    return data
