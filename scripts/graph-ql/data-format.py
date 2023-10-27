import csv
import pandas as pd

data = pd.read_csv('T-ETH-C_tvl.csv')

for position in data:
        position["totalBalance"] = int(position["totalBalance"]) / 10**18

print(data)