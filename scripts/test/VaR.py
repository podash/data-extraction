import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the Ribbon finance data
ribbon_finance_data = pd.read_csv('ribbon_finance_data_2clear.csv', index_col='Date')

# Calculate the daily returns
ribbon_finance_returns = ribbon_finance_data.pct_change()

# Calculate the Delta-Normal VaR
def delta_normal_var(returns, confidence_level):
  """Calculates the Delta-Normal VaR of a given series of returns at a given confidence level.

  Args:
    returns: A pandas Series of returns.
    confidence_level: The desired confidence level, expressed as a decimal between 0 and 1.

  Returns:
    A float representing the Delta-Normal VaR.
  """

  # Calculate the mean and standard deviation of the returns
  mean_return = returns.mean()
  std_return = returns.std()

  # Calculate the z-score corresponding to the desired confidence level
  z_score = np.percentile(np.random.randn(10000), confidence_level)

  # Calculate the VaR
  var = mean_return + z_score * std_return

  return var

# Calculate the 95% Delta-Normal VaR of the daily returns
var_95 = delta_normal_var(ribbon_finance_returns, confidence_level=0.95)

# Calculate the 99% Delta-Normal VaR of the daily returns
var_99 = delta_normal_var(ribbon_finance_returns, confidence_level=0.99)

# Print the results
print('95% Delta-Normal VaR:', var_95)
print('99% Delta-Normal VaR:', var_99)

# Plot the distribution of the daily returns
plt.hist(ribbon_finance_returns)
plt.xlabel('Daily returns')
plt.ylabel('Frequency')
plt.title('Distribution of Ribbon finance daily returns')

# Plot the VaR lines
plt.axvline(var_95, color='red', linestyle='dashed', label='95% VaR')
plt.axvline(var_99, color='green', linestyle='dashed', label='99% VaR')
plt.legend()

# Show the plot
plt.show()
