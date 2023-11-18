# from pandas_datareader import data, wb
from datetime import datetime
# import pandas_datareader as pdr
import pandas as pd
# import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# import yfinance as yf
# import os
# setting start and end datetime objects
sns.set_style('whitegrid')
df = pd.read_pickle('all_banks')

# data = data.DataReader(y_symbols, start, end)

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

# print( df.xs(key = 'Close', axis = 1, level = "Stock Info")['BAC'])


returns = pd.DataFrame()


for ticker in tickers:
    returns[ticker + ' Returns'] = df[ticker]['Close'].pct_change()


# closePrice = df.xs(key = 'Close', axis = 1, level = "Stock Info")
# closePriceBAC = df.xs(key = 'Close', axis = 1, level = "Stock Info")['BAC'].loc['2008']
# closePriceBAC = df.xs(key = 'Close', axis = 1, level = "Stock Info")['BAC'].loc['2015']
# closePriceBAC = df.xs(key = 'Close', axis = 1 , level = 'Stock Info')['BAC'].loc['2008']
closePrice = df.xs(key = 'Close', axis = 1 , level = 'Stock Info')
closePriceBAC = df.xs(key = 'Close', axis = 1 , level = 'Stock Info')['BAC'].loc['2008']
rollingAvg = closePriceBAC.rolling(30).mean()

sns.clustermap(data = closePrice.corr(), annot = True)
plt.savefig('./plots/clustermapClosePrice.png')

# part 2 (Optional)

# dataBAC = df['BAC'].loc['2015': '2016']
# dataBAC.iplot(kind = 'candle')
# dataMS = closePrice['MS'].loc['2015']
# dataMS.ta_plot(study = 'sma')
# dataSMA = df['BAC'].loc['2015']
# dataSMA.ta_plot(study = 'sma')
# dataSMA.iplot(study = 'boll')

# -- plots -- 

# sns.heatmap(data = closePrice.corr(), annot = True)
# sns.clustermap(data = closePrice.corr(), annot = True)





# sns.lineplot(data = closePriceBAC)
# sns.lineplot(data = rollingAvg)
# plt.savefig('./plots/clustermapClosePrice.png')
plt.show()


# sns.displot(data = returns['MS Returns'].loc['2015'], kde = True, bins = 60)


# sns.displot(data = returns['C Returns'].loc['2008'], kde = True, bins = 50)


# plt.show()


# print(
#         df.xs('Bank')
#         )


# print(maxClosePrice)

# data = pdr.get_data_yahoo(tickerList, start, end)


# print(df.head())




