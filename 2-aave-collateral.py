import requests
import csv
import numpy as np
import pandas as pd
from pandas import json_normalize
from datetime import datetime

query = """
query BorrowerPositions($where: Position_filter, $first: Int, $orderDirection: OrderDirection, $orderBy: Position_orderBy, $skip: Int, $block: Block_height, $snapshotsOrderBy2: PositionSnapshot_orderBy, $snapshotsOrderDirection2: OrderDirection, $snapshotsFirst2: Int, $positionsWhere2: Position_filter, $snapshotsOrderBy3: PositionSnapshot_orderBy, $snapshotsOrderDirection3: OrderDirection, $snapshotsFirst3: Int, $snapshotsWhere2: PositionSnapshot_filter) {
  positions(where: $where, first: $first, orderDirection: $orderDirection, orderBy: $orderBy, skip: $skip, block: $block) {
    timestampOpened
    side
    balance
    account {
      id
      positions(where: $positionsWhere2) {
        snapshots(orderBy: $snapshotsOrderBy3, orderDirection: $snapshotsOrderDirection3, first: $snapshotsFirst3, where: $snapshotsWhere2) {
          balanceUSD
          timestamp
        }
      }
    }
    market {
      name
    }
    snapshots(orderBy: $snapshotsOrderBy2, orderDirection: $snapshotsOrderDirection2, first: $snapshotsFirst2) {
      balanceUSD
      timestamp
    }
  }
}
"""

blocks = pd.read_csv('AAVE-V3-Polygon-WMATIC.csv')

with open ("AAVE-V3-Polygon-WMATIC-collteral.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['totalCollateralUSD', 'totalBorrowUSD'])
    writer.writeheader()
    for i in range(len(blocks)):
        endBlock = int(blocks['blockNumber'][i])

        variables = {
        "where": {
            "market_": {
            "name": "Aave Polygon WMATIC"
            },
            "side": "BORROWER",
            "balance_gt": 0
        },
        "first": 1000,
        "orderDirection": "desc",
        "orderBy": "balance",
        "skip": 0,
        "block": {
            "number": endBlock
        },
        "snapshotsOrderBy2": "timestamp",
        "snapshotsOrderDirection2": "desc",
        "snapshotsFirst2": 1,
        "positionsWhere2": {
            "isCollateral": True
        },
        "snapshotsOrderBy3": "timestamp",
        "snapshotsOrderDirection3": "desc",
        "snapshotsFirst3": 1,
        "snapshotsWhere2": {
            "balanceUSD_gt": 0
        }
        }
    
    
        data = {
        "query": query,
        "variables": variables
        }
        response = requests.post("https://api.thegraph.com/subgraphs/name/messari/aave-v3-polygon", json=data)

        results = response.json()

        df = json_normalize(results['data']['positions'])
    
        #TOTAL COLLATERAL
        total_collateral_usd = 0
        for index, row in df.iterrows():
            for snapshot in row['account.positions']:
                snapshots = snapshot.get('snapshots', [])
                if snapshots:
                    first_snapshot = snapshots[0]
                    if isinstance(first_snapshot['balanceUSD'], list) and not first_snapshot['balanceUSD']:
                        continue
                    total_collateral_usd += float(first_snapshot['balanceUSD'])
        print("TOTAL COLLATERAL USD:", total_collateral_usd)

        #TOTAL BORROW
        total_borrow_usd = 0
        for index, row in df.iterrows():
            for snapshot in row['snapshots']:
                snapshots = snapshot.get('snapshots', [])
                if isinstance(snapshot['balanceUSD'], list) and not snapshot['balanceUSD']:
                    continue
                total_borrow_usd += float(snapshot['balanceUSD'])
        print("TOTAL BORROW USD:", total_borrow_usd)

        writer.writerow({
            "totalCollateralUSD": total_collateral_usd,
            "totalBorrowUSD": total_borrow_usd
        })
