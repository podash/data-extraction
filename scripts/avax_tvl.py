import requests
import csv
import numpy as np
import pandas as pd
from datetime import datetime

query = """
query TVL($block: Block_height, $vaultId: ID!) {
  vault(block: $block, id: $vaultId) {
    totalValueLockedUSD
    createdTimestamp
  }
}
"""
header = [
    "totalValueLockedUSD",
    "createdTimestamp"
]

blocks = pd.read_csv('T-AVAX-C_block-height.csv')

with open ("T-AVAX-C_tvl.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for i in range(len(blocks)):
        endBlock = int(blocks['blockId'][i])
        variables = {
        "block": {
            "number": endBlock
        },
        "vaultId": "0x6bf686d99a4ce17798c45d09c21181fac29a9fb3"
        }

        data = {
            "query": query,
            "variables": variables
        }

        response = requests.post("https://api.thegraph.com/subgraphs/name/messari/ribbon-finance-avalanche", json=data)

        results = response.json()
        totalValueLockedUSD = results['data']['vault']['totalValueLockedUSD']
        writer.writerow({"totalValueLockedUSD": totalValueLockedUSD})