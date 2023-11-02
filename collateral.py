import pandas as pd

mainFile = "AAVE-V3-ETH-wstETH.csv"

ltvFile = "AAVE-V3-ETH-wstETH-LTV"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(mainFile)

ls = pd.read_csv(ltvFile)

# Make the necessary changes to the DataFrame
df['maximumLTV'] = ls['maximumLTV']

df["totalCollateralBalanceUSD"] = (df["totalBorrowBalanceUSD"] / df["maximumLTV"]) * 100

# Write the DataFrame back to the CSV file
df.to_csv(mainFile, index=False)
