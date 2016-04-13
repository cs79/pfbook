#
# Example technical analysis using pandas
# tech_analysis_ex.py
#

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from __future__ import division

sp500 = web.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', \
    end='4/14/2014')

# generate 2-month and 1-year time series trend data
# need to refactor vs book to accommodate updated syntax
sp500['42d'] = sp500['Close'].rolling(window=42).mean().round(2)
sp500['252d'] = sp500['Close'].rolling(window=252).mean().round(2)
sp500['42-252'] = sp500['42d'] - sp500['252d']

# simple signal regime
SD = 50  # assumed signal value level; could grid search a more optimal one
sp500['Regime'] = np.where(sp500['42-252'] > SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252'] < -SD, -1, sp500['Regime'])
sp500['Regime'].value_counts()
sp500['Regime'].plot(lw=1.5)
plt.ylim([-1.1, 1.1])

# backtest
sp500['Market'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Regime'].shift(1) * sp500['Market']  # regime returns

# visualize cumulative continuous (not log) returns from long-only vs. strategy
sp500[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True, \
    figsize=(8, 5))
