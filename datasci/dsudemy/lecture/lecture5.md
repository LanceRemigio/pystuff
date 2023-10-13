# Intro to Numpy 


## NumPy Arrays

We can create an array by creating a list and using numpy to cast it as an array by using the following 
````python
my_list = [1,2,3]
arr = np.array(my_list)
print(arr) # prints out the array
````

We can create matrices by using a list of list and casting it as an array using numpy

````python
my_mat = [[1,2,3], [4,5,6], [7,8,9]]
np.array([[1,2,3], [4,5,6], [7,8,9]])
````
## arange

We can use the numpy function `arange` to create a list using a range of values that we can specify; that is, we can have the following syntax
````python
np.arange(0,11)
print([0,1,2,3,4,5,6,7,8,9,10])
````
The first two arguments specify the range and the endpoint is exclusive.
We can add a third argument to `arange` to specify the step size of each number in the list. For example, if we have `np.arange(0,11,2)`, then the computer will return the following list
````
[0,2,4,6,8,10]
````
## zeros
We can generate an array of zeroes by using the `zeros` function. Typing `np.zeros(3)` returns an 1d array with 3 zeroes in it. We can also make a m by n dimensional array by typing, for example, `np.zeros(2,3)` to get  
````
array([0., 0., 0.,],
      [0., 0., 0.,])

````
## ones
Likewise, we can generate an array of ones using the same logic as above but with the function `ones` instead. 

## Linspace

With `linspace`, we can specify the beginning points and endpoints in the first two arguments of our function and then specify how many points we want in total in the third argument. This creates an array of values within a certain range with an `n` amount of numbers. This is not to be confused with `arange` where we specify the step size of our values.


## Identity matrices

We can generate a diagonal square matrix with all ones in the diagonal by using the `eye` function. The syntax is as follows:
````python
np.eye(n) # where n is the number of ones in the diagonal
# if n= 4, then we get a 4 by 4 array with 4 ones down the diagonal
````
## Creating random arrays

### random.rand()
We can create a random array with the following syntax
````python
rand()
````
This returns an array of random `n` numbers. We can also create a matrix of random values by specifying a second argument, indicating the number of columns we want. 

### randn()

The `randn()` function creates a random array of numbers from a standard distribution (the Gaussian Function). Again, we can create a matrix using a second argument.

### randint()

We can also create a random array with just integers by using the `randint` function. We can specify the left and right endpoints with inclusive and exclusive respectively for the first two arguments and the amount of numbers you want in the array in the third.

Suppose we generate a random array of numbers with the following code:
````python
arr = np.arange(25)
````
and want to reshape our array into a 5x5 matrix, we can type the following code:
````python
print(arr.reshape(5,5)) 
````
Note that this will throw off an error if the number of columns times the number of rows does not return the same dimension as the one dimension array.

## Max and min of arrays

We can grab the max number of an array by typing the following code:
````python
anarray.max()
````
Similarly, we can return the min number of an array by typing:
````python
anarray.min()
````

We can grab the index location of the max and min respectively by typing 
````python
anarray.argmax() # grabs index location of maximum value
anarray.argmin() # grabs index location of minimum value
````


## Getting the shape of a vector/array

`arr.shape` returns the dimensions of the array.

## Dtype

`arr.dtype` returns the data type of an array.


## Shorthand stuff

Instead of using the long winded expression `np.random.randint` we can instead use the following import statement
````python
from numpy.random import randint
randint(2,10)
````
so we can just use the function directly.
