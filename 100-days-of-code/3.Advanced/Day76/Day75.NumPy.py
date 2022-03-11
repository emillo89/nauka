
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

#Find the first elements on axis number 3 [[ 0, 4], [ 7, 5], [ 5, 97]]
print(mystery_array[:,:, :1])

#createa a vector a with values ranging from 10 to 29
a = np.arange(10,30)
print(a)

#array containing only the last 3 values of a
b = a[-3:]
print(b)

#Create a subset with only the 4th, 5th, and 6th values
subset = a[3:7]
print(subset)

#Create a subset of a containing all the values except for the first 12
subset = a[12:]
print(subset)

#Create a subset that only contains the even numbers
print(a[::2])

#revers 1 method
print(np.flip(a))

#reverse 2 method
print(a[::-1])

#find non-zero elements
b = [6,0,9,0,0,5,0]
print(np.nonzero(b))

#generate a 3x3x3 array with random numbers
from numpy.random import random
z = random((3,3,3))
print(z)

#create a vector x of size 9 with values spaced out evenly between 0 to 100
N=9
x = np.linspace(0,100,N)
print(x)

# create another vector y of size 9 with values between -3 to 3
n=9
x = np.linspace(0,100,num=9)
y = np.linspace(start=-3,stop=3,num=N)
plt.plot(x,y)
plt.show()

#generated a 128x128 pixel image of random noise
noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)
plt.show()












