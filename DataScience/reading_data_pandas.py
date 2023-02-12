# Python will satisfy all of our Machine Learning needs. We’ll use the Pandas module for data manipulation.

import pandas as pd
df = pd.read_csv('titanic.csv')
print(df.head())

# For print our statistics review
print(df.describe())