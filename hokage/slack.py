from http import HTTPStatus
import requests

def slack_notify(url, title, text, color="#B22222"):
    try:
        payload = {"attachments": [{"color": color, "title": title, "text": text}]}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != HTTPStatus.OK:
            raise Exception("Error to notify slack")
        return response
    except Exception as e:
        print(f"slack error: {e}")
