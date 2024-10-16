# %%

import numpy as np
from random import randint

# %%
 
# Why use nparrays instead of lists?
# 1) efficiency
# 2) Major flexibility

#EX
# create two N*N matrix and sum them 
N=5

a = [[1 for _ in range(N)] for __ in range(N)]
b = [[5 for _ in range(N)] for __ in range(N)]

## complicated which is bad
# also wastes a lot of memory for each object 

#np has a fixed type usage instead of py list that can accept everything

a = np.array([1, 2, 3, 4.5])
print(a)

# there are a lot of data types
# integers: int8, int16, int32, int64
# float: float16, float32, float64

# Collections: collections of elements of the same type that can 
# even be multidimensional arrays 

# %%
N=6
b = np.array([np.array([i for i in range(N)]) for __ in range(N+2)])
print(b)

# the axes are the dimension of the multidimensional array 
# vector = 1 axis, matrix = 2 axis 

# multidimensional arrays with numpy can be also mentioned with negative numbers

# the shape of a np array is returned as a tuple
print(b.shape)
# %%
print(np.array([[0,1], [3, 2], [4, 3]], dtype='int16').dtype)

# Hyper Matrix
print(np.ones((2, 4, 5)))



# %%
# start, stop, #items
print(np.linspace(1, 5, 1000))

# start, stop, step
print(np.arange(1, 5, 0.1))


# %%
a =np.array([np.array([i for i in range(4)]) for __ in range(4+2)])
print(a.size, a.ndim)


# %%
# Universal function, either binary (two input) or unary(one input)
# and apply something

# the two elements of binary function must have roughly the same shape
# ex sum member a member is universal 

a =np.array([np.array([i for i in range(4)]) for __ in range(4+2)])
b =np.array([np.array([i for i in range(4)]) for __ in range(4+2)])

print(a*b)


# %%
# Unary function -> take a single array and apply a function element wise
# ex np.abs() or np.exp() or np.cos()

a =np.array([np.array([i for i in range(4)]) for __ in range(4+2)])

print(np.cos(a))
# %%
# Generate an array of 10 random integers between 1 and 100
random_integers = np.random.randint(1, 101, 10)
print(random_integers)
# %%
print(np.random.random((10, 5)))

# %%
# the min/max function 
    # if array 1 dimensional min/max gives the position 
    # if array > 1 dimensional the max/min value is given 
    
# a =np.array([[np.array([randint(0, 3500) for i in range(4)]) for __ in range(4+2)] for ___ in range(1)])
a =np.array([np.array([randint(0, 350) for i in range(4)]) for __ in range(4+2)])

print(a)
print(np.max(a), np.min(a))

# creates a 1 dimensional array
print(a.flatten())
print(np.max(a.flatten()), np.min(a.flatten()))

# Computes the minimum/maximum along a single dimension
# 0 for cols, 1 for rows
print(np.max(a, axis=1))# %%
print(np.sum(a, axis=0))

# %%
print(np.array([[[1],[4]], [[2], [6]], [[3],[7]]]))

# %%
print(np.ones((3, 4, 2)))
# %%
# you can sort 1D arrays as usual 
# on 2+ dim you can sort each dimension