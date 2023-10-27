import os
import csv
from eth_account import Account

# Number of wallets to generate
num_wallets = 255  # You can change this as needed

# Create a list to store wallet information
wallets = []

# Generate Ethereum wallets
for _ in range(num_wallets):
    account = Account.create()
    private_key = account._private_key.hex()
    address = account.address
    wallets.append({"Private Key": private_key, "Address": address})

# Define the CSV file path
csv_file = "ethereum_wallets.csv"

# Check if the CSV file already exists
file_exists = os.path.isfile(csv_file)

# Write wallet information to the CSV file
with open(csv_file, mode='a', newline='') as file:
    fieldnames = ["Private Key", "Address"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header if the file doesn't exist
    if not file_exists:
        writer.writeheader()

    # Write wallet data
    for wallet in wallets:
        writer.writerow(wallet)

print(f"{num_wallets} Ethereum wallets generated and saved to {csv_file}.")
