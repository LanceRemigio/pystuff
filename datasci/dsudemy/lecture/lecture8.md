# Intro to Pandas

## Topics
- Series 
- DataFrames
- Missing data
- GroupBy
- Merging, Joining, and Concatenating
- Operations
- Data Input and Output


## Series

Similar to a numpy array but contains access labels; that is, it can be accessed by a label.

Importing the module is as easy as the following:
````python
import pandas as pd
````

Consider the following:

````python
labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
````

The `Series` function creates a table that creates a link between data and associated labels. It takes in either an array, list, or a dictionary as its first and second argument. The second argument creates the label linking to its associated data values. We can create a series by typing the following:
````python
a_table = pd.Series(data = my_data, index = labels)
````
This creates the following output

````
a    10
b    20
c    30
dtype: int64
````

If we  have a dictionary, then we would just need to pass in the dictionary. Keep in mind that the default argument for the second parameter will be a list of `n` numbers starting from 0. So we have
````python
table_2 = pd.Series(d)
````
which will have an output of 
````
a    10
b    20
c    30
dtype: int64
````
We can access data from a series by using the bracket notation (the same way we access a regular list). We can pass in either a string or an int (depending on the data type of our label) to access the data. Say we want to access 30 from the series above. Then we would just need to pass in the string "c" to access 30; that is, 
````python
table_2["c"]
````
We can also do operations with series. Suppose we have the following two series 
````
-> ser1  
USA        1
Germany    2
USSR       3
Japan      4
dtype: int64
-> ser2
USA        1
Germany    2
Italy      5
Japan      4
dtype: int64
````

When trying to add `ser1` and `ser2`, python will try to add the two series element-wise. But notice that we can't add both `USSR` and `Italy` since they do not have matching labels. Hence, we will have the resulting series 
````
Germany    4.0
Italy      NaN
Japan      8.0
USA        2.0
USSR       NaN
dtype: float64
````
which leaves `Italy` and `USSR` with Nan values.

Another interesting characteristic of the Series function is that it can also store values that are built-in functions. For example, we can pass in the following arguments
````python
ser_func = pd.Series([len, sum], [0,1])
````
and returns the follwoing series
````
0    <built-in function len>
1    <built-in function sum>
dtype: object
````
