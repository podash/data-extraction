import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV data into a DataFrame
data = pd.read_csv('ribbon_finance_data.csv')  # Replace 'your_data.csv' with the actual CSV file path

# Calculate daily returns
data['returns'] = data['token_price'].pct_change()

# Parameters for VAR calculation
confidence_level = 0.95  # You can adjust this based on your risk tolerance
time_horizon = 1  # Number of days for the time horizon

# Calculate VAR using historical simulation method
var = -np.percentile(data['returns'].dropna(), (1 - confidence_level) * 100)
var *= data['token_price'].iloc[-1]  # Convert to the token price at the end of the data

# Print VAR value
print(f"Value at Risk (VAR) at {confidence_level*100}% confidence for {time_horizon} day(s): {var:.2f} USD")

# Create a histogram of returns
plt.figure(figsize=(10, 6))
plt.hist(data['returns'].dropna(), bins=50, alpha=0.75, color='b', edgecolor='k')
plt.title('Histogram of Daily Returns')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

