
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


"""# Linear Algebra with Vectors"""
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

#add v1 + v2
print(v1 + v2)

#add list1 + list2 (concatenate list)
print(list1 + list2)

#Multiplying the two vectors
print(v1 * v2)

#Multiplying the two list
# list1 * list2
# this operation would not work at all

"""Broadcasting and Scalars"""

#Broadcasting and Scalars
#single number is often called a scalar
#suma vector with scalar
array_2d = np.array([[1,2,3,4],[5,6,7,8]])
print(array_2d + 10)

#Multicplications vector with scalar
print(array_2d * 5)

"""Matrix Multiplication with @ and .matmul()"""

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

#multiply a1 with b1
c = np.matmul(a1, b1)
print(c)

""" second method multiply 
c = a1 @ b1
c
"""

"""Manipulating Images as ndarrays"""

from scipy import misc
from PIL import Image

img = misc.face()
print(img)
plt.imshow(img)

"""**Challenge**: What is the data type of `img`? Also, what is the shape of `img` and how many dimensions does it have? What is the resolution of the image?"""

#What is the data type of img
type(img)
print(img.shape)
print(img.ndim)

"""Convert the image to black and white"""
grey_vals = np.array([0.2126, 0.7152, 0.0722])

# Convert the image to black and white
sRGB = img / 255
print(sRGB)

#matrix multiplication to multiply our two ndarrays
img_gray = sRGB @ grey_vals

plt.imshow(img_gray, cmap='gray')

#flip
plt.imshow(np.flip(img_gray), cmap='gray')

#Rotate the colour image
plt.imshow(np.rot90(img))

#Invert the colour image
solar_img = 255 - img
plt.imshow(solar_img)

"""# Use your Own Image!"""

file_name = 'yummy_macarons.jpg'

my_img = Image.open(file_name)
img_array = np.array(my_img)

print(img_array.ndim)
print(img_array.shape)

"""#### Use PIL to open """
plt.imshow(img_array)
plt.imshow(255 - img_array)
plt.show()










