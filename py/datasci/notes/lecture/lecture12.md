# Missing Data

We can use pandas to fill in values that are missing from a table.


Suppose we create the following dictionary
````python
d = {'A': [1,2,np.nan], 'B': [5, np.nan, np.nan], 'C': [1,2,3]}

and create the following data frame using pandas
````python
df = pd.DataFrame(d)
````
which creates
````
````
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3



## Dropping NULL values
````
Let's suppose that we want to drop our NULL values. Then we would simply just type the following
````python
df.dropna()
````
and get
````
     A    B  C
0  1.0  5.0  1
````
Note that the function `dropna()` has a default argument of `axis = 0` (meaning the rows). To perform the action based on the columns instead of the rows, we can specify the following argument `axis = 1`.


We can also specify a threshold on the amount of NA values we would like to keep. In other words, we can specify an argument to limit the amount null values we have in our data frame. We can do this by typing the following code
````python
df.dropna(thresh = 2)
````
which specifies that we want to have an upper bound (that is exclusive) of a total of 2 NULL values in our data frame.

## Filling in NULL Values

We can fill in NULL values of a data frame by using the `fillna` function. We can do this triviallyby passing in a string called 'FILL VALUE' (this can be an integer as well): 
````python
df.fillna(value = 'FILL VALUE')
````
and returns
````
            A           B  C
0         1.0         5.0  1
1         2.0  FILL VALUE  2
2  FILL VALUE  FILL VALUE  3

````
We can also fill in NULL values by assigning the mean of the data frame. We can do this by typing the following code
````python
df['A'].fillna(value = df['A'].mean())
````
which will return the output below:
````
0    1.0
1    2.0
2    1.5
Name: A, dtype: float64
````




