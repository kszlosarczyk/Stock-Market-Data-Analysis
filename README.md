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

stock-market-analysis/
├── .env
├── config.py
├── main.py
├── requirements.txt
├── stock analysis.ipynb
│
├── data/
│   ├── BBG list_txt
│
├── output/
│   └── plots/
│
├── powerbi/
│   └── dashboards.pdf
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_transformation.py
│   ├── export_to_files.py
│   └── plots.py

# 5. Visualizations

The project generates charts for each ticker including:
- SMA / EMA trends
- Daily returns
- Volatility
- Bollinger Bands

All plots are saved in:
output/plots/

# 6. Power BI Dashboard

A Power BI dashboard has been created to visualize the stock market data and analytical signals.

The dashboard is based on the CSV and Excel outputs from the project.

It provides interactive charts for:
- Price trends with SMA/EMA overlays
- Technical indicators (RSI, Bollinger Bands)
- Signal analysis and trade recommendations

Note: The .pbix file is not included in this repository. 
Use the exported CSV/Excel files from output/ to load the dashboard in Power BI Desktop.

This allows stakeholders to explore the data interactively without sharing the raw Power BI project file.

# 7. How to Run the Project

## 7.1 Create Environment

python -m venv venv
Activate the environment.

## 7.2 Install Dependencies

pip install -r requirements.txt

## 7.3 Configure Environment Variables

Example .env file:

PERIOD=200d
TICKERS_FILE=data/tickers.txt
OUTPUT_DIR=output
DOWNLOAD_PAUSE=1

## 7.4 Run the Project

python main.py

## 7.5 Output Files

Results will be generated in:

output/
output/plots/

Including:
- CSV datasets
- Excel reports
- analytical plots

# 8. Analytical Notebook

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

# 9. Technology Stack

Power BI
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

# 10. License

MIT License