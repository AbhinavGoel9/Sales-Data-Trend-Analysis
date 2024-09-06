import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load cleaned data
time_series = pd.read_csv('cleaned_superstore_sales.csv', parse_dates=['Order Date'], index_col='Order Date')
time_series = time_series.resample('D').sum()['Sales']

# Split data into train and test sets
train = time_series[:int(0.8*len(time_series))]
test = time_series[int(0.8*len(time_series)):]

# Build ARIMA model
model = ARIMA(train, order=(5,1,0))
model_fit = model.fit()

# Forecast future sales
forecast = model_fit.forecast(steps=len(test))

# Plot forecast
plt.figure(figsize=(12, 6))
plt.plot(train.index, train, label='Training Data')
plt.plot(test.index, test, label='Test Data')
plt.plot(test.index, forecast, label='Forecast', color='red')
plt.title('Sales Forecasting')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.savefig('sales_forecast.png')  # Save figure
plt.show()

# Evaluate model performance (e.g., Mean Absolute Error)
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(test, forecast)
print(f'Mean Absolute Error: {mae}')
