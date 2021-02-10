#!usr/bin/python3

# This code uses the package rpy2 to use a data set from R. We then create a function called 'data' that takes the name of the data set we want from R 
and returns that data set.
import rpy2.robjects as ro
from rpy2.robjects import r, pandas2ri, conversion

# The following are two different ways to write a function.  The first is the way you are typically taught how write a function:
def data(name):
    return conversion.rpy2py(r[name])

# The second is a very common way to write brief, one liner functions known as Lambda Functions.
# data = lambda name : conversion.rpy2py(r[name])

# Both are valid so you may choose which you implement for this Code Review

# We would like the mtcars data set from R so we input 'mtcars' in the data function to return the data set.
mtcars = data('mtcars')

# To convert our r2py DataFrame to a pandas DataFrame, we do the following.
with conversion.localconverter(ro.default_converter + pandas2ri.converter):
    mtcars = conversion.rpy2py(mtcars)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1) Find the mean of the miles per gallon variable.

print("1) Mean of mpg variable = ", np.mean(mtcars.mpg))
# 20.0906

#2) Compute the linear correlation between the "mpg" and "cyl" variables.

print("Linear Correlation mpg-cyl = ", (mtcars.mpg.corr(mtcars.cyl)))
# -0.85216

#3) Compute the linear correlation between the "mpg" and "gear" variables.

print("Linear Correlation mpg-gear = ", (mtcars.mpg.corr(mtcars.gear)))
# 0.480284

#4) Find the mean of the "mpg" variable for each value of the "gear" variable.

print("Mean mpg-gear = ", mtcars.groupby("gear").mean().mpg)
# 3.0, 16.107
# 4.0, 24.533
# 5.0, 21.380

#5) Find the median of the "mpg" variable for each value of the "gear" variable.

print("Median mpg-gear = ", mtcars.groupby("gear").median().mpg)
# 3.0, 15.5
# 4.0, 22.8
# 5.0, 19.7

#6) Find the make and model (or the row number) of the car with the highest miles per gallon. What are its "cyl" and "gear" values?

print("Make and model of car with hgihest mpg is ", mtcars.loc[mtcars["mpg"].idxmax()])
#Toyota Corolla at 33.900, cyl = 4.000 and ger = 4.000

#7 Find the frequency of the number of carburetors ("carb" variable) in the cars in this data set and sort these values by the least frequent to
#most frequent.

print("Frequency of each number of carburetors from least to most is ", mtcars.carb.value_counts(ascending = True))
#8.0, 1
#3.0, 3
#1.0, 7
#4.0, 10
#2.0, 10

#8 The "am" variable contains a 0 for a car with automatic transmission and a 1 for a car with manual transmission. Using 1 line of code,
# find the minimum and maximum horsepower ("hp" variable) for both a car with automatic transmission and a car with manual transmission
# out of these sample of cars. (Should return 4 
print("Min and max for variable am = ", mtcars.groupby("am").hp.agg(['min','max']))
# am = 0.0: 62.0, 245.0
# am = 1.0: 52.0, 335.0

#9 Histogram


plt.hist(mtcars.mpg, bins = 5)
plt.xlabel("Interval")
plt.ylabel("# of cars")
plt.title("Mtcars Histogram")
plt.show()