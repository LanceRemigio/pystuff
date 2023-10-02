import numpy as np
import pandas as pd
from numpy.random import randn
from sqlalchemy import create_engine



# data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
# print(data[0].head())

df = pd.read_csv('example')
print(df)

engine = create_engine('sqlite:///:memory:')

df.to_sql('df',con = engine)

sql_df = pd.read_sql('df', con=engine)







print(sql_df)
