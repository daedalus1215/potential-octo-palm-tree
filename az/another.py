import json
from binance import Client
import pandas as pd


def get_api_essentals(data):
    return data['api_key'], data['api_secret']


with open('./settings.json', 'r') as file:
    data = json.load(file)

api_key, api_secret = get_api_essentals(data)

client = Client(api_key=api_key, api_secret=api_secret, tld="us")

client.create_test_order(symbol="BTCUSDT",
                         side="BUY",
                         type = "MARKET",
                         quantity = 1.0)