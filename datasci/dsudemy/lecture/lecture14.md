
# Merging, Joining, and Concatenating

Suppose we have the following data frames

````python
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    }, 
                     index = [0,1,2,3]
)

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


````

which returns the following data frames respectively

````
df1 = 
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
````


```` 
df2 = 
    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
````

````
     A    B    C    D
0   A8   B8   C8   D8
1   A9   B9   C9   D9
2  A10  B10  C10  D10
3  A11  B11  C11  D11
````


## Concatenation 

Concatenation involves combining pieces of data frames together. Make sure the data frames have match dimensions and that they match along the axis you are trying to concatenate on. You can concatenate two data frames together using the `concat` function found in pandas. Using our data frames from above, we can type the following:
````python
pd.concat([df1, df2, df3])
````
which returns

````
     A    B    C    D
0   A0   B0   C0   D0
1   A1   B1   C1   D1
2   A2   B2   C2   D2
3   A3   B3   C3   D3
4   A4   B4   C4   D4
5   A5   B5   C5   D5
6   A6   B6   C6   D6
7   A7   B7   C7   D7
0   A8   B8   C8   D8
1   A9   B9   C9   D9
2  A10  B10  C10  D10
3  A11  B11  C11  D11
````

We can also concatenate using the columns of the data frames. We can do this by specifying `axis = 1 ` when we pass in the arguments into the concat function. 
````python
pd.concat([df1, df2, df3], axis = 1 )
````
which returns the followin data frame
````
      A    B    C    D    A    B    C    D    A    B    C    D
0    A0   B0   C0   D0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
1    A1   B1   C1   D1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2    A2   B2   C2   D2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
3    A3   B3   C3   D3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4   NaN  NaN  NaN  NaN   A4   B4   C4   D4  NaN  NaN  NaN  NaN
5   NaN  NaN  NaN  NaN   A5   B5   C5   D5  NaN  NaN  NaN  NaN
6   NaN  NaN  NaN  NaN   A6   B6   C6   D6  NaN  NaN  NaN  NaN
7   NaN  NaN  NaN  NaN   A7   B7   C7   D7  NaN  NaN  NaN  NaN
8   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A8   B8   C8   D8
9   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A9   B9   C9   D9
10  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A10  B10  C10  D10
11  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11
````

## Merging

We can merge DataFrames together by using similar methods found in SQL. For example, we can merge two data frames together, called `left` and `right`, by typing the following code:
````python
pd.merge(left, right, how = 'inner', on = 'key')
````
where 
````python
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
````

````
left = 
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3
````

and

````
right = 
  key1 key2   C
0   K0   K0  C0
1   K1   K0  C1
2   K1   K0  C2
3   K2   K0  C3
````



Then we would have the following merged data frame:
````
  key1 key2   A   B   C
0   K0   K0  A0  B0  C0
1   K1   K0  A2  B2  C1
2   K1   K0  A2  B2  C2

````

As we can see, the merging along an `inner` join takes grabs the keys where the two data frames match. In this case, we have `K0 K0` and `K1 K0` are the only set of keys that match. 

## Joining

We can also join two dataframes together by using the `join` function. Suppose we have the following two dataframes
````python
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
````
If we want to join `left` and `right` together, they all we have to do is type the following:
````python
left.join(right)
````
Keep in mind that the default for how we would join the two tables together is set to `inner`. This would return the following dataframe:
````
     A   B    C    D
K0  A0  B0   C0   D0
K1  A1  B1  NaN  NaN
K2  A2  B2   C2   D2
````

Note that we are only using the first three rows of the `left` data frame to join the `right` data frame together. Hence, when we get to the keys `K1`, we won't have any values because `right` didn't have any values specified there. This is the difference between `join` and `merge`. When we use `join` we glue data frames together without having to match anything but if we use `merge` then we do.  
