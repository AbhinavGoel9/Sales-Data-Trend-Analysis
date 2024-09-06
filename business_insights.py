import pandas as pd

# Load cleaned data
data = pd.read_csv('cleaned_superstore_sales.csv')

# Example: Identify key trends
top_categories = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("Top Categories:\n", top_categories)

# Example: Regional sales insights
regional_sales = data.groupby('Region')['Sales'].sum()
print("Regional Sales:\n", regional_sales)
