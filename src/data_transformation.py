import numpy as np
import pandas as pd


def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["BBG", "Date"]).copy()

    df["Close_Change"] = df.groupby("BBG")["Close"].diff()
    df["Close_Change_Pct"] = df.groupby("BBG")["Close"].pct_change() * 100

    df["Volume_Change"] = df.groupby("BBG")["Volume"].diff()
    df["Volume_Change_Pct"] = df.groupby("BBG")["Volume"].pct_change() * 100

    df["Daily_Return"] = df.groupby("BBG")["Close"].pct_change()

    df["SMA_7"] = df.groupby("BBG")["Close"].transform(lambda x: x.rolling(7).mean())
    df["SMA_30"] = df.groupby("BBG")["Close"].transform(lambda x: x.rolling(30).mean())
    df["SMA_50"] = df.groupby("BBG")["Close"].transform(lambda x: x.rolling(50).mean())
    df["SMA_100"] = df.groupby("BBG")["Close"].transform(lambda x: x.rolling(100).mean())

    df["EMA_12"] = df.groupby("BBG")["Close"].transform(
        lambda x: x.ewm(span=12, adjust=False).mean()
    )
    df["EMA_20"] = df.groupby("BBG")["Close"].transform(
        lambda x: x.ewm(span=20, adjust=False).mean()
    )
    df["EMA_26"] = df.groupby("BBG")["Close"].transform(
        lambda x: x.ewm(span=26, adjust=False).mean()
    )
    df["EMA_50"] = df.groupby("BBG")["Close"].transform(
        lambda x: x.ewm(span=50, adjust=False).mean()
    )

    df["Volatility_30"] = df.groupby("BBG")["Daily_Return"].transform(
        lambda x: x.rolling(30).std()
    )
    df["RSI_14"] = df.groupby("BBG")["Close"].transform(calculate_rsi)

    df["MACD"] = df["EMA_12"] - df["EMA_26"]
    df["MACD_Signal"] = df.groupby("BBG")["MACD"].transform(
        lambda x: x.ewm(span=9, adjust=False).mean()
    )
    df["MACD_Hist"] = df["MACD"] - df["MACD_Signal"]

    df["BB_Middle"] = df.groupby("BBG")["Close"].transform(
        lambda x: x.rolling(20).mean()
    )
    df["BB_Std"] = df.groupby("BBG")["Close"].transform(
        lambda x: x.rolling(20).std()
    )

    df["BB_Upper"] = df["BB_Middle"] + 2 * df["BB_Std"]
    df["BB_Lower"] = df["BB_Middle"] - 2 * df["BB_Std"]

    return df


def calculate_signals(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Signal_MA_Cross_Buy"] = (
        (df["SMA_7"] > df["SMA_30"])
        & (
            df.groupby("BBG")["SMA_7"].shift(1)
            <= df.groupby("BBG")["SMA_30"].shift(1)
        )
    )

    df["Signal_MA_Cross_Sell"] = (
        (df["SMA_7"] < df["SMA_30"])
        & (
            df.groupby("BBG")["SMA_7"].shift(1)
            >= df.groupby("BBG")["SMA_30"].shift(1)
        )
    )

    df["Signal_MACD_Buy"] = (
        (df["MACD"] > df["MACD_Signal"])
        & (
            df.groupby("BBG")["MACD"].shift(1)
            <= df.groupby("BBG")["MACD_Signal"].shift(1)
        )
    )

    df["Signal_MACD_Sell"] = (
        (df["MACD"] < df["MACD_Signal"])
        & (
            df.groupby("BBG")["MACD"].shift(1)
            >= df.groupby("BBG")["MACD_Signal"].shift(1)
        )
    )

    df["Signal_BB_Buy"] = df["Close"] < df["BB_Lower"]
    df["Signal_BB_Sell"] = df["Close"] > df["BB_Upper"]

    df["Trade_Score"] = (
        df["Signal_MA_Cross_Buy"].astype(int)
        - df["Signal_MA_Cross_Sell"].astype(int)
        + df["Signal_MACD_Buy"].astype(int)
        - df["Signal_MACD_Sell"].astype(int)
    )

    return df


def trade_score_label(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Trade_Label"] = np.select(
        [
            df["Trade_Score"] >= 2,
            df["Trade_Score"] == 1,
            df["Trade_Score"] == 0,
            df["Trade_Score"] == -1,
            df["Trade_Score"] <= -2,
        ],
        ["STRONG BUY", "BUY", "NEUTRAL", "SELL", "STRONG SELL"],
        default="NEUTRAL",
    )

    return df
