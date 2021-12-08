# Data frames is the whole table while Series is just a column
import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# load data in a dataframe object
df = pd.DataFrame(data)
print(df)
#locate row
print(df.loc[0])
print(df.loc[[0, 1]])

# Named Indexes
dff = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(dff)
print(dff.loc["day1"])