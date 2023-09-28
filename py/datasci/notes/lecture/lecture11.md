# DataFrames Part 3

- Multiple index
- index hierarchy

## Index Levels

Suppose we have the following code that is set up for making a random data frame. This sets up the indices for the data frame. Note that understanding this code is not that important right now.

````python
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
````

To set up the data frame, we need to type the following code:
````python
df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])
````
which returns
````
             A         B
G1 1  0.346072  0.809253
   2  0.113898  1.493420
   3 -1.043341 -0.378519
G2 1  0.059164  0.614241
   2  0.728681 -1.185233
   3 -0.897470  0.340756
````

We can grab sub-data frames by passing in the outer-most index into the bracket notation. 
````python
df.loc['G1']
````
which returns
````
          A         B
1 -1.403003  0.633053
2 -0.058977 -1.092689
3 -1.590239  0.100552
````

We can grab values within this sub-data frame by using the `loc` function again. Suppose we grab the first row. Typing
````python
df.loc['G1'].loc[1]
````
which returns the following series:
````
A    1.097556
B    0.355663
Name: 1, dtype: float64
````

If we type `df.index.names`, we will see that our outer-most indices are not named; that is, the output will return  
````
[None, None]
````


We can rename our indices by assigning the `df.index.names` to a list. 

````python
df.index.names = ['Groups', 'Num']
````

Grabbing values from our data frame follows the syntax structure below:
````python
data_frame.loc['outer-most'].loc['row']['column']
````


## Cross Sections

We can grab both sections of a data-frame by cutting into the dataframe using the `xs` function, specifiying the row we want to grab, and specifying the level. In other words, we should have the following code:
````python
df.(row_grab, level = 'name of column')
````
For example, if we want the first row of both sub-data frames of the following data-frame 
````
df = 
             A         B
G1 1  0.384680  1.497211
   2 -1.299449 -0.032950
   3  0.513747 -2.422435
G2 1  0.368893  0.026358
   2 -0.014966 -1.088581
   3  0.121241 -0.601243
````
Then we would need to type the following code:
````python
df.xs(1, level = 'Num')
````
to get
````

````

