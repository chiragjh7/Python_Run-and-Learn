# Series is a column in a table
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

# Creating labels
myVar = pd.Series(a, index = ["x", "y", "z"])
print(myVar)
print(myVar["y"])

# key value Object as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
# var = pd.Series(calories)
var = pd.Series(calories, index=["day1", "day2"])
print(var)
