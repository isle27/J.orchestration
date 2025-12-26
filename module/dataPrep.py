from datetime import datetime, timedelta
from oprations.utils import generate_random
def prepare_body(bodydef, collection):
    body={}
    for k,v in bodydef.items():
        steps=v.split(".")  # ["collection", "user", "id"]
        if steps[0]=="collection":
            print("❤🤍❣💟☮☪🛐💥💢💤",collection.get(steps[1]))
            body[k]=collection.get(steps[1]).get(steps[2]) # engineerId: collection.user.id
        elif v.startswith("date"):
            now = datetime.now()
            steps=v.split("+")
            actualDate= now + timedelta(days=int(steps[1]))
            body[k]=int(actualDate.timestamp() * 1000)
        elif v.startswith("random"):
            steps=v.split("-")
            data=generate_random(steps[1])
            body[k]=data
    return body       

def prepare_params(paramdef,collection):
    param={}
    for k,v in paramdef.items():
        if type(v)==str and v.startswith("simple") :
            steps=v.split(".")  # ["collection", "user", "id"]
            print(steps,"💛💚🧡")
            if steps[1]=="collection":
                param[k]=collection.get(steps[2]).get(steps[3]) # engineerId: collection.user.id
            
        else:
            param[k]=v
            
        
    return param       
        

def prepare_route_extension(route_extension_def, collection):
    steps=route_extension_def.split(".")
    return f"/{collection.get(steps[0]).get(steps[1])}"