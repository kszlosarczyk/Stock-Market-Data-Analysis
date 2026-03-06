from config import PERIOD, TICKERS_FILE
from src.data_loader import load_tickers_from_txt, download_data
from src.data_transformation import (
    calculate_indicators,
    calculate_signals,
    trade_score_label,
)
from src.export_to_files import save_outputs
from src.plots import (
    plot_daily_return,
    plot_price_and_averages,
    plot_price_with_bollinger,
    plot_volatility,
    plot_histogram_returns,
    plot_correlation_heatmap,
)


def main() -> None:
    """Main ETL and analysis pipeline."""

    tickers = load_tickers_from_txt(TICKERS_FILE)
    df = download_data(tickers, period=PERIOD)

    if df.empty:
        print("No data downloaded. Exiting.")
        return

    df = calculate_indicators(df)
    df = calculate_signals(df)
    df = trade_score_label(df)

    save_outputs(df)

    plot_price_and_averages(df)
    plot_price_with_bollinger(df)
    plot_daily_return(df)
    plot_volatility(df)
    plot_histogram_returns(df)
    plot_correlation_heatmap(df)

    print("Analysis completed. Results saved to output/ directory.")


if __name__ == "__main__":
    main()
