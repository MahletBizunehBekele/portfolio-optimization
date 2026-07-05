import pandas as pd


def clean_data(df):
    """
    Basic preprocessing.
    """

    df = df.copy()

    # Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort by date
    df.sort_values("Date", inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Handle missing values
    df.ffill(inplace=True)
    df.bfill(inplace=True)

    return df


def calculate_daily_returns(df):
    """
    Compute percentage daily returns.
    """

    df = df.copy()

    df["Daily Return"] = df["Adj Close"].pct_change()

    return df


def rolling_statistics(df, window=30):
    """
    Rolling mean and volatility.
    """

    df = df.copy()

    df["Rolling Mean"] = df["Adj Close"].rolling(window).mean()

    df["Rolling Std"] = df["Adj Close"].rolling(window).std()

    return df