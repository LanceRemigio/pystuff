# Group By

- Groupby allows to group all the rows of a column of data and outputs a single row with a single value using some aggregate function.

- We are going to learn how to use `Groupby` using `Pandas` 


Suppose we type the following code below: 
````python
import numpy as np
import pandas as pd
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]
}
df = pd.DataFrame(data)
````
which returns the data frame below

````
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
````

We can group rows together by some column name using the `groupby` function in pandas.

We can pass in the the column name of data we want to aggregate in the following way:
````python
byComp = df.groupby('Company')
````
We can use the `mean` function to aggregate the values found in the rows of the `Company` column in the following way:
````python
compMean = byComp.mean()
````
which returns the following data frame:
````
         Sales
Company       
FB       296.5
GOOG     160.0
MSFT     232.0
````

We can do `sum()` on the groupbys by typing the following:
````python
le_sum = df.groupby('Company').sum()
````
We can also describe the table by using the `describe()` method to show all the relevant information about the data.
````python
byComp = df.groupby('Company').describe()
````
which will return the following data frame:
````
        Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
````


