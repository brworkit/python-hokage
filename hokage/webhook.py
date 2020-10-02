import requests
from http import HTTPStatus

def notify(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != HTTPStatus.CREATED:
        print(f"Webhook status response: {response.status_code}")
    return response.json()