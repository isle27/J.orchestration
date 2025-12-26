import json
import random
from oprations.apiOps import call_api
from oprations.config import ROLE_PLAYS
from globals import globals
from module.dataPrep import prepare_body, prepare_params, prepare_route_extension

with open("./resource/apiDef.json", "r") as f:
    print(type(f))
    data=json.loads(f.read())

login_body={
    "email": "orcm@jegna.edr",
    "password": "password123"
}
globals.header={
    "content-type":"json",
    "Authorization":f"Bearer {call_api(route='/update-user/login',met='POST',body=login_body).get('accessToken')}"
}
globals.incidents=call_api(route="/incidents",met="GET",params={
        "page": 1,
        "limit": 100
    }).get("data")
globals.assignable_users=call_api(route="/update-user/assignable-users",met="GET",params={
    "page": 1,
    "limit": 20
})

# print(globals.assignable_users)






for role in ROLE_PLAYS:

    goals= data.get(role)
    # print("❤❤❤",ROLE_PLAYS,role)
    # print("💨💨💨",goals)
    for k, v in goals.items():
        if type(v)==list:
            local_grouped=[]
            collection={}
            for item in v:
                if item.get("type")=="api":
                    body=prepare_body(item.get("body"), collection)
                    params=prepare_params(item.get("params"), collection)
                    route_extension=prepare_route_extension(item.get("route_extension"),collection)
                    res=call_api(item.get("route")+route_extension, item.get("method"), body, params)
                else:
                    if item.get("action") == "filter":
                        print("running filter")
                        if item.get("data") == "incidents":
                            print("\t running incidents")
                            
                            for incident in globals.incidents:
                                # print(item.get("operation"))
                                ops=item.get("operation").split("==") # [status, backlog]
                                print("\t\t checking found", incident[ops[0]], ops[1])
                                
                                if incident[ops[0]]==ops[1]:
                                    print("\t\t matching found")
                                    
                                    local_grouped.append(incident)
                                    print("❤🧡💚💝💨💫💨 local",local_grouped)
                     
                    elif item.get("action") == "selectOne":
                        if item.get("data")=="local_selection":
                            collection[item.get("data")]=random.choice(local_grouped) #{incidents: {}, users: {}}
                        if item.get("data")=="users":
                            collection[item.get("data")]=random.choice(globals.assignable_users) #{incidents: {}}
                            
                        # print("❤❤❤💌💌💟💟💫💫💨🔯🔯", collection)
                            


