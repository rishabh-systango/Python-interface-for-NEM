

namespace_schema = {
            "transaction": {'type': 'dict', 'schema': {
	                "signer": {'type': 'string', 'required': True},
	                "rentalFeeSink": {'type': 'string', 'required': True},
	                "newPart": {'type': 'string', 'required': True},
	                "parent": {'type': 'string', 'required': False, 'nullable': True}
            	}
            },
            "privateKey": {'type': 'string', 'required': True}
}

mosiacs_schema = {}