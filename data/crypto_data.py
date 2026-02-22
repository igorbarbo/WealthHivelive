import requests
import pandas as pd

def get_crypto_history(coin_id, vs_currency="usd", days=365*5):
    """
    Retorna histórico de preços de uma crypto do CoinGecko
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency={vs_currency}&days={days}"
    r = requests.get(url)
    data = r.json()
    prices = pd.DataFrame(data['prices'], columns=['timestamp','price'])
    prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
    prices.set_index('timestamp', inplace=True)
    return prices
