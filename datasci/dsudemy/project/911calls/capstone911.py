import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')



df['Reason'] =  df['title'].apply(lambda x: x.split(':')[0])

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
       
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)

df['Month'] = df['timeStamp'].apply(lambda x : x.month)

df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

dmap = {
        0:'Mon',
        1:'Tue',
        2:'Wed',
        3:'Thu',
        4:'Fri',
        5:'Sat',
        6:'Sun'
        }

df['Day of Week'] = df['Day of Week'].map(dmap)



df['Date'] = df['timeStamp'].apply(lambda x: x.date())

print(df['Reason'].value_counts())

# sns.countplot(data = df, x = 'Reason')






# groupByDay = df.groupby(by = ['Day of Week', 'Hour']).count()['Reason'].unstack() # didn't know you could groupby two columns
# sns.heatmap(groupByDay)
# sns.clustermap(groupByDay)

# groupByMonth = df.groupby(by = ['Day of Week', 'Month']).count()['Reason'].unstack()
# sns.heatmap(groupByMonth)
# sns.clustermap(groupByMonth)

# print(df[['Day of Week', 'Hour']].unstack())
# print(df[['Day of Week', 'Hour']].head())

# print(df[['Day of Week', 'Hour']].unstack(level = 0).groupby('Hour'))





# print(df[['Day of Week', 'Hour']])

# print(df[['Day of Week', 'Hour']].unstack(level = 0))

plt.show()
