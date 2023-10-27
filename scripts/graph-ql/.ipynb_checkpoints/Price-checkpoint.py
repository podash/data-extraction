import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ribbon_data = pd.read_csv('ribbon_finance_data.csv')

def drawdown(prices):
  wealth_index = prices / prices[0]
  wealth_index = pd.Series(wealth_index)
  drawdown = (wealth_index.cummax() - wealth_index) / wealth_index.cummax()
  return drawdown.max()

# Plot the drawdown
plt.plot(ribbon_data)
plt.plot(ribbon_data.rolling(252).min())
plt.legend(['Close', 'Rolling minimum (252 days)'])
plt.title('Ribbon Finance Drawdown')
plt.show()

# Print the percentage of loss
print('Maximum drawdown:', drawdown)
print('Percentage of loss:', drawdown * 100)