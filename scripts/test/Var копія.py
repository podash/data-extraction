import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_var(df, confidence_level):
  """
  Calculates the Value at Risk (VaR) of a given dataset using the historical simulation approach.

  Args:
    df: A Pandas DataFrame containing the historical returns of the asset.
    confidence_level: The confidence level of the VaR calculation, expressed as a percentage.

  Returns:
    The VaR of the asset at the given confidence level.
  """

  # Calculate the daily returns of the asset.
  returns = df["token_price"].pct_change()

  # Sort the returns from worst to best.
  sorted_returns = returns.sort_values(ascending=False)

  # Calculate the VaR as the negative of the (1 - confidence_level)th percentile of the sorted returns.
  var = sorted_returns.iloc[int(1 - confidence_level * 100)] * df["token_price"].iloc[-1]

  return var

# Read the CSV file containing the historical RBN token prices.
df = pd.read_csv("ribbon_finance_data.csv")

# Calculate the VaR of the RBN token at the 95% confidence level.
var = calculate_var(df, 0.95)

# Generate a plot of the historical returns and the VaR.
plt.figure(figsize=(10, 6))
plt.plot(df["token_price"].pct_change())
plt.axhline(y=var, color="red", linestyle="--")
plt.xlabel("day")
plt.ylabel("Return (%)")
plt.title("Value at Risk of RBN Token (95% Confidence Level)")
plt.show()
