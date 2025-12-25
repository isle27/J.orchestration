import json
import random
from oprations.apiOps import call_api
from oprations.config import ROLE_PLAYS
from globals import globals
from module.dataPrep import prepare_body, prepare_params, prepare_route_extension

with open("./resource/apiDef.json", "r") as f:
    data=json.load(f.read())

login_body={
    "email": "orcm@jegna.edr",
    "password": "password123"
}
globals.header={
    "content-type":"json",
    "Authprization":f"Bearer {call_api(route="/update-user/login",met="POST",body=login_body).json()["accessToken"]}"
}
globals.incidents=call_api(route="/incidents",met="GET",params={
    "page": 1,
    "limit": 20})["data"]
globals.assignable_users=call_api(route="/update-user",met="GET",params={
    "page": 1,
    "limit": 20})["data"]

print(globals.incidents)

quit()




for role in ROLE_PLAYS:
    goals= data[role]
    for k, v in goals:
        if type(v)==list:
            local_grouped=[]
            collection={}
            for item in v:
                if v.type=="api":
                    body=prepare_body(v.body, collection)
                    params=prepare_params(v.params, collection)
                    route_extension=prepare_route_extension(v.route_extension,collection)
                    res=call_api(v.get("route")+route_extension, v.get("method"), body, params)
                else:
                    if v.action == "filter":
                        if v.data == "incidents":
                            for incident in globals.incidents:
                                ops=v.operations.split("==") # [status, backlog]
                                if incident[ops[0]]==ops[1]:
                                    local_grouped.append(incident)
                        elif v.data=="users":
                            for incident in globals.assignable_users:
                                ops=v.operations.split("==") # [status, backlog]
                                if incident[ops[0]]==ops[1]:
                                    local_grouped.append(incident)
                    elif v.action == "selectOne":
                        if v.data=="local_selection":
                            collection[v.data]=random.choice(local_grouped) #{incidents: {}, users: {}}
                        if v.data=="users":
                            collection[v.data]=random.choice(globals.assignable_users) #{incidents: {}}
                            


