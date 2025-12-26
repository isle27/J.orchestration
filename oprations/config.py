 # Load env variables, global settings
import json
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ROLE_PLAYS = json.loads(os.getenv("ROLE_PLAYS","[]"))

print(ROLE_PLAYS)