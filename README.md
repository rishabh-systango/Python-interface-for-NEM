# Nem Rest api's using Python-Flask


We have prepared Flask based API framework to access NEM's API.

## Install instructions
  - Install Python3.6
  - Create a virtualenv with command : virtualenv -p python3.6 venv
  - Activate virtualenv: source venv/bin/activate
  - Install dependencies : pip install -r requirements.txt


By default, this api's will work on NEM's testnet environment, If you wants to work on any other environment( like "mijin", "main") export env like: 
	- export nem_env=testnet
	- export nem_base_url=http://127.0.0.1:5000

Update configuration values in Config.py files for 'mijin' and  'main'.

Ref URL: https://nemproject.github.io