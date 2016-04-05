# ticker data fetch and plot

# imports
import numpy as np
import pandas as pd
import pandas.io.data as web

# retrieve ticker data
goog = web.DataReader('GOOG', data_source = 'google', start='3/14/2009', end='4/14/2014')

# analytics
goog['log_ret'] = np.log(goog.Close / goog.Close.shift(1))
goog['volatility'] = pd.rolling_std(goog.log_ret, window=252) * np.sqrt(252)

# visualize
goog[['Close', 'volatility']].plot(subplots = True, color='blue', figsize = (8,6))
