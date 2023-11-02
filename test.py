import requests
import csv
import numpy as np
import pandas as pd
from datetime import datetime
import json

data = {
  "data": {
    "markets": [
      {
        "name": "Aave Ethereum GHO"
      },
      {
        "name": "Aave Ethereum DAI"
      },
      {
        "name": "Aave Ethereum wstETH"
      },
      {
        "name": "Aave Ethereum STG"
      },
      {
        "name": "Aave Ethereum USDT"
      },
      {
        "name": "Aave Ethereum BAL"
      },
      {
        "name": "Aave Ethereum LUSD"
      },
      {
        "name": "Aave Ethereum sDAI"
      },
      {
        "name": "Aave Ethereum WETH"
      },
      {
        "name": "Aave Ethereum ENS"
      },
      {
        "name": "Aave Ethereum KNC"
      },
      {
        "name": "Aave Ethereum LINK"
      },
      {
        "name": "Aave Ethereum WBTC"
      },
      {
        "name": "Aave Ethereum 1INCH"
      },
      {
        "name": "Aave Ethereum CRV"
      },
      {
        "name": "Aave Ethereum MKR"
      },
      {
        "name": "Aave Ethereum cbETH"
      },
      {
        "name": "Aave Ethereum USDC"
      },
      {
        "name": "Aave Ethereum LDO"
      },
      {
        "name": "Aave Ethereum AAVE"
      },
      {
        "name": "Aave Ethereum RPL"
      },
      {
        "name": "Aave Ethereum SNX"
      },
      {
        "name": "Aave Ethereum rETH"
      },
      {
        "name": "Aave Ethereum FRAX"
      },
      {
        "name": "Aave Ethereum UNI"
      }
    ]
  }
}

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

markets = data['data']['markets']

for position in markets:
    position_name = position['name']
    csv_name = str(position_name) + '.csv'

    variables = {
    "orderDirection": "desc",
    "orderBy": "timestamp",
    "where": {
        "market_": {
         "name": position_name
        }
    },
    "first": 303    
    }

    data = {
        "query": query,
        "variables": variables
    }

    response = requests.post("https://api.thegraph.com/subgraphs/name/messari/aave-v3-ethereum", json=data)
    results = response.json()
    market_daily_snapshots = results["data"]["marketDailySnapshots"]

    with open(csv_name, mode="w", newline="") as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=["datetime", "totalValueLockedUSD", "totalBorrowBalanceUSD", "totalDepositBalanceUSD", "utilizationRate", "borrowerStableRate", "borrowerVariableRate", "lenderVariableRate", "market", "dailyDepositUSD", "dailyWithdrawUSD", "inputTokenPriceUSD", "blockNumber"])

        writer.writeheader()

        for snapshot in market_daily_snapshots:
            timestamp = datetime.utcfromtimestamp(int(snapshot["timestamp"]))
            datetime_str = timestamp.strftime("%Y-%m-%d")
            writer.writerow({
                "totalBorrowBalanceUSD": snapshot["totalBorrowBalanceUSD"],
                "totalDepositBalanceUSD": snapshot["totalDepositBalanceUSD"],
                "datetime": datetime_str,
                "totalValueLockedUSD": snapshot["totalValueLockedUSD"],
                "utilizationRate": float(snapshot["totalBorrowBalanceUSD"]) / float(snapshot["totalDepositBalanceUSD"]),
                "borrowerStableRate": snapshot["rates"][0]["rate"],
                "borrowerVariableRate": snapshot["rates"][1]["rate"],
                "lenderVariableRate": snapshot["rates"][2]["rate"],
                "dailyDepositUSD": snapshot["dailyDepositUSD"],
                "dailyWithdrawUSD": snapshot["dailyWithdrawUSD"],
                "inputTokenPriceUSD": snapshot["inputTokenPriceUSD"],
                "market": snapshot["market"]["name"],
                "blockNumber": snapshot["blockNumber"]
            })


