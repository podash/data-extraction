import requests
import numpy as np
import pandas as pd
import csv

# Replace with your own API key from Etherscan
api_key = '8PS4Z8QPS6NHD8W32G375QP282D2GU3HDR'

# Replace with your transaction hash
transaction_hash = pd.read_csv('T-AAVE-C_otokens.csv')

header = [
    "blockId"
]

with open ("T-AAVE-C_block-height.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for i in range(len(transaction_hash)):
        txHash = transaction_hash['openTxhash'][i]

        url = f'https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={txHash}&apikey={api_key}'

        response = requests.get(url)
        data = response.json()

        if 'result' in data and 'blockNumber' in data['result']:
            block_height = int(data['result']['blockNumber'], 16)
        
        writer.writerow({"blockId": block_height})

