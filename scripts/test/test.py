import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ribbon_finance_data.csv')

ribbon_data = np.array(df)

np_ribbon_prices = ribbon_data[:,3]



def drawdown(prices):
  wealth_index = prices / prices[0]
  wealth_index = pd.Series(wealth_index)
  drawdown = (wealth_index.cummax() - wealth_index) / wealth_index.cummax()
  return drawdown.max()

print(drawdown(np_ribbon_prices))

ribbon_prices = pd.Series(np_ribbon_prices)
# Plot the drawdown
plt.plot(ribbon_prices)
plt.plot(ribbon_prices.rolling(252).min())
plt.legend(['Close', 'Rolling minimum (252 days)'])
plt.title('Ribbon Finance Drawdown')
plt.show()

# Print the percentage of loss
print('Maximum drawdown:', drawdown)
print('Percentage of loss:', drawdown * 100)