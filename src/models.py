import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error
)
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from pmdarima import auto_arima


def train_test_split_time_series(df, split_date="2025-01-01"):
    """
    Chronologically split a time series dataset.
    """

    train = df[df["Date"] < split_date].copy()
    test = df[df["Date"] >= split_date].copy()

    return train, test


def fit_arima(train_series, order=(5, 1, 0)):
    """
    Train an ARIMA model.
    """

    model = ARIMA(train_series, order=order)

    fitted_model = model.fit()

    return fitted_model


def forecast(model, steps):
    """
    Generate forecasts.
    """

    predictions = model.forecast(steps=steps)

    return predictions


def evaluate(actual, predicted):

    mae = mean_absolute_error(actual, predicted)

    rmse = np.sqrt(mean_squared_error(actual, predicted))

    mape = mean_absolute_percentage_error(actual, predicted)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "MAPE": mape
    }



def auto_fit_arima(train_series):

    model = auto_arima(
        train_series,
        seasonal=False,
        trace=True,
        suppress_warnings=True,
        stepwise=True
    )

    return model