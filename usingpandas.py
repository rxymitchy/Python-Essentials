import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [20, 30, 40],
        'city': ['Nairobi', 'Mombasa', 'Kisumu']}

df = pd.DataFrame(data)
print(df)

# select a column
print(df['name'])

# select multiple columns
print(df[['name', 'city']])

# select rows by index
print(df.loc[1])

# select by condition
print(df[df['age'] > 30])

# Add a new column
df['salary'] = [5000, 6000, 7000]
print(df)

# Group by age and get salary for each group
grouped = df.groupby('age') ['salary'].mean()
print(grouped)

#sorting values
df_sorted = df.sort_values(by='salary', ascending=False) # descending order
print(df_sorted)

#dropping a column
df.drop('city', axis=1, inplace=True)
print(df)