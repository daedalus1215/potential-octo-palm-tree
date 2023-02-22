import json
from binance import Client
import pandas as pd


def get_api_essentals(data):
    return data['api_key'], data['api_secret']


with open('./settings.json', 'r') as file:
    data = json.load(file)

api_key, api_secret = get_api_essentals(data)

client = Client(api_key=api_key, api_secret=api_secret, tld="us")
account = client.get_account()
balances = account["balances"]
print(balances)
df = pd.DataFrame(balances)
df.info()

df.free = pd.to_numeric(df.free, errors="coerce")
df.locked = pd.to_numeric(df.locked, errors="coerce")
df.loc[df.free > 0]
print(client.get_asset_balance(asset="BTC"))
print(client.get_asset_balance(asset="ETH"))
float(client.get_asset_balance(asset="USD")["free"])

print(client.get_symbol_ticker(symbol="BTCUSDT"))
print(client.get_avg_price(symbol="BTCUSDT"))
df = pd.DataFrame(client.get_all_tickers())
print(df)
print(df[df.symbol.str.contains("BTC")])
print(df[df.symbol.str.contains("BTC") & df.symbol.str.contains("USD")])
last24 = client.get_ticker(symbol="BTCUSDT")
print(last24)

print(float(last24["openPrice"]))