import pandas as pd
df = pd.read_csv('data.csv')

# Discovering duplicates
print(df.duplicated())

# Removing Duplicates
df.drop_duplicates(inplace=True)