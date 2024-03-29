import requests
import csv
import numpy as np
import pandas as pd
from datetime import datetime

query = """
query Query($orderDirection: OrderDirection, $orderBy: MarketDailySnapshot_orderBy, $where: MarketDailySnapshot_filter, $first: Int) {
  marketDailySnapshots(orderDirection: $orderDirection, orderBy: $orderBy, where: $where, first: $first) {
    totalValueLockedUSD
    totalBorrowBalanceUSD
    totalDepositBalanceUSD
    timestamp
    rates {
      rate
    }
    market {
      name
    }
    dailyDepositUSD
    dailyWithdrawUSD
    inputTokenPriceUSD
    blockNumber
  }
}
"""
variables = {
    "orderDirection": "desc",
  "orderBy": "timestamp",
  "where": {
    "market_": {
      "name": "Aave Polygon WMATIC"
    }
  },
  "first": 330    
}

data = {
    "query": query,
    "variables": variables
}

response = requests.post("https://api.thegraph.com/subgraphs/name/messari/aave-v3-polygon", json=data)

results = response.json()

market_daily_snapshots = results["data"]["marketDailySnapshots"]

with open("AAVE-V3-Polygon-WMATIC.csv", mode="w", newline="") as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=["datetime", "totalValueLockedUSD", "totalBorrowBalanceUSD", "totalDepositBalanceUSD", "borrowerStableRate", "borrowerVariableRate", "lenderVariableRate", "market", "dailyDepositUSD", "dailyWithdrawUSD", "inputTokenPriceUSD", "blockNumber"])

    writer.writeheader()

    for snapshot in market_daily_snapshots:
        timestamp = datetime.utcfromtimestamp(int(snapshot["timestamp"]))
        datetime_str = timestamp.strftime("%Y-%m-%d")
        writer.writerow({
            "totalBorrowBalanceUSD": snapshot["totalBorrowBalanceUSD"],
            "totalDepositBalanceUSD": snapshot["totalDepositBalanceUSD"],
            "datetime": datetime_str,
            "totalValueLockedUSD": snapshot["totalValueLockedUSD"],
            "borrowerStableRate": snapshot["rates"][0]["rate"],
            "borrowerVariableRate": snapshot["rates"][1]["rate"],
            "lenderVariableRate": snapshot["rates"][2]["rate"],
            "dailyDepositUSD": snapshot["dailyDepositUSD"],
            "dailyWithdrawUSD": snapshot["dailyWithdrawUSD"],
            "inputTokenPriceUSD": snapshot["inputTokenPriceUSD"],
            "market": snapshot["market"]["name"],
            "blockNumber": snapshot["blockNumber"]
        })
