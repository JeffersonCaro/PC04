import requests
import json

try:
    api_bitcoin=requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    api_bitcoin=api_bitcoin.json()

    dolar_bitcoin=float(api_bitcoin['price'])

    n=int(input('Ingrese la cantidad de bitcoins: '))

    dolar_bitcoin=n*dolar_bitcoin
    print(f'tienes: {dolar_bitcoin:,.4f}dolares en Bitcoins')
except ValueError:
    print('Error')
except requests.RequestException:
    print('Error')