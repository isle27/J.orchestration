import requests
from oprations.config import BASE_URL
from globals import globals
def call_api(route, met="GET", params=None, body=None):
    res=requests.request(BASE_URL+route, method=met, headers=globals.header, params=params, json=body)
    return res


