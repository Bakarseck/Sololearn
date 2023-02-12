import pandas as pd
df = pd.read_csv('titanic.csv')
a = df['Fare'].values
print(a)
print(type(a))