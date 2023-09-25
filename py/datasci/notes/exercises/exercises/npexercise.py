import numpy as np
# from numpy.core.multiarray import array


# Create an array of 10 zeros

# arrzero = np.zeros(10)
# print(arrzero)

# Create an array of 10 ones

# arrones = np.ones(10)
# print(arrones)

# Create an array of 10 fives

# arrfives = arrones * 5
# print(arrfives)

# Create an array of the integers from 10 to 50

# arr = np.arange(10,51)
# print(arr)

# Create an array of all even integers from 10 to 50

# arr_even = arr[arr %2 == 0]
# or we could do 
# arr_even = np.arange(10,51,2) third argument is step size
# print(arr_even)


# Create a 3x3 matrix with values ranging from 0 to 8

# arr_3 = [np.arange(0,3), np.arange(3,6), np.arange(6,9)] 
# or you can do 
# arr_3 = np.arange(0,9)
# print(arr_3.reshape(3,3))


# print(np.array(arr_3))

# arrran = np.random.rand(1)
# print(arrran)


# Create a 3x3 identity matrix

# arr_id = np.eye(3)
# print(arr_id)

# Create an array of 25 random numbers from a standard normal distribution

# arr_dist = np.random.randn(25)
# print(arr_dist)

# Create the following matrix

# ranarr = np.linspace(0.01,1,100)
# round_arr = np.around(ranarr, 2)
# print(round_arr)

# another way you could do this is the following:

# ranarr = np.linspace(0.01, 1, 100).reshape(10,10)

# or

# ranarr = np.linspace(0,1,100).reshape(10,10) / 100


# arr_matrix = round_arr.reshape(10,10)
# print(arr_matrix)


# arr_20 = np.linspace(0,1,20)

# print(arr_20)

# Numpy Indexing and Selection

mat = np.arange(1,26).reshape(5,5)

print(mat.sum(axis = 0))



# print(mat)

# sub_mat = mat[2:5, 1:]
# print(sub_mat)

# get_20 = mat[3, 4]
# print(get_20)

# print(np.array(mat[0:3, 1]))
# sub_mat2 = np.array(mat[0:3, 1:2])


# an_arr = np.array([np.arange(12,16), np.arange(17,21), np.arange(22,26)])
# print(an_arr)

# sub_mat3 = np.array(mat[4])

# print(sub_mat3)

# sub_mat3 = np.array(mat[3:5, :])
 
# print(sub_mat3)

# mat = 
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

# print(np.sum(mat)) # = 325


# print(mat.reshape(5,5))


# print(np.std(mat))

# mat_trans = np.transpose(mat)




# def col_sum(x):
#     return [np.sum(i) for i in np.transpose(x)]





# print(col_sum(mat))







# sum_mat = np.sum(mat_trans[:5,:5])

# col1 = np.sum(mat_trans[0])
# col2 = np.sum(mat_trans[1])
# col3 = np.sum(mat_trans[2])
# col4 = np.sum(mat_trans[3])
# col5 = np.sum(mat_trans[4])

# print(np.array([col1, col2, col3 , col4 , col5 ]))


