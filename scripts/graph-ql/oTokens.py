import requests
import csv
from datetime import datetime

query = """
query oTokensQuery($first: Int, $orderBy: VaultShortPosition_orderBy, $orderDirection: OrderDirection, $where: VaultShortPosition_filter) {
  vaultShortPositions(first: $first, orderBy: $orderBy, orderDirection: $orderDirection, where: $where) {
    mintAmount
    openedAt
    openTxhash
    premiumEarned
    strikePrice
  }
}
"""

variables = {
  "first": 1000,
  "orderBy": "openedAt",
  "orderDirection": "desc",
  "where": {
    "vault": "0xcc323557c71c0d1d20a1861dc69c06c5f3cc9624"
  }
}

data = {
    "query": query,
    "variables": variables
}

header = [
    "openedAt",
    "mintAmount",
    "openTxhash",
    "strikePrice",
    "premiumEarned"
]

response = requests.post("https://api.thegraph.com/subgraphs/name/ribbon-finance/ribbon-v2", json=data)

results = response.json()

short_positions = results["data"]["vaultShortPositions"]

with open("T-USDC-P-ETH_otokens.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for position in short_positions:
        position['openedAt'] = datetime.utcfromtimestamp(int(position['openedAt'])).strftime('%Y-%m-%d')
        position["mintAmount"] = int(position["mintAmount"]) / 10**8
        position['premiumEarned'] = int(position['premiumEarned']) / 10**8
        position['strikePrice'] = int(position['strikePrice']) / 10**8
        writer.writerow(position)