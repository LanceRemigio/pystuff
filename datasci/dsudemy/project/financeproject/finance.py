from pandas_datareader import data, wb
from datetime import datetime
# import pandas_datareader as pdr
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import os
# setting start and end datetime objects

df = pd.read_pickle('all_banks')
# data = data.DataReader(y_symbols, start, end)




tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# print( df.xs(key = 'Close', axis = 1, level = "Stock Info")['BAC'])

returns = pd.DataFrame()

for ticker in tickers:
    returns[ticker + ' Returns'] = df[ticker]['Close'].pct_change()

print(returns.head())

# sns.pairplot(returns)



plt.show()



# print(
#         df.xs('Bank')
#         )


# print(maxClosePrice)

# data = pdr.get_data_yahoo(tickerList, start, end)


# print(df.head())




