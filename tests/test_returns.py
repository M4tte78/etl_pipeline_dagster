from assets.returns import daily_returns
import pandas as pd

def test_daily_returns():
    data = {
        "ticker": ["AAPL", "MSFT"],
        "yesterday": [100, 200],
        "today": [110, 190]
    }
    df = pd.DataFrame(data)
    result = daily_returns(df)
    assert abs(result.loc[result['ticker'] == 'AAPL', 'return'].values[0] - 0.10) < 1e-6
    assert abs(result.loc[result['ticker'] == 'MSFT', 'return'].values[0] + 0.05) < 1e-6
