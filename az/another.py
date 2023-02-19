import json
from binance import Client

with open('./settings.json', 'r') as file:
    data = json.load(file)
    api_key = data['api_key']
    api_secret = data['api_secret']
    client = Client(api_key = api_key, api_secret = api_secret, tld = "us")
    print(client.get_account()) # account details
