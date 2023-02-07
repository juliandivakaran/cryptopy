#BINANCE CLIEENT
from binance.client import Client

# ENTER YOUR BINANCE API KEY
api_key = "PAST YOUR BINANCE API KEY"

api_secret = "your api secret key"
client =Client(api_key,api_secret)
print(client.ping())


info = client.get_all_tickers()
print(info)

