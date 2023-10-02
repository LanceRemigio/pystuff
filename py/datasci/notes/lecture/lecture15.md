# Operations


## Uniqueness

Suppose we have the following data frame
````python
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()
````
which outputs the following data frame
````
   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
````
We can tell python to print out the unique values of the data frame above by typing 
````python
df['col2'].unique()
````
which returns a list of the unique values in `col2`; that is, 
````
[444 555 666]
````
To get the number of unique values in a row, we can use the `nunique` function. An example of this is the following:
````python
df['col2'].nunique()
````
which outputs the `3` which is what we expected. 

With the `value_counts()` function, can pass in the column we want to look at and return a series showing, with each row assigned to each value in the column, the number of times each value pops up in the column. We can do this by typing the following: 
````python
df['col2'].value_counts()
````

## Selecting Data

We can use conditional and logical operators to select certain data meeting some criteria from multiple columns in a data frame. Suppose we typed the following  
````python
newdf = df[( df['col1'] > 2 ) & ( df['col2'] == 444 )]
````
which should just return singular row where those conditions are valid
````
   col1  col2 col3
3     4   444  xyz
````

## Applying Functions

We can use the `apply()` function along with either functions or lambda functions and appy them to our analysis of data frames. Suppose we had the following function:
````python
def times2(x):
    return x*2
````
which returns every value that is passed onto this function multiplied by 2. Suppose we want to apply this function to a column 1 to our example data frame `df`. Then all we need to do is type the following:
````python
df['col1'].apply(times2)
````
which will return a time series with all the values in column 1 but multiplied by 2:
````
0    2
1    4
2    6
3    8
Name: col1, dtype: int64
````
We can apply any function we want to the `apply()` function. We can also shorten the above code by using lambda functions instead. This can be done in the following way: 
````python
df['col1'].apply(lambda x: x*2)
````


## Permanently Removing a Column

We can do this by typing:
````python
del df['col1']
````


## Get Column and Index names:
We can get all the columns returned in a list using the `columns` method
````python
df.columns
````

````
Index(['col1', 'col2', 'col3'], dtype='object')
````
In the same way, we can return a list of indices from the data frame and its step size.

````python
df.index
````
````
RangeIndex(start=0, stop=4, step=1)
````


## Sorting and Ordering a DataFrame
We can sort values in ascending order (similar to group by in SQL) by using the `sort_values()` function 

df.sort_values('col2')
````
which returns the following DataFrame with the indices of the values preserved
````
   col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  def
2     3   666  ghi
````

## Finding Null Values or Check for Null Values

We can output a DataFrame which returns boolean values in each row, showing us where we have null values in our DataFrame:

````python
df.isnull()
````

which returns the following:
````
    col1   col2   col3
0  False  False  False
1  False  False  False
2  False  False  False
3  False  False  False
````
We can also drop rows with NaN values such as the following:
````python
df.dropna()

````

## Filling in NaN values with something else

Suppose we created the following DataFrame:
````python
df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
````

Note that we can see that there are missing values in the 4th row of `col1` and in the 1st row of `col2` . We can fill in these missing values by using the `fillna` function:
````python
df.fillna('FILL')
````
which returns the following DataFrame:
````
   col1   col2 col3
0   1.0   FILL  abc
1   2.0  555.0  def
2   3.0  666.0  ghi
3  FILL  444.0  xyz
````

## Pivoting Tables
Suppose we have the following DataFrame:
````python
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
````


We can use the methods such pivoting tables from excel in pandas as well. We can do this by typing the following:
````python
df.pivot_table(values = 'D', index =  ['A', 'B'], columns =  ['C'])

````
This rearranges indices of the above DataFrame in terms of `A` and `B` (the values of each row are used as indices) and uses the values of the `D` column to fill in the values in the `x` and `y` columns. 

