import json
import csv
from datetime import datetime

json_data = {
  "data": {
    "reserveParamsHistoryItems": [
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698852899
      },
      {
        "totalLiquidityAsCollateral": "1681758840067319495932573",
        "timestamp": 1698852647
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698852527
      },
      {
        "totalLiquidityAsCollateral": "423013476347",
        "timestamp": 1698852491
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698852467
      },
      {
        "totalLiquidityAsCollateral": "465951935545164178962487",
        "timestamp": 1698852455
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698852371
      },
      {
        "totalLiquidityAsCollateral": "423013476347",
        "timestamp": 1698851999
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698851975
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698851591
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698851531
      },
      {
        "totalLiquidityAsCollateral": "18817100168886",
        "timestamp": 1698851531
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698851435
      },
      {
        "totalLiquidityAsCollateral": "423000919440",
        "timestamp": 1698851327
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698851267
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698851267
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698851267
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698851267
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698850967
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698850967
      },
      {
        "totalLiquidityAsCollateral": "423000919440",
        "timestamp": 1698850967
      },
      {
        "totalLiquidityAsCollateral": "422983434412",
        "timestamp": 1698850607
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698850607
      },
      {
        "totalLiquidityAsCollateral": "423000919440",
        "timestamp": 1698850607
      },
      {
        "totalLiquidityAsCollateral": "18817100168886",
        "timestamp": 1698850415
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698850331
      },
      {
        "totalLiquidityAsCollateral": "424783434412",
        "timestamp": 1698850331
      },
      {
        "totalLiquidityAsCollateral": "424783434412",
        "timestamp": 1698850331
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698850331
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698850223
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849707
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698849647
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698849647
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698849647
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698849647
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698849407
      },
      {
        "totalLiquidityAsCollateral": "60592034227506",
        "timestamp": 1698849215
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "18817100168886",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "60612034227506",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "20596005921248",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698849059
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848987
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698848915
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698848915
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848915
      },
      {
        "totalLiquidityAsCollateral": "1681757240067319495932573",
        "timestamp": 1698848807
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848759
      },
      {
        "totalLiquidityAsCollateral": "60612034227506",
        "timestamp": 1698848615
      },
      {
        "totalLiquidityAsCollateral": "424783434412",
        "timestamp": 1698848231
      },
      {
        "totalLiquidityAsCollateral": "424754501752",
        "timestamp": 1698848147
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848099
      },
      {
        "totalLiquidityAsCollateral": "60662034227506",
        "timestamp": 1698848063
      },
      {
        "totalLiquidityAsCollateral": "448754501752",
        "timestamp": 1698848027
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848015
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848015
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698848015
      },
      {
        "totalLiquidityAsCollateral": "60662034227506",
        "timestamp": 1698848003
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698848003
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698848003
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698848003
      },
      {
        "totalLiquidityAsCollateral": "60553603491361",
        "timestamp": 1698847967
      },
      {
        "totalLiquidityAsCollateral": "448754501752",
        "timestamp": 1698847919
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698847907
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698847907
      },
      {
        "totalLiquidityAsCollateral": "1681757120067319495932573",
        "timestamp": 1698847907
      },
      {
        "totalLiquidityAsCollateral": "-1363339545056413628825",
        "timestamp": 1698847907
      },
      {
        "totalLiquidityAsCollateral": "-1363339545056413628825",
        "timestamp": 1698847907
      },
      {
        "totalLiquidityAsCollateral": "1681757120067319495932573",
        "timestamp": 1698847907
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698847859
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698847667
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698847667
      },
      {
        "totalLiquidityAsCollateral": "60549108922103",
        "timestamp": 1698847643
      },
      {
        "totalLiquidityAsCollateral": "18817100168885",
        "timestamp": 1698847547
      },
      {
        "totalLiquidityAsCollateral": "448754501752",
        "timestamp": 1698847511
      },
      {
        "totalLiquidityAsCollateral": "18816199979421",
        "timestamp": 1698847439
      },
      {
        "totalLiquidityAsCollateral": "60584011622103",
        "timestamp": 1698847415
      },
      {
        "totalLiquidityAsCollateral": "1681757120067319495932573",
        "timestamp": 1698847379
      },
      {
        "totalLiquidityAsCollateral": "448753754043",
        "timestamp": 1698846827
      },
      {
        "totalLiquidityAsCollateral": "1681754620067319495932573",
        "timestamp": 1698846791
      },
      {
        "totalLiquidityAsCollateral": "1681754620067319495932573",
        "timestamp": 1698846791
      },
      {
        "totalLiquidityAsCollateral": "1654166912708857534060409",
        "timestamp": 1698846791
      },
      {
        "totalLiquidityAsCollateral": "60584011622103",
        "timestamp": 1698846779
      },
      {
        "totalLiquidityAsCollateral": "448617625994",
        "timestamp": 1698846743
      },
      {
        "totalLiquidityAsCollateral": "18816199979421",
        "timestamp": 1698846743
      },
      {
        "totalLiquidityAsCollateral": "448600308913",
        "timestamp": 1698846719
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698846707
      },
      {
        "totalLiquidityAsCollateral": "1654166912708857534060409",
        "timestamp": 1698846671
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698846563
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698846539
      },
      {
        "totalLiquidityAsCollateral": "1654166912708857534060409",
        "timestamp": 1698846479
      },
      {
        "totalLiquidityAsCollateral": "1654166912708857534060409",
        "timestamp": 1698846479
      },
      {
        "totalLiquidityAsCollateral": "1654161760884201277526767",
        "timestamp": 1698846479
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698846443
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698846263
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698846179
      },
      {
        "totalLiquidityAsCollateral": "1654161760884201277526767",
        "timestamp": 1698846143
      },
      {
        "totalLiquidityAsCollateral": "448600308913",
        "timestamp": 1698846107
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698846095
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698845999
      },
      {
        "totalLiquidityAsCollateral": "448600308913",
        "timestamp": 1698845939
      },
      {
        "totalLiquidityAsCollateral": "1654158250884201277526767",
        "timestamp": 1698845807
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698845723
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698845675
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698845531
      },
      {
        "totalLiquidityAsCollateral": "1654155300884201277526767",
        "timestamp": 1698845531
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698845531
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698845531
      },
      {
        "totalLiquidityAsCollateral": "448591691321",
        "timestamp": 1698845267
      },
      {
        "totalLiquidityAsCollateral": "-22903756571949248479136780",
        "timestamp": 1698845183
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698845183
      },
      {
        "totalLiquidityAsCollateral": "448580215170",
        "timestamp": 1698845147
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698845135
      },
      {
        "totalLiquidityAsCollateral": "1654155300884201277526767",
        "timestamp": 1698845087
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698844967
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698844967
      },
      {
        "totalLiquidityAsCollateral": "448551626124",
        "timestamp": 1698844967
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698844919
      },
      {
        "totalLiquidityAsCollateral": "448551626124",
        "timestamp": 1698844799
      },
      {
        "totalLiquidityAsCollateral": "448551626124",
        "timestamp": 1698844799
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698844799
      },
      {
        "totalLiquidityAsCollateral": "65584011622103",
        "timestamp": 1698844775
      },
      {
        "totalLiquidityAsCollateral": "448551626124",
        "timestamp": 1698844727
      },
      {
        "totalLiquidityAsCollateral": "448551626124",
        "timestamp": 1698844727
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698844727
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698844667
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698844595
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698844595
      },
      {
        "totalLiquidityAsCollateral": "1654153120884201277526767",
        "timestamp": 1698844595
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698844319
      },
      {
        "totalLiquidityAsCollateral": "1654153120884201277526767",
        "timestamp": 1698844295
      },
      {
        "totalLiquidityAsCollateral": "1654149250884201277526767",
        "timestamp": 1698844199
      },
      {
        "totalLiquidityAsCollateral": "1654148697884201277526767",
        "timestamp": 1698844163
      },
      {
        "totalLiquidityAsCollateral": "1654148697884201277526767",
        "timestamp": 1698844163
      },
      {
        "totalLiquidityAsCollateral": "1654092627680047681865343",
        "timestamp": 1698844163
      },
      {
        "totalLiquidityAsCollateral": "448551626124",
        "timestamp": 1698844163
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698844163
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698844163
      },
      {
        "totalLiquidityAsCollateral": "1654092627680047681865343",
        "timestamp": 1698844115
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698844079
      },
      {
        "totalLiquidityAsCollateral": "1654087827680047681865343",
        "timestamp": 1698843959
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698843935
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698843887
      },
      {
        "totalLiquidityAsCollateral": "65604011622103",
        "timestamp": 1698843887
      },
      {
        "totalLiquidityAsCollateral": "65502900561497",
        "timestamp": 1698843887
      },
      {
        "totalLiquidityAsCollateral": "1654085597680047681865343",
        "timestamp": 1698843887
      },
      {
        "totalLiquidityAsCollateral": "1654087097680047681865343",
        "timestamp": 1698843887
      },
      {
        "totalLiquidityAsCollateral": "65502900561497",
        "timestamp": 1698843815
      },
      {
        "totalLiquidityAsCollateral": "1654085597680047681865343",
        "timestamp": 1698843815
      },
      {
        "totalLiquidityAsCollateral": "1654085597680047681865343",
        "timestamp": 1698843815
      },
      {
        "totalLiquidityAsCollateral": "448403223850",
        "timestamp": 1698843479
      },
      {
        "totalLiquidityAsCollateral": "65502900561497",
        "timestamp": 1698843431
      },
      {
        "totalLiquidityAsCollateral": "448403223850",
        "timestamp": 1698843395
      },
      {
        "totalLiquidityAsCollateral": "448403223850",
        "timestamp": 1698843371
      },
      {
        "totalLiquidityAsCollateral": "1654085597680047681865343",
        "timestamp": 1698843347
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "465951935545164178962487",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "1654083597680047681865343",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "1654083597680047681865343",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "1656986700963158323659560",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "465951935545164178962487",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698843191
      },
      {
        "totalLiquidityAsCollateral": "18866199979421",
        "timestamp": 1698842879
      },
      {
        "totalLiquidityAsCollateral": "65502900561497",
        "timestamp": 1698842867
      },
      {
        "totalLiquidityAsCollateral": "65422568331940",
        "timestamp": 1698842855
      },
      {
        "totalLiquidityAsCollateral": "18826207979421",
        "timestamp": 1698842807
      },
      {
        "totalLiquidityAsCollateral": "465951935545164178962487",
        "timestamp": 1698842807
      },
      {
        "totalLiquidityAsCollateral": "1656986700963158323659560",
        "timestamp": 1698842783
      },
      {
        "totalLiquidityAsCollateral": "4698926538587275278972526",
        "timestamp": 1698842759
      },
      {
        "totalLiquidityAsCollateral": "18826207979421",
        "timestamp": 1698842567
      },
      {
        "totalLiquidityAsCollateral": "65422568331940",
        "timestamp": 1698842351
      },
      {
        "totalLiquidityAsCollateral": "465937706898351952636827",
        "timestamp": 1698842339
      },
      {
        "totalLiquidityAsCollateral": "65422568331940",
        "timestamp": 1698842243
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841979
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841979
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841979
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841967
      },
      {
        "totalLiquidityAsCollateral": "1656981500963158323659560",
        "timestamp": 1698841931
      },
      {
        "totalLiquidityAsCollateral": "1656981500963158323659560",
        "timestamp": 1698841895
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698841727
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841727
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841727
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841727
      },
      {
        "totalLiquidityAsCollateral": "1656981500963158323659560",
        "timestamp": 1698841691
      },
      {
        "totalLiquidityAsCollateral": "38233605007059945802045",
        "timestamp": 1698841691
      },
      {
        "totalLiquidityAsCollateral": "38233605007059945802045",
        "timestamp": 1698841691
      },
      {
        "totalLiquidityAsCollateral": "1656981500963158323659560",
        "timestamp": 1698841691
      },
      {
        "totalLiquidityAsCollateral": "448403223850",
        "timestamp": 1698841679
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841679
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841679
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698841679
      },
      {
        "totalLiquidityAsCollateral": "18826207979421",
        "timestamp": 1698841655
      },
      {
        "totalLiquidityAsCollateral": "1656981500963158323659560",
        "timestamp": 1698841487
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698841199
      },
      {
        "totalLiquidityAsCollateral": "2866433541103975541954",
        "timestamp": 1698840959
      },
      {
        "totalLiquidityAsCollateral": "2866433541103975541954",
        "timestamp": 1698840959
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698840959
      },
      {
        "totalLiquidityAsCollateral": "1656981500963158323659560",
        "timestamp": 1698840611
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698840563
      },
      {
        "totalLiquidityAsCollateral": "18826207979421",
        "timestamp": 1698840491
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698840455
      },
      {
        "totalLiquidityAsCollateral": "1656979000963158323659560",
        "timestamp": 1698840299
      },
      {
        "totalLiquidityAsCollateral": "1656979000963158323659560",
        "timestamp": 1698840299
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698840299
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698840215
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698840083
      },
      {
        "totalLiquidityAsCollateral": "448403223850",
        "timestamp": 1698839999
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698839891
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698839891
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698839891
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698839891
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698839795
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698839795
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698839795
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698839747
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698839747
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698839747
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698839339
      },
      {
        "totalLiquidityAsCollateral": "466916706898351952636827",
        "timestamp": 1698839015
      },
      {
        "totalLiquidityAsCollateral": "18826207979421",
        "timestamp": 1698838943
      },
      {
        "totalLiquidityAsCollateral": "1656975059904601727210394",
        "timestamp": 1698838427
      },
      {
        "totalLiquidityAsCollateral": "18846542979421",
        "timestamp": 1698838391
      },
      {
        "totalLiquidityAsCollateral": "25023115971618190733694",
        "timestamp": 1698838223
      },
      {
        "totalLiquidityAsCollateral": "466928706898351952636827",
        "timestamp": 1698838223
      },
      {
        "totalLiquidityAsCollateral": "1656974599904601727210394",
        "timestamp": 1698838043
      },
      {
        "totalLiquidityAsCollateral": "1656974599904601727210394",
        "timestamp": 1698838043
      },
      {
        "totalLiquidityAsCollateral": "1656972629372111719488976",
        "timestamp": 1698838043
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698837899
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698837863
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698837851
      },
      {
        "totalLiquidityAsCollateral": "1656972629372111719488976",
        "timestamp": 1698837803
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698837275
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698837203
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698837203
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698837203
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698837131
      },
      {
        "totalLiquidityAsCollateral": "466931566898351952636827",
        "timestamp": 1698837095
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698837023
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836891
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836891
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836891
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836891
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836891
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836759
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836603
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698836555
      },
      {
        "totalLiquidityAsCollateral": "1898073512081075805173872",
        "timestamp": 1698836555
      },
      {
        "totalLiquidityAsCollateral": "466931566898351952636827",
        "timestamp": 1698836555
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698836495
      },
      {
        "totalLiquidityAsCollateral": "448360537506",
        "timestamp": 1698836471
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698836447
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698836447
      },
      {
        "totalLiquidityAsCollateral": "466931566898351952636827",
        "timestamp": 1698836399
      },
      {
        "totalLiquidityAsCollateral": "448360537506",
        "timestamp": 1698836351
      },
      {
        "totalLiquidityAsCollateral": "26895995528175105691043420",
        "timestamp": 1698836291
      },
      {
        "totalLiquidityAsCollateral": "18752818877896",
        "timestamp": 1698836279
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836243
      },
      {
        "totalLiquidityAsCollateral": "1656969629372111719488976",
        "timestamp": 1698836243
      },
      {
        "totalLiquidityAsCollateral": "1656965195638157994747842",
        "timestamp": 1698836243
      },
      {
        "totalLiquidityAsCollateral": "1656965195638157994747842",
        "timestamp": 1698836231
      },
      {
        "totalLiquidityAsCollateral": "466930355216117785765741",
        "timestamp": 1698836183
      },
      {
        "totalLiquidityAsCollateral": "466930355216117785765741",
        "timestamp": 1698836183
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698836183
      },
      {
        "totalLiquidityAsCollateral": "65404416516840",
        "timestamp": 1698836171
      },
      {
        "totalLiquidityAsCollateral": "1656965219708770545584336",
        "timestamp": 1698836171
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698836171
      },
      {
        "totalLiquidityAsCollateral": "1656965195638157994747842",
        "timestamp": 1698836171
      },
      {
        "totalLiquidityAsCollateral": "1656965219708770545584336",
        "timestamp": 1698836171
      },
      {
        "totalLiquidityAsCollateral": "65402760516840",
        "timestamp": 1698836159
      },
      {
        "totalLiquidityAsCollateral": "65402760516840",
        "timestamp": 1698836147
      },
      {
        "totalLiquidityAsCollateral": "3527650344072951952294",
        "timestamp": 1698836027
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698836015
      },
      {
        "totalLiquidityAsCollateral": "1656967772702892868100701",
        "timestamp": 1698835931
      },
      {
        "totalLiquidityAsCollateral": "26810995528175105691043420",
        "timestamp": 1698835907
      },
      {
        "totalLiquidityAsCollateral": "18752818877896",
        "timestamp": 1698835775
      },
      {
        "totalLiquidityAsCollateral": "18752818877896",
        "timestamp": 1698835559
      },
      {
        "totalLiquidityAsCollateral": "1656967772702892868100701",
        "timestamp": 1698835307
      },
      {
        "totalLiquidityAsCollateral": "1656967672702892868100701",
        "timestamp": 1698835139
      },
      {
        "totalLiquidityAsCollateral": "1656967672702892868100701",
        "timestamp": 1698835139
      },
      {
        "totalLiquidityAsCollateral": "1656963891396825940143655",
        "timestamp": 1698835139
      },
      {
        "totalLiquidityAsCollateral": "65402760516840",
        "timestamp": 1698834983
      },
      {
        "totalLiquidityAsCollateral": "1656963891396825940143655",
        "timestamp": 1698834707
      },
      {
        "totalLiquidityAsCollateral": "1656963891396825940143655",
        "timestamp": 1698834707
      },
      {
        "totalLiquidityAsCollateral": "1656963891396825940143655",
        "timestamp": 1698834707
      },
      {
        "totalLiquidityAsCollateral": "0",
        "timestamp": 1698834203
      },
      {
        "totalLiquidityAsCollateral": "65402760516840",
        "timestamp": 1698833879
      },
      {
        "totalLiquidityAsCollateral": "18752818877896",
        "timestamp": 1698833303
      },
      {
        "totalLiquidityAsCollateral": "1656963891396825940143655",
        "timestamp": 1698833303
      },
      {
        "totalLiquidityAsCollateral": "466930355216117785765741",
        "timestamp": 1698833303
      },
      {
        "totalLiquidityAsCollateral": "65402760516840",
        "timestamp": 1698833267
      },
      {
        "totalLiquidityAsCollateral": "65452760516840",
        "timestamp": 1698833195
      },
      {
        "totalLiquidityAsCollateral": "18752818877896",
        "timestamp": 1698833183
      },
      {
        "totalLiquidityAsCollateral": "65452760516840",
        "timestamp": 1698833183
      },
      {
        "totalLiquidityAsCollateral": "65452760516840",
        "timestamp": 1698833003
      },
      {
        "totalLiquidityAsCollateral": "18752818877896",
        "timestamp": 1698832823
      },
      {
        "totalLiquidityAsCollateral": "1656963891396825940143655",
        "timestamp": 1698832691
      }
    ]
  }
}

market_daily_snapshots = json_data["data"]["reserveParamsHistoryItems"]

with open("AAVE-V3-ETH-reserves.csv", mode="w", newline="") as csv_file:
    
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "totalLiquidityAsCollateral"])

    writer.writeheader()

    for snapshot in market_daily_snapshots:

        timestamp = datetime.utcfromtimestamp(int(snapshot["timestamp"]))
        datetime_str = timestamp.strftime("%Y-%m-%d")

        writer.writerow({
            "timestamp": datetime_str,
            "totalLiquidityAsCollateral": snapshot["totalLiquidityAsCollateral"]
        })
