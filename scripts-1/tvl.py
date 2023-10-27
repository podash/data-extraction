import requests
import csv
import numpy as np
import pandas as pd

query = """
query TVL($block: Block_height, $where: Vault_filter) {
  vaults(block: $block, where: $where) {
    totalBalance
  }
}
"""
header = [
    "totalBalance"
]

blocks = pd.read_csv('T-AAVE-C_block-height.csv')

with open ("T-AAVE-C_tvl.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for i in range(len(blocks)):
        endBlock = int(blocks['blockId'][i])
        variables = {
        "block": {
            "number": endBlock
        },
        "where": {
            "id": "0xe63151a0ed4e5fafdc951d877102cf0977abd365"
        }
        }

        data = {
            "query": query,
            "variables": variables
        }

        response = requests.post("https://api.thegraph.com/subgraphs/name/ribbon-finance/ribbon-v2", json=data)

        results = response.json()
        totalBalance = int(results['data']['vaults'][0]['totalBalance'])/ 10**18
        writer.writerow({"totalBalance": totalBalance})