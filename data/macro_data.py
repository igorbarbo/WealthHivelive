import requests
import pandas as pd

def get_fred_series(series_id, api_key, start="2000-01-01", end="2026-01-01"):
    """
    Retorna série histórica do FRED
    """
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json&observation_start={start}&observation_end={end}"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame([{'date':obs['date'], 'value':float(obs['value'])} for obs in data['observations']])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df
