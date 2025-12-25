from oprations.utils import login
import requests
from oprations.config import BASE_URL
import random
import time



def get_dashboard_part1(token):
    endpoints = {
        "incidents": f"{BASE_URL}/dashboards/executive/incidents",
        "assignee": f"{BASE_URL}/update-user/assignable-users",
        "status": f"{BASE_URL}/dashboards/executive/status",
        "incident": f"{BASE_URL}/dashboards/executive/incident",
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    results = {}

    for name, url in endpoints.items():
        try:
            
            if name == "incidents":
                params = {
                            "view": "events",
                            "type": "All",
                            "startDate": "2025-12-08",
                            "endDate": "2025-12-22"
                        }
                response = requests.get(url, headers=headers, params=params)            
            else:
                 response = requests.get(url, headers=headers)
           
            response.raise_for_status()
            results[name] = response.json()
            print(f"{name} fetched successfully")
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {name}: {response.status_code} - {response.text}")
            results[name] = None

    return results



def get_incidents(token):
    url = f"{BASE_URL}/incidents"
    params = {
        "page": 1,
        "limit": 20
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        incidents = response.json()

        incident_list = incidents['data']
        print(f"Fetched {len(incidents['data'])} incidents")
        
        filtered = []
        filtered2 = []
        for backlog in incident_list:
            if backlog.get("ticket_status") == "Backlog":
                filtered.append(backlog)
        for InProgress in incident_list:
            if InProgress.get("ticket_status") == "InProgress":
                filtered2.append(InProgress)

        return random.choice(filtered) if filtered else None,random.choice(filtered2) if filtered2 else None

    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e.response.status_code, e.response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
   
    return None



def assign_incident(token, incident_id, engineer_id, remark="Assigned via script", deadline_ms=None):
    
    if deadline_ms is None:
        deadline_ms = int((time.time() + 24*60*60) * 1000)

    url = f"{BASE_URL}/incidents/{incident_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "engineerId": engineer_id,
        "deadline": deadline_ms,
        "remark": remark
    }

    try:

        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"Incident {incident_id} assigned successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None
    



def reassign_incident(token, incident_id, engineer_id, remark="Reassigned via script", deadline_ms=None):
    if deadline_ms is None:
        deadline_ms = int((time.time() + 24*60*60) * 1000)

    url = f"{BASE_URL}/reAssign/{incident_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "engineerId": engineer_id,
        "deadline": deadline_ms,
        "remark": remark
    }
    try:

        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"Incident {incident_id} reassigned successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

def  view_resolution_summary(token):
    url = f"{BASE_URL}/resolution-summary"
    params = {
        "page": 1,
        "limit": 20
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.get(url,headers=headers,params=params)
        response.raise_for_status()
        print("resolution summarys get successful")
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

