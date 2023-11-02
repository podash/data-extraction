import requests
import csv
from datetime import datetime
import pandas as pd

query = """
query Markets($block: Block_height, $where: Market_filter) {
  markets(block: $block, where: $where) {
    maximumLTV
  }
}
"""

header = [
    "maximumLTV"
]

blocks = pd.read_csv('AAVE-V3-ETH-USDC.csv')

with open ("AAVE-V3-ETH-DAI-LTV.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for i in range(len(blocks)):
        endBlock = int(blocks['blockNumber'][i])
        variables = {
            "block": {
            "number": endBlock
            },
            "where": {
                "name": "Aave Ethereum USDC"
            }    
        }

        data = {
            "query": query,
            "variables": variables
        }

        response = requests.post("https://api.thegraph.com/subgraphs/name/messari/aave-v3-ethereum", json=data)

        results = response.json()
        
        market_daily_snapshots = results["data"]["markets"]

        for snapshot in market_daily_snapshots:
            writer.writerow({
                "maximumLTV": snapshot["maximumLTV"],
            })
