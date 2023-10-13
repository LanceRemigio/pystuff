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
## Grabbing columns

To grab the column of a data frame, we can use the bracket notation and pass in the name of the column of the data we want to grab: 
````python
df = pd.DataFrame(randn(5,4), row_index, col_index)
col_w = df['W']
````
which returns the following series
````
A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64
````
To get the a list of columns, we can pass in a list of columns we want. Suppose we want columns `W` and `Z`, then we would simply pass in a list containing both `W` and `Z`; that is,
````python
df[['W','Z']] 
````
which returns the following data frame
````
          W         Z
A  2.706850  0.503826
B  0.651118  0.605965
C -2.018168 -0.589001
D  0.188695  0.955057
E  0.190794  0.683509
````

## Adding Columns 

To add columns, we would simply pass in column we want to create (as if if already exists) and assign the values in that column; that is, 
````python
df['new'] = df['W'] + df['Y']
````
which returns
````
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.614819
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
C -2.018168  0.740122  0.528813 -0.589001 -1.489355
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
E  0.190794  1.978757  2.605967  0.683509  2.796762
````

## Dropping Columns

If we want to drop columns, we need to pass in `axis = 1` and the column we want to drop into the `drop` function. In addition, we need to add the `inplace = true` argument to actually have any changes to your data frame. We can see this in the following:
````python
df.drop('new', inplace = True)
````
This is important because we want to drop columns without accidently losing information.

## Dropping Rows 

Remember that the default argument for the axis argument in the `drop` function is 0. The syntax is as easy as passing the name of the row in; that is, 
````python
df.drop('E')
print(df)
````

## Shape of data frames

We can find the shape of a data frame by just typing the following:
````python
df.shape
````

## Selecting Multiple Columns

We can select multiple columns by passing in a list of the names of the columns using the bracket notation; that is, 
````python
df[['Z', 'X']]
````

## Selecting Multiple Rows

We can use the method `loc` to select the a row from a data frame
````python
df.loc['A']
````
which returns
````
W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64
````
Notice that if we select a singular row or column, all we get back is a series. Another way to select rows is to pass in the integer index using the `iloc` method. For example, we have
````python
df.iloc[2]
````

To select multiple rows or subsets of the data frame, we can pass in a list of rows into the `loc` function. For example, in our data frame we have
````python
df.loc[['A', 'B'], ['W', 'Y']]
````



