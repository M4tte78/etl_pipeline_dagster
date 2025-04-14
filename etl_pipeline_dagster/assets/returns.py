import pandas as pd
from dagster import asset

@asset(deps=["daily_prices"])
def daily_returns(daily_prices: pd.DataFrame) -> pd.DataFrame:
    df = daily_prices.copy()

    if 'ticker' not in df.columns:
        raise ValueError("'ticker' column missing from daily_prices")

    df["return"] = (df["today"] - df["yesterday"]) / df["yesterday"]
    return df[["ticker", "return"]].sort_values("return", ascending=False)
