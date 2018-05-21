from flask import Flask
from flask_restful import Api
from controllers.account_controller import *
from controllers.transaction_controller import *

app = Flask(__name__)

api = Api(app)

api.add_resource(AccountController, '/api/account', endpoint= 'accountDetails')
api.add_resource(HeartbeatController, '/api/heartbeat', endpoint= 'heartbeat')
api.add_resource(AccountControllerStatus, '/api/account/status', endpoint= 'account_status')
api.add_resource(CreateNamespaceController, '/api/namespace', endpoint= 'create_namespace')
api.add_resource(CreateMosaicController, '/api/mosaic', endpoint= 'create_mosaic')
api.add_resource(CreateMultisignController, '/api/multisign', endpoint= 'create_multisign')
api.add_resource(InitiateMultisignTransactionController, '/api/multisign/transfer', endpoint= 'create_multisign_transaction')
api.add_resource(CosigningMultisigTransactionController, '/api/multisign/cosigning_transaction', endpoint= 'cosigning_multisig_transaction')
api.add_resource(CreateMosaicTransferController, '/api/mosaic_transaction', endpoint= 'create_mosaic_transaction')




if __name__ == '__main__':
    app.run(debug=True)