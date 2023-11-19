from pandas_datareader import data, wb
import datetime  
import pandas as pd
# import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# sets the style of the seaborn plots
sns.set_style('whitegrid')

# Creating start time and end time
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# create the keys for the our new dataframe
tickers = ['BAC', 'MS', 'C', 'WFC', 'GS' , 'JPM' ]

# Reading in and storing each bank's stock data in a list
listOfBanks = [data.DataReader(item, 'stooq', start, end) for item in tickers] 

# concatenating the dataframes together into one
bank_stocks = pd.concat(listOfBanks , axis = 1 , keys = tickers)

bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

closePrice = bank_stocks.xs(key = 'Close', axis = 1 , level = 'Stock Info' ).max()

# creates a new data frame based on the stock returns of each bank
returns = pd.DataFrame()

for ticker in tickers:
    returns[ticker  + ' Returns'] = bank_stocks[ticker]['Close'].pct_change()




# prints the head of the dataframe
# print(
#         bank_stocks.head(5)
#         )

# Max Close Price for each bank's stock throughout the time period

# print(
#         closePrice.max()
#         )






