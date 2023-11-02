import json
import csv
from datetime import datetime

json_data = {
  "data": {
    "marketDailySnapshots": [
      {
        "totalValueLockedUSD": "78296516.01037523959303388002426279",
        "totalBorrowBalanceUSD": "62550905.05678750566863712549447226",
        "totalDepositBalanceUSD": "78296516.01037523959303388002426279",
        "timestamp": "1698654995",
        "rates": [
          {
            "rate": "11.9972431964941708"
          },
          {
            "rate": "4.9931079912354271"
          },
          {
            "rate": "3.003593848634705"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "44428007.60860060493277132437655713",
        "dailyWithdrawUSD": "43932567.77068021166612353218072644",
        "inputTokenPriceUSD": "0.9983821934516989872532880984950193"
      },
      {
        "totalValueLockedUSD": "78595255.59207618790334561423979548",
        "totalBorrowBalanceUSD": "63114968.16360994214615710052183447",
        "totalDepositBalanceUSD": "78595255.59207618790334561423979548",
        "timestamp": "1698620567",
        "rates": [
          {
            "rate": "13.1390560211600884"
          },
          {
            "rate": "6.1390560211600884"
          },
          {
            "rate": "3.6990044810681306"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "175990599.616066571981101301720271",
        "dailyWithdrawUSD": "176024899.716802133137906357139897",
        "inputTokenPriceUSD": "1.008626888875239418844723639143262"
      },
      {
        "totalValueLockedUSD": "78618458.44208995371820046806873064",
        "totalBorrowBalanceUSD": "63014656.26278662615160839730628181",
        "totalDepositBalanceUSD": "78618458.44208995371820046806873064",
        "timestamp": "1698536735",
        "rates": [
          {
            "rate": "12.5717058077007"
          },
          {
            "rate": "5.5717058077007"
          },
          {
            "rate": "3.356099869741833"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "17917.97946396064705225043557213091",
        "dailyWithdrawUSD": "61882.16806051398999775585055211487",
        "inputTokenPriceUSD": "1.00860823812725363641096843481311"
      },
      {
        "totalValueLockedUSD": "77826347.96598317651703526688940376",
        "totalBorrowBalanceUSD": "61922684.58088882922008737657894137",
        "totalDepositBalanceUSD": "77826347.96598317651703526688940376",
        "timestamp": "1698450911",
        "rates": [
          {
            "rate": "11.9891288422442434"
          },
          {
            "rate": "4.9728221056106085"
          },
          {
            "rate": "2.9795791697583952"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2131195.58871437891825013358135913",
        "dailyWithdrawUSD": "733653.8076846279968317761063872727",
        "inputTokenPriceUSD": "0.9980211260774619618846279605548269"
      },
      {
        "totalValueLockedUSD": "75928960.38261036942302923074278478",
        "totalBorrowBalanceUSD": "61406584.19857272934493203237573888",
        "totalDepositBalanceUSD": "75928960.38261036942302923074278478",
        "timestamp": "1698361043",
        "rates": [
          {
            "rate": "15.2763416788843099"
          },
          {
            "rate": "8.2763416788843099"
          },
          {
            "rate": "5.0020179518926593"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "120252.423531030629240216839216892",
        "dailyWithdrawUSD": "224358.8153260138536621687948622189",
        "inputTokenPriceUSD": "0.9916447873927926244393225224101542"
      },
      {
        "totalValueLockedUSD": "77149305.33332372781230922434968745",
        "totalBorrowBalanceUSD": "63294700.07483939563359947453124003",
        "totalDepositBalanceUSD": "77149305.33332372781230922434968745",
        "timestamp": "1698265583",
        "rates": [
          {
            "rate": "19.6566976857796408"
          },
          {
            "rate": "12.6566976857796408"
          },
          {
            "rate": "7.7296560822465332"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "45128214.15075564390407139165289427",
        "dailyWithdrawUSD": "45202034.8674848226942259368370378",
        "inputTokenPriceUSD": "1.00647318725159279715901026620495"
      },
      {
        "totalValueLockedUSD": "76434742.58541494526417122862952907",
        "totalBorrowBalanceUSD": "62555117.75491324753894936934637061",
        "totalDepositBalanceUSD": "76434742.58541494526417122862952907",
        "timestamp": "1698186311",
        "rates": [
          {
            "rate": "18.9043804448128545"
          },
          {
            "rate": "11.9043804448128545"
          },
          {
            "rate": "7.2557501452154429"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "90412520.49585876432841215535021774",
        "dailyWithdrawUSD": "91103562.45252825320271458997937952",
        "inputTokenPriceUSD": "0.9964271032596274112701435653178288"
      },
      {
        "totalValueLockedUSD": "77478461.31075321209060190523543507",
        "totalBorrowBalanceUSD": "61825275.33904466316624216024708473",
        "totalDepositBalanceUSD": "77478461.31075321209060190523543507",
        "timestamp": "1698105371",
        "rates": [
          {
            "rate": "11.9949171484497096"
          },
          {
            "rate": "4.987292871124274"
          },
          {
            "rate": "2.9971886425175085"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "220633185.5797026419284119175649415",
        "dailyWithdrawUSD": "220637675.8475292490024770914966116",
        "inputTokenPriceUSD": "1.001100932680112031356169007756026"
      },
      {
        "totalValueLockedUSD": "77098989.26032297505040859367763588",
        "totalBorrowBalanceUSD": "61836183.75441155393695988758693632",
        "totalDepositBalanceUSD": "77098989.26032297505040859367763588",
        "timestamp": "1698016403",
        "rates": [
          {
            "rate": "12.7634413683439376"
          },
          {
            "rate": "5.7634413683439376"
          },
          {
            "rate": "3.4721857236237265"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "44551529.90282827005250994483531323",
        "dailyWithdrawUSD": "45197342.94933499686468717064417294",
        "inputTokenPriceUSD": "0.9957454232886581147857960406837793"
      },
      {
        "totalValueLockedUSD": "77560915.74031793212487678793693936",
        "totalBorrowBalanceUSD": "61739182.1630031900385816806391946",
        "totalDepositBalanceUSD": "77560915.74031793212487678793693936",
        "timestamp": "1697913383",
        "rates": [
          {
            "rate": "11.9900213621045962"
          },
          {
            "rate": "4.9750534052614904"
          },
          {
            "rate": "2.9825557477804568"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2216324.787496654906464442473026339",
        "dailyWithdrawUSD": "2222867.570468516930572591877644058",
        "inputTokenPriceUSD": "0.9935357805536912299827928049922065"
      },
      {
        "totalValueLockedUSD": "78700315.01305877488913434588391967",
        "totalBorrowBalanceUSD": "62541357.04317864942009351948043808",
        "totalDepositBalanceUSD": "78700315.01305877488913434588391967",
        "timestamp": "1697843639",
        "rates": [
          {
            "rate": "11.9866923721209553"
          },
          {
            "rate": "4.9667309303023883"
          },
          {
            "rate": "2.9727005884256319"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4614217.654605340142327006004707402",
        "dailyWithdrawUSD": "4289048.319769024316558507262819458",
        "inputTokenPriceUSD": "1.008134783072583993618789601976117"
      },
      {
        "totalValueLockedUSD": "77533055.57530660476951771665382668",
        "totalBorrowBalanceUSD": "62194074.92064869753452995219962665",
        "totalDepositBalanceUSD": "77533055.57530660476951771665382668",
        "timestamp": "1697757695",
        "rates": [
          {
            "rate": "12.8106205779026728"
          },
          {
            "rate": "5.8106205779026728"
          },
          {
            "rate": "3.5006610898873641"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "88801254.28461636793286801298498027",
        "dailyWithdrawUSD": "88921907.30062013632889605478795271",
        "inputTokenPriceUSD": "0.9974567891666820099787676748513796"
      },
      {
        "totalValueLockedUSD": "77461988.12420275235059535060387107",
        "totalBorrowBalanceUSD": "62058748.46163991593010399690108343",
        "totalDepositBalanceUSD": "77461988.12420275235059535060387107",
        "timestamp": "1697662943",
        "rates": [
          {
            "rate": "12.4314730829498178"
          },
          {
            "rate": "5.4314730829498178"
          },
          {
            "rate": "3.2718736613465722"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "132719587.7999236840205828372327453",
        "dailyWithdrawUSD": "133362469.2884192384460655206697361",
        "inputTokenPriceUSD": "0.9951310109955086574599937177824726"
      },
      {
        "totalValueLockedUSD": "78877740.71836551025643717780868547",
        "totalBorrowBalanceUSD": "62672741.07976447491639742149539557",
        "totalDepositBalanceUSD": "78877740.71836551025643717780868547",
        "timestamp": "1697586227",
        "rates": [
          {
            "rate": "11.9863877283691739"
          },
          {
            "rate": "4.9659693209229348"
          },
          {
            "rate": "2.9717276970945703"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "223055803.5608813844098793378262026",
        "dailyWithdrawUSD": "222989520.3901565218232666116858369",
        "inputTokenPriceUSD": "1.005106327500691793621926751017465"
      },
      {
        "totalValueLockedUSD": "78120730.81331762570158695794870741",
        "totalBorrowBalanceUSD": "62201747.44376204277440424564130102",
        "totalDepositBalanceUSD": "78120730.81331762570158695794870741",
        "timestamp": "1697500547",
        "rates": [
          {
            "rate": "11.9905637217816809"
          },
          {
            "rate": "4.9764093044542021"
          },
          {
            "rate": "2.9840991215120669"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4461812.131505044177791690450979353",
        "dailyWithdrawUSD": "2851889.080438169790954216540030902",
        "inputTokenPriceUSD": "0.9964094590553972525214510908170112"
      },
      {
        "totalValueLockedUSD": "76832013.36032900895128419251381227",
        "totalBorrowBalanceUSD": "62029286.02738123300703941482615344",
        "totalDepositBalanceUSD": "76832013.36032900895128419251381227",
        "timestamp": "1697413931",
        "rates": [
          {
            "rate": "14.7510234139789987"
          },
          {
            "rate": "7.7510234139789987"
          },
          {
            "rate": "4.6803345028546895"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2141139.923101354636769239879634058",
        "dailyWithdrawUSD": "1848230.410211695030061622189963188",
        "inputTokenPriceUSD": "1.000680593292803624505786227046536"
      },
      {
        "totalValueLockedUSD": "76463214.58402746610508309073904681",
        "totalBorrowBalanceUSD": "62017110.16292505815277622416207163",
        "totalDepositBalanceUSD": "76463214.58402746610508309073904681",
        "timestamp": "1697324951",
        "rates": [
          {
            "rate": "16.1515434620064769"
          },
          {
            "rate": "9.1515434620064769"
          },
          {
            "rate": "5.541002434594716"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1580531.150568458077534480426877684",
        "dailyWithdrawUSD": "2742259.608834310706586524076979515",
        "inputTokenPriceUSD": "0.999884021082888753467130786567338"
      },
      {
        "totalValueLockedUSD": "77725469.83923030953382097876301414",
        "totalBorrowBalanceUSD": "62165027.13318735766707424956648895",
        "totalDepositBalanceUSD": "77725469.83923030953382097876301414",
        "timestamp": "1697239847",
        "rates": [
          {
            "rate": "11.999505338081597"
          },
          {
            "rate": "4.9987633452039924"
          },
          {
            "rate": "3.0107722194114452"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1676978.223199677198987541792801377",
        "dailyWithdrawUSD": "1935454.430251693963534848120756005",
        "inputTokenPriceUSD": "1.001388921713428618538267366579411"
      },
      {
        "totalValueLockedUSD": "77967552.94479045940621062713861238",
        "totalBorrowBalanceUSD": "62151887.1169126910935625329394399",
        "totalDepositBalanceUSD": "77967552.94479045940621062713861238",
        "timestamp": "1697146043",
        "rates": [
          {
            "rate": "11.9928757074445559"
          },
          {
            "rate": "4.9821892686113897"
          },
          {
            "rate": "2.9910305233346772"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1636544.810779382828138552485296125",
        "dailyWithdrawUSD": "2174252.835073532962786859640050917",
        "inputTokenPriceUSD": "1.001339560704627249313853906566873"
      },
      {
        "totalValueLockedUSD": "78378231.10075199445900432609325934",
        "totalBorrowBalanceUSD": "63243157.86955215974720955413408466",
        "totalDepositBalanceUSD": "78378231.10075199445900432609325934",
        "timestamp": "1697065631",
        "rates": [
          {
            "rate": "14.5862209876266884"
          },
          {
            "rate": "7.5862209876266884"
          },
          {
            "rate": "4.5798045564879976"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1009997.353063194837647260152765143",
        "dailyWithdrawUSD": "1720729.638338547144155423707484106",
        "inputTokenPriceUSD": "0.9998298983821934952647010546123212"
      },
      {
        "totalValueLockedUSD": "79107266.64098509791231387941956538",
        "totalBorrowBalanceUSD": "63304751.96093052299227000887056597",
        "totalDepositBalanceUSD": "79107266.64098509791231387941956538",
        "timestamp": "1696982219",
        "rates": [
          {
            "rate": "12.0896335019965569"
          },
          {
            "rate": "5.0896335019965569"
          },
          {
            "rate": "3.0665180176317586"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4348722.42687386509667685578725967",
        "dailyWithdrawUSD": "1270609.967046642046016946906754142",
        "inputTokenPriceUSD": "1.000204157882251229845817065897489"
      },
      {
        "totalValueLockedUSD": "75935300.68948090190996896910051647",
        "totalBorrowBalanceUSD": "64540521.70241500293411410538737596",
        "totalDepositBalanceUSD": "75935300.68948090190996896910051647",
        "timestamp": "1696894043",
        "rates": [
          {
            "rate": "30.727699006263753"
          },
          {
            "rate": "23.727699006263753"
          },
          {
            "rate": "14.9628527775880387"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1239089.026527916239942103763423085",
        "dailyWithdrawUSD": "12750974.52949158785059512197593861",
        "inputTokenPriceUSD": "0.9992904431761986241325435465732214"
      },
      {
        "totalValueLockedUSD": "88204205.90834148855568179309497965",
        "totalBorrowBalanceUSD": "68601571.02884990397056911203173267",
        "totalDepositBalanceUSD": "88204205.90834148855568179309497965",
        "timestamp": "1696802975",
        "rates": [
          {
            "rate": "11.944395423336134"
          },
          {
            "rate": "4.8609885583403349"
          },
          {
            "rate": "2.8480703459038791"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4993.822449551435621934262171568458",
        "dailyWithdrawUSD": "92395.22612060247953459304948728143",
        "inputTokenPriceUSD": "1.008379037116098738043422027908532"
      },
      {
        "totalValueLockedUSD": "87432317.13827405982514827889650631",
        "totalBorrowBalanceUSD": "68052552.83961958463854890412007498",
        "totalDepositBalanceUSD": "87432317.13827405982514827889650631",
        "timestamp": "1696722983",
        "rates": [
          {
            "rate": "11.9458629839712475"
          },
          {
            "rate": "4.8646574599281189"
          },
          {
            "rate": "2.8523089996850946"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "88008304.76984328720056682385660781",
        "dailyWithdrawUSD": "88019508.97500430410455321983388835",
        "inputTokenPriceUSD": "0.9986524903051356053520581048912073"
      },
      {
        "totalValueLockedUSD": "87653301.74197193651928360914885914",
        "totalBorrowBalanceUSD": "68159362.33036028734489116455302234",
        "totalDepositBalanceUSD": "87653301.74197193651928360914885914",
        "timestamp": "1696636391",
        "rates": [
          {
            "rate": "11.9440035897770024"
          },
          {
            "rate": "4.8600089744425061"
          },
          {
            "rate": "2.8469247560576912"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "400169.19599239738577586347945766",
        "dailyWithdrawUSD": "2168.463759887726900517149146457471",
        "inputTokenPriceUSD": "1.001151669393153259074315906126189"
      },
      {
        "totalValueLockedUSD": "87435378.56319325934441078723163358",
        "totalBorrowBalanceUSD": "68468218.12159370802515876025643948",
        "totalDepositBalanceUSD": "87435378.56319325934441078723163358",
        "timestamp": "1696545227",
        "rates": [
          {
            "rate": "11.9576797739521447"
          },
          {
            "rate": "4.8941994348803618"
          },
          {
            "rate": "2.8867445254300465"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "90804667.61800610871548530379911594",
        "dailyWithdrawUSD": "91962159.22364536880571843350671543",
        "inputTokenPriceUSD": "1.003326213435429373948921333042663"
      },
      {
        "totalValueLockedUSD": "88410325.62224959730792669262752989",
        "totalBorrowBalanceUSD": "67333443.31702382313014809497320551",
        "totalDepositBalanceUSD": "88410325.62224959730792669262752989",
        "timestamp": "1696462415",
        "rates": [
          {
            "rate": "11.9040031375665264"
          },
          {
            "rate": "4.7600078439163161"
          },
          {
            "rate": "2.7322012788591401"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "875345.5935065351516198585994543066",
        "dailyWithdrawUSD": "1209593.484797289219408070325851572",
        "inputTokenPriceUSD": "1.001202470452140946326299586244146"
      },
      {
        "totalValueLockedUSD": "88543794.30630071942404142516438388",
        "totalBorrowBalanceUSD": "67177854.76578372127426878392463326",
        "totalDepositBalanceUSD": "88543794.30630071942404142516438388",
        "timestamp": "1696377395",
        "rates": [
          {
            "rate": "11.8967401141420819"
          },
          {
            "rate": "4.7418502853552046"
          },
          {
            "rate": "2.7116292631002073"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "988856.98055890490920330333748747",
        "dailyWithdrawUSD": "2043940.473724245328356004432898682",
        "inputTokenPriceUSD": "0.999034230254759753559711317946127"
      },
      {
        "totalValueLockedUSD": "89596017.62001196431161206005398123",
        "totalBorrowBalanceUSD": "71668999.8169604635562722809694299",
        "totalDepositBalanceUSD": "89596017.62001196431161206005398123",
        "timestamp": "1696289987",
        "rates": [
          {
            "rate": "11.9997811305083724"
          },
          {
            "rate": "4.9994528262709309"
          },
          {
            "rate": "3.0105485349453225"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "47037290.31427648730983236171420401",
        "dailyWithdrawUSD": "46437310.97133877453613658308228387",
        "inputTokenPriceUSD": "0.9991139152794056352732052907223043"
      },
      {
        "totalValueLockedUSD": "88834986.54338598512245125291471809",
        "totalBorrowBalanceUSD": "67005171.29295105547342873359684664",
        "totalDepositBalanceUSD": "88834986.54338598512245125291471809",
        "timestamp": "1696202867",
        "rates": [
          {
            "rate": "11.885663127620642"
          },
          {
            "rate": "4.7141578190516049"
          },
          {
            "rate": "2.6803556202830829"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2390240.040642127007534277293193908",
        "dailyWithdrawUSD": "1964251.340567671397478899041905053",
        "inputTokenPriceUSD": "0.9972904100887798940611514235594758"
      },
      {
        "totalValueLockedUSD": "88349430.33445961669901752985924863",
        "totalBorrowBalanceUSD": "71949517.00436798556083201620266533",
        "totalDepositBalanceUSD": "88349430.33445961669901752985924863",
        "timestamp": "1696117883",
        "rates": [
          {
            "rate": "17.3902840549802987"
          },
          {
            "rate": "10.3902840549802987"
          },
          {
            "rate": "6.3142110995268522"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1630302.071928849873079189745592022",
        "dailyWithdrawUSD": "2435994.976424514331569106150512984",
        "inputTokenPriceUSD": "0.9967644968897844405826277574407684"
      },
      {
        "totalValueLockedUSD": "89569677.94229284013924089827853564",
        "totalBorrowBalanceUSD": "55383704.49622520764484622320281674",
        "totalDepositBalanceUSD": "89569677.94229284013924089827853564",
        "timestamp": "1696026899",
        "rates": [
          {
            "rate": "11.5458267496088418"
          },
          {
            "rate": "3.8645668740221046"
          },
          {
            "rate": "1.8126756753823621"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2655662.108797813202875969113330209",
        "dailyWithdrawUSD": "1533256.285402665094557263355722504",
        "inputTokenPriceUSD": "1.001588857762484966073573239025212"
      },
      {
        "totalValueLockedUSD": "87996213.49766635760752976172911335",
        "totalBorrowBalanceUSD": "66227012.40667356336797175837852248",
        "totalDepositBalanceUSD": "87996213.49766635760752976172911335",
        "timestamp": "1695930767",
        "rates": [
          {
            "rate": "11.8815293906494263"
          },
          {
            "rate": "4.7038234766235658"
          },
          {
            "rate": "2.6690688856026756"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "44226502.25061638370188689789128775",
        "dailyWithdrawUSD": "44823616.80762591857780103413436904",
        "inputTokenPriceUSD": "0.9966004815241370820292920273419754"
      },
      {
        "totalValueLockedUSD": "89721119.15723746164800412878898764",
        "totalBorrowBalanceUSD": "66945265.80295621512929350032692427",
        "totalDepositBalanceUSD": "89721119.15723746164800412878898764",
        "timestamp": "1695857627",
        "rates": [
          {
            "rate": "11.865370124589912"
          },
          {
            "rate": "4.6634253114747799"
          },
          {
            "rate": "2.6238885865320728"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "91519774.26871447295546339328386866",
        "dailyWithdrawUSD": "90454986.42981401528328635598860599",
        "inputTokenPriceUSD": "1.0093844487630023519890436751761"
      },
      {
        "totalValueLockedUSD": "87721224.34270889635894197380745154",
        "totalBorrowBalanceUSD": "66238347.27876150011251652770397641",
        "totalDepositBalanceUSD": "87721224.34270889635894197380745154",
        "timestamp": "1695771743",
        "rates": [
          {
            "rate": "11.8877506568311297"
          },
          {
            "rate": "4.7193766420778242"
          },
          {
            "rate": "2.6866021389876749"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "124266.4835215214822998550701000178",
        "dailyWithdrawUSD": "1204434.902729997119126872025548657",
        "inputTokenPriceUSD": "0.9989754870207966533951642045940049"
      },
      {
        "totalValueLockedUSD": "88842107.31165243647900635725176114",
        "totalBorrowBalanceUSD": "66268569.0673035664233602480078998",
        "totalDepositBalanceUSD": "88842107.31165243647900635725176114",
        "timestamp": "1695672419",
        "rates": [
          {
            "rate": "11.8647841581014565"
          },
          {
            "rate": "4.6619603952536412"
          },
          {
            "rate": "2.6222564922429736"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "177609804.4981712034986462817418182",
        "dailyWithdrawUSD": "177580825.8875652257914998704268305",
        "inputTokenPriceUSD": "0.9995512066049013357687816428451682"
      },
      {
        "totalValueLockedUSD": "88822988.78432718712857602709782675",
        "totalBorrowBalanceUSD": "66233847.0817008682665026844278034",
        "totalDepositBalanceUSD": "88822988.78432718712857602709782675",
        "timestamp": "1695599627",
        "rates": [
          {
            "rate": "11.8642082604813806"
          },
          {
            "rate": "4.6605206512034515"
          },
          {
            "rate": "2.620665709772821"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "132874234.881199924766489567740052",
        "dailyWithdrawUSD": "132884308.7415363204161825287003093",
        "inputTokenPriceUSD": "0.9997578078982118654655681687612705"
      },
      {
        "totalValueLockedUSD": "88799520.96976411607326356985005032",
        "totalBorrowBalanceUSD": "66206434.76179925478541266229018856",
        "totalDepositBalanceUSD": "88799520.96976411607326356985005032",
        "timestamp": "1695511871",
        "rates": [
          {
            "rate": "11.863929184505015"
          },
          {
            "rate": "4.6598229612625374"
          },
          {
            "rate": "2.6198884028401422"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "263324240.8250323241744256507999785",
        "dailyWithdrawUSD": "263473916.3515298789237407178953303",
        "inputTokenPriceUSD": "0.9994626183912764880780350749323929"
      },
      {
        "totalValueLockedUSD": "88669637.89166256984272055311059303",
        "totalBorrowBalanceUSD": "65958529.92907406522083788202403205",
        "totalDepositBalanceUSD": "88669637.89166256984272055311059303",
        "timestamp": "1695427175",
        "rates": [
          {
            "rate": "11.8596699047599335"
          },
          {
            "rate": "4.6491747618998337"
          },
          {
            "rate": "2.6080627977441504"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "526497587.4850972102512098064363292",
        "dailyWithdrawUSD": "526497796.074324938193865673634366",
        "inputTokenPriceUSD": "0.9964095092529309655407385962583754"
      },
      {
        "totalValueLockedUSD": "89413730.87349491528320365298798675",
        "totalBorrowBalanceUSD": "66555737.0080098405690918764230481",
        "totalDepositBalanceUSD": "89413730.87349491528320365298798675",
        "timestamp": "1695322043",
        "rates": [
          {
            "rate": "11.8608917513575414"
          },
          {
            "rate": "4.6522293783938536"
          },
          {
            "rate": "2.6114463111091171"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4879869.090804378897041796158783081",
        "dailyWithdrawUSD": "5262721.754853795779073517460706316",
        "inputTokenPriceUSD": "1.004885325746072534673594787108539"
      },
      {
        "totalValueLockedUSD": "89598740.50870150082476679019582961",
        "totalBorrowBalanceUSD": "66771299.94557133249796740549316967",
        "totalDepositBalanceUSD": "89598740.50870150082476679019582961",
        "timestamp": "1695251111",
        "rates": [
          {
            "rate": "11.8630639310460848"
          },
          {
            "rate": "4.6576598276152119"
          },
          {
            "rate": "2.6174087017304659"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "709.0888589399659148574296336792045",
        "dailyWithdrawUSD": "538705.0390330902513160392169907763",
        "inputTokenPriceUSD": "1.002798688692851931644494511039992"
      },
      {
        "totalValueLockedUSD": "89875842.15482623530267853396649916",
        "totalBorrowBalanceUSD": "66609077.7374339585232978498654942",
        "totalDepositBalanceUSD": "89875842.15482623530267853396649916",
        "timestamp": "1695152255",
        "rates": [
          {
            "rate": "11.852807416232317"
          },
          {
            "rate": "4.6320185405807924"
          },
          {
            "rate": "2.5889426480856926"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "133524494.4976378252543828884917853",
        "dailyWithdrawUSD": "133989467.8405700057920736859002741",
        "inputTokenPriceUSD": "1.000003305262338078042948294005566"
      },
      {
        "totalValueLockedUSD": "90343379.34238987255811367043332409",
        "totalBorrowBalanceUSD": "66613677.05603430453823546453518879",
        "totalDepositBalanceUSD": "90343379.34238987255811367043332409",
        "timestamp": "1695065627",
        "rates": [
          {
            "rate": "11.843346206842626"
          },
          {
            "rate": "4.608365517106565"
          },
          {
            "rate": "2.5628274178762657"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "440302502.1830159933366214319839148",
        "dailyWithdrawUSD": "441579933.8979344144692075995281338",
        "inputTokenPriceUSD": "1.000130180656453727015578162201627"
      },
      {
        "totalValueLockedUSD": "91563505.44768601693626088604412491",
        "totalBorrowBalanceUSD": "66703480.63332398850515065707666999",
        "totalDepositBalanceUSD": "91563505.44768601693626088604412491",
        "timestamp": "1694994995",
        "rates": [
          {
            "rate": "11.8212347226158286"
          },
          {
            "rate": "4.5530868065395716"
          },
          {
            "rate": "2.5022922083980552"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "272318.8294822344075574877980298246",
        "dailyWithdrawUSD": "1050815.519110285560295602561679395",
        "inputTokenPriceUSD": "0.9995890977950972229484708538778233"
      },
      {
        "totalValueLockedUSD": "92051585.67254701472837633770723573",
        "totalBorrowBalanceUSD": "66116043.51775395202673930657654409",
        "totalDepositBalanceUSD": "92051585.67254701472837633770723573",
        "timestamp": "1694900327",
        "rates": [
          {
            "rate": "11.795624080512588"
          },
          {
            "rate": "4.4890602012814699"
          },
          {
            "rate": "2.4332411165635012"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "175390722.8684098383891942234727904",
        "dailyWithdrawUSD": "175391459.7476473610741766740488719",
        "inputTokenPriceUSD": "0.9965381981159649908476943609555633"
      },
      {
        "totalValueLockedUSD": "92044879.5344562790323873814603889",
        "totalBorrowBalanceUSD": "66038235.84593591713698546491389527",
        "totalDepositBalanceUSD": "92044879.5344562790323873814603889",
        "timestamp": "1694821535",
        "rates": [
          {
            "rate": "11.7936415987711249"
          },
          {
            "rate": "4.4841039969278121"
          },
          {
            "rate": "2.4279413720140415"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "487829667.0417364183150000166473839",
        "dailyWithdrawUSD": "487856121.0559231391787681766196615",
        "inputTokenPriceUSD": "0.9965381981159649908476943609555633"
      },
      {
        "totalValueLockedUSD": "93205168.86720482779866597758291397",
        "totalBorrowBalanceUSD": "66851398.73728138060316286342605329",
        "totalDepositBalanceUSD": "93205168.86720482779866597758291397",
        "timestamp": "1694733695",
        "rates": [
          {
            "rate": "11.7931240661986002"
          },
          {
            "rate": "4.4828101654965005"
          },
          {
            "rate": "2.4265535379292982"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "188238220.8726080089750742943240111",
        "dailyWithdrawUSD": "182372690.1306650591356120669101167",
        "inputTokenPriceUSD": "1.008904128655372565114240596699838"
      },
      {
        "totalValueLockedUSD": "86310091.82520002053104158903138655",
        "totalBorrowBalanceUSD": "71327050.0036454022228137358440931",
        "totalDepositBalanceUSD": "86310091.82520002053104158903138655",
        "timestamp": "1694649467",
        "rates": [
          {
            "rate": "21.9015654906407875"
          },
          {
            "rate": "14.9015654906407875"
          },
          {
            "rate": "9.1661675230831514"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "177517730.8228751938955872368689373",
        "dailyWithdrawUSD": "178647986.826112043657178447823344",
        "inputTokenPriceUSD": "0.9977165815894225739811327211130503"
      },
      {
        "totalValueLockedUSD": "88368426.7889755912712247830787977",
        "totalBorrowBalanceUSD": "67059942.02314577094587438325379905",
        "totalDepositBalanceUSD": "88368426.7889755912712247830787977",
        "timestamp": "1694562563",
        "rates": [
          {
            "rate": "11.897168391223721"
          },
          {
            "rate": "4.7429209780593025"
          },
          {
            "rate": "2.7132252604195203"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "338001059.5359104270591382649673932",
        "dailyWithdrawUSD": "341288096.7440688960392983596512416",
        "inputTokenPriceUSD": "1.00848879228722346360536049874284"
      },
      {
        "totalValueLockedUSD": "91417295.33481427110727084744990633",
        "totalBorrowBalanceUSD": "76457387.08556645955020215664714913",
        "totalDepositBalanceUSD": "91417295.33481427110727084744990633",
        "timestamp": "1694476295",
        "rates": [
          {
            "rate": "25.6333087160929981"
          },
          {
            "rate": "18.6333087160929981"
          },
          {
            "rate": "11.5922867558267396"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "316958507.9667052791218710221754543",
        "dailyWithdrawUSD": "309588088.6729141830521850179110409",
        "inputTokenPriceUSD": "1.005694059168697947827614655647979"
      },
      {
        "totalValueLockedUSD": "83128953.14163440211308067651154974",
        "totalBorrowBalanceUSD": "69770947.42033622160285605261673565",
        "totalDepositBalanceUSD": "83128953.14163440211308067651154974",
        "timestamp": "1694389835",
        "rates": [
          {
            "rate": "26.7410511362062823"
          },
          {
            "rate": "19.7410511362062823"
          },
          {
            "rate": "12.3129816692903444"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "134182634.2787503098228623909502667",
        "dailyWithdrawUSD": "141297305.3597321159873693270581",
        "inputTokenPriceUSD": "0.9951753403714787620719538379323553"
      },
      {
        "totalValueLockedUSD": "90711569.5729159848771664886190452",
        "totalBorrowBalanceUSD": "71061669.30035354708719328786749737",
        "totalDepositBalanceUSD": "90711569.5729159848771664886190452",
        "timestamp": "1694283851",
        "rates": [
          {
            "rate": "11.9584503315863419"
          },
          {
            "rate": "4.8961258289658549"
          },
          {
            "rate": "2.8887671573982607"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "89414855.18212075319572524064503658",
        "dailyWithdrawUSD": "90166321.45010543055399046642318615",
        "inputTokenPriceUSD": "1.001135065088705555109163059885001"
      },
      {
        "totalValueLockedUSD": "90805932.57094636988567583387172034",
        "totalBorrowBalanceUSD": "70551013.1528733544940704938816679",
        "totalDepositBalanceUSD": "90805932.57094636988567583387172034",
        "timestamp": "1694216519",
        "rates": [
          {
            "rate": "11.9423561798197312"
          },
          {
            "rate": "4.8558904495493279"
          },
          {
            "rate": "2.8418961363210055"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "397037562.8432895352813609563249382",
        "dailyWithdrawUSD": "398004245.4574197371496848463648768",
        "inputTokenPriceUSD": "0.9940616537951433205075267969459546"
      },
      {
        "totalValueLockedUSD": "92167005.5992832106130572451585546",
        "totalBorrowBalanceUSD": "70850464.04039654876868041019549319",
        "totalDepositBalanceUSD": "92167005.5992832106130572451585546",
        "timestamp": "1694125211",
        "rates": [
          {
            "rate": "11.9217950159926249"
          },
          {
            "rate": "4.8044875399815623"
          },
          {
            "rate": "2.782574473997067"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "225509882.3100926093288644686015285",
        "dailyWithdrawUSD": "220585494.1845896910322501260459983",
        "inputTokenPriceUSD": "0.9984754361682211590874103175033727"
      },
      {
        "totalValueLockedUSD": "87663322.84246735770764930474051463",
        "totalBorrowBalanceUSD": "71172325.62352242261562224187796145",
        "totalDepositBalanceUSD": "87663322.84246735770764930474051463",
        "timestamp": "1694041067",
        "rates": [
          {
            "rate": "16.455848340700704"
          },
          {
            "rate": "9.455848340700704"
          },
          {
            "rate": "5.7331314399068535"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "133572212.7109251550879361910076526",
        "dailyWithdrawUSD": "133947159.710941558441329525392192",
        "inputTokenPriceUSD": "1.003246996741667852763046168225583"
      },
      {
        "totalValueLockedUSD": "87962029.05096921548071035932369999",
        "totalBorrowBalanceUSD": "71127495.82154893334158964289591621",
        "totalDepositBalanceUSD": "87962029.05096921548071035932369999",
        "timestamp": "1693951343",
        "rates": [
          {
            "rate": "15.2308431439414234"
          },
          {
            "rate": "8.2308431439414234"
          },
          {
            "rate": "4.9771107483235931"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "292907778.7970511969629009599774438",
        "dailyWithdrawUSD": "290340389.7742333357969433519758359",
        "inputTokenPriceUSD": "1.00256335966023126144692087210276"
      },
      {
        "totalValueLockedUSD": "85049971.10054153141195084954798701",
        "totalBorrowBalanceUSD": "70850703.14762077500100477764851955",
        "totalDepositBalanceUSD": "85049971.10054153141195084954798701",
        "timestamp": "1693861703",
        "rates": [
          {
            "rate": "24.392849137845468"
          },
          {
            "rate": "17.392849137845468"
          },
          {
            "rate": "10.7750776574787588"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "44034711.25058045411672590718795473",
        "dailyWithdrawUSD": "48844187.8507557564350282088276599",
        "inputTokenPriceUSD": "0.9988565735578803981779831442912195"
      },
      {
        "totalValueLockedUSD": "89793844.86980440139133986308387699",
        "totalBorrowBalanceUSD": "71176200.90645212393502348359752304",
        "totalDepositBalanceUSD": "89793844.86980440139133986308387699",
        "timestamp": "1693783403",
        "rates": [
          {
            "rate": "11.9816551356339388"
          },
          {
            "rate": "4.9541378390848471"
          },
          {
            "rate": "2.9569665887154126"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "136077463.2240764106808653818638189",
        "dailyWithdrawUSD": "132701069.5460382462756925575683039",
        "inputTokenPriceUSD": "0.9984001064845351565660649274803012"
      },
      {
        "totalValueLockedUSD": "86608577.71354011233138274934357619",
        "totalBorrowBalanceUSD": "72513698.9604870297719990916415143",
        "totalDepositBalanceUSD": "86608577.71354011233138274934357619",
        "timestamp": "1693699151",
        "rates": [
          {
            "rate": "25.9715142111031719"
          },
          {
            "rate": "18.9715142111031719"
          },
          {
            "rate": "11.8098108431580108"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2962408.955570953403139338586042655",
        "dailyWithdrawUSD": "4910554.634846774743300572136766714",
        "inputTokenPriceUSD": "1.000791600394308938769924014006996"
      },
      {
        "totalValueLockedUSD": "87829628.5658496524290476138895235",
        "totalBorrowBalanceUSD": "72083215.28327528629442512802167142",
        "totalDepositBalanceUSD": "87829628.5658496524290476138895235",
        "timestamp": "1693611971",
        "rates": [
          {
            "rate": "19.7685253847450637"
          },
          {
            "rate": "12.7685253847450637"
          },
          {
            "rate": "7.808502222441887"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "224778721.8510891087206514985794617",
        "dailyWithdrawUSD": "227086712.9873333055169717777160309",
        "inputTokenPriceUSD": "0.9928021522770299202439675093118596"
      },
      {
        "totalValueLockedUSD": "90835348.60251948757235957557351699",
        "totalBorrowBalanceUSD": "72813634.42517881590717254102465412",
        "totalDepositBalanceUSD": "90835348.60251948757235957557351699",
        "timestamp": "1693522631",
        "rates": [
          {
            "rate": "12.5999652614031731"
          },
          {
            "rate": "5.5999652614031731"
          },
          {
            "rate": "3.3732817409770296"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "441302345.5325611684099048736470264",
        "dailyWithdrawUSD": "441169824.2526474553791010557452808",
        "inputTokenPriceUSD": "1.001133529370438859609548236166413"
      },
      {
        "totalValueLockedUSD": "90729454.14354722164623475913384031",
        "totalBorrowBalanceUSD": "72794258.36508165713154048519272088",
        "totalDepositBalanceUSD": "90729454.14354722164623475913384031",
        "timestamp": "1693425839",
        "rates": [
          {
            "rate": "12.8707246968985716"
          },
          {
            "rate": "5.8707246968985716"
          },
          {
            "rate": "3.5371212669132407"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1328245.31464149551621044769473236",
        "dailyWithdrawUSD": "1273046.431043056200389191459546409",
        "inputTokenPriceUSD": "1.001573411950240067488951302324242"
      },
      {
        "totalValueLockedUSD": "90627160.06066985189959824563912558",
        "totalBorrowBalanceUSD": "72843414.82934594526930500226995813",
        "totalDepositBalanceUSD": "90627160.06066985189959824563912558",
        "timestamp": "1693352147",
        "rates": [
          {
            "rate": "13.4137293398290915"
          },
          {
            "rate": "6.4137293398290915"
          },
          {
            "rate": "3.8665646378611176"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2501928.127028485089182125305291083",
        "dailyWithdrawUSD": "14751503.09905998135357239118819447",
        "inputTokenPriceUSD": "1.001168946699471003343100189481166"
      },
      {
        "totalValueLockedUSD": "103701165.8666079574433650202153486",
        "totalBorrowBalanceUSD": "76667920.3070864156350824276167002",
        "totalDepositBalanceUSD": "103701165.8666079574433650202153486",
        "timestamp": "1693266347",
        "rates": [
          {
            "rate": "11.8482891274229257"
          },
          {
            "rate": "4.6207228185573143"
          },
          {
            "rate": "2.5747274451141466"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "653580.2151407610127226258516606643",
        "dailyWithdrawUSD": "2135763.367528060582136140689567283",
        "inputTokenPriceUSD": "1.009289519461503164845874321550811"
      },
      {
        "totalValueLockedUSD": "104000308.0579871136338681919920324",
        "totalBorrowBalanceUSD": "73346406.17206786773951708651648531",
        "totalDepositBalanceUSD": "104000308.0579871136338681919920324",
        "timestamp": "1693175867",
        "rates": [
          {
            "rate": "11.7631285893903807"
          },
          {
            "rate": "3.5262571787807615"
          },
          {
            "rate": "2.1364106184753957"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "6485292.951492995054635853006817375",
        "dailyWithdrawUSD": "1462059.955794776991378516557042938",
        "inputTokenPriceUSD": "0.9978645680144045888907193923092985"
      },
      {
        "totalValueLockedUSD": "98814557.63854838771498960870092249",
        "totalBorrowBalanceUSD": "73281329.02702373084953916548866517",
        "totalDepositBalanceUSD": "98814557.63854838771498960870092249",
        "timestamp": "1693088219",
        "rates": [
          {
            "rate": "11.8540104119399868"
          },
          {
            "rate": "3.7080208238799736"
          },
          {
            "rate": "2.3596116696297774"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2528831.717162565775769597777807415",
        "dailyWithdrawUSD": "576891.1847251222991791462780911795",
        "inputTokenPriceUSD": "0.9963009974619488344944460126825447"
      },
      {
        "totalValueLockedUSD": "97375553.40760654305101916709892871",
        "totalBorrowBalanceUSD": "73547511.09918509179395865651122526",
        "totalDepositBalanceUSD": "97375553.40760654305101916709892871",
        "timestamp": "1693003547",
        "rates": [
          {
            "rate": "11.8882426345038458"
          },
          {
            "rate": "3.7764852690076917"
          },
          {
            "rate": "2.4466014329313173"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1418984.308527268535708280560495481",
        "dailyWithdrawUSD": "3824138.490055727947458928506360562",
        "inputTokenPriceUSD": "1.00168420514083324911563714839107"
      },
      {
        "totalValueLockedUSD": "99555922.34168670553399679419357741",
        "totalBorrowBalanceUSD": "75300746.61604886443415002823917957",
        "totalDepositBalanceUSD": "99555922.34168670553399679419357741",
        "timestamp": "1692915755",
        "rates": [
          {
            "rate": "11.8909147346212325"
          },
          {
            "rate": "3.7818294692424651"
          },
          {
            "rate": "2.452890099178176"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4455826.998828008089435107720168278",
        "dailyWithdrawUSD": "7043257.937813560707592862418625912",
        "inputTokenPriceUSD": "0.9994924823395728716284877492266538"
      },
      {
        "totalValueLockedUSD": "102132985.1595036508309262654729843",
        "totalBorrowBalanceUSD": "76803759.99788728393556732000762042",
        "totalDepositBalanceUSD": "102132985.1595036508309262654729843",
        "timestamp": "1692833171",
        "rates": [
          {
            "rate": "11.8799929748094766"
          },
          {
            "rate": "3.7599859496189531"
          },
          {
            "rate": "2.4245100488432981"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "9008954.414504629660865023512347277",
        "dailyWithdrawUSD": "10655194.9109461541136106860556405",
        "inputTokenPriceUSD": "0.9994743593088946397750393491480039"
      },
      {
        "totalValueLockedUSD": "103845120.7870194812816522171522698",
        "totalBorrowBalanceUSD": "76863344.59499572154988564599427748",
        "totalDepositBalanceUSD": "103845120.7870194812816522171522698",
        "timestamp": "1692748487",
        "rates": [
          {
            "rate": "11.8504312606914293"
          },
          {
            "rate": "3.7008625213828586"
          },
          {
            "rate": "2.3496445395974073"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4557847.84607107122732073702651445",
        "dailyWithdrawUSD": "499206.8312988549420898221473422842",
        "inputTokenPriceUSD": "1.000255386356987332631204650772866"
      },
      {
        "totalValueLockedUSD": "99410940.69638178738237108367676124",
        "totalBorrowBalanceUSD": "79734566.81373480190571143865189396",
        "totalDepositBalanceUSD": "99410940.69638178738237108367676124",
        "timestamp": "1692653927",
        "rates": [
          {
            "rate": "12.7762081040946176"
          },
          {
            "rate": "4.7762081040946176"
          },
          {
            "rate": "3.2697196884002444"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5645362.982149622558119075339564563",
        "dailyWithdrawUSD": "5892508.912824989509797362322392798",
        "inputTokenPriceUSD": "0.9963901036788731403111337002077556"
      },
      {
        "totalValueLockedUSD": "99706587.38784483961001023245534759",
        "totalBorrowBalanceUSD": "79745504.75277842484104991602970746",
        "totalDepositBalanceUSD": "99706587.38784483961001023245534759",
        "timestamp": "1692570131",
        "rates": [
          {
            "rate": "11.9995032998985175"
          },
          {
            "rate": "3.999006599797035"
          },
          {
            "rate": "2.7381479595970016"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2208014.42113268067240393478536889",
        "dailyWithdrawUSD": "168948.3827486305041526926781251096",
        "inputTokenPriceUSD": "0.9973134619664617166662284182190737"
      },
      {
        "totalValueLockedUSD": "97284849.21108728603130320811402845",
        "totalBorrowBalanceUSD": "80315166.36214915635430385164693491",
        "totalDepositBalanceUSD": "97284849.21108728603130320811402845",
        "timestamp": "1692488927",
        "rates": [
          {
            "rate": "21.5874689022963492"
          },
          {
            "rate": "13.5874689022963492"
          },
          {
            "rate": "9.4759287676040892"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "935303.3286979637903786726942023203",
        "dailyWithdrawUSD": "3778148.106781279862216032014721802",
        "inputTokenPriceUSD": "0.9936071548159468372616068321397867"
      },
      {
        "totalValueLockedUSD": "101262113.5378508509242730259386311",
        "totalBorrowBalanceUSD": "78429046.12081132274568340636161871",
        "totalDepositBalanceUSD": "101262113.5378508509242730259386311",
        "timestamp": "1692402731",
        "rates": [
          {
            "rate": "11.9362869303605024"
          },
          {
            "rate": "3.8725738607210048"
          },
          {
            "rate": "2.569788088367741"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "600415974.3130822655840498990412553",
        "dailyWithdrawUSD": "602834475.2232657935151871181619919",
        "inputTokenPriceUSD": "1.003910806473352186918459050045304"
      },
      {
        "totalValueLockedUSD": "102317123.1694080485600360952471919",
        "totalBorrowBalanceUSD": "83731568.45704370329951427350365676",
        "totalDepositBalanceUSD": "102317123.1694080485600360952471919",
        "timestamp": "1692316535",
        "rates": [
          {
            "rate": "18.8823698374848533"
          },
          {
            "rate": "10.8823698374848533"
          },
          {
            "rate": "7.5368517136901074"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3728083.926908756334113315011354474",
        "dailyWithdrawUSD": "6951370.010545846670498451118063872",
        "inputTokenPriceUSD": "0.9911039396638408070782537699696308"
      },
      {
        "totalValueLockedUSD": "106579034.4089159769294920149196864",
        "totalBorrowBalanceUSD": "85328545.42337321342543526002750109",
        "totalDepositBalanceUSD": "106579034.4089159769294920149196864",
        "timestamp": "1692219743",
        "rates": [
          {
            "rate": "12.2296652040062929"
          },
          {
            "rate": "4.2296652040062929"
          },
          {
            "rate": "2.8992227510894236"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "42761.23896200729376635524704641048",
        "dailyWithdrawUSD": "1390539.009476253321014550193872814",
        "inputTokenPriceUSD": "1.001303096142213127193731871551212"
      },
      {
        "totalValueLockedUSD": "107569427.1451291798904823107173178",
        "totalBorrowBalanceUSD": "86267870.57789975295557316461471773",
        "totalDepositBalanceUSD": "107569427.1451291798904823107173178",
        "timestamp": "1692142535",
        "rates": [
          {
            "rate": "12.7400491017121672"
          },
          {
            "rate": "4.7400491017121672"
          },
          {
            "rate": "3.2477741791842887"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "6283092.231630183690066988813530275",
        "dailyWithdrawUSD": "3679221.576217035597350106172707792",
        "inputTokenPriceUSD": "0.9980570211693921681762236599102082"
      },
      {
        "totalValueLockedUSD": "105410196.7195555456986695995578995",
        "totalBorrowBalanceUSD": "85451573.49625319394084609245544748",
        "totalDepositBalanceUSD": "105410196.7195555456986695995578995",
        "timestamp": "1692055247",
        "rates": [
          {
            "rate": "15.9964268465847641"
          },
          {
            "rate": "7.9964268465847641"
          },
          {
            "rate": "5.5008778556118213"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "206108574.5913937361099738564645268",
        "dailyWithdrawUSD": "207489360.704789433018468129692392",
        "inputTokenPriceUSD": "1.002267692471469920240816567842337"
      },
      {
        "totalValueLockedUSD": "106452053.1311334144283247485948689",
        "totalBorrowBalanceUSD": "85467849.23953907954499503824988871",
        "totalDepositBalanceUSD": "106452053.1311334144283247485948689",
        "timestamp": "1691967383",
        "rates": [
          {
            "rate": "13.0785219357685985"
          },
          {
            "rate": "5.0785219357685985"
          },
          {
            "rate": "3.4800005693497885"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "23055.94010708356516534814331317617",
        "dailyWithdrawUSD": "33672.94406303446720491561093468556",
        "inputTokenPriceUSD": "0.9991912484829341445818941617397852"
      },
      {
        "totalValueLockedUSD": "106540066.3811854029557626426208322",
        "totalBorrowBalanceUSD": "85526346.97739668273832767760850265",
        "totalDepositBalanceUSD": "106540066.3811854029557626426208322",
        "timestamp": "1691876243",
        "rates": [
          {
            "rate": "13.0357002028881551"
          },
          {
            "rate": "5.0357002028881551"
          },
          {
            "rate": "3.450625402664363"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2747755.814541158689103915718675662",
        "dailyWithdrawUSD": "401787.4014757180711032457957740291",
        "inputTokenPriceUSD": "1.000035245088405598158829029098818"
      },
      {
        "totalValueLockedUSD": "103870508.4115066596298706790112307",
        "totalBorrowBalanceUSD": "85333390.94000114613645430967896022",
        "totalDepositBalanceUSD": "103870508.4115066596298706790112307",
        "timestamp": "1691794679",
        "rates": [
          {
            "rate": "20.0759433321091886"
          },
          {
            "rate": "12.0759433321091886"
          },
          {
            "rate": "8.3904515609034566"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "323494.299306072378145660210178",
        "dailyWithdrawUSD": "1279825.518368721549625880182429732",
        "inputTokenPriceUSD": "0.9972038936021726107031875612935232"
      },
      {
        "totalValueLockedUSD": "105133928.2999838283723441596902237",
        "totalBorrowBalanceUSD": "85263482.539672027608802573648918",
        "totalDepositBalanceUSD": "105133928.2999838283723441596902237",
        "timestamp": "1691709779",
        "rates": [
          {
            "rate": "16.1243675850742408"
          },
          {
            "rate": "8.1243675850742408"
          },
          {
            "rate": "5.5904182290483083"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2160.185758249377363757908149325954",
        "dailyWithdrawUSD": "234881.0091860261780162646162402103",
        "inputTokenPriceUSD": "1.000361415731616397922004092671281"
      },
      {
        "totalValueLockedUSD": "105435473.5726797461672126834076497",
        "totalBorrowBalanceUSD": "85322030.47706382551600620074041614",
        "totalDepositBalanceUSD": "105435473.5726797461672126834076497",
        "timestamp": "1691624099",
        "rates": [
          {
            "rate": "15.4628091886433541"
          },
          {
            "rate": "7.4628091886433541"
          },
          {
            "rate": "5.1285083236005543"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1142747.618948718337107110119295632",
        "dailyWithdrawUSD": "2116434.699032573315093937561567347",
        "inputTokenPriceUSD": "1.001180243548610793014460844958812"
      },
      {
        "totalValueLockedUSD": "106372654.1208729601998414614206123",
        "totalBorrowBalanceUSD": "86953235.60118706919481502130969466",
        "totalDepositBalanceUSD": "106372654.1208729601998414614206123",
        "timestamp": "1691538683",
        "rates": [
          {
            "rate": "18.5397498992285101"
          },
          {
            "rate": "10.5397498992285101"
          },
          {
            "rate": "7.2940755619292899"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "801967574.9609396398366118538019101",
        "dailyWithdrawUSD": "806909218.4466876683223215936166438",
        "inputTokenPriceUSD": "1.000983126441058020649467300929618"
      },
      {
        "totalValueLockedUSD": "111297696.4078610231896869059371728",
        "totalBorrowBalanceUSD": "87218670.72342354036775934335923483",
        "totalDepositBalanceUSD": "111297696.4078610231896869059371728",
        "timestamp": "1691444231",
        "rates": [
          {
            "rate": "11.9591292375939239"
          },
          {
            "rate": "3.9182584751878478"
          },
          {
            "rate": "2.6323653826476898"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "217942999.7315755082989024135150997",
        "dailyWithdrawUSD": "211554823.6783134100206571203498114",
        "inputTokenPriceUSD": "1.001038146361696150165247947192392"
      },
      {
        "totalValueLockedUSD": "104542283.8510703569354599205692223",
        "totalBorrowBalanceUSD": "85694916.65090092197952058274257066",
        "totalDepositBalanceUSD": "104542283.8510703569354599205692223",
        "timestamp": "1691365619",
        "rates": [
          {
            "rate": "19.3931052041991457"
          },
          {
            "rate": "11.3931052041991457"
          },
          {
            "rate": "7.9017643377612298"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3600208.318600891106391019488881118",
        "dailyWithdrawUSD": "5087784.871065657781493659845115766",
        "inputTokenPriceUSD": "0.9977353568586585613335571473042134"
      },
      {
        "totalValueLockedUSD": "106544617.0207843417324895953097599",
        "totalBorrowBalanceUSD": "86382843.88425072203183142423856717",
        "totalDepositBalanceUSD": "106544617.0207843417324895953097599",
        "timestamp": "1691278751",
        "rates": [
          {
            "rate": "16.0374167703802995"
          },
          {
            "rate": "8.0374167703802995"
          },
          {
            "rate": "5.5296999978107407"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4575446.296477353004252462537844169",
        "dailyWithdrawUSD": "4027109.862579437824367253037342504",
        "inputTokenPriceUSD": "1.002819203153679617891393479953871"
      },
      {
        "totalValueLockedUSD": "105300512.2717579685998214234120292",
        "totalBorrowBalanceUSD": "85830227.56227288525272516634795577",
        "totalDepositBalanceUSD": "105300512.2717579685998214234120292",
        "timestamp": "1691191451",
        "rates": [
          {
            "rate": "17.6615624693195595"
          },
          {
            "rate": "9.6615624693195595"
          },
          {
            "rate": "6.671531072022676"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "167064.0238331045032311760527820257",
        "dailyWithdrawUSD": "1491410.683550688518126687771771852",
        "inputTokenPriceUSD": "0.9964340544727692707830733153119563"
      },
      {
        "totalValueLockedUSD": "106445579.0123423548661056080465616",
        "totalBorrowBalanceUSD": "86961422.90990699215000075094061365",
        "totalDepositBalanceUSD": "106445579.0123423548661056080465616",
        "timestamp": "1691103275",
        "rates": [
          {
            "rate": "18.358588905518686"
          },
          {
            "rate": "10.358588905518686"
          },
          {
            "rate": "7.1655914084756886"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "11540064.98927561102574816278762161",
        "dailyWithdrawUSD": "11748254.61234022520978581023157774",
        "inputTokenPriceUSD": "0.9949182615894749529666947493995643"
      },
      {
        "totalValueLockedUSD": "107645345.3083078086399624188569602",
        "totalBorrowBalanceUSD": "89566225.7744530041566458821506732",
        "totalDepositBalanceUSD": "107645345.3083078086399624188569602",
        "timestamp": "1691016887",
        "rates": [
          {
            "rate": "24.0183038475703032"
          },
          {
            "rate": "16.0183038475703032"
          },
          {
            "rate": "11.2567825359619207"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "855172.7072820356348601348590007279",
        "dailyWithdrawUSD": "1615260.997383895617886996753975772",
        "inputTokenPriceUSD": "1.004505557639308718746125615429461"
      },
      {
        "totalValueLockedUSD": "108334272.3626589744166519591424939",
        "totalBorrowBalanceUSD": "88850646.33207102919209478875250156",
        "totalDepositBalanceUSD": "108334272.3626589744166519591424939",
        "timestamp": "1690933127",
        "rates": [
          {
            "rate": "19.5571134938232021"
          },
          {
            "rate": "11.5571134938232021"
          },
          {
            "rate": "8.020135376722663"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "6011471.963423148445271853622567917",
        "dailyWithdrawUSD": "11527357.26914591960627148885271405",
        "inputTokenPriceUSD": "1.004086956677629026377366089907517"
      },
      {
        "totalValueLockedUSD": "113395175.0888341562993427763699932",
        "totalBorrowBalanceUSD": "92675702.51765032813425817865838867",
        "totalDepositBalanceUSD": "113395175.0888341562993427763699932",
        "timestamp": "1690847711",
        "rates": [
          {
            "rate": "18.4801680834504839"
          },
          {
            "rate": "10.4801680834504839"
          },
          {
            "rate": "7.2535871643897481"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "410807523.167815745775076662763873",
        "dailyWithdrawUSD": "420962409.4736133363177466764729927",
        "inputTokenPriceUSD": "0.9999078887556304317729245589344522"
      },
      {
        "totalValueLockedUSD": "123501319.6961113972649594326767602",
        "totalBorrowBalanceUSD": "101378004.3486351006786849651289543",
        "totalDepositBalanceUSD": "123501319.6961113972649594326767602",
        "timestamp": "1690757963",
        "rates": [
          {
            "rate": "19.8245289796233157"
          },
          {
            "rate": "11.8245289796233157"
          },
          {
            "rate": "8.2153350739755983"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "205052148.1068602041375377389596466",
        "dailyWithdrawUSD": "208717974.1494797807588652261258905",
        "inputTokenPriceUSD": "0.9999694060644734617580082683711045"
      },
      {
        "totalValueLockedUSD": "127133810.4466544436849454765187908",
        "totalBorrowBalanceUSD": "105190182.2924687683703825616968165",
        "totalDepositBalanceUSD": "127133810.4466544436849454765187908",
        "timestamp": "1690674203",
        "rates": [
          {
            "rate": "22.2738925331706779"
          },
          {
            "rate": "14.2738925331706779"
          },
          {
            "rate": "9.9891624966039129"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "923401.5684005003694678505860070417",
        "dailyWithdrawUSD": "8929615.825011093276739599790499642",
        "inputTokenPriceUSD": "0.9999859028824099987655481319500226"
      },
      {
        "totalValueLockedUSD": "134895032.6464813197079963215482711",
        "totalBorrowBalanceUSD": "105158141.5993706997879642320630687",
        "totalDepositBalanceUSD": "134895032.6464813197079963215482711",
        "timestamp": "1690586063",
        "rates": [
          {
            "rate": "11.9488875759283179"
          },
          {
            "rate": "3.8977751518566357"
          },
          {
            "rate": "2.5976847503060298"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "376429.9592838847909487837111702107",
        "dailyWithdrawUSD": "542126.7033295552479216666631275203",
        "inputTokenPriceUSD": "0.998245498753063528051464271588501"
      },
      {
        "totalValueLockedUSD": "135300481.2672651716960271475127912",
        "totalBorrowBalanceUSD": "107750497.9798029137672463111167353",
        "totalDepositBalanceUSD": "135300481.2672651716960271475127912",
        "timestamp": "1690500191",
        "rates": [
          {
            "rate": "11.9909474036620704"
          },
          {
            "rate": "3.9818948073241407"
          },
          {
            "rate": "2.7098492969555549"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "199881323.8721323686854175840849016",
        "dailyWithdrawUSD": "200107377.1894081195395462450517539",
        "inputTokenPriceUSD": "1.000105315863938347357719591684475"
      },
      {
        "totalValueLockedUSD": "135419174.2110897765482456718521106",
        "totalBorrowBalanceUSD": "107014517.1289797895380616987950088",
        "totalDepositBalanceUSD": "135419174.2110897765482456718521106",
        "timestamp": "1690415075",
        "rates": [
          {
            "rate": "11.9756152874978389"
          },
          {
            "rate": "3.9512305749956778"
          },
          {
            "rate": "2.6686505093440864"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "399849945.0156169276151735892574589",
        "dailyWithdrawUSD": "400378179.663793011253275800639453",
        "inputTokenPriceUSD": "0.9994066193606618434270879204245079"
      },
      {
        "totalValueLockedUSD": "135931618.6016237162205930002141685",
        "totalBorrowBalanceUSD": "107074726.7815274821207756783994066",
        "totalDepositBalanceUSD": "135931618.6016237162205930002141685",
        "timestamp": "1690322543",
        "rates": [
          {
            "rate": "11.969274831827751"
          },
          {
            "rate": "3.938549663655502"
          },
          {
            "rate": "2.6516586646353085"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "201.3209200055172751695295707606223",
        "dailyWithdrawUSD": "165567.0853615938288096977702896666",
        "inputTokenPriceUSD": "0.9993821295810400284566635390773856"
      },
      {
        "totalValueLockedUSD": "136212738.1872240143937445568976159",
        "totalBorrowBalanceUSD": "107157048.6803678225275431982728079",
        "totalDepositBalanceUSD": "136212738.1872240143937445568976159",
        "timestamp": "1690237367",
        "rates": [
          {
            "rate": "11.9667214962233379"
          },
          {
            "rate": "3.9334429924466758"
          },
          {
            "rate": "2.6448081339812335"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "51392.50211527530761054105664013639",
        "dailyWithdrawUSD": "183766.9959515426517032476256062372",
        "inputTokenPriceUSD": "1.00031634110976701889843965699786"
      },
      {
        "totalValueLockedUSD": "136418064.4984611168049270668226277",
        "totalBorrowBalanceUSD": "106756757.9898355790000699320574158",
        "totalDepositBalanceUSD": "136418064.4984611168049270668226277",
        "timestamp": "1690154459",
        "rates": [
          {
            "rate": "11.9564256027425674"
          },
          {
            "rate": "3.9128512054851348"
          },
          {
            "rate": "2.6174466847994505"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "68590.38740995451143438038335609634",
        "dailyWithdrawUSD": "129420.6513771874072553910811600872",
        "inputTokenPriceUSD": "1.000933177143043083007184115641314"
      },
      {
        "totalValueLockedUSD": "135843439.505924534149246613488614",
        "totalBorrowBalanceUSD": "106346250.5138179208035463161308651",
        "totalDepositBalanceUSD": "135843439.505924534149246613488614",
        "timestamp": "1690069295",
        "rates": [
          {
            "rate": "11.9571466007674577"
          },
          {
            "rate": "3.9142932015349154"
          },
          {
            "rate": "2.6193491016749958"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "13759.13604762798404129606000712146",
        "dailyWithdrawUSD": "18834.88960752366436428964235097524",
        "inputTokenPriceUSD": "0.9963571724099603280308662644387918"
      },
      {
        "totalValueLockedUSD": "136402699.8699533655188667440724733",
        "totalBorrowBalanceUSD": "106854162.1865397699614186146182862",
        "totalDepositBalanceUSD": "136402699.8699533655188667440724733",
        "timestamp": "1689979259",
        "rates": [
          {
            "rate": "11.9584312110331215"
          },
          {
            "rate": "3.9168624220662431"
          },
          {
            "rate": "2.6227525068996643"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "399742613.7134547622644612730932763",
        "dailyWithdrawUSD": "399552868.9016040252444357400430332",
        "inputTokenPriceUSD": "1.000508965432781845167306920428604"
      },
      {
        "totalValueLockedUSD": "135978903.2420940944941144146138725",
        "totalBorrowBalanceUSD": "106682660.1446009936640229645629307",
        "totalDepositBalanceUSD": "135978903.2420940944941144146138725",
        "timestamp": "1689888743",
        "rates": [
          {
            "rate": "11.961381828082294"
          },
          {
            "rate": "3.922763656164588"
          },
          {
            "rate": "2.6306017102319646"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2722600.529988832261881864757735172",
        "dailyWithdrawUSD": "2888302.507688313968738822006158304",
        "inputTokenPriceUSD": "0.998882172254010063111089350107583"
      },
      {
        "totalValueLockedUSD": "136244669.5530449285729007616268815",
        "totalBorrowBalanceUSD": "107006395.3300083807471677899127953",
        "totalDepositBalanceUSD": "136244669.5530449285729007616268815",
        "timestamp": "1689810299",
        "rates": [
          {
            "rate": "11.9634961759324383"
          },
          {
            "rate": "3.9269923518648767"
          },
          {
            "rate": "2.6362011058401468"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "672762.184648520385332607639663757",
        "dailyWithdrawUSD": "386491.6562605787678095257782846529",
        "inputTokenPriceUSD": "0.9997056163684434412324019348101726"
      },
      {
        "totalValueLockedUSD": "135817194.8174301994869301364663282",
        "totalBorrowBalanceUSD": "106914434.0945585046361956705575826",
        "totalDepositBalanceUSD": "135817194.8174301994869301364663282",
        "timestamp": "1689724367",
        "rates": [
          {
            "rate": "11.9679833977751233"
          },
          {
            "rate": "3.9359667955502467"
          },
          {
            "rate": "2.6481885954228608"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "208003.8973897603458629568911187631",
        "dailyWithdrawUSD": "165809.3788869369744138991152777508",
        "inputTokenPriceUSD": "0.9987602964066472605503623441649446"
      },
      {
        "totalValueLockedUSD": "135843463.3624894334589866286134196",
        "totalBorrowBalanceUSD": "106918646.068981867412523431687277",
        "totalDepositBalanceUSD": "135843463.3624894334589866286134196",
        "timestamp": "1689636755",
        "rates": [
          {
            "rate": "11.9676803575548442"
          },
          {
            "rate": "3.9353607151096884"
          },
          {
            "rate": "2.6473771496898726"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "6182332.867665413992262992783257771",
        "dailyWithdrawUSD": "6306519.068205692204268177811307192",
        "inputTokenPriceUSD": "0.9988414713276401284027330967697519"
      },
      {
        "totalValueLockedUSD": "136184209.8458532446287959983155037",
        "totalBorrowBalanceUSD": "107116536.5818681104937897890468969",
        "totalDepositBalanceUSD": "136184209.8458532446287959983155037",
        "timestamp": "1689541175",
        "rates": [
          {
            "rate": "11.9663897990670863"
          },
          {
            "rate": "3.9327795981341725"
          },
          {
            "rate": "2.6439249295867176"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "226903.1504808147591878542119181528",
        "dailyWithdrawUSD": "156610.2087843577753919280415665902",
        "inputTokenPriceUSD": "1.000517473488988753331727431164486"
      },
      {
        "totalValueLockedUSD": "136348802.7227086906770177380208608",
        "totalBorrowBalanceUSD": "107422459.6037378520552967684737138",
        "totalDepositBalanceUSD": "136348802.7227086906770177380208608",
        "timestamp": "1689460463",
        "rates": [
          {
            "rate": "11.9696252770447844"
          },
          {
            "rate": "3.9392505540895687"
          },
          {
            "rate": "2.6525529614178011"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2918785.502883959982836770865759945",
        "dailyWithdrawUSD": "2235268.519684049732587987767914752",
        "inputTokenPriceUSD": "1.002323996830487928705670022331758"
      },
      {
        "totalValueLockedUSD": "135684872.0471541367119541644505057",
        "totalBorrowBalanceUSD": "106482107.5716855378490256485753311",
        "totalDepositBalanceUSD": "135684872.0471541367119541644505057",
        "timestamp": "1689376583",
        "rates": [
          {
            "rate": "11.9619369844077957"
          },
          {
            "rate": "3.9238739688155915"
          },
          {
            "rate": "2.6321613227420181"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "203813645.9324854147475562735370045",
        "dailyWithdrawUSD": "203861411.7914971594359519264926044",
        "inputTokenPriceUSD": "1.00255212718133304324836791041766"
      },
      {
        "totalValueLockedUSD": "135189794.2640712410913321130147765",
        "totalBorrowBalanceUSD": "101407549.6596029295204549384508915",
        "totalDepositBalanceUSD": "135189794.2640712410913321130147765",
        "timestamp": "1689291719",
        "rates": [
          {
            "rate": "11.8752804550479818"
          },
          {
            "rate": "3.7505609100959636"
          },
          {
            "rate": "2.4070424316834807"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1882020.624639114267296206960978943",
        "dailyWithdrawUSD": "18887494.88561464911016953589907681",
        "inputTokenPriceUSD": "0.9972974837181867626072651271520965"
      },
      {
        "totalValueLockedUSD": "152747631.0093031098521515781120819",
        "totalBorrowBalanceUSD": "105404083.1937573049944766194788499",
        "totalDepositBalanceUSD": "152747631.0093031098521515781120819",
        "timestamp": "1689198179",
        "rates": [
          {
            "rate": "11.7251339241455874"
          },
          {
            "rate": "3.4502678482911749"
          },
          {
            "rate": "2.039098233216611"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "8033210.649797979977395087193468868",
        "dailyWithdrawUSD": "9668836.08967064642249340719898571",
        "inputTokenPriceUSD": "1.001453116456115992253287826585873"
      },
      {
        "totalValueLockedUSD": "154297667.0686313139520613589088584",
        "totalBorrowBalanceUSD": "106930644.2544408689201670646921085",
        "totalDepositBalanceUSD": "154297667.0686313139520613589088584",
        "timestamp": "1689119279",
        "rates": [
          {
            "rate": "11.732537682005099"
          },
          {
            "rate": "3.4650753640101979"
          },
          {
            "rate": "2.0562655493610382"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "9814.014456580147815612465449404744",
        "dailyWithdrawUSD": "142895.5972532562420341866358273793",
        "inputTokenPriceUSD": "1.000963767715580934622964481346627"
      },
      {
        "totalValueLockedUSD": "152821551.917732188421955065682886",
        "totalBorrowBalanceUSD": "107655181.7793242952040010667677301",
        "totalDepositBalanceUSD": "152821551.917732188421955065682886",
        "timestamp": "1689032771",
        "rates": [
          {
            "rate": "11.7611250667466455"
          },
          {
            "rate": "3.5222501334932909"
          },
          {
            "rate": "2.128464481742465"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1149980.278761171716766709757824361",
        "dailyWithdrawUSD": "1395983.829719094166688260987260214",
        "inputTokenPriceUSD": "0.9905919808112548514909555308562476"
      },
      {
        "totalValueLockedUSD": "154568499.1026975152767734673582665",
        "totalBorrowBalanceUSD": "110641692.2552956403140395633337184",
        "totalDepositBalanceUSD": "154568499.1026975152767734673582665",
        "timestamp": "1688940107",
        "rates": [
          {
            "rate": "11.7895239715249783"
          },
          {
            "rate": "3.5790479430499566"
          },
          {
            "rate": "2.3258910808355464"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "273917.2688817951445264419232358197",
        "dailyWithdrawUSD": "314011.1539879805500933480346354527",
        "inputTokenPriceUSD": "1.000398826975090294140150078606843"
      },
      {
        "totalValueLockedUSD": "154475194.9369228286128620235810499",
        "totalBorrowBalanceUSD": "110511955.2724463943996077747772927",
        "totalDepositBalanceUSD": "154475194.9369228286128620235810499",
        "timestamp": "1688860343",
        "rates": [
          {
            "rate": "11.7885052187927458"
          },
          {
            "rate": "3.5770104375854915"
          },
          {
            "rate": "2.3232714360913677"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1560662.339800876169281597420349319",
        "dailyWithdrawUSD": "1599124.666365716300822585863040141",
        "inputTokenPriceUSD": "0.9996007650883855047002570451812118"
      },
      {
        "totalValueLockedUSD": "155758557.9181789760674430808330068",
        "totalBorrowBalanceUSD": "112237516.6073248100582906110840783",
        "totalDepositBalanceUSD": "155758557.9181789760674430808330068",
        "timestamp": "1688770835",
        "rates": [
          {
            "rate": "11.8014650140807342"
          },
          {
            "rate": "3.6029300281614685"
          },
          {
            "rate": "2.3566058314976005"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "136532.6703001726190767913863096308",
        "dailyWithdrawUSD": "569129.6215026306557542912480580837",
        "inputTokenPriceUSD": "1.007728851398751067570090543930348"
      },
      {
        "totalValueLockedUSD": "154897363.1635063123010378540473291",
        "totalBorrowBalanceUSD": "110650001.6267595517948718250784676",
        "totalDepositBalanceUSD": "154897363.1635063123010378540473291",
        "timestamp": "1688687291",
        "rates": [
          {
            "rate": "11.7858587330817564"
          },
          {
            "rate": "3.5717174661635127"
          },
          {
            "rate": "2.3163980977977457"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "766257.7913510453034399572929689982",
        "dailyWithdrawUSD": "3287176.810413025763006398352930976",
        "inputTokenPriceUSD": "0.9994496615646236958495952595775593"
      },
      {
        "totalValueLockedUSD": "157286477.4476865257374096071542412",
        "totalBorrowBalanceUSD": "112510237.3280203117134281068985245",
        "totalDepositBalanceUSD": "157286477.4476865257374096071542412",
        "timestamp": "1688585579",
        "rates": [
          {
            "rate": "11.7882999395256019"
          },
          {
            "rate": "3.5765998790512039"
          },
          {
            "rate": "2.322328051694047"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1566514.595283972003061126350678811",
        "dailyWithdrawUSD": "1963094.546918959291965269213011605",
        "inputTokenPriceUSD": "0.9987677330572709156737180203900239"
      },
      {
        "totalValueLockedUSD": "156562912.8148206449162078054568368",
        "totalBorrowBalanceUSD": "111703576.4387118987625957479132702",
        "totalDepositBalanceUSD": "156562912.8148206449162078054568368",
        "timestamp": "1688510279",
        "rates": [
          {
            "rate": "11.7836839061163509"
          },
          {
            "rate": "3.5673678122327018"
          },
          {
            "rate": "2.3104587359066043"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "19023092.13226404431188586807428492",
        "dailyWithdrawUSD": "19390733.81962013556655392094675002",
        "inputTokenPriceUSD": "0.9917142491865453435496930764064562"
      },
      {
        "totalValueLockedUSD": "156896383.3976897179145420435485546",
        "totalBorrowBalanceUSD": "111766634.4862830325806974790972802",
        "totalDepositBalanceUSD": "156896383.3976897179145420435485546",
        "timestamp": "1688425631",
        "rates": [
          {
            "rate": "11.7808976046706069"
          },
          {
            "rate": "3.5617952093412139"
          },
          {
            "rate": "2.3032939551267256"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "212401104.5548103059017778548621148",
        "dailyWithdrawUSD": "200609365.799648491374722323017431",
        "inputTokenPriceUSD": "0.9916702929421682585151939031545449"
      },
      {
        "totalValueLockedUSD": "146439623.0925728490846784167805602",
        "totalBorrowBalanceUSD": "111855379.8731877246393633043974722",
        "totalDepositBalanceUSD": "146439623.0925728490846784167805602",
        "timestamp": "1688338199",
        "rates": [
          {
            "rate": "11.90958044789839"
          },
          {
            "rate": "3.81916089579678"
          },
          {
            "rate": "2.6452323328030237"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "201989174.1411125216243626469247935",
        "dailyWithdrawUSD": "203580705.9194209876788060896361538",
        "inputTokenPriceUSD": "1.000865116757161132589220896508726"
      },
      {
        "totalValueLockedUSD": "147391262.7778198130331168800542133",
        "totalBorrowBalanceUSD": "111324512.1117451745161793556089024",
        "totalDepositBalanceUSD": "147391262.7778198130331168800542133",
        "timestamp": "1688249615",
        "rates": [
          {
            "rate": "11.888246763831138"
          },
          {
            "rate": "3.7764935276622761"
          },
          {
            "rate": "2.5869499786941278"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "201122494.2205005467594127702956173",
        "dailyWithdrawUSD": "201903671.1184413417374044045081761",
        "inputTokenPriceUSD": "0.9965759394611286240611750462225779"
      },
      {
        "totalValueLockedUSD": "148163852.7764942263616223388082861",
        "totalBorrowBalanceUSD": "111605252.411419703904176019837515",
        "totalDepositBalanceUSD": "148163852.7764942263616223388082861",
        "timestamp": "1688169227",
        "rates": [
          {
            "rate": "11.8831376283382361"
          },
          {
            "rate": "3.7662752566764721"
          },
          {
            "rate": "2.5730096134083958"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "203157831.3141556546415599166486995",
        "dailyWithdrawUSD": "203755152.6569652677458697969786716",
        "inputTokenPriceUSD": "0.9965908213701772180544922024078478"
      },
      {
        "totalValueLockedUSD": "149279267.8539392586833839902088027",
        "totalBorrowBalanceUSD": "112185615.774533790911441008849266",
        "totalDepositBalanceUSD": "149279267.8539392586833839902088027",
        "timestamp": "1688081627",
        "rates": [
          {
            "rate": "11.8787862413487034"
          },
          {
            "rate": "3.7575724826974068"
          },
          {
            "rate": "2.5610053535209748"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "518766.6455408615481836479699148874",
        "dailyWithdrawUSD": "1271067.736707245926600123708073572",
        "inputTokenPriceUSD": "1.000145537653825147808310200033416"
      },
      {
        "totalValueLockedUSD": "149839973.0345570210244459830038408",
        "totalBorrowBalanceUSD": "116932554.0712427975036541208168802",
        "totalDepositBalanceUSD": "149839973.0345570210244459830038408",
        "timestamp": "1687992359",
        "rates": [
          {
            "rate": "11.9509558558357559"
          },
          {
            "rate": "3.9019117116715118"
          },
          {
            "rate": "2.7590147993441212"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1853411.192081099030596467948092769",
        "dailyWithdrawUSD": "1888197.193708778802290318687152996",
        "inputTokenPriceUSD": "0.9989447245059764242094068338973843"
      },
      {
        "totalValueLockedUSD": "150015043.1136229136684806342719118",
        "totalBorrowBalanceUSD": "112166313.0615661087387317488744714",
        "totalDepositBalanceUSD": "150015043.1136229136684806342719118",
        "timestamp": "1687910231",
        "rates": [
          {
            "rate": "11.8692497315358567"
          },
          {
            "rate": "3.7384994630717133"
          },
          {
            "rate": "2.5352813395317303"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "13727320.49352846976110503211406393",
        "dailyWithdrawUSD": "11004749.79642911534439761881384322",
        "inputTokenPriceUSD": "0.9999548372273993390236724493400022"
      },
      {
        "totalValueLockedUSD": "147271929.8947880969225991223316009",
        "totalBorrowBalanceUSD": "111985816.6184250648589113625446216",
        "totalDepositBalanceUSD": "147271929.8947880969225991223316009",
        "timestamp": "1687820843",
        "rates": [
          {
            "rate": "11.9010026880981498"
          },
          {
            "rate": "3.8020053761962996"
          },
          {
            "rate": "2.6214367426408554"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2615858.272392359234719640837979137",
        "dailyWithdrawUSD": "2303485.678048538708355397699213515",
        "inputTokenPriceUSD": "0.9999021735850070826526781703183168"
      },
      {
        "totalValueLockedUSD": "146888635.4349092714364544374205522",
        "totalBorrowBalanceUSD": "109184944.7198561427474003146867547",
        "totalDepositBalanceUSD": "146888635.4349092714364544374205522",
        "timestamp": "1687736555",
        "rates": [
          {
            "rate": "11.8582932496452748"
          },
          {
            "rate": "3.7165864992905496"
          },
          {
            "rate": "2.5064133496839843"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1619441.250936063826333201204356836",
        "dailyWithdrawUSD": "1990124.345283938914407609239374335",
        "inputTokenPriceUSD": "0.9994972265220682018157448916160623"
      },
      {
        "totalValueLockedUSD": "147346003.6496801770282454715010617",
        "totalBorrowBalanceUSD": "108770234.9808037906155396315795918",
        "totalDepositBalanceUSD": "147346003.6496801770282454715010617",
        "timestamp": "1687650191",
        "rates": [
          {
            "rate": "11.845488713323552"
          },
          {
            "rate": "3.6909774266471039"
          },
          {
            "rate": "2.4723754391065738"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "185234.6432646441873030961459987118",
        "dailyWithdrawUSD": "237306.438949241148940520156839563",
        "inputTokenPriceUSD": "1.000163109722778697065672906982278"
      },
      {
        "totalValueLockedUSD": "147404925.9501787611690959158865262",
        "totalBorrowBalanceUSD": "108789653.4214056014925808284562378",
        "totalDepositBalanceUSD": "147404925.9501787611690959158865262",
        "timestamp": "1687561235",
        "rates": [
          {
            "rate": "11.8450803535427645"
          },
          {
            "rate": "3.6901607070855291"
          },
          {
            "rate": "2.4712859888798538"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3245646.316275921511489786644079692",
        "dailyWithdrawUSD": "2082623.946000412404667464974779884",
        "inputTokenPriceUSD": "1.000287464579225191120780235347986"
      },
      {
        "totalValueLockedUSD": "145054802.2262304300451451752009552",
        "totalBorrowBalanceUSD": "107011224.0721748376752147804201769",
        "totalDepositBalanceUSD": "145054802.2262304300451451752009552",
        "timestamp": "1687477727",
        "rates": [
          {
            "rate": "11.8443226779238441"
          },
          {
            "rate": "3.6886453558476881"
          },
          {
            "rate": "2.4694398528567675"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "632508.8140953124481833742407016319",
        "dailyWithdrawUSD": "224828.2203293418417113225546512315",
        "inputTokenPriceUSD": "0.9921779082083560395710060115810946"
      },
      {
        "totalValueLockedUSD": "146695797.9318582995863891653981426",
        "totalBorrowBalanceUSD": "104307633.2549375010988846371432705",
        "totalDepositBalanceUSD": "146695797.9318582995863891653981426",
        "timestamp": "1687391939",
        "rates": [
          {
            "rate": "11.7776166221718785"
          },
          {
            "rate": "3.5552332443437569"
          },
          {
            "rate": "2.2963801045213901"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3616191.334714993534328239715499657",
        "dailyWithdrawUSD": "3317960.568147054258826849417669295",
        "inputTokenPriceUSD": "1.006016975649109115631663551894937"
      },
      {
        "totalValueLockedUSD": "145159290.1629059534460434105586954",
        "totalBorrowBalanceUSD": "102522009.4323153235081359747786104",
        "totalDepositBalanceUSD": "145159290.1629059534460434105586954",
        "timestamp": "1687304195",
        "rates": [
          {
            "rate": "11.7656798399236804"
          },
          {
            "rate": "3.5313596798473607"
          },
          {
            "rate": "2.2661191892195861"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "10377449.45699464495126538528415233",
        "dailyWithdrawUSD": "2063161.862622937876172564640011832",
        "inputTokenPriceUSD": "0.9975489153495888290186170228007125"
      },
      {
        "totalValueLockedUSD": "137372397.1695346659596715583588101",
        "totalBorrowBalanceUSD": "106741720.7338498472333422780761665",
        "totalDepositBalanceUSD": "137372397.1695346659596715583588101",
        "timestamp": "1687218455",
        "rates": [
          {
            "rate": "11.9425597575766983"
          },
          {
            "rate": "3.8851195151533966"
          },
          {
            "rate": "2.7320957134075754"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "506672.908650397273280481872322851",
        "dailyWithdrawUSD": "5118861.354873144100414913116061361",
        "inputTokenPriceUSD": "1.001470954271543355693742860179065"
      },
      {
        "totalValueLockedUSD": "141970187.0225628765375487736544678",
        "totalBorrowBalanceUSD": "111139001.609487981853423542433138",
        "totalDepositBalanceUSD": "141970187.0225628765375487736544678",
        "timestamp": "1687131947",
        "rates": [
          {
            "rate": "11.9570819555520771"
          },
          {
            "rate": "3.9141639111041541"
          },
          {
            "rate": "2.7722059745569724"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1767339.967524903825674868164884328",
        "dailyWithdrawUSD": "1133195.801890174473707922393916835",
        "inputTokenPriceUSD": "1.001459536567183252644776817246002"
      },
      {
        "totalValueLockedUSD": "140766688.6905764910961252080229119",
        "totalBorrowBalanceUSD": "110537040.0406951037581119862484467",
        "totalDepositBalanceUSD": "140766688.6905764910961252080229119",
        "timestamp": "1687044323",
        "rates": [
          {
            "rate": "11.9631234504218875"
          },
          {
            "rate": "3.9262469008437751"
          },
          {
            "rate": "2.7892506311095634"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "515549.7056446280727157085863341866",
        "dailyWithdrawUSD": "1569.461280754402571972929246594462",
        "inputTokenPriceUSD": "0.9975142751731242022605200826384864"
      },
      {
        "totalValueLockedUSD": "139945571.4092742592052662048010659",
        "totalBorrowBalanceUSD": "106563010.4031074526703834290053825",
        "totalDepositBalanceUSD": "139945571.4092742592052662048010659",
        "timestamp": "1686959531",
        "rates": [
          {
            "rate": "11.9036495246499415"
          },
          {
            "rate": "3.807299049299883"
          },
          {
            "rate": "2.6242169207098218"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5019864.647403116627824912445595504",
        "dailyWithdrawUSD": "4476103.391955217222315097469544254",
        "inputTokenPriceUSD": "0.9952384597783104970485755152973847"
      },
      {
        "totalValueLockedUSD": "140965498.4262234503426711023935022",
        "totalBorrowBalanceUSD": "111547809.8298997978800691195955984",
        "totalDepositBalanceUSD": "140965498.4262234503426711023935022",
        "timestamp": "1686871499",
        "rates": [
          {
            "rate": "11.9782805848869006"
          },
          {
            "rate": "3.9565611697738012"
          },
          {
            "rate": "2.8327664445437568"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "205189908.9413043651922563083374988",
        "dailyWithdrawUSD": "210833377.5921260758691752738219444",
        "inputTokenPriceUSD": "1.006457072802391558106539894706592"
      },
      {
        "totalValueLockedUSD": "145177103.4688030103929123335325962",
        "totalBorrowBalanceUSD": "107561223.3561027280778594671433915",
        "totalDepositBalanceUSD": "145177103.4688030103929123335325962",
        "timestamp": "1686783047",
        "rates": [
          {
            "rate": "11.852240140395086"
          },
          {
            "rate": "3.704480280790172"
          },
          {
            "rate": "2.491800742312432"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "214942755.3721044669864047187745274",
        "dailyWithdrawUSD": "215372665.0556142655037518299353416",
        "inputTokenPriceUSD": "0.9954201752187614947541102696147531"
      },
      {
        "totalValueLockedUSD": "146369598.2808046446966860905742448",
        "totalBorrowBalanceUSD": "109044835.447475082121897604946842",
        "totalDepositBalanceUSD": "146369598.2808046446966860905742448",
        "timestamp": "1686699935",
        "rates": [
          {
            "rate": "11.8624898193279308"
          },
          {
            "rate": "3.7249796386558616"
          },
          {
            "rate": "2.5205276929659533"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "202059643.6701148832077517589196585",
        "dailyWithdrawUSD": "204208824.3637295249187249406104762",
        "inputTokenPriceUSD": "1.000667924041364249213930718279337"
      },
      {
        "totalValueLockedUSD": "148144855.7133084735165214278328198",
        "totalBorrowBalanceUSD": "109027831.3938302115581245633835269",
        "totalDepositBalanceUSD": "148144855.7133084735165214278328198",
        "timestamp": "1686611747",
        "rates": [
          {
            "rate": "11.8398842011621818"
          },
          {
            "rate": "3.6797684023243635"
          },
          {
            "rate": "2.4602328601772534"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "862839.6139773943963600066831929469",
        "dailyWithdrawUSD": "2102784.851742341914143195030994418",
        "inputTokenPriceUSD": "0.9983619114851199416294158266605038"
      },
      {
        "totalValueLockedUSD": "149603443.3075108778825394096987602",
        "totalBorrowBalanceUSD": "108995519.7778529583923783434595113",
        "totalDepositBalanceUSD": "149603443.3075108778825394096987602",
        "timestamp": "1686526847",
        "rates": [
          {
            "rate": "11.8214059532721322"
          },
          {
            "rate": "3.6428119065442643"
          },
          {
            "rate": "2.4115444977922789"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1183283.561331811133101124046850621",
        "dailyWithdrawUSD": "943254.5838965452855814739726206587",
        "inputTokenPriceUSD": "0.9998774935718362652473878572800983"
      },
      {
        "totalValueLockedUSD": "149392409.5426885803208110023281207",
        "totalBorrowBalanceUSD": "112548117.6289836594601713573707559",
        "totalDepositBalanceUSD": "149392409.5426885803208110023281207",
        "timestamp": "1686438287",
        "rates": [
          {
            "rate": "11.8834296270993755"
          },
          {
            "rate": "3.766859254198751"
          },
          {
            "rate": "2.5762170393931382"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "200305351.1790658653518465468362173",
        "dailyWithdrawUSD": "203028678.0030991301034295409328221",
        "inputTokenPriceUSD": "1.000149275040519424644363287249912"
      },
      {
        "totalValueLockedUSD": "151980421.0536629926087214713289406",
        "totalBorrowBalanceUSD": "114860502.2698143078341568126567176",
        "totalDepositBalanceUSD": "151980421.0536629926087214713289406",
        "timestamp": "1686354863",
        "rates": [
          {
            "rate": "11.8893950245701979"
          },
          {
            "rate": "3.7787900491403958"
          },
          {
            "rate": "2.5919470301005136"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "557628.1002851458152979338073744525",
        "dailyWithdrawUSD": "5050825.09264404605033619182975288",
        "inputTokenPriceUSD": "0.9993756093649131811502437459652725"
      },
      {
        "totalValueLockedUSD": "156503292.8619399775809409031804255",
        "totalBorrowBalanceUSD": "118530760.3224200491448967696447197",
        "totalDepositBalanceUSD": "156503292.8619399775809409031804255",
        "timestamp": "1686261611",
        "rates": [
          {
            "rate": "11.8934214781765288"
          },
          {
            "rate": "3.7868429563530576"
          },
          {
            "rate": "2.6022388472664312"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "930474.3082387950703685097628657045",
        "dailyWithdrawUSD": "4216503.682428279882379299310989433",
        "inputTokenPriceUSD": "0.999677152059420273324653933415505"
      },
      {
        "totalValueLockedUSD": "159777775.1016806817591470267690866",
        "totalBorrowBalanceUSD": "118524016.8324489456396733023998049",
        "totalDepositBalanceUSD": "159777775.1016806817591470267690866",
        "timestamp": "1686182183",
        "rates": [
          {
            "rate": "11.8545122530187678"
          },
          {
            "rate": "3.7090245060375356"
          },
          {
            "rate": "2.4972812997262797"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4177981.232018150978762824409475824",
        "dailyWithdrawUSD": "4529859.459194258529601446933291885",
        "inputTokenPriceUSD": "0.9996761321266948780775216171452167"
      },
      {
        "totalValueLockedUSD": "160101752.598810373793961002408782",
        "totalBorrowBalanceUSD": "118459235.5526073087562314646658719",
        "totalDepositBalanceUSD": "160101752.598810373793961002408782",
        "timestamp": "1686095387",
        "rates": [
          {
            "rate": "11.849747952806724"
          },
          {
            "rate": "3.699495905613448"
          },
          {
            "rate": "2.4845630606539491"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4209516.864896096667833223355260866",
        "dailyWithdrawUSD": "5070196.849600647708575555501786897",
        "inputTokenPriceUSD": "0.9995778886838140027674804311691428"
      },
      {
        "totalValueLockedUSD": "160811259.8170300039780215029939421",
        "totalBorrowBalanceUSD": "120920839.6912571728176467703520361",
        "totalDepositBalanceUSD": "160811259.8170300039780215029939421",
        "timestamp": "1686009395",
        "rates": [
          {
            "rate": "11.8798552835607839"
          },
          {
            "rate": "3.7597105671215678"
          },
          {
            "rate": "2.5649341720530825"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3516520.918184753987381832853062361",
        "dailyWithdrawUSD": "3424133.204284577124468408397003048",
        "inputTokenPriceUSD": "0.998811614658249267246729996722047"
      },
      {
        "totalValueLockedUSD": "160091255.9005606538542509787617938",
        "totalBorrowBalanceUSD": "120432882.1726374053277128243691586",
        "totalDepositBalanceUSD": "160091255.9005606538542509787617938",
        "timestamp": "1685908775",
        "rates": [
          {
            "rate": "11.8806898712121687"
          },
          {
            "rate": "3.7613797424243374"
          },
          {
            "rate": "2.5671927421395812"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1908276.258160578057565221511300998",
        "dailyWithdrawUSD": "1930232.309807352247927841362431861",
        "inputTokenPriceUSD": "0.9949989566318325585890173641166809"
      },
      {
        "totalValueLockedUSD": "161603274.5523154804867594954666598",
        "totalBorrowBalanceUSD": "120598991.3951599564236337136491121",
        "totalDepositBalanceUSD": "161603274.5523154804867594954666598",
        "timestamp": "1685836667",
        "rates": [
          {
            "rate": "11.8656631628789729"
          },
          {
            "rate": "3.7313263257579459"
          },
          {
            "rate": "2.5268367369982127"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4006189.58776671415150327506590621",
        "dailyWithdrawUSD": "4125683.287003000999966341810414087",
        "inputTokenPriceUSD": "1.004323755801535804029637595712031"
      },
      {
        "totalValueLockedUSD": "159763177.9339914142552775232938444",
        "totalBorrowBalanceUSD": "117171155.8182839028949852140938741",
        "totalDepositBalanceUSD": "159763177.9339914142552775232938444",
        "timestamp": "1685750147",
        "rates": [
          {
            "rate": "11.8335119341480112"
          },
          {
            "rate": "3.6670238682960223"
          },
          {
            "rate": "2.4415750253380294"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "248175.1421793484042521577634145386",
        "dailyWithdrawUSD": "5204293.668531578551429844615426226",
        "inputTokenPriceUSD": "0.992223596072854593796572121423992"
      },
      {
        "totalValueLockedUSD": "165692931.590179483579107482771903",
        "totalBorrowBalanceUSD": "115593592.9073394341097160373893758",
        "totalDepositBalanceUSD": "165692931.590179483579107482771903",
        "timestamp": "1685657015",
        "rates": [
          {
            "rate": "11.7440924723383619"
          },
          {
            "rate": "3.4881849446767238"
          },
          {
            "rate": "2.2116461696692143"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "203946209.2387952571517537420432409",
        "dailyWithdrawUSD": "205012444.155817701543647041820951",
        "inputTokenPriceUSD": "0.9979659224971605290157538542294377"
      },
      {
        "totalValueLockedUSD": "168366575.5356268876955360900336808",
        "totalBorrowBalanceUSD": "116721222.9391601720841219676898819",
        "totalDepositBalanceUSD": "168366575.5356268876955360900336808",
        "timestamp": "1685577527",
        "rates": [
          {
            "rate": "11.7331401337061488"
          },
          {
            "rate": "3.4662802674122976"
          },
          {
            "rate": "2.1863356651407406"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1413692072.86944806545449301273194",
        "dailyWithdrawUSD": "1415145158.958622917856992229305465",
        "inputTokenPriceUSD": "1.007644700791730628297534896301842"
      },
      {
        "totalValueLockedUSD": "168181899.1093709799804467575296694",
        "totalBorrowBalanceUSD": "114285260.3050237133980946452278065",
        "totalDepositBalanceUSD": "168181899.1093709799804467575296694",
        "timestamp": "1685479307",
        "rates": [
          {
            "rate": "11.6988330481099425"
          },
          {
            "rate": "3.397666096219885"
          },
          {
            "rate": "2.1017651379915258"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "468998.2100295370126274926711802743",
        "dailyWithdrawUSD": "476671.1126198137925301873305585559",
        "inputTokenPriceUSD": "0.9979333990537074521584573193666512"
      },
      {
        "totalValueLockedUSD": "169604876.3059808614516236194690411",
        "totalBorrowBalanceUSD": "115290259.1989525791974158113844629",
        "totalDepositBalanceUSD": "169604876.3059808614516236194690411",
        "timestamp": "1685404655",
        "rates": [
          {
            "rate": "11.699393733766157"
          },
          {
            "rate": "3.398787467532314"
          },
          {
            "rate": "2.1031263472083191"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "200255621.5399426033317236807331549",
        "dailyWithdrawUSD": "200943058.9654855750211758924558608",
        "inputTokenPriceUSD": "1.006386698609462125060532213770374"
      },
      {
        "totalValueLockedUSD": "168682318.7469772964616134858752359",
        "totalBorrowBalanceUSD": "115542762.7078633130048352194166653",
        "totalDepositBalanceUSD": "168682318.7469772964616134858752359",
        "timestamp": "1685318351",
        "rates": [
          {
            "rate": "11.7124303561422233"
          },
          {
            "rate": "3.4248607122844467"
          },
          {
            "rate": "2.1348955761095188"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1165783.060428074166433716017029212",
        "dailyWithdrawUSD": "1198493.274336855201215935195406243",
        "inputTokenPriceUSD": "0.9969028827337385682821132723256811"
      },
      {
        "totalValueLockedUSD": "169310161.572216929776422788372261",
        "totalBorrowBalanceUSD": "117075826.4747369166744657488794856",
        "totalDepositBalanceUSD": "169310161.572216929776422788372261",
        "timestamp": "1685230295",
        "rates": [
          {
            "rate": "11.7287171515996981"
          },
          {
            "rate": "3.4574343031993961"
          },
          {
            "rate": "2.1763618272709352"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2708014.311059453896438308643743361",
        "dailyWithdrawUSD": "202392.4890542119152428477915872722",
        "inputTokenPriceUSD": "1.000400852689146363075125245187083"
      },
      {
        "totalValueLockedUSD": "166251697.9811008414734917999510577",
        "totalBorrowBalanceUSD": "117023170.3829633347497218881145519",
        "totalDepositBalanceUSD": "166251697.9811008414734917999510577",
        "timestamp": "1685129267",
        "rates": [
          {
            "rate": "11.7597278162339249"
          },
          {
            "rate": "3.5194556324678498"
          },
          {
            "rate": "2.2542093205490761"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "0",
        "dailyWithdrawUSD": "2135.541309504200661184970944363509",
        "inputTokenPriceUSD": "0.9972143388674813441255079749566403"
      },
      {
        "totalValueLockedUSD": "166254853.0012592892162616969437225",
        "totalBorrowBalanceUSD": "118056759.1269854691667581629742938",
        "totalDepositBalanceUSD": "166254853.0012592892162616969437225",
        "timestamp": "1685057303",
        "rates": [
          {
            "rate": "11.775236646598769"
          },
          {
            "rate": "3.5504732931975381"
          },
          {
            "rate": "2.293473659706719"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "263998.7926137558888581184910916931",
        "dailyWithdrawUSD": "389328.397718922423393831291529926",
        "inputTokenPriceUSD": "0.9972507972679064604414857179349021"
      },
      {
        "totalValueLockedUSD": "167076828.5966738345903375813325444",
        "totalBorrowBalanceUSD": "119214795.5226889361493158187114329",
        "totalDepositBalanceUSD": "167076828.5966738345903375813325444",
        "timestamp": "1684972643",
        "rates": [
          {
            "rate": "11.7838308254564217"
          },
          {
            "rate": "3.5676616509128434"
          },
          {
            "rate": "2.3155038774589255"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "203552265.875815127986344241150367",
        "dailyWithdrawUSD": "203556067.2509846573073864154262379",
        "inputTokenPriceUSD": "1.001484723527269703161169061148158"
      },
      {
        "totalValueLockedUSD": "166951371.50546167845606270486618",
        "totalBorrowBalanceUSD": "119952087.7340891274307068428437965",
        "totalDepositBalanceUSD": "166951371.50546167845606270486618",
        "timestamp": "1684886123",
        "rates": [
          {
            "rate": "11.7962118178484565"
          },
          {
            "rate": "3.5924236356969129"
          },
          {
            "rate": "2.3472503954760296"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "200269819.5476230186901178005333211",
        "dailyWithdrawUSD": "201108549.9613647262749643243899831",
        "inputTokenPriceUSD": "1.000793040255055511443040165989211"
      },
      {
        "totalValueLockedUSD": "167912870.4307921718647797153627748",
        "totalBorrowBalanceUSD": "118471768.95837019555932780571238",
        "totalDepositBalanceUSD": "167912870.4307921718647797153627748",
        "timestamp": "1684781795",
        "rates": [
          {
            "rate": "11.7638864270211834"
          },
          {
            "rate": "3.5277728540423668"
          },
          {
            "rate": "2.2646918853555088"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3546728.552470598200984734945207435",
        "dailyWithdrawUSD": "3457079.886155188960923570416691448",
        "inputTokenPriceUSD": "1.001610046707774549353242082755048"
      },
      {
        "totalValueLockedUSD": "167511095.4683389413688486774474354",
        "totalBorrowBalanceUSD": "118113283.0468409809703273988413234",
        "totalDepositBalanceUSD": "167511095.4683389413688486774474354",
        "timestamp": "1684699235",
        "rates": [
          {
            "rate": "11.7627669262031891"
          },
          {
            "rate": "3.5255338524063781"
          },
          {
            "rate": "2.261854148642143"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1082095.596188579630815379681515572",
        "dailyWithdrawUSD": "704096.7498235575804256669471602486",
        "inputTokenPriceUSD": "0.9998130214790291868761803389639706"
      },
      {
        "totalValueLockedUSD": "167648079.6032206407257663330057468",
        "totalBorrowBalanceUSD": "118697366.1515768210583992492733366",
        "totalDepositBalanceUSD": "167648079.6032206407257663330057468",
        "timestamp": "1684626983",
        "rates": [
          {
            "rate": "11.7700365313921692"
          },
          {
            "rate": "3.5400730627843385"
          },
          {
            "rate": "2.2803235852393987"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "15871890.2114783475509233749949621",
        "dailyWithdrawUSD": "707459.0370625442710802832307489992",
        "inputTokenPriceUSD": "1.002952186840057145017099832281326"
      },
      {
        "totalValueLockedUSD": "152654608.5191858829226462207278299",
        "totalBorrowBalanceUSD": "120310578.0051955268762935753392963",
        "totalDepositBalanceUSD": "152654608.5191858829226462207278299",
        "timestamp": "1684539827",
        "rates": [
          {
            "rate": "11.9703056223158025"
          },
          {
            "rate": "3.940611244631605"
          },
          {
            "rate": "2.8191914078284742"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "203886426.5282732931951243668301441",
        "dailyWithdrawUSD": "205344510.9682854004853238565810603",
        "inputTokenPriceUSD": "1.004164484151284596967499924139811"
      },
      {
        "totalValueLockedUSD": "152989737.517530473089975955640851",
        "totalBorrowBalanceUSD": "115600442.0529306283503084310120192",
        "totalDepositBalanceUSD": "152989737.517530473089975955640851",
        "timestamp": "1684452287",
        "rates": [
          {
            "rate": "11.8890215027885336"
          },
          {
            "rate": "3.7780430055770671"
          },
          {
            "rate": "2.5942622124029702"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5414680.502596788247832346920614291",
        "dailyWithdrawUSD": "5417892.360643039987890736452388723",
        "inputTokenPriceUSD": "0.9969131220379636818154598828579195"
      },
      {
        "totalValueLockedUSD": "154382927.9344729497900197449525913",
        "totalBorrowBalanceUSD": "115856180.1088586040668119232744096",
        "totalDepositBalanceUSD": "154382927.9344729497900197449525913",
        "timestamp": "1684364687",
        "rates": [
          {
            "rate": "11.8761157890771212"
          },
          {
            "rate": "3.7522315781542424"
          },
          {
            "rate": "2.5594578586852756"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "6565379.036739543293360906294103955",
        "dailyWithdrawUSD": "3232418.957060303193531350697947309",
        "inputTokenPriceUSD": "1.006050572438774371828160791103113"
      },
      {
        "totalValueLockedUSD": "150453589.026684805762954157115484",
        "totalBorrowBalanceUSD": "115387172.6489768571548142085164541",
        "totalDepositBalanceUSD": "150453589.026684805762954157115484",
        "timestamp": "1684275815",
        "rates": [
          {
            "rate": "11.9173203399808859"
          },
          {
            "rate": "3.8346406799617719"
          },
          {
            "rate": "2.6719472719410206"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1566654.848260143148301248786522091",
        "dailyWithdrawUSD": "4883084.286059291397415440363846564",
        "inputTokenPriceUSD": "1.002150489486213192867299357517095"
      },
      {
        "totalValueLockedUSD": "153796881.101454709020210805079632",
        "totalBorrowBalanceUSD": "115507067.7090466939919229369897369",
        "totalDepositBalanceUSD": "153796881.101454709020210805079632",
        "timestamp": "1684194779",
        "rates": [
          {
            "rate": "11.8775898860176228"
          },
          {
            "rate": "3.7551797720352457"
          },
          {
            "rate": "2.5634105861621766"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2043567.984835469304487477750163234",
        "dailyWithdrawUSD": "1649976.521412738700162362409999107",
        "inputTokenPriceUSD": "1.002197813265805197882862093999415"
      },
      {
        "totalValueLockedUSD": "153505949.5675585831227369666039316",
        "totalBorrowBalanceUSD": "115039297.2264372232320600472486949",
        "totalDepositBalanceUSD": "153505949.5675585831227369666039316",
        "timestamp": "1684108391",
        "rates": [
          {
            "rate": "11.8735302670993213"
          },
          {
            "rate": "3.7470605341986426"
          },
          {
            "rate": "2.552565039653816"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "351153.5239967462100747392694102484",
        "dailyWithdrawUSD": "1195592.693776784499414818212760621",
        "inputTokenPriceUSD": "1.002898310790898372258545647847292"
      },
      {
        "totalValueLockedUSD": "152813623.2392212267648123066972789",
        "totalBorrowBalanceUSD": "113887388.6310696768426348442150556",
        "totalDepositBalanceUSD": "152813623.2392212267648123066972789",
        "timestamp": "1684020659",
        "rates": [
          {
            "rate": "11.86317337662982"
          },
          {
            "rate": "3.7263467532596399"
          },
          {
            "rate": "2.524563875824621"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5172136.545348604003056497830690468",
        "dailyWithdrawUSD": "2438945.298967995724299174415887612",
        "inputTokenPriceUSD": "0.9929689320802918684615545562030595"
      },
      {
        "totalValueLockedUSD": "151502217.2387387833079323155368688",
        "totalBorrowBalanceUSD": "115470176.9795333758875085774495155",
        "totalDepositBalanceUSD": "151502217.2387387833079323155368688",
        "timestamp": "1683935795",
        "rates": [
          {
            "rate": "11.9054192358823283"
          },
          {
            "rate": "3.8108384717646566"
          },
          {
            "rate": "2.6390293846610108"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4562282.028510775178175571671045684",
        "dailyWithdrawUSD": "3604413.422925846938470979561544974",
        "inputTokenPriceUSD": "1.002254338965942748070317489691716"
      },
      {
        "totalValueLockedUSD": "149792603.981276186586274749293045",
        "totalBorrowBalanceUSD": "114670689.8911028134500623082406262",
        "totalDepositBalanceUSD": "149792603.981276186586274749293045",
        "timestamp": "1683840179",
        "rates": [
          {
            "rate": "11.913822938319958"
          },
          {
            "rate": "3.8276458766399159"
          },
          {
            "rate": "2.6621762921423218"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5105912.108141128652674073230853144",
        "dailyWithdrawUSD": "2817298.209188734797476158236858776",
        "inputTokenPriceUSD": "0.9975426952473581583650424029585849"
      },
      {
        "totalValueLockedUSD": "147511276.2862476222398532225383211",
        "totalBorrowBalanceUSD": "117291272.8561867550417416410898846",
        "totalDepositBalanceUSD": "147511276.2862476222398532225383211",
        "timestamp": "1683758291",
        "rates": [
          {
            "rate": "11.9878342762564234"
          },
          {
            "rate": "3.9756685525128467"
          },
          {
            "rate": "2.8693760282276895"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "9017161.070613073068757284920666346",
        "dailyWithdrawUSD": "9061967.603282427412963660114463255",
        "inputTokenPriceUSD": "0.997706756443835826383126492463739"
      },
      {
        "totalValueLockedUSD": "147894142.4739850248926611232061667",
        "totalBorrowBalanceUSD": "117657173.5646544495389885958047777",
        "totalDepositBalanceUSD": "147894142.4739850248926611232061667",
        "timestamp": "1683669995",
        "rates": [
          {
            "rate": "11.988873375873887"
          },
          {
            "rate": "3.977746751747774"
          },
          {
            "rate": "2.8723257265390539"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1353916.002946032391707962141821763",
        "dailyWithdrawUSD": "778606.2275849536878108760688317735",
        "inputTokenPriceUSD": "1.000085188508921114723899327290334"
      },
      {
        "totalValueLockedUSD": "147434007.8750414812367036561147787",
        "totalBorrowBalanceUSD": "117750066.5189224209713600624019679",
        "totalDepositBalanceUSD": "147434007.8750414812367036561147787",
        "timestamp": "1683581003",
        "rates": [
          {
            "rate": "11.9966557117974116"
          },
          {
            "rate": "3.9933114235948232"
          },
          {
            "rate": "2.8946338510568363"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "489017.4688685869984285828965383606",
        "dailyWithdrawUSD": "49504.7230772384631860530060190899",
        "inputTokenPriceUSD": "1.000956096578232890729281489868535"
      },
      {
        "totalValueLockedUSD": "145624857.9808104290006449106401109",
        "totalBorrowBalanceUSD": "115555348.0449169634086782231686411",
        "totalDepositBalanceUSD": "145624857.9808104290006449106401109",
        "timestamp": "1683491795",
        "rates": [
          {
            "rate": "11.9837832991968698"
          },
          {
            "rate": "3.9675665983937396"
          },
          {
            "rate": "2.8580051999446061"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "37338.99102977620090148886644749692",
        "dailyWithdrawUSD": "182408.7197842471634279398728932399",
        "inputTokenPriceUSD": "0.9917423009372875084804910480470731"
      },
      {
        "totalValueLockedUSD": "145732398.2773995068510401301419979",
        "totalBorrowBalanceUSD": "116128753.1630323694991929929922979",
        "totalDepositBalanceUSD": "145732398.2773995068510401301419979",
        "timestamp": "1683414887",
        "rates": [
          {
            "rate": "11.9921560125112376"
          },
          {
            "rate": "3.9843120250224752"
          },
          {
            "rate": "2.8818220663517675"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "247139.105375305506057479826791887",
        "dailyWithdrawUSD": "312726.0939808436062911101395988367",
        "inputTokenPriceUSD": "0.9915749837885446471315764713300475"
      },
      {
        "totalValueLockedUSD": "147296802.4124271755004274253744764",
        "totalBorrowBalanceUSD": "117851848.4698587790360088003934144",
        "totalDepositBalanceUSD": "147296802.4124271755004274253744764",
        "timestamp": "1683319619",
        "rates": [
          {
            "rate": "12.0364611090262912"
          },
          {
            "rate": "4.0364611090262912"
          },
          {
            "rate": "2.9305710379858775"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "803732.1699774120107458502056217336",
        "dailyWithdrawUSD": "843893.3205307169931124220905736545",
        "inputTokenPriceUSD": "1.001873339087643250031467154219583"
      },
      {
        "totalValueLockedUSD": "147677293.3879650586153046296593111",
        "totalBorrowBalanceUSD": "114995595.0222001298991591900795932",
        "totalDepositBalanceUSD": "147677293.3879650586153046296593111",
        "timestamp": "1683241031",
        "rates": [
          {
            "rate": "11.9467365223513725"
          },
          {
            "rate": "3.893473044702745"
          },
          {
            "rate": "2.7536664980618699"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "342123.7392907454948614155625916601",
        "dailyWithdrawUSD": "179482.7276584348551269827352609695",
        "inputTokenPriceUSD": "1.004264660860331616269164300393099"
      },
      {
        "totalValueLockedUSD": "147577611.5564599354748754549209555",
        "totalBorrowBalanceUSD": "114071286.1854455706260337538114919",
        "totalDepositBalanceUSD": "147577611.5564599354748754549209555",
        "timestamp": "1683156359",
        "rates": [
          {
            "rate": "11.9323934509878443"
          },
          {
            "rate": "3.8647869019756886"
          },
          {
            "rate": "2.7138454607703897"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "886879.5245810937662765691230307086",
        "dailyWithdrawUSD": "25631.7835960744360063840350185173",
        "inputTokenPriceUSD": "1.004774446822895903035483604360773"
      },
      {
        "totalValueLockedUSD": "145129463.4990736395061880280513563",
        "totalBorrowBalanceUSD": "112411997.6554669901495008477281182",
        "totalDepositBalanceUSD": "145129463.4990736395061880280513563",
        "timestamp": "1683055955",
        "rates": [
          {
            "rate": "11.9364075634134128"
          },
          {
            "rate": "3.8728151268268255"
          },
          {
            "rate": "2.7251239033071557"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1395134.583435377459490246904490566",
        "dailyWithdrawUSD": "3299348.649592991331654323227756749",
        "inputTokenPriceUSD": "0.994065918993646452755406700640523"
      },
      {
        "totalValueLockedUSD": "147126821.0289329655777740588969766",
        "totalBorrowBalanceUSD": "112533825.1834362844937783145083939",
        "totalDepositBalanceUSD": "147126821.0289329655777740588969766",
        "timestamp": "1682974907",
        "rates": [
          {
            "rate": "11.9121894983256889"
          },
          {
            "rate": "3.8243789966513778"
          },
          {
            "rate": "2.6580459269130548"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1398520.783193747366971698599959418",
        "dailyWithdrawUSD": "1436067.685568914200099387936399316",
        "inputTokenPriceUSD": "0.9948646176680317583065758228941373"
      },
      {
        "totalValueLockedUSD": "146750169.459076286378497974406892",
        "totalBorrowBalanceUSD": "112716218.1606514108597144421665867",
        "totalDepositBalanceUSD": "146750169.459076286378497974406892",
        "timestamp": "1682896835",
        "rates": [
          {
            "rate": "11.9202045584834191"
          },
          {
            "rate": "3.8404091169668383"
          },
          {
            "rate": "2.6799014904160644"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2921936.509331375354753007973632924",
        "dailyWithdrawUSD": "3892833.583658995471534852148530688",
        "inputTokenPriceUSD": "0.99213927980796869648371663939395"
      },
      {
        "totalValueLockedUSD": "149149851.1978170699935531364026515",
        "totalBorrowBalanceUSD": "119383559.3529992281144599301662593",
        "totalDepositBalanceUSD": "149149851.1978170699935531364026515",
        "timestamp": "1682810807",
        "rates": [
          {
            "rate": "12.159890759824394"
          },
          {
            "rate": "4.159890759824394"
          },
          {
            "rate": "3.0193339756063601"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1605661.021763794303996367254694197",
        "dailyWithdrawUSD": "2628598.870929732855500963377500615",
        "inputTokenPriceUSD": "1.001889088817360118472863893645308"
      },
      {
        "totalValueLockedUSD": "150462936.2031006736732732220965933",
        "totalBorrowBalanceUSD": "121140080.103684647124446900369036",
        "totalDepositBalanceUSD": "150462936.2031006736732732220965933",
        "timestamp": "1682724335",
        "rates": [
          {
            "rate": "13.9181949653792421"
          },
          {
            "rate": "5.9181949653792421"
          },
          {
            "rate": "4.2979873877181274"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "10448748.31588580907595448504057723",
        "dailyWithdrawUSD": "63296148.59994098592119744177352214",
        "inputTokenPriceUSD": "1.003937230433496192050412421885587"
      },
      {
        "totalValueLockedUSD": "202897619.3263365264917005303667971",
        "totalBorrowBalanceUSD": "144327045.0563301981862981876260544",
        "totalDepositBalanceUSD": "202897619.3263365264917005303667971",
        "timestamp": "1682629007",
        "rates": [
          {
            "rate": "11.7783226187979985"
          },
          {
            "rate": "3.556645237595997"
          },
          {
            "rate": "2.2968075414157322"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "207027792.8824916079467563968237223",
        "dailyWithdrawUSD": "207543128.0805183384364083248147194",
        "inputTokenPriceUSD": "1.001117482996664666598282965039635"
      },
      {
        "totalValueLockedUSD": "203478206.6860708574386432027414492",
        "totalBorrowBalanceUSD": "142748272.039571566889109772255817",
        "totalDepositBalanceUSD": "203478206.6860708574386432027414492",
        "timestamp": "1682549831",
        "rates": [
          {
            "rate": "11.7538511941228692"
          },
          {
            "rate": "3.5077023882457385"
          },
          {
            "rate": "2.2347831921123943"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "11412700.69873321655781043286548286",
        "dailyWithdrawUSD": "4670923.653041278519155810003851935",
        "inputTokenPriceUSD": "1.0015058722826642774959228027823"
      },
      {
        "totalValueLockedUSD": "197595616.1693043252656441493231894",
        "totalBorrowBalanceUSD": "145587864.6535445416186203788613222",
        "totalDepositBalanceUSD": "197595616.1693043252656441493231894",
        "timestamp": "1682466923",
        "rates": [
          {
            "rate": "11.8419916108408397"
          },
          {
            "rate": "3.6839832216816793"
          },
          {
            "rate": "2.4626802167586835"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4496562.859690283960822934764726669",
        "dailyWithdrawUSD": "2618956.925932287057176920881357075",
        "inputTokenPriceUSD": "1.005731130781727438497446529922208"
      },
      {
        "totalValueLockedUSD": "193659554.9606745948909329133983472",
        "totalBorrowBalanceUSD": "144750498.0704299108931554243465261",
        "totalDepositBalanceUSD": "193659554.9606745948909329133983472",
        "timestamp": "1682379011",
        "rates": [
          {
            "rate": "11.8686196521483742"
          },
          {
            "rate": "3.7372393042967485"
          },
          {
            "rate": "2.5337106045370408"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1491625.438516997962198287209196021",
        "dailyWithdrawUSD": "1357124.29305373333923538618670435",
        "inputTokenPriceUSD": "0.9953055308240705695459123379491269"
      },
      {
        "totalValueLockedUSD": "194992663.9846764055060046569008581",
        "totalBorrowBalanceUSD": "148418819.8575951857690013881094736",
        "totalDepositBalanceUSD": "194992663.9846764055060046569008581",
        "timestamp": "1682283731",
        "rates": [
          {
            "rate": "11.9028759449144894"
          },
          {
            "rate": "3.8057518898289789"
          },
          {
            "rate": "2.6263591798805643"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "154793.4554005307395243493437562545",
        "dailyWithdrawUSD": "210037.554619393720763272427947547",
        "inputTokenPriceUSD": "1.002939788107182891987597663946508"
      },
      {
        "totalValueLockedUSD": "193065759.469032939049337005950891",
        "totalBorrowBalanceUSD": "147028339.4754337636552140661487372",
        "totalDepositBalanceUSD": "193065759.469032939049337005950891",
        "timestamp": "1682207063",
        "rates": [
          {
            "rate": "11.9038624549659129"
          },
          {
            "rate": "3.8077249099318259"
          },
          {
            "rate": "2.6290445000997983"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "790351.8533558533450943680413277484",
        "dailyWithdrawUSD": "8561551.365525454015563171339154697",
        "inputTokenPriceUSD": "0.9928181389758620825141963575922075"
      },
      {
        "totalValueLockedUSD": "202864652.9716184450729404061645183",
        "totalBorrowBalanceUSD": "150215438.071259960137666239587258",
        "totalDepositBalanceUSD": "202864652.9716184450729404061645183",
        "timestamp": "1682118155",
        "rates": [
          {
            "rate": "11.8511771043383614"
          },
          {
            "rate": "3.7023542086767228"
          },
          {
            "rate": "2.4864262648763365"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "7163882.424854679974541552092596842",
        "dailyWithdrawUSD": "8898842.328785317124245873267577643",
        "inputTokenPriceUSD": "1.003067461099717466895618549054768"
      },
      {
        "totalValueLockedUSD": "204278392.2730408135470593192555487",
        "totalBorrowBalanceUSD": "151584844.1737938394376307436001169",
        "totalDepositBalanceUSD": "204278392.2730408135470593192555487",
        "timestamp": "1682030975",
        "rates": [
          {
            "rate": "11.8551248218200079"
          },
          {
            "rate": "3.7102496436400157"
          },
          {
            "rate": "2.4967546394879717"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3980453.96183683151365480322120738",
        "dailyWithdrawUSD": "11158064.56783595043148208631759395",
        "inputTokenPriceUSD": "1.001579206850489933146342526031817"
      },
      {
        "totalValueLockedUSD": "209471257.2239139961819486275730922",
        "totalBorrowBalanceUSD": "154562288.3349898544257672703494363",
        "totalDepositBalanceUSD": "209471257.2239139961819486275730922",
        "timestamp": "1681947239",
        "rates": [
          {
            "rate": "11.8446708849489993"
          },
          {
            "rate": "3.6893417698979985"
          },
          {
            "rate": "2.4682603360193326"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "15952006.40058503739872148014022018",
        "dailyWithdrawUSD": "23098410.05965278514226685792182148",
        "inputTokenPriceUSD": "0.9922592829127880537091607815173282"
      },
      {
        "totalValueLockedUSD": "217234003.7968237405114516547322047",
        "totalBorrowBalanceUSD": "155098940.4181790428444292789560959",
        "totalDepositBalanceUSD": "217234003.7968237405114516547322047",
        "timestamp": "1681856759",
        "rates": [
          {
            "rate": "11.7849285040443547"
          },
          {
            "rate": "3.5698570080887093"
          },
          {
            "rate": "2.312128026706374"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "201185427.8970096819850809221851279",
        "dailyWithdrawUSD": "202405564.4265143406580146808356337",
        "inputTokenPriceUSD": "0.9952566170677705790333450935763339"
      },
      {
        "totalValueLockedUSD": "219475178.6110311173913994598197537",
        "totalBorrowBalanceUSD": "156952762.7032118904292078566677191",
        "totalDepositBalanceUSD": "219475178.6110311173913994598197537",
        "timestamp": "1681775159",
        "rates": [
          {
            "rate": "11.787818205685864"
          },
          {
            "rate": "3.575636411371728"
          },
          {
            "rate": "2.3194297025331166"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "379962.4628492612295249392789098461",
        "dailyWithdrawUSD": "102179501.4330906232327939537275208",
        "inputTokenPriceUSD": "1.000025100576715643286120752809872"
      },
      {
        "totalValueLockedUSD": "320766137.4712761341701696861126484",
        "totalBorrowBalanceUSD": "150647934.3969077517480323087403894",
        "totalDepositBalanceUSD": "320766137.4712761341701696861126484",
        "timestamp": "1681688303",
        "rates": [
          {
            "rate": "11.17412553689618"
          },
          {
            "rate": "2.34825107379236"
          },
          {
            "rate": "1.0091143626121504"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "486641.412913953699014995611991305",
        "dailyWithdrawUSD": "4473270.082958502616182187223082582",
        "inputTokenPriceUSD": "1.000098493001558049353628898556641"
      },
      {
        "totalValueLockedUSD": "322111986.5118028824238853330023823",
        "totalBorrowBalanceUSD": "146426352.8208033768129831910556879",
        "totalDepositBalanceUSD": "322111986.5118028824238853330023823",
        "timestamp": "1681602983",
        "rates": [
          {
            "rate": "11.1364549587481186"
          },
          {
            "rate": "2.2729099174962372"
          },
          {
            "rate": "0.9464919889887404"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5561490.694389623105222434966221817",
        "dailyWithdrawUSD": "1709912.96136430521252591758519275",
        "inputTokenPriceUSD": "0.992034697330261669503839436948819"
      },
      {
        "totalValueLockedUSD": "321817049.0298447333083362222572218",
        "totalBorrowBalanceUSD": "145263833.7028684278122108069904",
        "totalDepositBalanceUSD": "321817049.0298447333083362222572218",
        "timestamp": "1681515635",
        "rates": [
          {
            "rate": "11.1284655899252359"
          },
          {
            "rate": "2.2569311798504717"
          },
          {
            "rate": "0.9338115851069595"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "7007610.178998316460996863735774113",
        "dailyWithdrawUSD": "7447604.055500380559030300879205646",
        "inputTokenPriceUSD": "1.003153032450449864914850115968973"
      },
      {
        "totalValueLockedUSD": "322050124.6997243340247113706401452",
        "totalBorrowBalanceUSD": "140225843.459271123061325278601089",
        "totalDepositBalanceUSD": "322050124.6997243340247113706401452",
        "timestamp": "1681428731",
        "rates": [
          {
            "rate": "11.0885401623802987"
          },
          {
            "rate": "2.1770803247605973"
          },
          {
            "rate": "0.8701793982186119"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "226543510.5905041392430122268352468",
        "dailyWithdrawUSD": "222446991.365203567619784393280182",
        "inputTokenPriceUSD": "0.9997161450799697681624389338570405"
      },
      {
        "totalValueLockedUSD": "317185658.8010832783681399992897456",
        "totalBorrowBalanceUSD": "153291224.8617915919431927426927222",
        "totalDepositBalanceUSD": "317185658.8010832783681399992897456",
        "timestamp": "1681340207",
        "rates": [
          {
            "rate": "11.2082133152659267"
          },
          {
            "rate": "2.4164266305318534"
          },
          {
            "rate": "1.0674762296647694"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "404430811.181368618288489073520667",
        "dailyWithdrawUSD": "400096020.5239595460809029663256993",
        "inputTokenPriceUSD": "0.9972655465447437089736814040637969"
      },
      {
        "totalValueLockedUSD": "313243551.0235350527396720362325375",
        "totalBorrowBalanceUSD": "144416675.2392878967714088322731802",
        "totalDepositBalanceUSD": "313243551.0235350527396720362325375",
        "timestamp": "1681255211",
        "rates": [
          {
            "rate": "11.1525905858072205"
          },
          {
            "rate": "2.3051811716144411"
          },
          {
            "rate": "0.9736184587001627"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "203619514.8605357300994772074738873",
        "dailyWithdrawUSD": "201217226.5126754669537655119094348",
        "inputTokenPriceUSD": "0.9985393154401780294125496965059622"
      },
      {
        "totalValueLockedUSD": "310955343.0125091685935500154632466",
        "totalBorrowBalanceUSD": "139676956.9270848473755230573518031",
        "totalDepositBalanceUSD": "310955343.0125091685935500154632466",
        "timestamp": "1681169819",
        "rates": [
          {
            "rate": "11.1229659921387025"
          },
          {
            "rate": "2.245931984277405"
          },
          {
            "rate": "0.9254139231429829"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1629117.310458942864370871125214869",
        "dailyWithdrawUSD": "4578664.521935256619871083933588532",
        "inputTokenPriceUSD": "0.9986891578689848732919037609813985"
      },
      {
        "totalValueLockedUSD": "314070696.4935179190845467149933771",
        "totalBorrowBalanceUSD": "134922132.0997253009553263542577966",
        "totalDepositBalanceUSD": "314070696.4935179190845467149933771",
        "timestamp": "1681084547",
        "rates": [
          {
            "rate": "11.0739786361278007"
          },
          {
            "rate": "2.1479572722556013"
          },
          {
            "rate": "0.8480974493047687"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "400173915.5136159209218342398001819",
        "dailyWithdrawUSD": "400210349.5033211917227932328642714",
        "inputTokenPriceUSD": "0.9992046109333851996849427646878286"
      },
      {
        "totalValueLockedUSD": "313795627.8061026844668688492571111",
        "totalBorrowBalanceUSD": "134929063.3919457552829827666203919",
        "totalDepositBalanceUSD": "313795627.8061026844668688492571111",
        "timestamp": "1680995039",
        "rates": [
          {
            "rate": "11.0749752916573819"
          },
          {
            "rate": "2.1499505833147638"
          },
          {
            "rate": "0.8496274231980749"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "205199168.2543657132530565570062074",
        "dailyWithdrawUSD": "205347020.7456462224810559535344936",
        "inputTokenPriceUSD": "0.9982402440150582790815232046824432"
      },
      {
        "totalValueLockedUSD": "313802184.3956154643426819252712819",
        "totalBorrowBalanceUSD": "134894209.5798944122061832409130529",
        "totalDepositBalanceUSD": "313802184.3956154643426819252712819",
        "timestamp": "1680894623",
        "rates": [
          {
            "rate": "11.0746751580343112"
          },
          {
            "rate": "2.1493503160686224"
          },
          {
            "rate": "0.8491531442207008"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1190951.404365576252283795971471471",
        "dailyWithdrawUSD": "586302.585850231636159089933474116",
        "inputTokenPriceUSD": "0.9978209268574281066483224807145378"
      },
      {
        "totalValueLockedUSD": "313663365.5022785029499991349755801",
        "totalBorrowBalanceUSD": "134889880.815739859091810034952793",
        "totalDepositBalanceUSD": "313663365.5022785029499991349755801",
        "timestamp": "1680824591",
        "rates": [
          {
            "rate": "11.0751162777766442"
          },
          {
            "rate": "2.1502325555532884"
          },
          {
            "rate": "0.8498644018206576"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "205132173.9488469645745309185193302",
        "dailyWithdrawUSD": "200548645.1864821015929943989001169",
        "inputTokenPriceUSD": "0.9993262233369957545025802106749889"
      },
      {
        "totalValueLockedUSD": "308932288.3186686038571724729986416",
        "totalBorrowBalanceUSD": "134194178.5961291418305941305140088",
        "totalDepositBalanceUSD": "308932288.3186686038571724729986416",
        "timestamp": "1680737351",
        "rates": [
          {
            "rate": "11.0859510192476389"
          },
          {
            "rate": "2.1719020384952777"
          },
          {
            "rate": "0.8669051002918958"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "200788320.8846479509263109147130525",
        "dailyWithdrawUSD": "200309387.6692618696081174030070407",
        "inputTokenPriceUSD": "0.9988754928955945114043884618374139"
      },
      {
        "totalValueLockedUSD": "309129425.2863559215845939749011051",
        "totalBorrowBalanceUSD": "136533299.8142382336211832628768951",
        "totalDepositBalanceUSD": "309129425.2863559215845939749011051",
        "timestamp": "1680651575",
        "rates": [
          {
            "rate": "11.1041754888540843"
          },
          {
            "rate": "2.2083509777081686"
          },
          {
            "rate": "0.8955393677411126"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "198216915.4418147806371919337821191",
        "dailyWithdrawUSD": "203453915.3626857559312638147695777",
        "inputTokenPriceUSD": "1.001092346294221496724838101845418"
      },
      {
        "totalValueLockedUSD": "316315206.5641951425029429610683544",
        "totalBorrowBalanceUSD": "136809531.8066763631098748624819119",
        "totalDepositBalanceUSD": "316315206.5641951425029429610683544",
        "timestamp": "1680562499",
        "rates": [
          {
            "rate": "11.0812749715139768"
          },
          {
            "rate": "2.1625499430279536"
          },
          {
            "rate": "0.8593652394185345"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "259353.3444621504360889060275434073",
        "dailyWithdrawUSD": "541162.9199912635128659418952525249",
        "inputTokenPriceUSD": "1.007322970910270466479480597856073"
      },
      {
        "totalValueLockedUSD": "314463666.1100734988553966332035936",
        "totalBorrowBalanceUSD": "129327369.4799675312759803068926454",
        "totalDepositBalanceUSD": "314463666.1100734988553966332035936",
        "timestamp": "1680471671",
        "rates": [
          {
            "rate": "11.0281579441849913"
          },
          {
            "rate": "2.0563158883699826"
          },
          {
            "rate": "0.7790260304335171"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "200483068.6841686612068091009604399",
        "dailyWithdrawUSD": "200598336.0895180890682350956555805",
        "inputTokenPriceUSD": "1.000560908275109799450921284217778"
      },
      {
        "totalValueLockedUSD": "312668118.9019041356558756653213177",
        "totalBorrowBalanceUSD": "127106595.9881783605511043250887366",
        "totalDepositBalanceUSD": "312668118.9019041356558756653213177",
        "timestamp": "1680393215",
        "rates": [
          {
            "rate": "11.0163056781816662"
          },
          {
            "rate": "2.0326113563633325"
          },
          {
            "rate": "0.7616518128571577"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "200791.8985314004977960219607049967",
        "dailyWithdrawUSD": "1797104.867644185547869114565587773",
        "inputTokenPriceUSD": "0.9945027080978456758590844021758833"
      },
      {
        "totalValueLockedUSD": "314333353.4463266674363572240751065",
        "totalBorrowBalanceUSD": "126104145.970321670333572266304002",
        "totalDepositBalanceUSD": "314333353.4463266674363572240751065",
        "timestamp": "1680306455",
        "rates": [
          {
            "rate": "11.0029488041759429"
          },
          {
            "rate": "2.0058976083518858"
          },
          {
            "rate": "0.7422301861948842"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "199556790.5134421555739375451059807",
        "dailyWithdrawUSD": "200103749.7155454815458304111826281",
        "inputTokenPriceUSD": "0.9947487410824096767299210658300223"
      },
      {
        "totalValueLockedUSD": "316430831.0367705671894607581316744",
        "totalBorrowBalanceUSD": "125861028.1250594488629110521099885",
        "totalDepositBalanceUSD": "316430831.0367705671894607581316744",
        "timestamp": "1680215927",
        "rates": [
          {
            "rate": "10.9943799271964195"
          },
          {
            "rate": "1.9887598543928389"
          },
          {
            "rate": "0.729931937892713"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "402895556.3941653118508394302728627",
        "dailyWithdrawUSD": "402653010.7026091589496064469784415",
        "inputTokenPriceUSD": "0.9996809735662901233307055500603212"
      },
      {
        "totalValueLockedUSD": "317237300.0351773321403006044632793",
        "totalBorrowBalanceUSD": "125687421.0388405879416009291962426",
        "totalDepositBalanceUSD": "317237300.0351773321403006044632793",
        "timestamp": "1680133811",
        "rates": [
          {
            "rate": "10.9904839344623315"
          },
          {
            "rate": "1.980967868924663"
          },
          {
            "rate": "0.7243994983306645"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4971772.850165493114906591119168778",
        "dailyWithdrawUSD": "12735499.04308534109666601290954882",
        "inputTokenPriceUSD": "1.002897027790083243081800345769654"
      },
      {
        "totalValueLockedUSD": "325126316.4738143180040767880329209",
        "totalBorrowBalanceUSD": "124646010.0684885947427495524362371",
        "totalDepositBalanceUSD": "325126316.4738143180040767880329209",
        "timestamp": "1680041183",
        "rates": [
          {
            "rate": "10.958442639703153"
          },
          {
            "rate": "1.916885279406306"
          },
          {
            "rate": "0.6792166774509087"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "310747.7138772269714612723608631684",
        "dailyWithdrawUSD": "1670319.016183989585458633165320922",
        "inputTokenPriceUSD": "1.003189133576306049661670547647545"
      },
      {
        "totalValueLockedUSD": "327046413.2624623304268703368589704",
        "totalBorrowBalanceUSD": "124665341.4245039712144127026629674",
        "totalDepositBalanceUSD": "327046413.2624623304268703368589704",
        "timestamp": "1679960135",
        "rates": [
          {
            "rate": "10.9529633750984155"
          },
          {
            "rate": "1.905926750196831"
          },
          {
            "rate": "0.6716353268555378"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "420716.2340644986505468652826513435",
        "dailyWithdrawUSD": "61867339.20529907865761850732051237",
        "inputTokenPriceUSD": "1.00492401299316882803466424469011"
      },
      {
        "totalValueLockedUSD": "384937593.678202140471297471769479",
        "totalBorrowBalanceUSD": "123731575.842912676545084078067477",
        "totalDepositBalanceUSD": "384937593.678202140471297471769479",
        "timestamp": "1679873591",
        "rates": [
          {
            "rate": "10.8035818307881571"
          },
          {
            "rate": "1.6071636615763141"
          },
          {
            "rate": "0.4807332170488418"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "141287.5552595628892356933231010117",
        "dailyWithdrawUSD": "5025924.066009232328325400317326892",
        "inputTokenPriceUSD": "0.9956238843084295976781595954048508"
      },
      {
        "totalValueLockedUSD": "391367633.5646787389525549976885127",
        "totalBorrowBalanceUSD": "123732645.9042952426016327609733594",
        "totalDepositBalanceUSD": "391367633.5646787389525549976885127",
        "timestamp": "1679786855",
        "rates": [
          {
            "rate": "10.7903860870004131"
          },
          {
            "rate": "1.5807721740008262"
          },
          {
            "rate": "0.4654603892179228"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3031025.41517757451386541255946787",
        "dailyWithdrawUSD": "6368843.316680220048413788003862925",
        "inputTokenPriceUSD": "0.999525187754795303493636633710716"
      },
      {
        "totalValueLockedUSD": "396440999.3365098100888354238934981",
        "totalBorrowBalanceUSD": "124368621.2999563318875923159118463",
        "totalDepositBalanceUSD": "396440999.3365098100888354238934981",
        "timestamp": "1679702063",
        "rates": [
          {
            "rate": "10.7842818269903661"
          },
          {
            "rate": "1.5685636539807323"
          },
          {
            "rate": "0.4584644185130385"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "10296791.29045379890667228577246747",
        "dailyWithdrawUSD": "30088944.36262551876891598767988661",
        "inputTokenPriceUSD": "1.003781517276906273748902778039435"
      },
      {
        "totalValueLockedUSD": "415601880.1568862533067539777166687",
        "totalBorrowBalanceUSD": "124050544.9976388460791648277069199",
        "totalDepositBalanceUSD": "415601880.1568862533067539777166687",
        "timestamp": "1679615015",
        "rates": [
          {
            "rate": "10.7462100135247113"
          },
          {
            "rate": "1.4924200270494226"
          },
          {
            "rate": "0.4159636215710064"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "399221.1491160076695928037912543761",
        "dailyWithdrawUSD": "10500929.14626924409786845462330866",
        "inputTokenPriceUSD": "1.002105505430187751209146611589225"
      },
      {
        "totalValueLockedUSD": "424222297.3059187436614803840496174",
        "totalBorrowBalanceUSD": "123127497.5528111664710434427628136",
        "totalDepositBalanceUSD": "424222297.3059187436614803840496174",
        "timestamp": "1679529023",
        "rates": [
          {
            "rate": "10.725606999872858"
          },
          {
            "rate": "1.4512139997457159"
          },
          {
            "rate": "0.3938740043646883"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "18843190.39219851931456290790077126",
        "dailyWithdrawUSD": "15322449.25926793755428344605016266",
        "inputTokenPriceUSD": "0.9984981636439844281918782325997999"
      },
      {
        "totalValueLockedUSD": "422968003.1331014309647962223717895",
        "totalBorrowBalanceUSD": "119387374.5908759939403368515011202",
        "totalDepositBalanceUSD": "422968003.1331014309647962223717895",
        "timestamp": "1679442827",
        "rates": [
          {
            "rate": "10.7056523436958425"
          },
          {
            "rate": "1.4113046873916851"
          },
          {
            "rate": "0.3735284767860989"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "357325.7139711959616482551060605218",
        "dailyWithdrawUSD": "1328588.103449639474401787167792271",
        "inputTokenPriceUSD": "1.003680246349741994327051343640912"
      },
      {
        "totalValueLockedUSD": "423315992.251618783887873969873982",
        "totalBorrowBalanceUSD": "116481170.0067085547210292709527364",
        "totalDepositBalanceUSD": "423315992.251618783887873969873982",
        "timestamp": "1679355491",
        "rates": [
          {
            "rate": "10.6879089345844563"
          },
          {
            "rate": "1.3758178691689126"
          },
          {
            "rate": "0.3557837825265361"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5983635.460537126541020467073572355",
        "dailyWithdrawUSD": "8326011.684772969644979351278653423",
        "inputTokenPriceUSD": "1.002210133928369078144425245293602"
      },
      {
        "totalValueLockedUSD": "425747621.2695695192893933442733693",
        "totalBorrowBalanceUSD": "116290387.1483472057397426059154462",
        "totalDepositBalanceUSD": "425747621.2695695192893933442733693",
        "timestamp": "1679269787",
        "rates": [
          {
            "rate": "10.6828597085845628"
          },
          {
            "rate": "1.3657194171691256"
          },
          {
            "rate": "0.3507404701897615"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3049173.089879931351931982473254315",
        "dailyWithdrawUSD": "5887120.155548383993956527653693945",
        "inputTokenPriceUSD": "1.002426909228666957876460231196196"
      },
      {
        "totalValueLockedUSD": "425927924.3873639818083923994153422",
        "totalBorrowBalanceUSD": "114088891.8110145022556207300432747",
        "totalDepositBalanceUSD": "425927924.3873639818083923994153422",
        "timestamp": "1679181599",
        "rates": [
          {
            "rate": "10.6696488859714393"
          },
          {
            "rate": "1.3392977719428787"
          },
          {
            "rate": "0.3377758227646734"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "205012373.3590421023311868305716096",
        "dailyWithdrawUSD": "1939258.442898658935979206422699312",
        "inputTokenPriceUSD": "0.996102539870264118303626811647251"
      },
      {
        "totalValueLockedUSD": "225336234.4594443782712325936055566",
        "totalBorrowBalanceUSD": "112164492.0118891529239043363681265",
        "totalDepositBalanceUSD": "225336234.4594443782712325936055566",
        "timestamp": "1679097479",
        "rates": [
          {
            "rate": "11.2444119354503719"
          },
          {
            "rate": "2.4888238709007439"
          },
          {
            "rate": "1.13786865387558"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "7176517.924877840048082418357636872",
        "dailyWithdrawUSD": "73090367.74226571324687315052718803",
        "inputTokenPriceUSD": "1.00622283558909088825534800441364"
      },
      {
        "totalValueLockedUSD": "292543046.2088468679836736764341133",
        "totalBorrowBalanceUSD": "110191412.0927430520260445958690886",
        "totalDepositBalanceUSD": "292543046.2088468679836736764341133",
        "timestamp": "1679006027",
        "rates": [
          {
            "rate": "10.9416680209067919"
          },
          {
            "rate": "1.8833360418135839"
          },
          {
            "rate": "0.6583883680935603"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1306441.476933390894774037667251092",
        "dailyWithdrawUSD": "31598030.88095664994233581469342596",
        "inputTokenPriceUSD": "1.008516959765243960400463293977284"
      },
      {
        "totalValueLockedUSD": "320393133.7868920972746270708020411",
        "totalBorrowBalanceUSD": "105002910.8615027652654054278525984",
        "totalDepositBalanceUSD": "320393133.7868920972746270708020411",
        "timestamp": "1678923479",
        "rates": [
          {
            "rate": "10.8193283942984841"
          },
          {
            "rate": "1.6386567885969682"
          },
          {
            "rate": "0.5022113386880839"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "23821166.48325392051804883251603691",
        "dailyWithdrawUSD": "75583999.12253351597325690722640557",
        "inputTokenPriceUSD": "1.000020716319274622552573769983732"
      },
      {
        "totalValueLockedUSD": "372626812.702026101348218042681364",
        "totalBorrowBalanceUSD": "92961911.56166044641915574626413238",
        "totalDepositBalanceUSD": "372626812.702026101348218042681364",
        "timestamp": "1678836515",
        "rates": [
          {
            "rate": "10.623692944152513"
          },
          {
            "rate": "1.247385888305026"
          },
          {
            "rate": "0.2974599423909261"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "324196430.8702306189084750823738032",
        "dailyWithdrawUSD": "367960305.897778583231452977944517",
        "inputTokenPriceUSD": "1.0013484046605016595347110438494"
      },
      {
        "totalValueLockedUSD": "415748447.3559750393890830578091171",
        "totalBorrowBalanceUSD": "91607348.89783280734559702695401775",
        "totalDepositBalanceUSD": "415748447.3559750393890830578091171",
        "timestamp": "1678748795",
        "rates": [
          {
            "rate": "10.550857895840883"
          },
          {
            "rate": "1.101715791681766"
          },
          {
            "rate": "0.2344513295172971"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "77184523.37916755550393277618533427",
        "dailyWithdrawUSD": "185815651.3830683829322837954183722",
        "inputTokenPriceUSD": "0.9997622631866323027139873639631992"
      },
      {
        "totalValueLockedUSD": "520146629.5198541432031225867507043",
        "totalBorrowBalanceUSD": "87293245.14928605487530272852379918",
        "totalDepositBalanceUSD": "520146629.5198541432031225867507043",
        "timestamp": "1678665539",
        "rates": [
          {
            "rate": "10.4195606722255975"
          },
          {
            "rate": "0.8391213444511951"
          },
          {
            "rate": "0.1399505493785894"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "342627413.6171134143238507526983351",
        "dailyWithdrawUSD": "138360055.8390605879703808569546031",
        "inputTokenPriceUSD": "0.9921439951582546101415286957847605"
      },
      {
        "totalValueLockedUSD": "321599899.0468724018152989110668675",
        "totalBorrowBalanceUSD": "113992373.7246233895402091427934437",
        "totalDepositBalanceUSD": "321599899.0468724018152989110668675",
        "timestamp": "1678579163",
        "rates": [
          {
            "rate": "10.8861347356396399"
          },
          {
            "rate": "1.7722694712792798"
          },
          {
            "rate": "0.5837798938095533"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "447555602.4268934233838296049215219",
        "dailyWithdrawUSD": "322795239.2709029537632163763977362",
        "inputTokenPriceUSD": "1.005812847092204247791768042692406"
      },
      {
        "totalValueLockedUSD": "196679845.8105569147599558517666787",
        "totalBorrowBalanceUSD": "97100303.67313936174938669079056022",
        "totalDepositBalanceUSD": "196679845.8105569147599558517666787",
        "timestamp": "1678492739",
        "rates": [
          {
            "rate": "11.234242531437639"
          },
          {
            "rate": "2.4684850628752781"
          },
          {
            "rate": "1.1229053406804648"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "47089704.29321520374983075675194054",
        "dailyWithdrawUSD": "25357515.74726117340609450707601654",
        "inputTokenPriceUSD": "0.9993586477759074810276162929447425"
      },
      {
        "totalValueLockedUSD": "175303389.8673820080503706381413494",
        "totalBorrowBalanceUSD": "98029158.79580851199798889808765951",
        "totalDepositBalanceUSD": "175303389.8673820080503706381413494",
        "timestamp": "1678405391",
        "rates": [
          {
            "rate": "11.3979920835368972"
          },
          {
            "rate": "2.7959841670737945"
          },
          {
            "rate": "1.4344646403706792"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "17183773.29776384704599257695411766",
        "dailyWithdrawUSD": "7508288.639982505499216810270354985",
        "inputTokenPriceUSD": "1.001462904336964495038278226728924"
      },
      {
        "totalValueLockedUSD": "163591909.80402702026400175954089",
        "totalBorrowBalanceUSD": "96840422.82614325598395280610633089",
        "totalDepositBalanceUSD": "163591909.80402702026400175954089",
        "timestamp": "1678317491",
        "rates": [
          {
            "rate": "11.4799075635614686"
          },
          {
            "rate": "2.9598151271229372"
          },
          {
            "rate": "1.604731664833812"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1390933.64320488042305045302130867",
        "dailyWithdrawUSD": "3137094.810366774220316615980309213",
        "inputTokenPriceUSD": "0.9894838407888232606763323926339232"
      },
      {
        "totalValueLockedUSD": "167740858.5438783069768347466203084",
        "totalBorrowBalanceUSD": "98358583.55175832796426740833476787",
        "totalDepositBalanceUSD": "167740858.5438783069768347466203084",
        "timestamp": "1678232327",
        "rates": [
          {
            "rate": "11.4659296958586939"
          },
          {
            "rate": "2.9318593917173878"
          },
          {
            "rate": "1.5749680808381135"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "310141.2345643040241208133772507019",
        "dailyWithdrawUSD": "687703.5077152593434518039242866305",
        "inputTokenPriceUSD": "1.003957233339450627478323278978566"
      },
      {
        "totalValueLockedUSD": "168578537.1710979271488874141418807",
        "totalBorrowBalanceUSD": "98906578.37550540230616448850567089",
        "totalDepositBalanceUSD": "168578537.1710979271488874141418807",
        "timestamp": "1678146515",
        "rates": [
          {
            "rate": "11.4667720842538769"
          },
          {
            "rate": "2.9335441685077538"
          },
          {
            "rate": "1.5766693859148647"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "8445236.696697432621205097187430387",
        "dailyWithdrawUSD": "7622360.099517070625820609894375475",
        "inputTokenPriceUSD": "1.0067453604335022846346559784002"
      },
      {
        "totalValueLockedUSD": "166989306.4473562407553015714829511",
        "totalBorrowBalanceUSD": "98291124.08466882542903850801385343",
        "totalDepositBalanceUSD": "166989306.4473562407553015714829511",
        "timestamp": "1678060523",
        "rates": [
          {
            "rate": "11.4715173208465748"
          },
          {
            "rate": "2.9430346416931496"
          },
          {
            "rate": "1.5870942173767094"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "277377.8178193219556741637904768476",
        "dailyWithdrawUSD": "456115.950867583397358047527691346",
        "inputTokenPriceUSD": "1.002249172364780302033976710739033"
      },
      {
        "totalValueLockedUSD": "165482272.353788689350770005166308",
        "totalBorrowBalanceUSD": "97388042.62987270399153767764574823",
        "totalDepositBalanceUSD": "165482272.353788689350770005166308",
        "timestamp": "1677974039",
        "rates": [
          {
            "rate": "11.4712751482861628"
          },
          {
            "rate": "2.9425502965723256"
          },
          {
            "rate": "1.5865496873305171"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "10252250.61801881157936040635118625",
        "dailyWithdrawUSD": "923279.2667589974052546470593924164",
        "inputTokenPriceUSD": "0.9921774295178329940451745058286925"
      },
      {
        "totalValueLockedUSD": "156064893.4049845653067632577489459",
        "totalBorrowBalanceUSD": "97406522.58194259418454325525626524",
        "totalDepositBalanceUSD": "156064893.4049845653067632577489459",
        "timestamp": "1677885971",
        "rates": [
          {
            "rate": "11.5603518535669623"
          },
          {
            "rate": "3.1207037071339246"
          },
          {
            "rate": "1.7814104045883858"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "10342480.77922463774912277746464814",
        "dailyWithdrawUSD": "20783310.95020705223202081576753333",
        "inputTokenPriceUSD": "0.9910561116859207832670187716730102"
      },
      {
        "totalValueLockedUSD": "167227296.7364696615452247581529806",
        "totalBorrowBalanceUSD": "103989738.7410735261881328151561511",
        "totalDepositBalanceUSD": "167227296.7364696615452247581529806",
        "timestamp": "1677798827",
        "rates": [
          {
            "rate": "11.5546157300740586"
          },
          {
            "rate": "3.1092314601481173"
          },
          {
            "rate": "1.7667468881549157"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "161755.5641951398088654644566866832",
        "dailyWithdrawUSD": "130083.3180603066048684492041565273",
        "inputTokenPriceUSD": "0.995539244124749014371404908701359"
      },
      {
        "totalValueLockedUSD": "167008313.720163837054688190462893",
        "totalBorrowBalanceUSD": "103472269.6714908710432701206908859",
        "totalDepositBalanceUSD": "167008313.720163837054688190462893",
        "timestamp": "1677714719",
        "rates": [
          {
            "rate": "11.5489080057270667"
          },
          {
            "rate": "3.0978160114541335"
          },
          {
            "rate": "1.7540673738578705"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "585151.9565855647610247447425721073",
        "dailyWithdrawUSD": "6219790.534151445593943766171047591",
        "inputTokenPriceUSD": "0.994474507344629810692586253164052"
      },
      {
        "totalValueLockedUSD": "172457642.1488954886429280949938473",
        "totalBorrowBalanceUSD": "96823810.78144867033275651627403077",
        "totalDepositBalanceUSD": "172457642.1488954886429280949938473",
        "timestamp": "1677628619",
        "rates": [
          {
            "rate": "11.4035874495321055"
          },
          {
            "rate": "2.8071748990642111"
          },
          {
            "rate": "1.4466099281769669"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3732602.908196867661828753014035679",
        "dailyWithdrawUSD": "1745604.487437677971658125509627115",
        "inputTokenPriceUSD": "0.993527822525133451765107682187418"
      },
      {
        "totalValueLockedUSD": "170243944.131277880458910983395851",
        "totalBorrowBalanceUSD": "96067369.03001415445487211494158353",
        "totalDepositBalanceUSD": "170243944.131277880458910983395851",
        "timestamp": "1677535739",
        "rates": [
          {
            "rate": "11.4107302226803493"
          },
          {
            "rate": "2.8214604453606985"
          },
          {
            "rate": "1.4613137033133847"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "15259011.48631474805455517832787595",
        "dailyWithdrawUSD": "12380537.40415356660021732927348478",
        "inputTokenPriceUSD": "0.9921636513444328312915229981895858"
      },
      {
        "totalValueLockedUSD": "169193231.4803111107627089393167848",
        "totalBorrowBalanceUSD": "97111959.14797386749495492276045194",
        "totalDepositBalanceUSD": "169193231.4803111107627089393167848",
        "timestamp": "1677453083",
        "rates": [
          {
            "rate": "11.4349258911115946"
          },
          {
            "rate": "2.8698517822231893"
          },
          {
            "rate": "1.5110546100671062"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4255077.416572847601331229442306807",
        "dailyWithdrawUSD": "3691945.064801203017170711530570936",
        "inputTokenPriceUSD": "1.00287614429404202585216618328624"
      },
      {
        "totalValueLockedUSD": "168428868.0478765828235978638653223",
        "totalBorrowBalanceUSD": "96319344.29928609936671797217651819",
        "totalDepositBalanceUSD": "168428868.0478765828235978638653223",
        "timestamp": "1677369287",
        "rates": [
          {
            "rate": "11.4296730416336742"
          },
          {
            "rate": "2.8593460832673485"
          },
          {
            "rate": "1.5003796696782302"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "10747397.73654548982914350413799742",
        "dailyWithdrawUSD": "10983796.86870543851142802297227144",
        "inputTokenPriceUSD": "1.001723702106097568801978963097556"
      },
      {
        "totalValueLockedUSD": "169051910.8265623827414783499662232",
        "totalBorrowBalanceUSD": "96470279.76002252176573484108180198",
        "totalDepositBalanceUSD": "169051910.8265623827414783499662232",
        "timestamp": "1677282491",
        "rates": [
          {
            "rate": "11.4266360528895918"
          },
          {
            "rate": "2.8532721057791837"
          },
          {
            "rate": "1.4941157236645122"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "11896504.43161956117125810281721597",
        "dailyWithdrawUSD": "9936275.412894785331603679331092499",
        "inputTokenPriceUSD": "1.003618323537753967810617357423666"
      },
      {
        "totalValueLockedUSD": "166775813.9513400662470128447164262",
        "totalBorrowBalanceUSD": "96219534.89785940314181802252816509",
        "totalDepositBalanceUSD": "166775813.9513400662470128447164262",
        "timestamp": "1677194543",
        "rates": [
          {
            "rate": "11.4423475541046606"
          },
          {
            "rate": "2.8846951082093211"
          },
          {
            "rate": "1.5266903219298925"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "915323.5624410542495675858465938264",
        "dailyWithdrawUSD": "2471190.056848629471687387339929394",
        "inputTokenPriceUSD": "1.00152505016153720364265767910531"
      },
      {
        "totalValueLockedUSD": "168510812.8758483869068155568380781",
        "totalBorrowBalanceUSD": "96214836.656311423734866128615141",
        "totalDepositBalanceUSD": "168510812.8758483869068155568380781",
        "timestamp": "1677109535",
        "rates": [
          {
            "rate": "11.4274273505354885"
          },
          {
            "rate": "2.854854701070977"
          },
          {
            "rate": "1.4957836831799942"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2383864.913420599373676143885774373",
        "dailyWithdrawUSD": "2552277.520477789602132130154417802",
        "inputTokenPriceUSD": "1.002624327577610941140902639547723"
      },
      {
        "totalValueLockedUSD": "167237916.8045499403621742536071971",
        "totalBorrowBalanceUSD": "94923393.50712141257762660049328388",
        "totalDepositBalanceUSD": "167237916.8045499403621742536071971",
        "timestamp": "1677022283",
        "rates": [
          {
            "rate": "11.4189864478845357"
          },
          {
            "rate": "2.8379728957690714"
          },
          {
            "rate": "1.4785471007676959"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "7338506.451708360332956047286432699",
        "dailyWithdrawUSD": "2792275.817217304612366709193504051",
        "inputTokenPriceUSD": "0.9936334474300072862675043607778696"
      },
      {
        "totalValueLockedUSD": "162322679.889862731444155641547787",
        "totalBorrowBalanceUSD": "96919874.61312494309600953624197588",
        "totalDepositBalanceUSD": "162322679.889862731444155641547787",
        "timestamp": "1676936819",
        "rates": [
          {
            "rate": "11.4927028880224854"
          },
          {
            "rate": "2.9854057760449708"
          },
          {
            "rate": "1.6329065868215804"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1771275.400539590743041966614450465",
        "dailyWithdrawUSD": "2937274.590773489567158087834294822",
        "inputTokenPriceUSD": "0.991348632666376295387533798475676"
      },
      {
        "totalValueLockedUSD": "163264600.2750314323545272959988071",
        "totalBorrowBalanceUSD": "98014752.52788469565925509381387525",
        "totalDepositBalanceUSD": "163264600.2750314323545272959988071",
        "timestamp": "1676847515",
        "rates": [
          {
            "rate": "11.5008564429800679"
          },
          {
            "rate": "3.0017128859601359"
          },
          {
            "rate": "1.6501661454493088"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5366028.952849241045290007064391365",
        "dailyWithdrawUSD": "6969907.52996373696301134322051452",
        "inputTokenPriceUSD": "0.9901038491311363128497980831790879"
      },
      {
        "totalValueLockedUSD": "166527542.5253542686054246658711139",
        "totalBorrowBalanceUSD": "99171654.33816827411563799684034696",
        "totalDepositBalanceUSD": "166527542.5253542686054246658711139",
        "timestamp": "1676763323",
        "rates": [
          {
            "rate": "11.4888166708418261"
          },
          {
            "rate": "2.9776333416836522"
          },
          {
            "rate": "1.6241298833688807"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "184443656.6812935406554012702251866",
        "dailyWithdrawUSD": "185113535.1139166933895174273746924",
        "inputTokenPriceUSD": "1.000204022054728464386487980040696"
      },
      {
        "totalValueLockedUSD": "167026076.988882492931275950213618",
        "totalBorrowBalanceUSD": "103424935.5580772635191666661657287",
        "totalDepositBalanceUSD": "167026076.988882492931275950213618",
        "timestamp": "1676674595",
        "rates": [
          {
            "rate": "11.5480347935118001"
          },
          {
            "rate": "3.0960695870236002"
          },
          {
            "rate": "1.7526731655964911"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1144249.267029410320808870876296715",
        "dailyWithdrawUSD": "3670614.338304862165869021008265213",
        "inputTokenPriceUSD": "0.9992786318940043823110754774353676"
      },
      {
        "totalValueLockedUSD": "170284655.3836512231821523292549486",
        "totalBorrowBalanceUSD": "103947008.9458403554737352695873649",
        "totalDepositBalanceUSD": "170284655.3836512231821523292549486",
        "timestamp": "1676591267",
        "rates": [
          {
            "rate": "11.5260762227576822"
          },
          {
            "rate": "3.0521524455153644"
          },
          {
            "rate": "1.7037983233291327"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2991684.419959747916468171679624851",
        "dailyWithdrawUSD": "4835665.457222834636280732300126041",
        "inputTokenPriceUSD": "1.003647698585591670740050907321613"
      },
      {
        "totalValueLockedUSD": "171705911.2508237268588247725574428",
        "totalBorrowBalanceUSD": "104442228.4157729849348833483677382",
        "totalDepositBalanceUSD": "171705911.2508237268588247725574428",
        "timestamp": "1676505287",
        "rates": [
          {
            "rate": "11.5206547720212494"
          },
          {
            "rate": "3.0413095440424988"
          },
          {
            "rate": "1.6916803500886754"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4441068.512143300623035097807545606",
        "dailyWithdrawUSD": "7184514.273038106904677147764485506",
        "inputTokenPriceUSD": "1.001209541874106729412974121640285"
      },
      {
        "totalValueLockedUSD": "173979422.7606583584880912222289668",
        "totalBorrowBalanceUSD": "105984014.996986500630260593873426",
        "totalDepositBalanceUSD": "173979422.7606583584880912222289668",
        "timestamp": "1676416667",
        "rates": [
          {
            "rate": "11.522938033641027"
          },
          {
            "rate": "3.045876067282054"
          },
          {
            "rate": "1.6962482229665866"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2566891.74642084081048510185671935",
        "dailyWithdrawUSD": "5629779.414571328989137305908617118",
        "inputTokenPriceUSD": "0.9985674194668375368100560833354019"
      },
      {
        "totalValueLockedUSD": "177232419.09773974902354800154686",
        "totalBorrowBalanceUSD": "106151392.6709024890791987370582244",
        "totalDepositBalanceUSD": "177232419.09773974902354800154686",
        "timestamp": "1676331635",
        "rates": [
          {
            "rate": "11.497346411194177"
          },
          {
            "rate": "2.9946928223883541"
          },
          {
            "rate": "1.6404494863787415"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "14110478.0081827688692836199949797",
        "dailyWithdrawUSD": "13882523.98156733014961397476180455",
        "inputTokenPriceUSD": "0.9996757037378492153426093415960499"
      },
      {
        "totalValueLockedUSD": "176758977.5300955935052949012321352",
        "totalBorrowBalanceUSD": "105534064.8309369514040187619545889",
        "totalDepositBalanceUSD": "176758977.5300955935052949012321352",
        "timestamp": "1676245475",
        "rates": [
          {
            "rate": "11.4926257861096079"
          },
          {
            "rate": "2.9852515722192157"
          },
          {
            "rate": "1.630391713675146"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1594095.850870973999482864667817777",
        "dailyWithdrawUSD": "2723304.284981974788755795985123892",
        "inputTokenPriceUSD": "0.9984052984960813738142057778893533"
      },
      {
        "totalValueLockedUSD": "177911299.2150745691139248525340777",
        "totalBorrowBalanceUSD": "105638592.0022499615683509694243434",
        "totalDepositBalanceUSD": "177911299.2150745691139248525340777",
        "timestamp": "1676159267",
        "rates": [
          {
            "rate": "11.4844269461089365"
          },
          {
            "rate": "2.9688538922178731"
          },
          {
            "rate": "1.6127840006659535"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "515762.3131392881018838924384085689",
        "dailyWithdrawUSD": "417930.294202508553042098790153426",
        "inputTokenPriceUSD": "0.9985858640763894597999929846467571"
      },
      {
        "totalValueLockedUSD": "177103585.5717858426097272913257511",
        "totalBorrowBalanceUSD": "105486694.6545910611820100894660545",
        "totalDepositBalanceUSD": "177103585.5717858426097272913257511",
        "timestamp": "1676073467",
        "rates": [
          {
            "rate": "11.4890527625838794"
          },
          {
            "rate": "2.9781055251677588"
          },
          {
            "rate": "1.622641643967012"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5995921.276669372346561660798031663",
        "dailyWithdrawUSD": "5734602.75730469465119403291488414",
        "inputTokenPriceUSD": "0.994645851641532053031026039503099"
      },
      {
        "totalValueLockedUSD": "177768632.399303675838574194676392",
        "totalBorrowBalanceUSD": "109360898.617970548356676107986551",
        "totalDepositBalanceUSD": "177768632.399303675838574194676392",
        "timestamp": "1675986995",
        "rates": [
          {
            "rate": "11.5379658589791595"
          },
          {
            "rate": "3.075931717958319"
          },
          {
            "rate": "1.728683951392064"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2053465.673089314764960254707676367",
        "dailyWithdrawUSD": "2365834.116416076642551019242493168",
        "inputTokenPriceUSD": "0.9998813912467778093069783786283323"
      },
      {
        "totalValueLockedUSD": "178637754.1399854938513723974479758",
        "totalBorrowBalanceUSD": "110793355.1538452383046614839521809",
        "totalDepositBalanceUSD": "178637754.1399854938513723974479758",
        "timestamp": "1675900043",
        "rates": [
          {
            "rate": "11.5505301682104755"
          },
          {
            "rate": "3.101060336420951"
          },
          {
            "rate": "1.7571058545488908"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "6218624.186724242859531264511989853",
        "dailyWithdrawUSD": "3139248.285904233796732788908123439",
        "inputTokenPriceUSD": "1.003153628831320812044269684328871"
      },
      {
        "totalValueLockedUSD": "175186873.8861148523963167431713147",
        "totalBorrowBalanceUSD": "110550800.1322242205452002536060406",
        "totalDepositBalanceUSD": "175186873.8861148523963167431713147",
        "timestamp": "1675813283",
        "rates": [
          {
            "rate": "11.5776115575548529"
          },
          {
            "rate": "3.1552231151097058"
          },
          {
            "rate": "1.8182159344173886"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3421665.414845240330034886454071341",
        "dailyWithdrawUSD": "8523371.411166693818011586602220646",
        "inputTokenPriceUSD": "1.001117776393900958081518888646947"
      },
      {
        "totalValueLockedUSD": "180645728.7974321826270899443465194",
        "totalBorrowBalanceUSD": "106027075.1772738631325691003610048",
        "totalDepositBalanceUSD": "180645728.7974321826270899443465194",
        "timestamp": "1675725623",
        "rates": [
          {
            "rate": "11.4673335344396095"
          },
          {
            "rate": "2.9346670688792189"
          },
          {
            "rate": "1.5770439491035467"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "9521878.057060849450026506506381045",
        "dailyWithdrawUSD": "4459728.067457730773627003979348322",
        "inputTokenPriceUSD": "1.003176038006901813057445348298915"
      },
      {
        "totalValueLockedUSD": "175860799.6463715257915641072569212",
        "totalBorrowBalanceUSD": "105914913.0348742597579654758088557",
        "totalDepositBalanceUSD": "175860799.6463715257915641072569212",
        "timestamp": "1675634135",
        "rates": [
          {
            "rate": "11.5056631534471658"
          },
          {
            "rate": "3.0113263068943315"
          },
          {
            "rate": "1.659380443301034"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2096959.669902030906834977479576722",
        "dailyWithdrawUSD": "1301845.291856258846160746853086",
        "inputTokenPriceUSD": "1.004836811539445536244469985450692"
      },
      {
        "totalValueLockedUSD": "174979357.4192131547239144853201028",
        "totalBorrowBalanceUSD": "104232625.6897114952228128970900778",
        "totalDepositBalanceUSD": "174979357.4192131547239144853201028",
        "timestamp": "1675549103",
        "rates": [
          {
            "rate": "11.4892122902122273"
          },
          {
            "rate": "2.9784245804244547"
          },
          {
            "rate": "1.6242408171295589"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4695384.820355554360860076832424498",
        "dailyWithdrawUSD": "4277169.342116523629879637682974253",
        "inputTokenPriceUSD": "1.004419594044853684473540177755081"
      },
      {
        "totalValueLockedUSD": "174604777.0263224793698266705131945",
        "totalBorrowBalanceUSD": "104115272.9857480566406614095626886",
        "totalDepositBalanceUSD": "174604777.0263224793698266705131945",
        "timestamp": "1675465679",
        "rates": [
          {
            "rate": "11.4907268409961066"
          },
          {
            "rate": "2.9814536819922131"
          },
          {
            "rate": "1.6275235569693401"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1380395.571800509680228070968536663",
        "dailyWithdrawUSD": "3079616.255756333827181855923278109",
        "inputTokenPriceUSD": "1.004615020603186380388727714706865"
      },
      {
        "totalValueLockedUSD": "174487277.2464032971733009661741489",
        "totalBorrowBalanceUSD": "101991815.4809661489591702821201631",
        "totalDepositBalanceUSD": "174487277.2464032971733009661741489",
        "timestamp": "1675381811",
        "rates": [
          {
            "rate": "11.4613064779231222"
          },
          {
            "rate": "2.9226129558462444"
          },
          {
            "rate": "1.5650506869891226"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5839576.607783616115098945790632905",
        "dailyWithdrawUSD": "7216056.522348135136876354127825767",
        "inputTokenPriceUSD": "0.9943136019643758985450344997474841"
      },
      {
        "totalValueLockedUSD": "177878880.2231130916468774767578395",
        "totalBorrowBalanceUSD": "105402382.5220086879133053715600904",
        "totalDepositBalanceUSD": "177878880.2231130916468774767578395",
        "timestamp": "1675295819",
        "rates": [
          {
            "rate": "11.4813776771936126"
          },
          {
            "rate": "2.9627553543872253"
          },
          {
            "rate": "1.6070483771811828"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2205013.891819854955624481118268611",
        "dailyWithdrawUSD": "2046717.778237175196773634159480874",
        "inputTokenPriceUSD": "1.005479225805830235350949160511115"
      },
      {
        "totalValueLockedUSD": "177120989.7799315380854391995516539",
        "totalBorrowBalanceUSD": "104921756.9997554633677728138859101",
        "totalDepositBalanceUSD": "177120989.7799315380854391995516539",
        "timestamp": "1675208195",
        "rates": [
          {
            "rate": "11.4809325506682286"
          },
          {
            "rate": "2.9618651013364572"
          },
          {
            "rate": "1.6061304515395979"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2986280.61486052127715664874220805",
        "dailyWithdrawUSD": "4003647.643351785526558362573126121",
        "inputTokenPriceUSD": "1.002235504798608434521238912433124"
      },
      {
        "totalValueLockedUSD": "178064781.1907296889941099765910017",
        "totalBorrowBalanceUSD": "105182111.4504237126213674563505222",
        "totalDepositBalanceUSD": "178064781.1907296889941099765910017",
        "timestamp": "1675122611",
        "rates": [
          {
            "rate": "11.4767385445530123"
          },
          {
            "rate": "2.9534770891060246"
          },
          {
            "rate": "1.5970920298331874"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "7665759.359617576207748877248370663",
        "dailyWithdrawUSD": "5539499.532588309064389338088963245",
        "inputTokenPriceUSD": "1.001862071675292789744032405193908"
      },
      {
        "totalValueLockedUSD": "174541349.9441979191280598821256569",
        "totalBorrowBalanceUSD": "99914285.64544745853137159159691867",
        "totalDepositBalanceUSD": "174541349.9441979191280598821256569",
        "timestamp": "1675034051",
        "rates": [
          {
            "rate": "11.4310967994311216"
          },
          {
            "rate": "2.8621935988622433"
          },
          {
            "rate": "1.5024122261000962"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1528620.861068867877640886712559214",
        "dailyWithdrawUSD": "1188094.540065741331794372873063941",
        "inputTokenPriceUSD": "0.9935316757656338263115094553610712"
      },
      {
        "totalValueLockedUSD": "176456947.2707518004461624614445757",
        "totalBorrowBalanceUSD": "97700736.06364253825958481643497499",
        "totalDepositBalanceUSD": "176456947.2707518004461624614445757",
        "timestamp": "1674944651",
        "rates": [
          {
            "rate": "11.384199942754183"
          },
          {
            "rate": "2.7683998855083661"
          },
          {
            "rate": "1.4075333303365595"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2788410.502332617092072438908371223",
        "dailyWithdrawUSD": "2496241.816397149820566961834789506",
        "inputTokenPriceUSD": "1.006443230669172919414450705103048"
      },
      {
        "totalValueLockedUSD": "174309964.4123971833003524861652007",
        "totalBorrowBalanceUSD": "96630328.69887690153321990632441101",
        "totalDepositBalanceUSD": "174309964.4123971833003524861652007",
        "timestamp": "1674861947",
        "rates": [
          {
            "rate": "11.385897129316874"
          },
          {
            "rate": "2.771794258633748"
          },
          {
            "rate": "1.4109314317034113"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "9284649.967278726771314831181917833",
        "dailyWithdrawUSD": "15809147.16910011585612816432026358",
        "inputTokenPriceUSD": "0.9955993449355895768762653569543389"
      },
      {
        "totalValueLockedUSD": "181261246.5696400661554786017556749",
        "totalBorrowBalanceUSD": "96760873.48473048347614173253542845",
        "totalDepositBalanceUSD": "181261246.5696400661554786017556749",
        "timestamp": "1674776459",
        "rates": [
          {
            "rate": "11.3345491702415953"
          },
          {
            "rate": "2.6690983404831907"
          },
          {
            "rate": "1.3099550735803984"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1982653.010824226410246087666605073",
        "dailyWithdrawUSD": "856250.0855859947627230810561591097",
        "inputTokenPriceUSD": "0.9980896790813004447997047900031473"
      },
      {
        "totalValueLockedUSD": "181885332.3358337427514016393834593",
        "totalBorrowBalanceUSD": "97577688.64349094155314697118550183",
        "totalDepositBalanceUSD": "181885332.3358337427514016393834593",
        "timestamp": "1674690563",
        "rates": [
          {
            "rate": "11.3411971100497969"
          },
          {
            "rate": "2.6823942200995938"
          },
          {
            "rate": "1.3228619171978453"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "9325294.915355434480808495997158552",
        "dailyWithdrawUSD": "4712082.495421273563584726017035666",
        "inputTokenPriceUSD": "1.007795047779918871387277873596741"
      },
      {
        "totalValueLockedUSD": "176109360.4342132272737157807006775",
        "totalBorrowBalanceUSD": "96690646.0550556816178789247382105",
        "totalDepositBalanceUSD": "176109360.4342132272737157807006775",
        "timestamp": "1674603839",
        "rates": [
          {
            "rate": "11.3725929886881492"
          },
          {
            "rate": "2.7451859773762984"
          },
          {
            "rate": "1.384521976326294"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2100283.933235337219066569886121985",
        "dailyWithdrawUSD": "1260447.508644956253216908177455081",
        "inputTokenPriceUSD": "1.00067356712997770000396819321289"
      },
      {
        "totalValueLockedUSD": "175680357.8043459841398639355394412",
        "totalBorrowBalanceUSD": "95881807.5660752652437649504916661",
        "totalDepositBalanceUSD": "175680357.8043459841398639355394412",
        "timestamp": "1674518147",
        "rates": [
          {
            "rate": "11.3644347078659339"
          },
          {
            "rate": "2.7288694157318679"
          },
          {
            "rate": "1.3683205245039294"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "830383.500480167867609708622628961",
        "dailyWithdrawUSD": "1506724.763475924811335466790463136",
        "inputTokenPriceUSD": "1.003065835763769123463432861024312"
      },
      {
        "totalValueLockedUSD": "176229560.0881940452123775304465364",
        "totalBorrowBalanceUSD": "95456942.18773179341266108919978662",
        "totalDepositBalanceUSD": "176229560.0881940452123775304465364",
        "timestamp": "1674430751",
        "rates": [
          {
            "rate": "11.3541554282322897"
          },
          {
            "rate": "2.7083108564645794"
          },
          {
            "rate": "1.3482143250699546"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4681676.097029351856325825420830427",
        "dailyWithdrawUSD": "3454568.215698636409516911137058658",
        "inputTokenPriceUSD": "1.002386287852208452785447247044989"
      },
      {
        "totalValueLockedUSD": "175686425.7136433159526125183510568",
        "totalBorrowBalanceUSD": "95460927.22286536174252268263411303",
        "totalDepositBalanceUSD": "175686425.7136433159526125183510568",
        "timestamp": "1674344783",
        "rates": [
          {
            "rate": "11.3583984991920415"
          },
          {
            "rate": "2.7167969983840831"
          },
          {
            "rate": "1.3566586368139991"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2475621.508510446455427203383711267",
        "dailyWithdrawUSD": "4927119.302341690646025056247828254",
        "inputTokenPriceUSD": "1.006342349788250016238711135536979"
      },
      {
        "totalValueLockedUSD": "176307633.7000504688752889606998906",
        "totalBorrowBalanceUSD": "94413537.54940993154156899518807898",
        "totalDepositBalanceUSD": "176307633.7000504688752889606998906",
        "timestamp": "1674258755",
        "rates": [
          {
            "rate": "11.3387605593720767"
          },
          {
            "rate": "2.6775211187441533"
          },
          {
            "rate": "1.3183694195003421"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4949915.253570519285532116572063794",
        "dailyWithdrawUSD": "4831631.593234070324303549965209533",
        "inputTokenPriceUSD": "0.9960077382229222622379878787379094"
      },
      {
        "totalValueLockedUSD": "178562257.8132749946024303476090184",
        "totalBorrowBalanceUSD": "95316186.57298616933801553790144973",
        "totalDepositBalanceUSD": "178562257.8132749946024303476090184",
        "timestamp": "1674171383",
        "rates": [
          {
            "rate": "11.3344943688699715"
          },
          {
            "rate": "2.6689887377399429"
          },
          {
            "rate": "1.31053170046986"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "303560.5829972542332176772241448462",
        "dailyWithdrawUSD": "245679.3614053459916145586455022379",
        "inputTokenPriceUSD": "1.008966260176902999602355224396548"
      },
      {
        "totalValueLockedUSD": "176750932.7521848210857377685191431",
        "totalBorrowBalanceUSD": "94041717.28697810634695516482299579",
        "totalDepositBalanceUSD": "176750932.7521848210857377685191431",
        "timestamp": "1674086279",
        "rates": [
          {
            "rate": "11.3301437932841536"
          },
          {
            "rate": "2.6602875865683072"
          },
          {
            "rate": "1.3021016612112217"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2131443.505008551331505533740131756",
        "dailyWithdrawUSD": "2309618.905365799965496789662485205",
        "inputTokenPriceUSD": "0.9990930386383168496677174733347144"
      },
      {
        "totalValueLockedUSD": "177224020.5996267743395848911946332",
        "totalBorrowBalanceUSD": "93913250.57578856410644369720978051",
        "totalDepositBalanceUSD": "177224020.5996267743395848911946332",
        "timestamp": "1673996891",
        "rates": [
          {
            "rate": "11.3247808560415193"
          },
          {
            "rate": "2.6495617120830387"
          },
          {
            "rate": "1.2918814374483552"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "1764005.673166435046582263766745296",
        "dailyWithdrawUSD": "2307538.154771980501388615109718509",
        "inputTokenPriceUSD": "1.000765981172392292134221971396453"
      },
      {
        "totalValueLockedUSD": "177694249.1238025644726837997881011",
        "totalBorrowBalanceUSD": "91403951.22563549160181836331535773",
        "totalDepositBalanceUSD": "177694249.1238025644726837997881011",
        "timestamp": "1673913083",
        "rates": [
          {
            "rate": "11.2859715299860912"
          },
          {
            "rate": "2.5719430599721825"
          },
          {
            "rate": "1.2193101143289857"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3263599.042684707901223276399543437",
        "dailyWithdrawUSD": "3590042.215155149746692486518563768",
        "inputTokenPriceUSD": "1.000387688295921297564519405257162"
      },
      {
        "totalValueLockedUSD": "178138507.3276135602742724456802258",
        "totalBorrowBalanceUSD": "86515957.35215773416899220427281606",
        "totalDepositBalanceUSD": "178138507.3276135602742724456802258",
        "timestamp": "1673826227",
        "rates": [
          {
            "rate": "11.2141662760330254"
          },
          {
            "rate": "2.4283325520660507"
          },
          {
            "rate": "1.0908625426020741"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2554397.258107506152361366219254322",
        "dailyWithdrawUSD": "896967.5919724646544236061754319704",
        "inputTokenPriceUSD": "1.001085552544853781130516263624646"
      },
      {
        "totalValueLockedUSD": "176644488.100153521511008134555447",
        "totalBorrowBalanceUSD": "85401442.00026286448087858238389043",
        "totalDepositBalanceUSD": "176644488.100153521511008134555447",
        "timestamp": "1673740067",
        "rates": [
          {
            "rate": "11.2086619992361906"
          },
          {
            "rate": "2.4173239984723813"
          },
          {
            "rate": "1.0821075080398025"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "5482665.106050132338856494500921145",
        "dailyWithdrawUSD": "8017119.957891213765374888270148602",
        "inputTokenPriceUSD": "1.002031163008726439660776418771041"
      },
      {
        "totalValueLockedUSD": "178818747.7846729594735564325803839",
        "totalBorrowBalanceUSD": "85349177.38061836832209979419694258",
        "totalDepositBalanceUSD": "178818747.7846729594735564325803839",
        "timestamp": "1673653703",
        "rates": [
          {
            "rate": "11.1932351786537948"
          },
          {
            "rate": "2.3864703573075896"
          },
          {
            "rate": "1.0551254055013429"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "8585968.049471609854527613520182712",
        "dailyWithdrawUSD": "4799526.934006958871246575371735366",
        "inputTokenPriceUSD": "0.9998693767069202581121841399683932"
      },
      {
        "totalValueLockedUSD": "175712293.6296944868981624508047739",
        "totalBorrowBalanceUSD": "87718086.49306621420060274610245673",
        "totalDepositBalanceUSD": "175712293.6296944868981624508047739",
        "timestamp": "1673567879",
        "rates": [
          {
            "rate": "11.2480349702513555"
          },
          {
            "rate": "2.4960699405027111"
          },
          {
            "rate": "1.1513988084261431"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "633519.0735086649799930450525406405",
        "dailyWithdrawUSD": "1301417.833381851753041801880030478",
        "inputTokenPriceUSD": "1.003388270456314864361317923485454"
      },
      {
        "totalValueLockedUSD": "176067205.3941423810186461529000603",
        "totalBorrowBalanceUSD": "87643398.55075547057654726837926068",
        "totalDepositBalanceUSD": "176067205.3941423810186461529000603",
        "timestamp": "1673477591",
        "rates": [
          {
            "rate": "11.244458713447062"
          },
          {
            "rate": "2.4889174268941241"
          },
          {
            "rate": "1.1449059746070102"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3116542.811440777592831023732046483",
        "dailyWithdrawUSD": "10503517.78168800864787052941545397",
        "inputTokenPriceUSD": "1.001623653496714390278062712237834"
      },
      {
        "totalValueLockedUSD": "182735665.9484743908828177217260461",
        "totalBorrowBalanceUSD": "87267527.38892293152409974174338032",
        "totalDepositBalanceUSD": "182735665.9484743908828177217260461",
        "timestamp": "1673394179",
        "rates": [
          {
            "rate": "11.1939031967335053"
          },
          {
            "rate": "2.3878063934670106"
          },
          {
            "rate": "1.0555378735781575"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "13443408.09944496092118734854689933",
        "dailyWithdrawUSD": "2914139.183412564262650938436865865",
        "inputTokenPriceUSD": "0.9975700246665342756953217528351811"
      },
      {
        "totalValueLockedUSD": "172341711.5276514448336880187733028",
        "totalBorrowBalanceUSD": "87489847.38384706564321504408174036",
        "totalDepositBalanceUSD": "172341711.5276514448336880187733028",
        "timestamp": "1673307707",
        "rates": [
          {
            "rate": "11.2691326200286825"
          },
          {
            "rate": "2.5382652400573651"
          },
          {
            "rate": "1.189785359811249"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "7835908.437003625214132118028983815",
        "dailyWithdrawUSD": "7965870.387378163885662096886347942",
        "inputTokenPriceUSD": "0.9984063210755710380725874115460067"
      },
      {
        "totalValueLockedUSD": "172730955.920496037403365505023437",
        "totalBorrowBalanceUSD": "94265257.69261390386355585780314875",
        "totalDepositBalanceUSD": "172730955.920496037403365505023437",
        "timestamp": "1673220047",
        "rates": [
          {
            "rate": "11.3643356661351477"
          },
          {
            "rate": "2.7286713322702953"
          },
          {
            "rate": "1.3690463357091937"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "40204750.60110812238368709040505719",
        "dailyWithdrawUSD": "40109334.70575519285815299678707665",
        "inputTokenPriceUSD": "0.9989621429341429158764216357876017"
      },
      {
        "totalValueLockedUSD": "172780099.0574031602650990571618828",
        "totalBorrowBalanceUSD": "94332009.4918492706561526585007977",
        "totalDepositBalanceUSD": "172780099.0574031602650990571618828",
        "timestamp": "1673133695",
        "rates": [
          {
            "rate": "11.3649134619187031"
          },
          {
            "rate": "2.7298269238374062"
          },
          {
            "rate": "1.370172102842104"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "149295.8804576568131454411046044165",
        "dailyWithdrawUSD": "1959.666207807352842383666702863779",
        "inputTokenPriceUSD": "0.9998319648815591843940601709475954"
      },
      {
        "totalValueLockedUSD": "172722034.9038949002900373021867243",
        "totalBorrowBalanceUSD": "94170957.7179668735719540578134802",
        "totalDepositBalanceUSD": "172722034.9038949002900373021867243",
        "timestamp": "1673048891",
        "rates": [
          {
            "rate": "11.3630412239585472"
          },
          {
            "rate": "2.7260824479170945"
          },
          {
            "rate": "1.366538414451205"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "2844891.457776536952233267750844894",
        "dailyWithdrawUSD": "6047655.232059037371402543690847493",
        "inputTokenPriceUSD": "1.000389325302185014240730494661085"
      },
      {
        "totalValueLockedUSD": "176163688.3743745700141791443974742",
        "totalBorrowBalanceUSD": "94206813.33160856546274768100826671",
        "totalDepositBalanceUSD": "176163688.3743745700141791443974742",
        "timestamp": "1672955759",
        "rates": [
          {
            "rate": "11.3369207789449352"
          },
          {
            "rate": "2.6738415578898705"
          },
          {
            "rate": "1.315710141458516"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "149901.6609678761044883210587853661",
        "dailyWithdrawUSD": "58203.84548775132362830258322671318",
        "inputTokenPriceUSD": "1.001288214370476782063367413682537"
      },
      {
        "totalValueLockedUSD": "175948974.3950498413617897022582756",
        "totalBorrowBalanceUSD": "94128067.94427787903829674185890547",
        "totalDepositBalanceUSD": "175948974.3950498413617897022582756",
        "timestamp": "1672873871",
        "rates": [
          {
            "rate": "11.3374333830673443"
          },
          {
            "rate": "2.6748667661346886"
          },
          {
            "rate": "1.316972398798503"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "3256136.943552044765656458788510148",
        "dailyWithdrawUSD": "509207.5164852131364120213826349628",
        "inputTokenPriceUSD": "1.000627705368902138297508981990076"
      },
      {
        "totalValueLockedUSD": "173070598.1011255045677237140940392",
        "totalBorrowBalanceUSD": "94059178.2420766984393739878317034",
        "totalDepositBalanceUSD": "173070598.1011255045677237140940392",
        "timestamp": "1672787999",
        "rates": [
          {
            "rate": "11.3586814186245834"
          },
          {
            "rate": "2.7173628372491669"
          },
          {
            "rate": "1.3584049239415522"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "907902.1948453641296196501538807291",
        "dailyWithdrawUSD": "216258.0036185627832469467701094795",
        "inputTokenPriceUSD": "0.9999226822601821656007195122597898"
      },
      {
        "totalValueLockedUSD": "173975161.1426677436968475371020635",
        "totalBorrowBalanceUSD": "94874089.33189826173061703059188751",
        "totalDepositBalanceUSD": "173975161.1426677436968475371020635",
        "timestamp": "1672701575",
        "rates": [
          {
            "rate": "11.3633272724571071"
          },
          {
            "rate": "2.7266545449142141"
          },
          {
            "rate": "1.367522078931614"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "224780.0834158541344153404152948902",
        "dailyWithdrawUSD": "127102.9791469405771226416364120114",
        "inputTokenPriceUSD": "1.007784625336655239483244851209358"
      },
      {
        "totalValueLockedUSD": "172380657.8694636608157788825912944",
        "totalBorrowBalanceUSD": "93730553.43840312220133985212756052",
        "totalDepositBalanceUSD": "172380657.8694636608157788825912944",
        "timestamp": "1672615127",
        "rates": [
          {
            "rate": "11.3593534613802757"
          },
          {
            "rate": "2.7187069227605514"
          },
          {
            "rate": "1.359767666889407"
          }
        ],
        "market": {
          "name": "Aave interest bearing DAI"
        },
        "dailyDepositUSD": "4937583.631527199496213515880874567",
        "dailyWithdrawUSD": "307903.7225324393246171500158345381",
        "inputTokenPriceUSD": "0.998254215381599929303636466675093"
      },
      {
        "totalValueLockedUSD": "168002431.686944951343427321279535",
        "totalBorrowBalanceUSD": "94132894.99767238224953298792371791",
        "totalDepositBalanceUSD": "168002431.686944951343427321279535",
        "timestamp": "1672530983",
        "rates": [
          {
            "rate": "11.4007659951291045"
          },
          {
            "rate": "2.8015319902582089"
          },
          {
            "rate": "1.4423320232477554"
          }
        ],
        "market": {
          "name": "Aave interest bearing WBTC"
        },
        "dailyDepositUSD": "540628.6031207008685365874456898244",
        "dailyWithdrawUSD": "4307846.907356977171285045213069664",
        "inputTokenPriceUSD": "0.9997928395219694724045688667810458"
      }
    ]
  }
}

market_daily_snapshots = json_data["data"]["marketDailySnapshots"]

with open("AAVE-V3-ETH-WBTC.csv", mode="w", newline="") as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=["datetime", "totalValueLockedUSD", "totalBorrowBalanceUSD", "totalDepositBalanceUSD", "utilizationRate", "borrowerStableRate", "borrowerVariableRate", "lenderVariableRate", "market", "dailyDepositUSD", "dailyWithdrawUSD", "inputTokenPriceUSD"])

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
            "market": snapshot["market"]["name"]
        })
