import requests

def get_token(crendencials):
    url = "https://hotspot.wuipi.net/api/v2/access/token"

    payload='grant_type=client_credentials'
    headers = {
    'Authorization': f'Basic {crendencials}',
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response