
import numpy as np

import matplotlib.pyplot as plt
from scipy import misc # contains an image of a racoon!
from PIL import Image # for reading image files

#n-dimensional means that we can work with everything from a single column 
#(1-dimensional) to the matrix (2-dimensional) 
#create a 1-dimensional array

my_array = np.array([1.1, 9.2, 8.1, 4.7])
print(my_array.shape)

#access an element
print(my_array[2])

#check the dimensions 
print(my_array.ndim)

"""#### 2-Dimensional Arrays (Matrices)"""
array_2d = np.array([[1, 2, 3, 9], 
                     [5, 6, 7, 8]])

print(array_2d)

#how many dimensions
print(f'array_2d has {array_2d.ndim} dimensions')

#shape
print(f'Its shape is {array_2d.shape}')

# how many rows and columns
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')

#access the 3rd value in the 2nd row
print(array_2d[1,2])

#access all the values in the first row
print(array_2d[0,:])

"""#### N-Dimensional Arrays (Tensors)"""

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

# Note all the square brackets!

#how mamy dimensions 
print(mystery_array.ndim)

# shape 
print(mystery_array.shape)

#access to the number 18
print(mystery_array[2,1,3])

#access to the [97, 0, 27, 18]
print(mystery_array[2,1,:])

#alle the first elements on axis number 3 [[ 0, 4], [ 7, 5], [ 5, 97]]
print(mystery_array[:,:, :1])











