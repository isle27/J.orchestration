from datetime import datetime, timedelta
from oprations.utils import generate_random
def prepare_body(bodydef, collection):
    body={}
    for k,v in bodydef.items():
        steps=v.split(".")  # ["collection", "user", "id"]
        if steps[0]=="collection":
            body[k]=collection.get(steps[1]).get(steps[2]) # engineerId: collection.user.id
        elif v.startswith("date"):
            now = datetime.now()
            steps=v.split("+")
            actualDate= now + timedelta(days=steps[1])
            body[k]=int(actualDate.timestamp() * 1000)
        elif v.startswith("random"):
            steps=v.split("-")
            data=generate_random(steps[1])
            body[k]=data
    return body       

def prepare_params():
    pass

def prepare_route_extension(route_extension_def, collection):
    steps=route_extension_def.split(".")
    return f"/{collection.get(steps[0]).get(steps[1])}"