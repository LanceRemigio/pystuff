# DataFrames Part 2 

Topics:
- Conditional Selection
- Multi index parts of a data frame

## Conditional Selection

To grab parts of a data frame that satisfies a condition, we can first create a data frame of booldean values; that is,
````python
mybool = df['W'] > 0 
````
Suppose we pass this into our data frame with the bracket notation
````python
df[mybool] 
````
which will return the following data frame
````
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
````
Notice how the `C` row is not included based on our condition. Suppose we wanted to select another column based on another condition. Let's suppose we want pass in the column `Z`  and pass in the condition with values that are less than 0.
````python
df[df['Z'] < 0]
````
which returns a singular row
````
          W         X         Y         Z
C -2.018168  0.740122  0.528813 -0.589001
````

We can select multiple columns where a specific condition is met. To do this, we can type 
````python
result = df[df['W'] > 0 ][ ['Y', 'X'] ]

````
which returns the following data frame
````
          Y         X
A  0.907969  0.628133
B -0.848077 -0.319318
D -0.933237 -0.758872
E  2.605967  1.978757
````

The first bracket contains a series of boolean values that is linked to each row in the column `W`. The second bracket contains the list of columns we want to look at where this condition is true.


## Multiple Conditions

We can use comparison operators to combine conditions together. Suppose we want to grab the part of our data frame that contains values that are greater than 0 in the `W` column AND greater than 1 in the `Y` column. We can do this by typing the following code:
````python
df[(df['W'] > 0 ) &  (df['Y'] >  1)]
````
which returns
````
          W         X         Y         Z
E  0.190794  1.978757  2.605967  0.683509
````

Note that if we passed in `and` instead of `&` we will get an error saying that the comparison between two boolean values when looking at two series is ambigious. If we wanted to use `or`, then we would just need to use the `|` operator.



## Indices

We can reset indices by taking the letters that we specified for rows in our data frame and create a new column that stores those values and have index be in terms of integers instead. We can do this by typing
````python
df.reset_index()
````
To make these changes permanent, just pass in `inplace = True`.

Another way we can modify indices so that we may overrite our originla index is to create a list and pass in that list into the `set_index` function; that is, we have  
````python
newind = 'CA NY WY CO'.split()
df['States'] = newind
df.set_index('States', inplace = True) # set inplace = True to make changes permanent
````
which returns
````
               W         X         Y         Z
States                                        
CA      2.706850  0.628133  0.907969  0.503826
NY      0.651118 -0.319318 -0.848077  0.605965
WY     -2.018168  0.740122  0.528813 -0.589001
OR      0.188695 -0.758872 -0.933237  0.955057
CO      0.190794  1.978757  2.605967  0.683509
````


