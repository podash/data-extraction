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

blocks = pd.read_csv('AAVE-V2-Ethereum.csv')



with open ("AAVE-V2-Ethereum-collteral-DAI.csv", mode="w", newline="") as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=['totalCollateralUSD'])
  writer.writeheader()
  for i in range(len(blocks)):
    endBlock = int(blocks['blockNumber'][i])
    print(endBlock)
    variables = {
      "first": 1000,
      "orderDirection": "desc",
      "orderBy": "balance",
      "block": {
        "number": endBlock,
      },
      "where": {
        "market_": {
          "name": "Aave interest bearing DAI"
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
    
    response = requests.post("https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum", json=data)

    results = response.json()

    df = json_normalize(results['data']['positions'])

    #TOTAL COLLATERAL
    total_collateral_usd = 0
    for index, row in df.iterrows():
      for snapshot  in row['snapshots']:
        snapshots = snapshot.get('snapshots', [])
        if len(row['account.positions']) == 0:
          continue
        total_collateral_usd += float(snapshot['balanceUSD'])
    print(total_collateral_usd)
    writer.writerow({
      "totalCollateralUSD": total_collateral_usd
    })
