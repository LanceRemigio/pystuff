# Lecture 7: Numpy Operations

- Array with Array 
- Array with Scalars
- Universal Array Functions


## Array with array operations

We can add two arrays together. First let us make the following array: 
````python
import numpy as np
arr = np.arange(0,11) # returns an array with the first 11 numbers starting from 0
````
Adding arrays together involve simply add `arr` to itself by using element by element basis; that is, we have
````python
arr + arr
````
We can also perform all our common operations `+,-,*,/` and numpy will perform them on an element by element basis.

## Array Operations With Scalars 

Array operations with scalars is simple. We can just take any array like the one we defined above and do any operation we wish by typing 
````python
arr + some_scalar 
````
which will add each element in the array in the scalar and return the result of the new array.

Note that if we try to divide `arr` by itself then we would receive a warning telling us that a division by zero has occured (in this case in the 0 index). Numpy will still print the array, but instead of a number in the first index of the array, we have a `Nan`. Similarly, if try to divide 1 by `arr` itself, then would receive a warning from numpy telling us that we can't divide by zero. Hence, the code
````python
1 / arr
````
will return the elements after performing the indicated operation but this time with `inf` as the first element of the array.

We can also square each element in an array by typing:
````python
arr ** 2
````

## Universal Operations with Arrays

Some universal operations we can perform with arrays using numpy are:
- `np.sqrt(arr)` 
- `np.exp(arr)`
- `np.max(arr)` which is equivalent to `arr.max()`
- `np.log(arr)` 
- `np.sin(arr)`
- `np.cos(arr)`
- and so on

