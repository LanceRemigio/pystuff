import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')



df1 = pd.read_csv('df1', index_col = 0)
df2 = pd.read_csv('df2')

df2.plot.bar()


plt.show()
