import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv('cleaned_superstore_sales.csv')

# Filter data by date range
data['Year'] = pd.to_datetime(data['Order Date']).dt.year

# Sales by Year
sales_by_year = data.groupby('Year')['Sales'].sum()

# Plot sales over time
plt.figure(figsize=(10, 6))
sales_by_year.plot(kind='line')
plt.title('Sales Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.grid(True)
plt.savefig('sales_over_time.png')  # Save figure
plt.show()

# Sales by Product Category
sales_by_category = data.groupby('Category')['Sales'].sum()
print(sales_by_category)

# Save additional visualizations as needed
