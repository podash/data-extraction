import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your CSV file with historical prices
file_path = 'ribbon_finance_data.csv'
df = pd.read_csv(file_path)

# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# Set the 'date' column as the index
df.set_index('date', inplace=True)

# Calculate the daily returns
df['daily_return'] = df['token_price'].pct_change()

# Calculate the cumulative returns
df['cumulative_return'] = (1 + df['daily_return']).cumprod()

# Calculate the maximum drawdown manually
max_drawdown = (df['cumulative_return'] / df['cumulative_return'].cummax() - 1).min()

# Find the start and end dates of the maximum drawdown
end_date = df[df['cumulative_return'] == df['cumulative_return'].cummax().max()].index[0]
start_date = df[df.index <= end_date]['cumulative_return'].idxmax()

# Calculate the duration of the maximum drawdown
max_drawdown_duration = (end_date - start_date).days

# Print the results
print(f"Maximum Drawdown: {max_drawdown:.2%}")
print(f"Maximum Drawdown Duration: {max_drawdown_duration} days")

# Plot the cumulative return and highlight the drawdown period
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['cumulative_return'], label='Cumulative Return', color='blue')
plt.fill_between(df.index, 0, df['cumulative_return'], where=(df.index >= start_date) & (df.index <= end_date), color='red', alpha=0.5)
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.title('RBN Token Maximum Drawdown')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
