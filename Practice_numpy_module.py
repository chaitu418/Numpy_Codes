"""

Numpy

Is an array processing package in python

It provides high performance multi domesntional array object
and tools for working with these areas

It contains

#a powerful n dimensional array object

tools for integrating c and c++
Useful linear algebra ,fourier transform and random number capabilities

Also its used as multi dimensional container and of generic data

1.Arrays in Numpy
Its main object is the homogeneous multi dimensional array.
2.in numpy dimnesions are claeed axes
numpy's arrays class is claeed ndarray.
It is also known by the alias array.
Example:
    [[1,2,3],
    [4,2,5]]

    here rank=2(as it is 2 dimensional or havinf 2 axes)
    first dimension axis length=2 and second dimension axis length=3
    overall shapes can be expressed as (2,3)

"""
#code to demonstrate basic array characteristics

import numpy as np

arr=np.array( [[1,2,3],
            [4,3,5]] )
#print type of array object
print("Array object type is",type(arr))

#to print number of dimensions we need to use it
print("No of dimensions",arr.ndim)

#printitng shape of array
print("share of array is {} and {} and {} ".format(arr.shape,arr.dtype,arr.size))


#creation of an numpy array
"""
There are various ways to create an numpy array

For example you can create an array from a regular python list or tuple using array function.

"""
#creating array from list with type float
a=np.array([[1,2,4],[5,8,7]],dtype='float')

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

#slicing the array
temp=arr[:2,::2]
print("array with first trwo rows and alternate 2 columns",temp)

#integer array indexing example
temp=arr[[0,1,2,3],[3,2,1,0]]
print(temp,type(temp))

#basic operations of built in arithematic functions are provided in numpy


#operations on single array
#we can use

#numpy to compute the mean median and standard deviationa nd variance of given array along second axis.

# sum_of_all=sum(all_elements)
# mean=sum_of_all/n

x=np.arange(6)
print(x,type(x))
r1=np.mean(x)
r2=np.average(x)
print(r1,r2)
assert np.allclose(r1,r2)
print("\nMean:",r1)
r1=np.std(x)
r2=np.sqrt(np.mean((x-np.mean(x))**2))
print(r1,r2)

