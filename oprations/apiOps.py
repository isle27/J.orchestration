import requests
from oprations.config import BASE_URL
from globals import globals
def call_api(route, met="GET", params=None, body=None):
    res=requests.request(met, BASE_URL+route, headers=globals.header, params=params, json=body)
    print("💔💔💔 \n ", res.json(), "💘💘💘💘💘")
    return res.json()


