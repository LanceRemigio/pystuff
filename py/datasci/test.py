import numpy as np
import pandas as pd
from numpy.random import randn



np.random.seed(101)

row_index = ['A', 'B', 'C', 'D', 'E']
col_index = ['W', 'X', 'Y', 'Z']
df = pd.DataFrame(randn(5,4), row_index, col_index)
print(df)


