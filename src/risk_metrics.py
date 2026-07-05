import numpy as np


def value_at_risk(returns, confidence=0.95):
    """
    Historical Value at Risk.
    """
    return np.percentile(returns.dropna(), (1-confidence)*100)


def sharpe_ratio(returns, risk_free_rate=0.02):
    """
    Annualized Sharpe Ratio.
    """
    excess_returns = returns.dropna() - risk_free_rate/252

    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()