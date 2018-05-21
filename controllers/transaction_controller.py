from flask_restful import Resource
from utils.nem import NEMConnect
from flask import request
from utils import utils
from config.config import CONFIG
import json
from cerberus import Validator
from validation_schema.transaction_schema import namespace_schema, mosiacs_schema

class CreateNamespaceController(Resource):
    def post(self):
        nem = NEMConnect()
        validator_obj = Validator(namespace_schema)
        data = json.loads(request.data)        
        validate = validator_obj.validate(data)
        response = {}
        if (validate):
            transation = data.get("transaction")
            if transation is not None:
                timestamp = utils.get_timestamp()
                transation["timeStamp"] = timestamp
                transation["deadline"] = utils.get_deadline(timestamp)
                transation["rentalFee"] = CONFIG["CreateNameSpace"].get("rentalFee")
                transation["fee"] = CONFIG["CreateNameSpace"].get("fee")
                transation["type"] = CONFIG["CreateNameSpace"].get("type")
                transation["version"] = CONFIG.get("version")
            response = nem.initiate_transaction(data)
        else:
            response['Errors'] = validator_obj.errors
        return response


class CreateMosaicController(Resource):
    def post(self):
        nem = NEMConnect()
        data = json.loads(request.data)        
        transation = data.get("transaction")
        if transation is not None:
            timestamp = utils.get_timestamp()
            transation["timeStamp"] = timestamp
            transation["deadline"] = utils.get_deadline(timestamp)
            transation["fee"] = CONFIG["CreateMosaic"].get("fee")
            transation["type"] = CONFIG["CreateMosaic"].get("type")
            transation["creationFee"] = CONFIG["CreateMosaic"].get("creationFee")
            transation["version"] = CONFIG.get("version")
        response = nem.initiate_transaction(data)
        return response


class CreateMosaicTransferController(Resource):
    def post(self):
        nem = NEMConnect()
        data = json.loads(request.data)        
        transation = data.get("transaction")
        if transation is not None:
            timestamp = utils.get_timestamp()
            transation["timeStamp"] = timestamp
            transation["deadline"] = utils.get_deadline(timestamp)
            transation["fee"] = CONFIG["CreateMosaicTransfer"].get("fee")
            transation["type"] = CONFIG["CreateMosaicTransfer"].get("type")
            transation["version"] = CONFIG.get("version")
        response = nem.initiate_transaction(data)
        return response


class CreateMultisignController(Resource):
    def post(self):
        nem = NEMConnect()
        data = json.loads(request.data)        
        transation = data.get("transaction")
        if transation is not None:
            timestamp = utils.get_timestamp()
            transation["timeStamp"] = timestamp
            transation["deadline"] = utils.get_deadline(timestamp)
            transation["fee"] = CONFIG["CreateMultiSign"].get("fee")
            transation["type"] = CONFIG["CreateMultiSign"].get("type")
            transation["creationFee"] = CONFIG["CreateMultiSign"].get("creationFee")
            transation["version"] = CONFIG.get("version")
        response = nem.initiate_transaction(data)
        return response

class InitiateMultisignTransactionController(Resource):
    def post(self):
        nem = NEMConnect()
        data = json.loads(request.data)        
        transation = data.get("transaction")
        if transation is not None:
            timestamp = utils.get_timestamp()
            transation["timeStamp"] = timestamp
            transation["deadline"] = utils.get_deadline(timestamp)
            transation["fee"] = CONFIG["InitiateMultiSignTransaction"].get("fee")
            transation["type"] = CONFIG["InitiateMultiSignTransaction"].get("type")
            transation["version"] = CONFIG.get("version")
            if transation.get("otherTrans") is not None:
                transation["otherTrans"]["fee"] = CONFIG["InitiateMultiSignTransaction"]["otherTrans"].get("fee")
                transation["otherTrans"]["type"] = CONFIG["InitiateMultiSignTransaction"]["otherTrans"].get("type")
                transation["otherTrans"]["timeStamp"] = transation["timeStamp"]
                transation["otherTrans"]["deadline"] = transation["deadline"]
                transation["otherTrans"]["version"] = CONFIG.get("version")
        
        response = nem.initiate_transaction(data)
        return response

class CosigningMultisigTransactionController(Resource):
    def post(self):
        nem = NEMConnect()
        data = json.loads(request.data)        
        transation = data.get("transaction")
        if transation is not None:
            timestamp = utils.get_timestamp()
            transation["timeStamp"] = timestamp
            transation["deadline"] = utils.get_deadline(timestamp)
            transation["fee"] = CONFIG["CosigningMultiSignTransaction"].get("fee")
            transation["type"] = CONFIG["CosigningMultiSignTransaction"].get("type")
            transation["version"] = CONFIG.get("version")        
        response = nem.initiate_transaction(data)
        return response
        
   