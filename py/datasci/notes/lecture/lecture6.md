# Lecture 5


- Basic indexing 
- Indexing a 2d array
    - grabbing sub-matrices
- Conditional selection



## Basic indexing

We can grab elements from an array the same way we would do it for a list. Simply use the splicing notation like the following `arr[i]` where `i` is the index the element is stored at. If we want to grab a list of values then we could just specify the start index and the end index like the following:
````python
arr = np.arange(0,11) 
print(arr[1:5]) 
````
which will return the array
````
[1,2,3,4]
````
If we want to grab every element from a list up to a specific point, then we would just need to specify the end point since the default argument for the left endpoint is just 0. That is, we have
````python
print(arr[:6])
````
which will gives us the following array
````
[0,1,2,3,4,5]
````
The opposite is true if we want to start at the left endpoint and grab everything after up to the end of the string; that is, 
````python
print(arr[5:]) # starts from index 5 up to end of the list
````
We can also reassign multiple elements at once with the following syntax:
````python
arr[0:5] = 100 # returns an array with the first 5 elements assigned to 100
````
Suppose we took a slice out of our original array. Then the following syntax 
````python
slice_of_arr = arr[0:6] 
````
will return the first 6 elements of the array `arr`.

Suppose we grab every element in that slice and assigned each element to 99. Then we would have 
the following array:
````python
[99,99,99,99,99,99]
````
but when we try to call back the original array `arr` then we would see that the first 6 elements are assigned to the value 99. Note that this doesn't create a copy of the original array. We are merely viewing what the array looks like.

In the event that we do want to have the copy of `arr`, what we can do is use the `copy` method to copy the array: 
````python
arr_copy = arr.copy()
````
If we want to reassign all the elements of this array, then we would need to do the following:
````python
arr_copy[:] = 100
````
But note that instead of changing the elements of the original array, the original array `arr` and its elements are preserved and are not changed. 



## Indexing a 2d array

Suppose we create the following array:
````python
arr_2d = np.array([[5,10,15], 
                  [20,25,30],
                  [35,40,45]]
                  )
````
We can grab the elements using the double bracket method way or the bracket comma method.
If we take the first element of this array, then we would just need to type:
````python
arr_2d[0]
````
which returns the first array of `arr_2d`. If we want the first element of that array, then we would type:
````python
arr_2d[0][0]
````
Using the bracket-comma method, we can write this down as follows:
````python
arr_2d[0,0]
````

## Grabbing sub-matrices matrix
Suppose we have the following array:
````python
arr_2d = np.array([[5,10,15], 
                  [20,25,30],
                  [35,40,45]])
````
We can use the slice notation to do this. Using the same array `arr_2d` again, we can grab sub-matrices `[10, 15], [25, 30]`. We can do this by typing the following:
````python
print(arr_2d[:2, 1:]) 
````
If we just want the first two arrays, we would just need to type the following:
````python
print(arr_2d[:2])
````
which would return `[5,10,15]` and `[20,25,30]`.


## Conditional selection

Suppose we create the following array:
````python
arr = np.arange(1,11)
````
which would return the array
````python
[1,2,3,4,5,6,7,8,9,10]
````
We can create an array of boolean values by typing the following
````python
bool_arr = arr > 5 
````
and casting it into our bracket notation to grab and return an array with all the values that meet the condition above. Hence, we would just have
````python
print(arr[bool_arr])
````
and have
````python
[6,7,8,9,10]
````
We can shorten the above by just typing 
````python
print(arr[arr>5])
````





