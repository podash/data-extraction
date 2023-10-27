import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load CSV data into a DataFrame
data = pd.read_csv('ribbon_finance_data.csv')  # Replace 'your_data.csv' with the actual CSV file path

# Calculate daily returns
data['returns'] = data['token_price'].pct_change()

# Parameters for VAR calculation
confidence_level = 0.95
time_horizon = 1

# Calculate VAR using historical simulation method
var = -np.percentile(data['returns'].dropna(), (1 - confidence_level) * 100)
var *= data['token_price'].iloc[-1]

# Print VAR value
print(f"Value at Risk (VAR) at {confidence_level*100}% confidence for {time_horizon} day(s): {var:.2f} USD")

# Create a histogram of returns
plt.figure(figsize=(10, 6))
plt.hist(data['returns'].dropna(), bins=50, alpha=0.75, color='b', edgecolor='k', density=True, label='Actual Returns')

# Calculate mean and standard deviation of returns
mean_return = data['returns'].mean()
std_return = data['returns'].std()

# Generate values for the normal distribution curve
x = np.linspace(data['returns'].min(), data['returns'].max(), 100)
pdf = norm.pdf(x, loc=mean_return, scale=std_return)

# Plot the normal distribution curve
plt.plot(x, pdf, 'r-', lw=2, label='Normal Distribution')

plt.title('Histogram of Daily Returns vs. Normal Distribution')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
