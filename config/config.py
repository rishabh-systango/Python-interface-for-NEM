import os

# env should be mijin, testnet or main.By default it is testnet.

TEST_NET_ENV = "testnet"
MIJIN_ENV = "mijin"
MAIN_ENV = "main"

# Testnet setting here.
TEST_NET_CONFIG = {
    "version": -1744830463,
    "CreateNameSpace": {
        "type": 8193,
        "fee": 150000,
        "rentalFee": 100000000,
    },
    "CreateMosaic": {
        "fee": 150000,
        "type": 16385,
        "creationFee": 10000000,
    },
    "CreateMultiSign": {
        "fee": 28000000,
        "type": 4097,
        "creationFee": 10000000,
    },
    "InitiateMultiSignTransaction": {
        "fee": 3000000,
        "type": 4100,
        "otherTrans": {
            "fee": 4000000,
            "type": 257
        }
    },
    "CosigningMultiSignTransaction": {
        "fee": 6000000,
        "type": 4098,
    },
    "CreateMosaicTransfer": {
        "fee": 30000000,
        "type": 257,
    }
}

# Mijin setting here.

MIJIN_CONFIG = {}

# main settings here

MAIN_CONFIG = {}


def get_config_from_env():
    nem_env = os.environ.get('nem_env')
    if nem_env == MIJIN_ENV:
        return MIJIN_CONFIG
    elif nem_env == MAIN_ENV:
        return MAIN_CONFIG
    else:
        return TEST_NET_CONFIG



CONFIG = get_config_from_env()