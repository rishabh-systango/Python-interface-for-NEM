import requests
import json
import os

BASE_URL = os.environ.get('nem_base_url', 'http://127.0.0.1:7890')

URL_MAP = { 'heartbeat': "/heartbeat", 
            "account": "/account/get?address=", 
            "account_status": "/account/status?address=",
            "prepare_announce": "/transaction/prepare-announce"
        }


class NEMConnect: 

    def __init__(self):
        self._URL_MAP = URL_MAP
        self._BASE_URL = BASE_URL


    def _get_complete_url(self, api_name):
        api_url = self._URL_MAP.get(api_name)
        url = self._BASE_URL + api_url
        return url


    def _get(self, url, payload={}):
        response = requests.get(url, params=payload)
        return {"content": json.loads(response._content), "status_code": response.status_code }

    def _post(self, url, payload={}, headers = {}):
        headers.update({'content-type': 'application/json'})
        response = requests.post(url, json= payload, headers=headers)
        return {"content": json.loads(response._content), "status_code": response.status_code }


    def get_heartbeat(self):
        url = self._get_complete_url('heartbeat')
        response = self._get(url)
        return response

    def get_account_detail(self, address):
        url = self._get_complete_url('account')
        response = self._get(url + address)
        return response

    def get_account_status(self, address):
        url = self._get_complete_url('account_status')
        response = self._get(url + address)
        return response

    def initiate_transaction(self, payload):
        url = self._get_complete_url('prepare_announce')
        response = self._post(url, payload)
        return response