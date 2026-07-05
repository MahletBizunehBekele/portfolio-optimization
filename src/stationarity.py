from statsmodels.tsa.stattools import adfuller


def adf_test(series):

    result = adfuller(series.dropna())

    output = {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "Lags Used": result[2],
        "Observations": result[3]
    }

    return output