import httpx, pandas as pd

def yahoo_minute(symbol: str) -> pd.DataFrame:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    params = {"interval": "1m", "range": "1d"}
    r = httpx.get(url, params=params, timeout=10).json()
    q = r["chart"]["result"][0]
    ts = pd.to_datetime(q["timestamp"], unit="s")
    prices = q["indicators"]["quote"][0]
    df = pd.DataFrame(prices, index=ts)
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    return df
