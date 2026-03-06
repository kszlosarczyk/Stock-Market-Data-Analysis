from dotenv import load_dotenv
import os

load_dotenv()

PERIOD = os.getenv("PERIOD", "200d")
TICKERS_FILE = os.getenv("TICKERS_FILE", "data/BBG list.txt")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
DOWNLOAD_PAUSE = int(os.getenv("DOWNLOAD_PAUSE", 1))
