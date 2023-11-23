import pandas as pd

mainFile = "AAVE-V3-Avalanche.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(mainFile)

# Make the necessary changes to the DataFrame
df['totalCollateralUSD-45%'] = df['totalCollateralUSD'] - df['totalCollateralUSD'] * 0.45


# Write the DataFrame back to the CSV file
df.to_csv(mainFile, index=False)
