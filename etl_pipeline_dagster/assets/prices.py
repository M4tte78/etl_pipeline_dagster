import yfinance as yf
import pandas as pd
from dagster import asset
from etl_pipeline_dagster.resources.config import ASSET_TICKERS

@asset
def daily_prices() -> pd.DataFrame:
    df = yf.download(ASSET_TICKERS[:20], period="2d", interval="1d", threads=True)

    if df.empty:
        raise ValueError("No data returned by yfinance. Possibly no internet or too many tickers.")

    if isinstance(df.columns, pd.MultiIndex):
        if 'Price' in df.columns.get_level_values(0):
            df = df['Price'].transpose()
        elif 'Close' in df.columns.get_level_values(0):
            df = df['Close'].transpose()
        else:
            raise KeyError("Neither 'Price' nor 'Close' found in yfinance data.")
    else:
        raise ValueError("Unexpected format from yfinance. Expected MultiIndex columns.")

    if df.shape[1] < 2:
        raise ValueError("Not enough data to compute returns (need 2 days).")

    df.columns = ["yesterday", "today"]

    # ✅ Forcer l'index en colonne "ticker"
    df = df.reset_index()
    df = df.rename(columns={df.columns[0]: "ticker"})  # garanti que la 1re colonne est bien "ticker"

    return df
