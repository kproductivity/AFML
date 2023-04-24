import mplfinance as mpf
import pandas as pd


def plot_candlestick(x: pd.DataFrame):
    mpf.plot(x, type='candle', mav=(3, 6, 9), volume=True, show_nontrading=True)


def plot_intraday(x: pd.DataFrame):
    mpf.plot(x, type='bars', volume=True, mav=(20, 40))
