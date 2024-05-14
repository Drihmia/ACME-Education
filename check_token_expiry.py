import requests
from datetime import datetime, timedelta
import json

with open("/Users/redouane/oauth2_creds.json", "r",
          encoding="utf-8") as auth_file:
    data = json.load(auth_file)
    if not data:
        exit(1)


def check_access_token_expiry(refresh_token):
    token_endpoint = 'https://oauth2.googleapis.com/token'
    client_id = data.get('google_client_id')
    client_secret = data.get('google_client_secret')
    grant_type = 'refresh_token'

    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': grant_type
    }

    response = requests.post(token_endpoint, data=payload)
    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']
        # Expiration time in seconds
        expires_in = token_info['expires_in']
        expiry_timestamp = datetime.utcnow() + timedelta(seconds=expires_in)
        current_time = datetime.utcnow()
        if current_time >= expiry_timestamp:
            print("Access token has expired.")
        else:
            print(f"Access token is still valid.")
    else:
        print('Error checking access token expiry:', response.json())


# Usage example
refresh_token = data.get('google_refresh_token')

check_access_token_expiry(refresh_token)
