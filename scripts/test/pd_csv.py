import pandas as pd

ribbon_data = pd.read_csv('ribbon_finance_data.csv', index_col=0)

print(ribbon_data)