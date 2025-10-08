import os, pathlib, json, httpx, pandas as pd
from fastapi import FastAPI, BackgroundTasks
from squeeze import squeeze_detector
from fetch import yahoo_minute

DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)
SYMS = os.getenv("TICKERS", "TSLA,AMD,GME").split(",")
app = FastAPI(title="Squeeze Machine API")

def update_symbol(sym: str):
    df = yahoo_minute(sym)
    sig = squeeze_detector(df).iloc[-1]
    df.tail(1).to_csv(DATA_DIR / f"{sym}.csv")
    with open(DATA_DIR / "signals.json", "w") as f:
        json.dump({sym: bool(sig)}, f)

@app.post("/refresh")
def refresh(bg: BackgroundTasks):
    for s in SYMS:
        bg.add_task(update_symbol, s)
    return {"status": "queued"}

@app.get("/signals")
def signals():
    fp = DATA_DIR / "signals.json"
    if fp.exists():
        return json.load(fp)
    return {}
