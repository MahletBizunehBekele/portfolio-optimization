import matplotlib.pyplot as plt


def plot_closing_prices(datasets):
    """
    Plot adjusted closing prices for all assets.
    """
    plt.figure(figsize=(14, 6))

    for ticker, df in datasets.items():
        plt.plot(df["Date"], df["Adj Close"], label=ticker)

    plt.title("Adjusted Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_daily_returns(datasets):
    """
    Plot daily returns for all assets.
    """
    plt.figure(figsize=(14, 6))

    for ticker, df in datasets.items():
        plt.plot(df["Date"], df["Daily Return"], alpha=0.6, label=ticker)

    plt.title("Daily Percentage Returns")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_rolling_statistics(df, ticker):
    """
    Plot rolling mean and rolling standard deviation.
    """
    plt.figure(figsize=(14,6))

    plt.plot(df["Date"], df["Adj Close"], label="Adjusted Close")
    plt.plot(df["Date"], df["Rolling Mean"], label="30-Day Mean")
    plt.plot(df["Date"], df["Rolling Std"], label="30-Day Std")

    plt.title(f"{ticker} Rolling Statistics")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def detect_outliers(df, threshold=3):
    """
    Detect unusually large daily returns using z-score.
    """
    returns = df["Daily Return"]

    z_scores = (returns - returns.mean()) / returns.std()

    outliers = df[z_scores.abs() > threshold]

    return outliers