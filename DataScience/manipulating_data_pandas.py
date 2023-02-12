import pandas as pd
df = pd.read_csv('titanic.csv')
col = df['Fare']
print(col)
small_df = df[['Age',  'Sex', 'Survived']]
print(small_df.head())

# Create a new column that contains the result of df['Sex'] == 'male'
df['male'] = df['Sex'] == 'male'