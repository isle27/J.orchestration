import requests
from oprations.config import BASE_URL
custom_header=None
def call_api(route, met, params=None, body=None):
    global custom_header
    res=requests.request(met,BASE_URL+route, headers=custom_header, params=params, json=body)
    return res

login_body={
    "email": "orcm@jegna.edr",
    "password": "password123"
}
respone=call_api(route="/update-user/login",met="POST",body=login_body)

print(respone.json()["accessToken"])