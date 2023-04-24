import numpy as np
import pandas as pd
import plotly.graph_objs as go
import yfinance as yf


def pcaWeights(cov, riskDist=None, riskTarget=1) -> Vect:
    """
    Compute hedging weights based on principal components
    :param cov: covariance of returns
    :param riskDist: user-defined risk distribution; if None, allocates to principal component
    :param riskTarget: sigma, risk target
    :return: vector of weights
    """
    eVal, eVec = np.linalg.eigh(cov)
    indices = eVal.argsort()[::-1]
    eVal, eVec = eVal[indices], eVec[:, indices]

    if riskDist is None:
        riskDist = np.zeros(cov.shape[0])
        riskDist[-1] = 1

    loads = riskTarget*(riskDist/eVal) ** .5
    wghts = np.dot(eVec, np.reshape(loads, (-1, 1)))
    ctr = (loads/riskTarget)**2*eVal

    return wghts


def get_data(tickers: str = 'MSFT', period: str = '5d', interval: str = '5m') -> pd.DataFrame:
    data = yf.download(tickers=tickers, period=period, interval=interval)
    return data
