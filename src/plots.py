import os
from typing import Optional
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import seaborn as sns

from config import OUTPUT_DIR


def _prepare_plot_directory() -> str:
    """
    Ensures that output/plots directory exists.
    Returns the path for saving plots.
    """
    plot_dir = os.path.join(OUTPUT_DIR, "plots")
    os.makedirs(plot_dir, exist_ok=True)
    return plot_dir


def _configure_date_axis(ax: plt.Axes) -> None:
    """
    Applies consistent date formatting to x-axis.
    """
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)


def plot_price_and_averages(df):
    """
    Plots Close price with SMA/EMA indicators for each ticker.
    """
    plot_dir = _prepare_plot_directory()

    for bbg in df["BBG"].unique():
        df_ticker = df[df["BBG"] == bbg]

        plt.figure(figsize=(20, 6))
        plt.plot(df_ticker["Date"], df_ticker["Close"], label="Close")
        plt.plot(df_ticker["Date"], df_ticker["SMA_50"], label="SMA 50")
        plt.plot(df_ticker["Date"], df_ticker["SMA_100"], label="SMA 100")
        plt.plot(df_ticker["Date"], df_ticker["EMA_20"], label="EMA 20")
        plt.plot(df_ticker["Date"], df_ticker["EMA_50"], label="EMA 50")

        plt.title(f"{bbg} - SMA / EMA")
        plt.legend()
        plt.grid(True)

        ax = plt.gca()
        _configure_date_axis(ax)

        plt.savefig(
            f"{plot_dir}/{bbg}_sma_ema.png",
            dpi=200,
            bbox_inches="tight",
        )
        plt.close()


def plot_daily_return(df):
    """
    Plots daily return bars for each ticker.
    """
    plot_dir = _prepare_plot_directory()

    for bbg in df["BBG"].unique():
        df_ticker = df[df["BBG"] == bbg]

        plt.figure(figsize=(20, 5))
        plt.bar(df_ticker["Date"], df_ticker["Daily_Return"])

        plt.title(f"{bbg} - Daily Return")
        plt.xticks(rotation=45)
        plt.grid(True)

        ax = plt.gca()
        _configure_date_axis(ax)

        plt.savefig(
            f"{plot_dir}/{bbg}_daily_return.png",
            dpi=200,
            bbox_inches="tight",
        )
        plt.close()


def plot_volatility(df):
    """
    Plots 30-day volatility for each ticker.
    """
    plot_dir = _prepare_plot_directory()

    for bbg in df["BBG"].unique():
        df_ticker = df[df["BBG"] == bbg]

        plt.figure(figsize=(12, 5))
        plt.plot(df_ticker["Date"], df_ticker["Volatility_30"])

        plt.title(f"{bbg} - Volatility 30")
        plt.xticks(rotation=45)
        plt.grid(True)

        ax = plt.gca()
        _configure_date_axis(ax)

        plt.savefig(
            f"{plot_dir}/{bbg}_volatility.png",
            dpi=200,
            bbox_inches="tight",
        )
        plt.close()


def plot_price_with_bollinger(df):
    """
    Plots price with Bollinger Bands for each ticker.
    """
    plot_dir = _prepare_plot_directory()

    for bbg in df["BBG"].unique():
        df_ticker = df[df["BBG"] == bbg]

        plt.figure(figsize=(20, 6))

        plt.plot(df_ticker["Date"], df_ticker["Close"], label="Close", linewidth=2)
        plt.plot(df_ticker["Date"], df_ticker["BB_Upper"], label="BB Upper", linestyle="--", alpha=0.7)
        plt.plot(df_ticker["Date"], df_ticker["BB_Middle"], label="BB Middle (SMA 20)", linestyle=":", alpha=0.9)
        plt.plot(df_ticker["Date"], df_ticker["BB_Lower"], label="BB Lower", linestyle="--", alpha=0.7)

        plt.fill_between(
            df_ticker["Date"],
            df_ticker["BB_Lower"],
            df_ticker["BB_Upper"],
            alpha=0.15,
        )

        plt.title(f"{bbg} - Bollinger Bands")
        plt.legend()
        plt.grid(True)

        ax = plt.gca()
        _configure_date_axis(ax)

        plt.savefig(
            f"{plot_dir}/{bbg}_bollinger.png",
            dpi=200,
            bbox_inches="tight",
        )
        plt.close()


def plot_histogram_returns(df):
    """
    Plots histogram of all daily returns combined.
    """
    plot_dir = _prepare_plot_directory()

    plt.figure(figsize=(10, 5))
    sns.histplot(df["Daily_Return"].dropna(), bins=50, kde=True)

    plt.title("Histogram of Daily Returns")
    plt.grid(True)

    plt.savefig(
        f"{plot_dir}/hist_daily_returns.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()


def plot_correlation_heatmap(df):
    """
    Generates correlation heatmap for selected numerical indicators.
    """
    plot_dir = _prepare_plot_directory()

    cols = ["Close", "Volume", "Daily_Return", "Volatility_30", "RSI_14", "MACD", "MACD_Signal"]
    corr = df[cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    plt.savefig(
        f"{plot_dir}/correlation_heatmap.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()
