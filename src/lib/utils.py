import pandas as pd


def get_data(symbol):
    """Read stock data for given symbols from CSV files."""
    df = pd.read_csv("data/{}.csv".format(symbol))
    df.set_index("Date", inplace=True)
    df.dropna(inplace=True)
    df.index = pd.to_datetime(df.index)
    return df
