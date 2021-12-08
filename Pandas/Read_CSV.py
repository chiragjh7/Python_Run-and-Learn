import pandas as pd
df = pd.read_csv('data.csv')
# print(df.to_string())
print(df)

# max rows 
print(pd.options.display.max_rows)

dff = pd.read_csv("data.csv")
pd.options.display.max_rows = 9999
print(dff)