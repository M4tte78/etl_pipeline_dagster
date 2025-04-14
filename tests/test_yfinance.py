import yfinance as yf
from etl_pipeline_dagster.resources.config import ASSET_TICKERS

df = yf.download(ASSET_TICKERS[:5], period="2d", interval="1d", group_by="ticker", threads=True)
print(df.columns)
print(df.head())
