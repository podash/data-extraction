import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("AAVE-V3-ETH-markets.csv")

# Make the necessary changes to the DataFrame
df["totalCollateralUSD"] = (df["totalBorrowBalanceUSD"] / df["maximumLTV"]) * 100

# Write the DataFrame back to the CSV file
df.to_csv("output.csv", index=False)
