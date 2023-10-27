import math
import warnings
import pandas as pd
import numpy as np
import numpy.random as npr
from pylab import plt, mpl

warnings.filterwarnings('ignore', 'invalid value encountered in log')

df_rbn = pd.read_csv('ribbon_finance_data.csv', parse_dates=['Date']).set_index('Date')

print(df_rbn)

npr.seed(3) # seed for getting the same result each time. 
# -------------Geometric Brownian Motion (granual/steps)--------------------
S0 = df_rbn['Close'].mean() # Starting Price
r = np.log(df_rbn['Close']/df_rbn['Close'].shift(1)).mean() * 365 # drift (expected rate of return)
sigma = np.log(df_rbn['Close']/df_rbn['Close'].shift(1)).std() * np.sqrt(365) # historical volatility
I = 1 # simulations
M = 500 # steps per simimulation
T = 1 # time period
dt = T / M # steps per time period

S = np.zeros((M + 1, I))
S[0] = S0
for t in range(1, M + 1):
    S[t] = S[t-1] + r * S[t-1] * dt + S[t-1] * sigma * math.sqrt(dt) * npr.standard_normal(I)



plt.figure(figsize=(15, 8), dpi=80)
plt.plot(S[:, :I])
plt.grid()
plt.title('RBN: Geometric Brownian Motion', fontweight='bold')
plt.xlabel('Time')
plt.ylabel('Underlying: Spot Price')
plt.show()