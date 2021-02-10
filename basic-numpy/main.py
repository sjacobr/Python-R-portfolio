#!/usr/bin/python3

z = [6,3,8,5,5,7,5,7,6,2,5,5,6,6,2,4,5,3,5,4,5,2,5,4,6,9,6,4,

       7,1,6,5,3,6,5,4,2,3,5,2,6,12,8,2,5,1,2,4,9,3,3,6,2,9,4,3,

       8,8,3,4,6,8,7,10,3,7,4,3,3,3,1,11,5,4,10,8,4,7,5,4,6,2,6,

       6,5,7,2,2,1,6,2,4,5,3,8,5,4,6,9,5,4,4,6,6,6,6,5,5,5,7,6,

       4,4,5,4,3,2,3,6,5,7,5,6,2,7,6,3,2,7,5,4,4,7,4,6,4,3,4,9,6,

       5,8,2,3,7,1,10,8,5,7,4,4,7,5,4,4,4,3,2,7,5,7,3,3,3,4,3,3,

       7,7,4,11,4,5,4,4,5,7,4,9,6,8,7,6,6,3,7,6,5,5,3,6,2,4,2,5,

       6,7,10,5,8,4,7,8,3,4,1,6,6,3,5,5,2,2,1,3,5,3,5,3,2,5,3,5,

       8,3,2,6,3,12,3,4,3,7,8,8,5,4,4,5,5,7,5,8,4,5,3,3,7,6,7,2,

       4,5,5,5,5,1,4,4,4,6,1,2,5,2,5,8,3,8,5,4,6,5,2,5,3,7,6,6,

       4,6,6,3,7,6,5,4,2,12,3,8,5,4,9,4,4,5,5,4,8,4,6,5,6,3,12,6,

       2,7,8,4,3,5,5,5,2,3,5,7,6,6,4,4,5,7,4,3,7,4,3,2,3,4,2,7,4,

       4,5,6,1,4,4,3,6,6,5,8,6,1,3,2,7,2,6,5,6,5,7,4,2,4,6,6,6,6,

       5,4,9,4,7,2,2,8,3,10,7,6,7,9,6,6,4,2,2,7,8,5,7,6,0,3,5,1,

       4,1,8,2,6,3,7,5,3,3,1,8,6,4,7,4,8,4,4,6,8,4,5,7,9,7,4,0,2,

       2,6,4,3,6,7,7,9,8,8,9,7,4,8,6,8,10,5,6,1,4,3,9,7,4,6,7,6,

       5,5,3,1,5,4,7,3,4,2,7,4,5,3,9,8,7,3,9,9,4,7,8,4,4,4,5,6,7,

       5,11,6,3,4,0,4,5,3,5,6,5,4,5,5,1,4,3,5,3]

import numpy as np

# Assign a value to a to be your random seed for this assignment.
a = 121940
np.random.seed(a)

# Create your array 
size = np.random.choice(range(10,50), 1)
x = np.random.choice(z, size)

# 1)  What is the length of the x array?
print("Length = ", len(x)) #length = 11

# 2) Find the sum of the numbers in the x array.
print("Sum = ", sum(x)) #sum = 63

# 3) Find the mean of the numbers in the x array.
print("Mean = ", np.mean(x)) #mean = 5.72727272

# 4) Find the standard deviation as was taught in Stat 121 of the numbers in the x array.
print("Standard Deviation = ", np.std(x, ddof = 1)) # SD = 2.901410315

# 5) Find the standard deviation a was taught in Stat 121 of the first 10 numbers in the x array.
print("Standard Deviation = ", np.std(x, ddof = 9)) #SD = 6.4877506958

# 6) Find the sum of the numbers in the x array whose index is even.
print("Sum = ",sum(x[0:11:2])) # sum = 32

# 7) Find the sum of the even numbers in the x array.
print("Sum = ", sum(x[x%2 == 0])) # sum = 32