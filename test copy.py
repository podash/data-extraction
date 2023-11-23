import requests
import csv
import numpy as np
import pandas as pd
from pandas import json_normalize
from datetime import datetime

query = """
query CollateralPosittion($first: Int, $orderDirection: OrderDirection, $orderBy: Position_orderBy, $where: Position_filter, $snapshotsFirst2: Int, $snapshotsOrderBy2: PositionSnapshot_orderBy, $snapshotsOrderDirection2: OrderDirection, $positionsWhere2: Position_filter, $snapshotsFirst3: Int, $snapshotsOrderBy3: PositionSnapshot_orderBy, $snapshotsOrderDirection3: OrderDirection, $snapshotsWhere2: PositionSnapshot_filter, $block: Block_height) {
  positions(first: $first, orderDirection: $orderDirection, orderBy: $orderBy, where: $where, block: $block) {
    balance
    market {
      name
    }
    isCollateral
    snapshots(first: $snapshotsFirst2, orderBy: $snapshotsOrderBy2, orderDirection: $snapshotsOrderDirection2) {
      balanceUSD
      timestamp
    }
    account {
      id
      positions(where: $positionsWhere2) {
        market {
          name
        }
        snapshots(first: $snapshotsFirst3, orderBy: $snapshotsOrderBy3, orderDirection: $snapshotsOrderDirection3, where: $snapshotsWhere2) {
          timestamp
          balanceUSD
        }
      }
    }

  }
}
"""

variables = {
  "first": 100,
  "orderDirection": "desc",
  "orderBy": "balance",
  "block": {
    "number": 18591552
  },
  "where": {
    "market_": {
      "name": "Aave Ethereum wstETH"
    },
    "isCollateral": True,
    "balance_gt": 0,
    "account_": {}
  },
  "snapshotsFirst2": 1,
  "snapshotsOrderBy2": "timestamp",
  "snapshotsOrderDirection2": "desc",
  "positionsWhere2": {
    "side": "BORROWER"
  },
  "snapshotsFirst3": 1,
  "snapshotsOrderBy3": "timestamp",
  "snapshotsOrderDirection3": "desc",
  "snapshotsWhere2": {
    "balanceUSD_gt": 0
  }
}

data = {
  "query": query,
  "variables": variables
}

response = requests.post("https://api.thegraph.com/subgraphs/name/messari/aave-v3-ethereum", json=data)

results = response.json()

df = json_normalize(results['data']['positions'])

print(df)

sum = 0
for index, row in df.iterrows():
  for snapshot  in row['snapshots']:
    sum += float(snapshot['balanceUSD'])