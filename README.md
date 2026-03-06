# Stock Market Analysis

# 1. Project Overview

This project is a Python-based financial data analysis pipeline that retrieves stock market data, calculates technical indicators, generates trading signals, and produces analytical visualizations.

The project demonstrates a clean workflow combining data extraction, financial analysis, and visualization.

# 2. Project Goals

The project aims to:
- Retrieve stock market data for configurable tickers
- Calculate common technical indicators
- Generate BUY / SELL analytical signals
- Export processed data to analytical formats
- Produce visualizations supporting exploratory analysis

# 3. Features

- Data Retrieval
- Tickers loaded from TXT file
- Data retrieved using the Yahoo Finance API
- Automatic merge into a consolidated dataset
- tqdm progress bar for download tracking
- Technical Indicators
- The following indicators are calculated:
- Moving Averages
- SMA: 7 / 30 / 50 / 100
- EMA: 12 / 20 / 26 / 50
- Momentum & Volatility
- Daily Returns
- 30-day Volatility
- RSI (14)
- Trend Indicators
- MACD
- Signal Line
- Histogram
- Bands
- Bollinger Bands
- Signal Generation
- Trading signals are generated using:
- Moving Average Crossovers
- MACD signals
- Bollinger Band signals
- Signals are aggregated into a Trade Score and classified as:
	- STRONG BUY
	- BUY
	- NEUTRAL
	- SELL
	- STRONG SELL

# 4. Project Structure

stock-analysis/
├── .env
├── config.py
├── main.py
├── requirements.txt
│
├── data/
│
├── output/
│   └── plots/
│
├── src/
│   ├── data_loader.py
│   ├── data_transformation.py
│   ├── export_to_files.py
│   └── plots.py
│
└── notebooks/

# 5. Visualizations

The project generates charts for each ticker including:
- SMA / EMA trends
- Daily returns
- Volatility
- Bollinger Bands
- Histogram of returns
- Correlation matrix
- Heatmap

All plots are saved in:
output/plots/

# 6. How to Run the Project

## 6.1 Create Environment
python -m venv venv
Activate the environment.

## 6.2 Install Dependencies

pip install -r requirements.txt

## 6.3 Configure Environment Variables

Example .env file:

PERIOD=200d
TICKERS_FILE=data/tickers.txt
OUTPUT_DIR=output
DOWNLOAD_PAUSE=1

## 6.4 Run the Project

python main.py

## 6.5 Output Files

Results will be generated in:

output/
output/plots/

Including:
- CSV datasets
- Excel reports
- analytical plots

# 7. Analytical Notebook

The directory contains:
stock_analysis.ipynb

This notebook presents a full analysis of stock market data retrieved by the project script. It covers:
- Loading historical stock data from the latest CSV file in output/
- Quick data exploration (EDA)
- info and describe
- list of available tickers
- Charts of processed indicators for each ticker
- Price with SMA / EMA overlays
- Daily Returns histogram
- Volatility trends
- Correlation analysis between indicators (Close, Volume, Daily Return, Volatility, RSI, MACD)
- Final conclusions summarizing data quality and insights
- Demonstrates a full analytical workflow from ETL to visualization

This notebook ensures that all processed data, indicators, and visualizations can be easily explored and validated.

# 8. Technology Stack

Python
pandas
numpy
matplotlib
seaborn
yfinance
tqdm
xlsxwriter
python-dotenv
Jupyter Notebook

# 9. License

MIT License