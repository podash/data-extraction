import json
import csv
from datetime import datetime

json_data = {
  "data": {
    "markets": [
      {
        "name": "Aave Ethereum GHO",
        "maximumLTV": "0",
        "totalBorrowBalanceUSD": "26526784.169592038304389069",
        "totalDepositBalanceUSD": "0"
      },
      {
        "name": "Aave Ethereum DAI",
        "maximumLTV": "77",
        "totalBorrowBalanceUSD": "62183142.25089508579612678186595116",
        "totalDepositBalanceUSD": "69354286.88433278520073695958171666"
      },
      {
        "name": "Aave Ethereum wstETH",
        "maximumLTV": "78.5",
        "totalBorrowBalanceUSD": "17741876.54985002743541960794493482",
        "totalDepositBalanceUSD": "1474339550.16927849641702036538802"
      },
      {
        "name": "Aave Ethereum STG",
        "maximumLTV": "35",
        "totalBorrowBalanceUSD": "0",
        "totalDepositBalanceUSD": "491927.76387380000000206568300432"
      },
      {
        "name": "Aave Ethereum USDT",
        "maximumLTV": "74",
        "totalBorrowBalanceUSD": "235442301.321952814268",
        "totalDepositBalanceUSD": "291955636.855356700288"
      },
      {
        "name": "Aave Ethereum BAL",
        "maximumLTV": "57",
        "totalBorrowBalanceUSD": "413014.27713044806695414926",
        "totalDepositBalanceUSD": "1158407.8184102432334284575"
      },
      {
        "name": "Aave Ethereum LUSD",
        "maximumLTV": "77",
        "totalBorrowBalanceUSD": "3535644.21188933056762537648863715",
        "totalDepositBalanceUSD": "4381472.73884875736940692892122325"
      },
      {
        "name": "Aave Ethereum sDAI",
        "maximumLTV": "77",
        "totalBorrowBalanceUSD": "0",
        "totalDepositBalanceUSD": "115959006.1288450896227121252615949"
      },
      {
        "name": "Aave Ethereum WETH",
        "maximumLTV": "80.5",
        "totalBorrowBalanceUSD": "542549428.2117440286892097250710064",
        "totalDepositBalanceUSD": "730354231.0534757203216679572124628"
      },
      {
        "name": "Aave Ethereum ENS",
        "maximumLTV": "39",
        "totalBorrowBalanceUSD": "15783.330299401168773047586",
        "totalDepositBalanceUSD": "271756.287341147229013336734"
      },
      {
        "name": "Aave Ethereum KNC",
        "maximumLTV": "35",
        "totalBorrowBalanceUSD": "0",
        "totalDepositBalanceUSD": "37652.00311873"
      },
      {
        "name": "Aave Ethereum LINK",
        "maximumLTV": "53",
        "totalBorrowBalanceUSD": "3722376.29236896886545969869054622",
        "totalDepositBalanceUSD": "35581966.98100251669029248075891452"
      },
      {
        "name": "Aave Ethereum WBTC",
        "maximumLTV": "73",
        "totalBorrowBalanceUSD": "41825213.1758304706957666",
        "totalDepositBalanceUSD": "360705205.8128591578151382"
      },
      {
        "name": "Aave Ethereum 1INCH",
        "maximumLTV": "57",
        "totalBorrowBalanceUSD": "54635.295909681564220417736412",
        "totalDepositBalanceUSD": "496445.066647667862096203117484"
      },
      {
        "name": "Aave Ethereum CRV",
        "maximumLTV": "35",
        "totalBorrowBalanceUSD": "460218.1617532384394350014593",
        "totalDepositBalanceUSD": "2130305.8703908276630389738509"
      },
      {
        "name": "Aave Ethereum MKR",
        "maximumLTV": "65",
        "totalBorrowBalanceUSD": "1024566.87625664931710341442032032",
        "totalDepositBalanceUSD": "15100890.861024176943734882419572"
      },
      {
        "name": "Aave Ethereum cbETH",
        "maximumLTV": "74.5",
        "totalBorrowBalanceUSD": "3470051.27151504181420851508570125",
        "totalDepositBalanceUSD": "18981703.35314467835826798266022375"
      },
      {
        "name": "Aave Ethereum USDC",
        "maximumLTV": "77",
        "totalBorrowBalanceUSD": "311640044.73603848434658",
        "totalDepositBalanceUSD": "347912948.99116887324854"
      },
      {
        "name": "Aave Ethereum LDO",
        "maximumLTV": "40",
        "totalBorrowBalanceUSD": "577862.0924261236925880165537119",
        "totalDepositBalanceUSD": "5371777.96574045321589712017194653"
      },
      {
        "name": "Aave Ethereum AAVE",
        "maximumLTV": "66",
        "totalBorrowBalanceUSD": "0",
        "totalDepositBalanceUSD": "49917418.38976906966568626166884664"
      },
      {
        "name": "Aave Ethereum RPL",
        "maximumLTV": "0",
        "totalBorrowBalanceUSD": "4535727.84914628499434484648418688",
        "totalDepositBalanceUSD": "10049375.4385307122286532846850584"
      },
      {
        "name": "Aave Ethereum SNX",
        "maximumLTV": "49",
        "totalBorrowBalanceUSD": "642407.15791415497387041329960356",
        "totalDepositBalanceUSD": "1308020.37626594464769115864128872"
      },
      {
        "name": "Aave Ethereum rETH",
        "maximumLTV": "74.5",
        "totalBorrowBalanceUSD": "5817784.34829145508989037355321915",
        "totalDepositBalanceUSD": "78678017.32837112235586093267576315"
      },
      {
        "name": "Aave Ethereum FRAX",
        "maximumLTV": "70",
        "totalBorrowBalanceUSD": "249404.94269428213390702902565842",
        "totalDepositBalanceUSD": "310437.29459326986683743546703922"
      },
      {
        "name": "Aave Ethereum UNI",
        "maximumLTV": "65",
        "totalBorrowBalanceUSD": "358881.03131294320155147092869456",
        "totalDepositBalanceUSD": "7143239.97680339059018407634242806"
      }
    ]
  }
}

market_daily_snapshots = json_data["data"]["markets"]

with open("AAVE-V3-ETH-markets.csv", mode="w", newline="") as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=["name", "maximumLTV", "totalBorrowBalanceUSD", "totalDepositBalanceUSD"])

    writer.writeheader()

    for snapshot in market_daily_snapshots:
        writer.writerow({
            "name": snapshot["name"],
            "maximumLTV": snapshot["maximumLTV"],
            "totalBorrowBalanceUSD": snapshot["totalBorrowBalanceUSD"],
            "totalDepositBalanceUSD": snapshot["totalDepositBalanceUSD"]
        })
