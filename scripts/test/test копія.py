import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ribbon_finance_data.csv")

# Calculate the daily returns
returns = df['price'].pct_change()

# Calculate the standard deviation of the daily returns
std_return = returns.std()

# Annualize the standard deviation
volatility = std_return * np.sqrt(252)

# Print the volatility
print(volatility)