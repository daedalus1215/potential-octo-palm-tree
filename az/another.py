import json
import requests
import binance
import panda


def get_api_essentals(data):
    return data['api_key'], data['api_secret']


with open('./settings.json', 'r') as file:
    data = json.load(file)

api_key, api_secret = get_api_essentals(data)

client = binance.Client(api_key=api_key, api_secret=api_secret, tld="us")

client.create_test_order(symbol="BTCUSDT",
                         side="BUY",
                         type = "MARKET",
                         quantity = 1.0)


def get_history(symbol, interval, start, end=None):
    bars = client.get_historical_klines(symbol=symbol, interval=interval, start_str=start, end_str=end, limit=1000)

    df = panda.DataFrame(bars)
    df["Date"] = panda.to_datetime(df.iloc[:, 0], unit="ms")
    df.columns = [
        "Open Time",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Close Time",
        "Quote Asset Volume",
        "Number of Trades",
        "Taker Buy Base Asset Volume",
        "Taker Buy Quote Asset Volume",
        "Ignore",
        "Date"]

    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
    df.set_index("Date", inplace=True)
    for column in df.columns:
        df[column] = panda.to_numeric(df[column], errors="coerce")

    return df