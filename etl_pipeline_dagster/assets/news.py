from dagster import asset
import pandas as pd

@asset
def daily_news() -> pd.DataFrame:
    # Simulons quelques actualités
    news = [
        {"title": "Tech stocks rally as earnings impress", "source": "Reuters"},
        {"title": "Energy sector dips amid oil price volatility", "source": "Bloomberg"},
        {"title": "Pharma gains momentum on vaccine news", "source": "CNBC"},
    ]
    return pd.DataFrame(news)
