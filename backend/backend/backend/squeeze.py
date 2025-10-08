import pandas as pd

def squeeze_detector(df, L=20, bb=2.0, kc=1.5, vf=1.5):
    ema = df.Close.ewm(span=L).mean()
    atr = (df.High - df.Low).rolling(L).mean()
    kc_hi, kc_lo = ema + kc*atr, ema - kc*atr
    sma = df.Close.rolling(L).mean()
    std = df.Close.rolling(L).std()
    bb_hi, bb_lo = sma + bb*std, sma - bb*std
    squeeze = (bb_lo > kc_lo) & (bb_hi < kc_hi)
    vol = df.Volume > vf*df.Volume.rolling(L).mean()
    macd = df.Close.ewm(12).mean() - df.Close.ewm(26).mean()
    sig = macd.ewm(9).mean()
    return squeeze & vol & (macd > sig)
