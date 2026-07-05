import os
import yfinance as yf
import pandas as pd


START_DATE = "2015-01-01"
END_DATE = "2026-06-30"

TICKERS = {
    "TSLA": "Tesla",
    "BND": "Vanguard Total Bond Market ETF",
    "SPY": "S&P 500 ETF"
}


def download_asset(ticker, start=START_DATE, end=END_DATE):
    """
    Download historical price data from Yahoo Finance.
    """
    df = yf.download(
        ticker,
        start=start,
        end=end,
        progress=False,
        auto_adjust=False
    )

    if df.empty:
        raise ValueError(f"No data returned for {ticker}")

    df.reset_index(inplace=True)
    return df


def save_data(df, ticker, folder="data/processed"):
    """
    Save downloaded data as CSV.
    """
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"{ticker}.csv")

    df.to_csv(path, index=False)

    print(f"Saved {ticker} -> {path}")


def load_all_assets():
    """
    Download and save all required assets.
    """

    datasets = {}

    for ticker in TICKERS:

        print(f"Downloading {ticker}...")

        df = download_asset(ticker)

        save_data(df, ticker)

        datasets[ticker] = df

    return datasets