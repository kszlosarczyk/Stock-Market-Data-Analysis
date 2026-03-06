import time
from typing import List

import pandas as pd
import yfinance as yf
from tqdm import tqdm

from config import DOWNLOAD_PAUSE


def load_tickers_from_txt(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if "," in text:
        tickers = [t.strip().strip("'").strip('"') for t in text.split(",")]
    else:
        tickers = [
            line.strip().strip("'").strip('"')
            for line in text.splitlines()
            if line.strip()
        ]

    return tickers


def download_data(tickers: List[str], period: str = "200d") -> pd.DataFrame:
    dfs = []

    for ticker in tqdm(tickers, desc="Downloading market data"):
        df = yf.download(ticker, period=period)

        if df.empty:
            print(f"No data for {ticker}")
            continue

        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
        df = df.reset_index()
        df["BBG"] = ticker

        dfs.append(df)
        time.sleep(DOWNLOAD_PAUSE)

    if not dfs:
        return pd.DataFrame()

    df = pd.concat(dfs, ignore_index=True)
    numeric_cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Date"] = pd.to_datetime(df["Date"])
    return df
