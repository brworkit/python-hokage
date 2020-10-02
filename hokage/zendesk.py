#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
from http import HTTPStatus

class Zendesk(object):
    def __init__(self, user, password):
        self.auth = HTTPBasicAuth(user, password)

    def create_ticket(self, url, subject, description, custom_fields, ticket_form_id=360000793711):
        headers = {'Content-Type': 'application/json'}
        payload = {
            "ticket": {
                "ticket_form_id": ticket_form_id,
                "type": "task",
                "subject": subject,
                "comment": {
                    "body": description
                },
                "custom_fields": custom_fields
            }
        }
        response = requests.post(
            url, auth=self.auth, headers=headers, json=payload)
        if response.status_code != HTTPStatus.CREATED:
            raise Exception(f"Zendesk status response: {response.status_code}")
        return response.json()

    def get_ticket(self, url, ticket_id):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url.format(ticket_id),
                                auth=self.auth, headers=headers)
        if response.status_code != HTTPStatus.OK:
            raise Exception(f"Zendesk status response: {response.status_code}")
        return response.json()
