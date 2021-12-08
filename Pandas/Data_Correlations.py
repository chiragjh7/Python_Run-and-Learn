# corr() method calculates the relatinship between each  columns in your data set.

import pandas as pd
df = pd.read_csv('data.csv')
print(df.corr())