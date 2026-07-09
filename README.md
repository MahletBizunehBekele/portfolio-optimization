# Portfolio Optimization using Time Series Forecasting

## Overview

This project was developed for GMF Investments to support data-driven portfolio management through financial time series forecasting and Modern Portfolio Theory (MPT).

The project analyzes historical market data for three financial assets, builds a forecasting model for Tesla stock prices, and uses the forecasting results to construct an optimized investment portfolio. The optimized portfolio is then evaluated through a simple backtesting strategy against a benchmark portfolio.

---

## Business Objective

GMF Investments aims to improve investment decisions by combining historical financial data with forecasting models and portfolio optimization techniques.

This project:

- Forecasts Tesla (TSLA) stock prices using ARIMA.
- Evaluates forecast accuracy using multiple error metrics.
- Optimizes portfolio allocation using Modern Portfolio Theory.
- Backtests the optimized portfolio against a benchmark.

---

## Dataset

Historical market data was downloaded using the **Yahoo Finance (yfinance)** Python library.

### Assets

| Asset | Ticker | Description |
|-------|--------|-------------|
| Tesla | TSLA | High-growth technology stock |
| Vanguard Total Bond Market ETF | BND | Investment-grade U.S. bonds |
| SPDR S&P 500 ETF | SPY | Tracks the S&P 500 Index |

### Time Period

**January 1, 2015 – June 30, 2026**

---

## Project Structure

```
portfolio-optimization/

├── .github/
│   └── workflows/
├── data/
│   └── processed/
├── notebooks/
│   └── 01_data_preprocessing_and_eda.ipynb
├── scripts/
├── src/
├── tests/
├── requirements.txt
└── README.md
```

---

## Methodology

### Task 1 – Data Preprocessing & Exploratory Data Analysis

- Downloaded historical data using yfinance
- Cleaned and preprocessed datasets
- Checked missing values
- Calculated daily returns
- Computed rolling mean and rolling standard deviation
- Identified outliers
- Performed Augmented Dickey-Fuller (ADF) stationarity tests
- Calculated:
  - Value at Risk (VaR)
  - Sharpe Ratio

Visualizations include:

- Closing Price Trends
- Daily Returns
- Rolling Volatility
- Outlier Detection

---

### Task 2 – Time Series Forecasting

A chronological train-test split was used:

- Training: 2015–2024
- Testing: 2025–2026

#### ARIMA

The ARIMA model was fitted using the training data.

Model selection was performed using **Auto ARIMA**, which selected:

```
ARIMA(0,1,0)
```

The forecasting model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

---

### Task 3 – Future Forecasting

The trained ARIMA model generated a 12-month forecast for Tesla stock prices.

Forecast visualization includes:

- Historical prices
- Future predictions
- 95% confidence intervals

The widening confidence intervals demonstrate increasing uncertainty over longer forecasting horizons.

---

### Task 4 – Portfolio Optimization

Portfolio optimization was performed using **PyPortfolioOpt**.

Steps:

- Estimated expected returns
- Computed covariance matrix
- Generated Efficient Frontier
- Identified:
  - Maximum Sharpe Ratio Portfolio
  - Minimum Volatility Portfolio

Portfolio performance metrics include:

- Expected Annual Return
- Portfolio Volatility
- Sharpe Ratio

---

### Task 5 – Backtesting

The optimized portfolio was compared against a benchmark portfolio consisting of:

- **60% SPY**
- **40% BND**

Performance metrics include:

- Total Return
- Annual Return
- Sharpe Ratio
- Maximum Drawdown

A cumulative return comparison plot was used to evaluate strategy performance.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- statsmodels
- pmdarima
- PyPortfolioOpt
- scikit-learn

---

## Results

Key findings include:

- Tesla exhibited significantly higher volatility than SPY and BND.
- Closing prices were non-stationary, while daily returns were stationary.
- Auto ARIMA selected an ARIMA(0,1,0) model based on the lowest AIC.
- Portfolio optimization favored diversification to maximize the Sharpe Ratio.
- The optimized portfolio was evaluated against a traditional balanced benchmark using historical backtesting.

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```
notebooks/01_data_preprocessing_and_eda.ipynb
```

---

## Repository

This repository contains:

- Data preprocessing
- Exploratory data analysis
- Time series forecasting
- Portfolio optimization
- Portfolio backtesting

developed as part of the GMF Investments Portfolio Optimization Challenge.