import pandas as pd

# Creating a Pandas Series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Pandas Series:")
print(series)

# Creating a Pandas DataFrame
data = {
    'Name': ['Agrim', 'Harsh', 'Mayank', 'Aryan'],
    'Age': [28, 24, 35, 32],
    'City': ['Haryana', 'Haryana', 'Bombay', 'Delhi']
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# Selecting a column from DataFrame
print("\nSelecting 'Name' column:")
print(df['Name'])

# Selecting multiple columns from DataFrame
print("\nSelecting 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])

# Adding a new column to DataFrame
df['Salary'] = [50000, 60000, 70000, 80000]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# Dropping a column from DataFrame
df = df.drop(columns=['City'])
print("\nDataFrame after dropping 'City' column:")
print(df)

# Filtering rows based on a condition
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Applying a function to a column
df['Age'] = df['Age'].apply(lambda x: x + 1)
print("\nDataFrame after incrementing 'Age' by 1:")
print(df)