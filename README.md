# Stock Market Analysis

Python-based stock market analytics project .
The project focuses on data extraction, indicator calculation, exploratory analysis and visualization.

# 1. Project Goal

The project aims to: 
• Retrieve stock market data for configurable tickers
• Calculate classic financial indicators (SMA, EMA, MACD, RSI, Bollinger Bands, Volatility)
• Generate BUY/SELL analytical signals
• Export results to CSV, Excel
• Produce visualizations saved to output/plots
• Demonstrate a clean ETL/EDA workflow in Python

# 2. Project Structure

stock-analysis/
• .env
• config.py
• main.py
• requirements.txt
• data/
• output/
– plots/
• src/
– data_loader.py
– data_transformation.py
– export_to_files.py
– plots.py
• notebooks/

# 3. Features

Data Retrieval
• Tickers loaded from TXT (comma-separated or line-separated)
• Data retrieved using Yahoo Finance API
• tqdm progress bar
• Automatic merge into one consolidated dataset

Indicators
The following metrics are calculated: • SMA: 7 / 30 / 50 / 100
• EMA: 12 / 20 / 26 / 50
• Daily Returns
• 30-day Volatility
• RSI 14
• MACD, Signal, Histogram
• Bollinger Bands

Signal Generation
• Moving Average Cross Buy/Sell
• MACD Buy/Sell
• Bollinger Buy/Sell
• Aggregated Trade Score
• Label: STRONG BUY / BUY / NEUTRAL / SELL / STRONG SELL

Export
• CSV
• Excel

Visualizations
Charts generated per ticker: • SMA / EMA
• Daily Returns
• Volatility
• Bollinger Bands
• Histogram of daily returns
• Correlation matrix
• Heatmap

All plots are saved into: output/plots/

Notebook
Folder notebooks/ contains a complete analysis walkthrough: 
• data loading
• EDA
• interpretation of indicators
• notes

# 4. How to Run the Project

## 4.1. Create environment

## 4.2. pip install -r requirements.txt

## 4.3. Configure .env

Example: 
PERIOD=200d
TICKERS_FILE=data/BBG list.txt
OUTPUT_DIR=output
DOWNLOAD_PAUSE=1

## 4.4. Run python main.py

## 4.5. Results appear in: 

output/
output/plots/

# 5. Technology Stack

Python
pandas
numpy
matplotlib
seaborn
yfinance
tqdm
xlsxwriter
dotenv

# 6. License

MIT License