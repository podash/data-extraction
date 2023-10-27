import numpy as np


def max_drawdown(prices):
  """Calculates the maximum drawdown of a given set of prices.

  Args:
    prices: A NumPy array of prices.

  Returns:
    A float representing the maximum drawdown.
  """

  # Calculate the peak-to-trough drawdown for each period.
  drawdowns = np.maximum(0, np.maximum.accumulate(prices) - prices)

  # Return the maximum drawdown.
  return np.max(drawdowns)


# Example usage:

prices = np.array([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50])

max_drawdown = max_drawdown(prices)

print(max_drawdown)
