from sklearn import linear_model
import pandas as pd
import numpy as np
from rpy2.robjects.packages import importr
base = importr('base')
datasets = importr('datasets')

#This gathers the longley dataset from R, to be used in Python
longley = datasets.__rdata__.fetch('longley')['longley']

#This labels the rows and columns of the dataframe.
longleydf = pd.DataFrame(longley, columns = ['1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962'], index = ['GNP.deflator', 'GNP', 'Unemployed', 'Armed.Forces', 'Population', 'Year', 'Employed'])

#This transposes the dataframe so it appears as it is in R.
longley_as_R = longleydf.transpose()
print(longley_as_R)

#These lines indicate which variables are explanatory and which are response variables.
X = longley_as_R[['GNP.deflator', 'GNP', 'Unemployed', 'Armed.Forces', 'Population', 'Year']]
Y = longley_as_R['Employed']

#These lines make the linear model and print the intercept and coefficient values.
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print("Intercept = ", regr.intercept_)
print("Coefficients = ", regr.coef_)
