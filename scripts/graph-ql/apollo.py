import requests
import csv
from datetime import datetime, timedelta
import datetime

def get_last_friday():
  """Returns the datetime of the last Friday."""

  today = datetime.date.today()
  weekday = today.weekday()

  # If today is Friday, then the last Friday is yesterday.
  if weekday == 4:
    return today - datetime.timedelta(days=1)

  # Otherwise, the last Friday is one week ago.
  return today - datetime.timedelta(days=weekday + 3)

last_friday = get_last_friday()

query = """
query TVL($block: Block_height, $where: Vault_filter) {
  vaults(block: $block, where: $where) {
    totalBalance
  }
}
"""
header = [
    "date",
    "totalBalance"
]

endBlock = 18328850
with open ("T-STETH-C_tvl.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for i in range(94):

        variables = {
        "block": {
            "number": endBlock - i * 7150 * 7
        },
        "where": {
            "id": "0x53773e034d9784153471813dacaff53dbbb78e8c"
        }
        }

        data = {
            "query": query,
            "variables": variables
        }

        response = requests.post("https://api.thegraph.com/subgraphs/name/ribbon-finance/ribbon-v2", json=data)

        results = response.json()
        date = (last_friday - timedelta(weeks=i)).strftime('%Y-%m-%d')
        totalBalance = int(results['data']['vaults'][0]['totalBalance'])/ 10**18
        writer.writerow({"totalBalance": totalBalance, "date": date})

