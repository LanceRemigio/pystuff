# Data Frames

This is going to be our main tool when working with pandas.

##

First we need to import our modules:

````python
import numpy as np
import pandas as pd
from numpy.random import randn
````

Suppose we have the following lines of code:
````python
np.random.seed(101)
row_index = ['A', 'B', 'C', 'D', 'E']
col_index = ['W', 'X', 'Y', 'Z']
df = pd.DataFrame(randn(5,4), row_index, col_index)
print(df)
````

````
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
````


