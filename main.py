from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import base64

app = FastAPI()

origins = [
    "*"
    ]
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:3000",
#     "https://wuipi.net/",
#     ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    ga_ap_mac: str
    ga_cmac: str
    ga_Qv:   str
    ga_user: str | None = None
    ga_pass: str | None = None

credentials = 'GzYbNKfU1nSoqoBa:L2aCXjjDzdpfT6p4NHpbl1Or7iXbI3'
b64 = base64.b64encode(credentials.encode('ascii'))
result = b64.decode('ascii')

def get_token():
    url = 'https://hotspot.wuipi.net/api/v2/access/token'
    payload='grant_type=client_credentials'
    headers = {
        'Authorization': 'Basic R3pZYk5LZlUxblNvcW9CYTpMMmFDWGpqRHpkcGZUNnA0TkhwYmwxT3I3aVhiSTM=',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    response = requests.request("POST", url, headers=headers, data=payload)

    resp = response.text
    resp_json = json.loads(resp)
    return resp_json['access_token']

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/user-login")
async def user_login(user: User):
    url = 'https://hotspot.wuipi.net/api/v2/ext-portals/login'
    headers = {
    'Authorization': f'Bearer {get_token()}',   
    'Content-Type': 'application/json'
    }

    payload = json.dumps(user.__dict__)

    response = requests.request("POST", url, headers=headers, data=payload)
    resp = response.text
    resp_json = json.loads(resp)
    return resp_json

@app.post("/user-logout")
async def user_login(user: User):
    url = 'https://hotspot.wuipi.net/api/v2/ext-portals/logout'
    headers = {
    'Authorization': f'Bearer {get_token()}',   
    'Content-Type': 'application/json'
    }

    payload = json.dumps(user.__dict__)

    response = requests.request("POST", url, headers=headers, data=payload)
    resp = response.text
    resp_json = json.loads(resp)
    return resp_json