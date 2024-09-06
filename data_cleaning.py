import pandas as pd

# Load the dataset
data = pd.read_csv('superstore_sales.csv')

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Fill missing values or drop rows/columns
data.fillna(method='ffill', inplace=True)

# Convert date column to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Check data types
print(data.dtypes)

# Save cleaned data for further analysis
data.to_csv('cleaned_superstore_sales.csv', index=False)
