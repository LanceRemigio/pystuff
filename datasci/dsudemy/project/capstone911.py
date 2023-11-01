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

# byMonth =  df.groupby('Month')['twp'].count()

df['Date'] = df['timeStamp'].apply(lambda x: x.date())


byDateEMS = df[df['Reason'] == 'EMS'].groupby('Date')['twp'].count() 
sns.lineplot(data = byDateEMS)
plt.title('EMS')



plt.show()
