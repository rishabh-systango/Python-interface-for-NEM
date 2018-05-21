from flask_restful import Resource
from utils.nem import NEMConnect
from flask import request
from utils import utils

class AccountController(Resource):

    def get(self):
        nem = NEMConnect()
        address = request.headers.get('Address')
        response = nem.get_account_detail(address)
        return response

class AccountControllerStatus(Resource):

    def get(self):
        nem = NEMConnect()
        address = request.headers.get('address')
        response = nem.get_account_detail(address)
        return response
    

class HeartbeatController(Resource):

    def get(self):
        nem = NEMConnect()
        response = nem.get_heartbeat()
        return response