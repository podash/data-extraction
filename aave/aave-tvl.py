import csv
import json
from datetime import datetime

data = {
  "data": {
    "financialsDailySnapshots": [
      {
        "totalDepositBalanceUSD": "3617483629.213660836913465990310198",
        "totalBorrowBalanceUSD": "1241025606.999977029932821443823343",
        "timestamp": "1698840959",
        "dailyLiquidateUSD": "12363.72043318492352998241604132",
        "dailyRepayUSD": "12738393.67717156741079497044294513"
      },
      {
        "totalDepositBalanceUSD": "3630522766.911840451390104756417957",
        "totalBorrowBalanceUSD": "1244631782.369737834990295640907211",
        "timestamp": "1698796787",
        "dailyLiquidateUSD": "841.52473689309044897948275485",
        "dailyRepayUSD": "57120443.34408845800468912043040376"
      },
      {
        "totalDepositBalanceUSD": "3603229135.867695852424341645742447",
        "totalBorrowBalanceUSD": "1249070592.156262965761467370550328",
        "timestamp": "1698710375",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "34255296.3890366193005821789979939"
      },
      {
        "totalDepositBalanceUSD": "3641387921.050397857980715029369588",
        "totalBorrowBalanceUSD": "1260827257.412495915539419651221123",
        "timestamp": "1698623951",
        "dailyLiquidateUSD": "4000.10050962863072145135843705",
        "dailyRepayUSD": "16291582.39908736098776281131772794"
      },
      {
        "totalDepositBalanceUSD": "3593339841.194603479108217598222011",
        "totalBorrowBalanceUSD": "1253475328.589480058177710622607174",
        "timestamp": "1698537599",
        "dailyLiquidateUSD": "5222.4556146708069311610668",
        "dailyRepayUSD": "18762908.87517872918059414297238582"
      },
      {
        "totalDepositBalanceUSD": "3606815861.409306875747897838392796",
        "totalBorrowBalanceUSD": "1254889988.095980129676804127814573",
        "timestamp": "1698451007",
        "dailyLiquidateUSD": "5454.50452681472729575478338686",
        "dailyRepayUSD": "43209165.86012788447621143289354561"
      },
      {
        "totalDepositBalanceUSD": "3635167919.315265279514546841335369",
        "totalBorrowBalanceUSD": "1261626607.241475779120049586466888",
        "timestamp": "1698364499",
        "dailyLiquidateUSD": "29958.27026978242810153416470527",
        "dailyRepayUSD": "40061756.20717680986994980793358751"
      },
      {
        "totalDepositBalanceUSD": "3628203746.291270454660282862765335",
        "totalBorrowBalanceUSD": "1258060454.573183405442280555848939",
        "timestamp": "1698278327",
        "dailyLiquidateUSD": "48944.48320739269395770914074139",
        "dailyRepayUSD": "45322273.98559586195007262250587782"
      },
      {
        "totalDepositBalanceUSD": "3628765913.578178529060545198861137",
        "totalBorrowBalanceUSD": "1259258806.111780570997566583169638",
        "timestamp": "1698191999",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "39162103.46785509289825886461520211"
      },
      {
        "totalDepositBalanceUSD": "3584918082.916859054132467629646084",
        "totalBorrowBalanceUSD": "1241525067.550439178902644535550741",
        "timestamp": "1698105563",
        "dailyLiquidateUSD": "857935.5549077590486416887183987",
        "dailyRepayUSD": "47579351.33968383082716253037330138"
      },
      {
        "totalDepositBalanceUSD": "3425772549.325777325190282879611911",
        "totalBorrowBalanceUSD": "1208903395.363411445420261434034915",
        "timestamp": "1698019199",
        "dailyLiquidateUSD": "1381.41010769917927366654348328",
        "dailyRepayUSD": "16427955.29044117995887739620610323"
      },
      {
        "totalDepositBalanceUSD": "3344410768.031507727833135848673082",
        "totalBorrowBalanceUSD": "1177527479.279488182435505487026387",
        "timestamp": "1697932175",
        "dailyLiquidateUSD": "57451.9201961331416089080956",
        "dailyRepayUSD": "34003741.87863430907492744679909559"
      },
      {
        "totalDepositBalanceUSD": "3260001624.605010973502142188786027",
        "totalBorrowBalanceUSD": "1173737785.933601761642175545454896",
        "timestamp": "1697846219",
        "dailyLiquidateUSD": "703.31308336836520717329754425",
        "dailyRepayUSD": "55962220.2657621355636886578035658"
      },
      {
        "totalDepositBalanceUSD": "3214121753.657003450900512003075835",
        "totalBorrowBalanceUSD": "1143314173.086701339620157468396747",
        "timestamp": "1697759651",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "32784479.74712721088850354877226902"
      },
      {
        "totalDepositBalanceUSD": "3196032393.007592727213629115346435",
        "totalBorrowBalanceUSD": "1152829291.843750113533061382681333",
        "timestamp": "1697673479",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "27821325.12794698314685224910730413"
      },
      {
        "totalDepositBalanceUSD": "3167867623.607378649870814814716243",
        "totalBorrowBalanceUSD": "1144893806.629279933841042253170975",
        "timestamp": "1697586719",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "22595529.2017480282417496244518034"
      },
      {
        "totalDepositBalanceUSD": "3151177196.681208778814777179951856",
        "totalBorrowBalanceUSD": "1124943072.472199996572368355972127",
        "timestamp": "1697500679",
        "dailyLiquidateUSD": "104244.79858033247644191268",
        "dailyRepayUSD": "33717160.253137350325695770194268"
      },
      {
        "totalDepositBalanceUSD": "3034332324.981179495917977448596036",
        "totalBorrowBalanceUSD": "1093208913.948300263509595661373929",
        "timestamp": "1697414387",
        "dailyLiquidateUSD": "79.5871284419283890866055",
        "dailyRepayUSD": "2661711.11732136407914738850755334"
      },
      {
        "totalDepositBalanceUSD": "3034105868.436316563540106286341629",
        "totalBorrowBalanceUSD": "1092245396.644435696223048886001875",
        "timestamp": "1697327519",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "4798655.76673925716136119080585233"
      },
      {
        "totalDepositBalanceUSD": "3006158139.899955895582315752941311",
        "totalBorrowBalanceUSD": "1081338971.105707725343764824951051",
        "timestamp": "1697241107",
        "dailyLiquidateUSD": "9621.70156161401782352356774004",
        "dailyRepayUSD": "42596441.49529665165065115957578282"
      },
      {
        "totalDepositBalanceUSD": "2991498933.345279021627543655142752",
        "totalBorrowBalanceUSD": "1111745878.137307915779619453847728",
        "timestamp": "1697154935",
        "dailyLiquidateUSD": "167408.56594719086385315634464656",
        "dailyRepayUSD": "21525451.7851516029558445920196931"
      },
      {
        "totalDepositBalanceUSD": "2984666155.237576436167291451254155",
        "totalBorrowBalanceUSD": "1095196983.901759677140308221135765",
        "timestamp": "1697068715",
        "dailyLiquidateUSD": "4969.11885486178847681925540686",
        "dailyRepayUSD": "23696058.8562166417679268794788496"
      },
      {
        "totalDepositBalanceUSD": "3024922181.021560308409239419112055",
        "totalBorrowBalanceUSD": "1099322478.903654763027928829489082",
        "timestamp": "1696982387",
        "dailyLiquidateUSD": "500.155334870287839366502",
        "dailyRepayUSD": "36216433.09340943642182481074167073"
      },
      {
        "totalDepositBalanceUSD": "3062116704.445895841437538367386313",
        "totalBorrowBalanceUSD": "1134686489.406367557920598235205554",
        "timestamp": "1696895795",
        "dailyLiquidateUSD": "33942.62960141628614032625819055",
        "dailyRepayUSD": "10166707.12510017587539867410539077"
      },
      {
        "totalDepositBalanceUSD": "3126267069.17112447171765802329142",
        "totalBorrowBalanceUSD": "1134586310.5573935869307979011112",
        "timestamp": "1696809551",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "34587213.22230633657367915126136903"
      },
      {
        "totalDepositBalanceUSD": "3175630093.641331772039730664872013",
        "totalBorrowBalanceUSD": "1143674861.883409568613316219993791",
        "timestamp": "1696722995",
        "dailyLiquidateUSD": "425.7500405730976965900967878",
        "dailyRepayUSD": "6004827.95945396106358670925319039"
      },
      {
        "totalDepositBalanceUSD": "3158664578.835269769954511928780977",
        "totalBorrowBalanceUSD": "1139623080.451050547362977006601888",
        "timestamp": "1696636691",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "3851801.70624119493850455576135885"
      },
      {
        "totalDepositBalanceUSD": "3087169663.824223955040326029052371",
        "totalBorrowBalanceUSD": "1117236526.690549088963678673224957",
        "timestamp": "1696550363",
        "dailyLiquidateUSD": "85.9399123768474693217968",
        "dailyRepayUSD": "15493204.20578973878865533811471999"
      },
      {
        "totalDepositBalanceUSD": "3115000544.992129734231190202729614",
        "totalBorrowBalanceUSD": "1121056196.807759982592874383482517",
        "timestamp": "1696463783",
        "dailyLiquidateUSD": "366.29133812709769268339014482",
        "dailyRepayUSD": "8225169.41527221290252656831487767"
      },
      {
        "totalDepositBalanceUSD": "3090403044.812057072949623204225684",
        "totalBorrowBalanceUSD": "1111500688.710898350707449141863427",
        "timestamp": "1696377599",
        "dailyLiquidateUSD": "589.55526850497649740500594",
        "dailyRepayUSD": "24032861.08163831072499549568848805"
      },
      {
        "totalDepositBalanceUSD": "3084885482.230278954125122874190609",
        "totalBorrowBalanceUSD": "1108879822.141269826579313370612067",
        "timestamp": "1696290719",
        "dailyLiquidateUSD": "2729.6542164642920732347675",
        "dailyRepayUSD": "31196690.35069649719937933136768784"
      },
      {
        "totalDepositBalanceUSD": "3136088896.811311512951178511711421",
        "totalBorrowBalanceUSD": "1109800241.072772221917229120152819",
        "timestamp": "1696204787",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "19131788.32738261944970005555777952"
      },
      {
        "totalDepositBalanceUSD": "3041563942.289806324286128968394547",
        "totalBorrowBalanceUSD": "1095297026.649152285005489814651306",
        "timestamp": "1696118147",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "18673384.46071202394373167986820487"
      },
      {
        "totalDepositBalanceUSD": "3058889326.256113696637853659527281",
        "totalBorrowBalanceUSD": "1104561110.262784606761515409674489",
        "timestamp": "1696031831",
        "dailyLiquidateUSD": "209.6566400184050474512162682",
        "dailyRepayUSD": "10870631.06765871109545457082869073"
      },
      {
        "totalDepositBalanceUSD": "3007834663.157389239887034612731023",
        "totalBorrowBalanceUSD": "1081295003.609389219035399523212811",
        "timestamp": "1695945227",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "27481801.53511013659543013780712125"
      },
      {
        "totalDepositBalanceUSD": "2925939584.160865489269930269763399",
        "totalBorrowBalanceUSD": "1058543195.634440922604245963446009",
        "timestamp": "1695859199",
        "dailyLiquidateUSD": "28994.29464916291575734428006008",
        "dailyRepayUSD": "13601950.33712357396469575169801115"
      },
      {
        "totalDepositBalanceUSD": "2901032051.660776785258398354419821",
        "totalBorrowBalanceUSD": "1043518562.474567052674922944469415",
        "timestamp": "1695772739",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "7940723.83996969856547259790774667"
      },
      {
        "totalDepositBalanceUSD": "2892312366.029396762821543113343959",
        "totalBorrowBalanceUSD": "1041225661.182796202565166503370325",
        "timestamp": "1695686375",
        "dailyLiquidateUSD": "11151.413026560110119680901552",
        "dailyRepayUSD": "11650605.75281950966061563726811463"
      },
      {
        "totalDepositBalanceUSD": "2813823033.216506600420977791196329",
        "totalBorrowBalanceUSD": "1029397141.060726249867789330257575",
        "timestamp": "1695599963",
        "dailyLiquidateUSD": "362.2621560166186624",
        "dailyRepayUSD": "12058053.5981233248299509149080108"
      },
      {
        "totalDepositBalanceUSD": "2821537778.057367775910516922206355",
        "totalBorrowBalanceUSD": "1036898873.625823290454995364476272",
        "timestamp": "1695513395",
        "dailyLiquidateUSD": "35600.9101830448",
        "dailyRepayUSD": "6349567.49076071029290849263157161"
      },
      {
        "totalDepositBalanceUSD": "2811656691.688934682609885466691152",
        "totalBorrowBalanceUSD": "1027596739.55488680295674145169969",
        "timestamp": "1695427175",
        "dailyLiquidateUSD": "246.0961508205347267",
        "dailyRepayUSD": "8485048.65050145770422050218797174"
      },
      {
        "totalDepositBalanceUSD": "2776436334.30863134841143774960511",
        "totalBorrowBalanceUSD": "1002194218.624710166814678359840266",
        "timestamp": "1695340379",
        "dailyLiquidateUSD": "4767.21157850923681936728",
        "dailyRepayUSD": "9336536.51483718702284860238858529"
      },
      {
        "totalDepositBalanceUSD": "2818275880.073356797101738641389073",
        "totalBorrowBalanceUSD": "1009198846.02106698878303006346758",
        "timestamp": "1695253811",
        "dailyLiquidateUSD": "3372.4015373914909",
        "dailyRepayUSD": "22022861.10459784885659781798372655"
      },
      {
        "totalDepositBalanceUSD": "2832344612.329298062689079994911292",
        "totalBorrowBalanceUSD": "1017873041.113244750943921146963685",
        "timestamp": "1695167999",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "4851917.53318735299826118449481668"
      },
      {
        "totalDepositBalanceUSD": "2790380517.464949972052527425830305",
        "totalBorrowBalanceUSD": "991539681.0201022864512295053642945",
        "timestamp": "1695081215",
        "dailyLiquidateUSD": "7844.7553639077659290972120151",
        "dailyRepayUSD": "21051034.64847568363906221575785366"
      },
      {
        "totalDepositBalanceUSD": "2753684333.547449725996516977990227",
        "totalBorrowBalanceUSD": "990639963.3567360652674470065836845",
        "timestamp": "1694994983",
        "dailyLiquidateUSD": "528.4191304482731950347816416",
        "dailyRepayUSD": "13247566.7199829327006734241436922"
      },
      {
        "totalDepositBalanceUSD": "2739041070.303163909039235406481307",
        "totalBorrowBalanceUSD": "994557780.7570609630650496861133009",
        "timestamp": "1694908271",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "4576402.30482320761926539670611294"
      },
      {
        "totalDepositBalanceUSD": "2746818472.627217218005794776756893",
        "totalBorrowBalanceUSD": "997908276.9686983682929746501611813",
        "timestamp": "1694822339",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "16045566.65986443059935056191327531"
      },
      {
        "totalDepositBalanceUSD": "2727768233.257435882265222067018108",
        "totalBorrowBalanceUSD": "987597734.5730747992504531470003337",
        "timestamp": "1694735939",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "10223442.58072998293430251028975216"
      },
      {
        "totalDepositBalanceUSD": "2680367305.969054942874353575863062",
        "totalBorrowBalanceUSD": "979321603.6865897767115556522247082",
        "timestamp": "1694649419",
        "dailyLiquidateUSD": "133.30112916847533879761",
        "dailyRepayUSD": "15783621.02339575325457871328757502"
      },
      {
        "totalDepositBalanceUSD": "2652681120.079100427027298230924813",
        "totalBorrowBalanceUSD": "973925541.544819137209099484574927",
        "timestamp": "1694563139",
        "dailyLiquidateUSD": "439.9687329465219323676",
        "dailyRepayUSD": "8710877.61315103945065249519048065"
      },
      {
        "totalDepositBalanceUSD": "2592444531.069259491547819690343786",
        "totalBorrowBalanceUSD": "955218149.5575891255024195058850485",
        "timestamp": "1694476775",
        "dailyLiquidateUSD": "218375.24101819181202525857143848",
        "dailyRepayUSD": "21301592.82400372564037443781911497"
      },
      {
        "totalDepositBalanceUSD": "2671707055.562223942304505078105271",
        "totalBorrowBalanceUSD": "980534728.4334615656687737330423921",
        "timestamp": "1694390255",
        "dailyLiquidateUSD": "3181.39065677582037252515363",
        "dailyRepayUSD": "12773516.28512831223896428350652644"
      },
      {
        "totalDepositBalanceUSD": "2669937346.366549455706205650579883",
        "totalBorrowBalanceUSD": "980903790.0260446214762218329637068",
        "timestamp": "1694303543",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "8559111.39476905605641019514389545"
      },
      {
        "totalDepositBalanceUSD": "2674454114.648289193597038115053865",
        "totalBorrowBalanceUSD": "983872451.25187847885712539809532",
        "timestamp": "1694216903",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "13268860.99103722601547773565322916"
      },
      {
        "totalDepositBalanceUSD": "2684855123.129897172120638452359621",
        "totalBorrowBalanceUSD": "985764121.9655005097808993542496079",
        "timestamp": "1694130323",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "113655914.2786829307256465955606788"
      },
      {
        "totalDepositBalanceUSD": "2590232298.881900719693158652764444",
        "totalBorrowBalanceUSD": "940432386.0407646916157310928294953",
        "timestamp": "1694044343",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "42929599.81276223949824302256175916"
      },
      {
        "totalDepositBalanceUSD": "2625118512.144992623124130725713819",
        "totalBorrowBalanceUSD": "958807869.3831500346410484260615323",
        "timestamp": "1693958195",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "19841029.07443041160175265066247391"
      },
      {
        "totalDepositBalanceUSD": "2614047075.70012234903443717435719",
        "totalBorrowBalanceUSD": "966940695.7336440428988796721625077",
        "timestamp": "1693871459",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "19213898.40297437555260749963582986"
      },
      {
        "totalDepositBalanceUSD": "2599120701.490535987312028084459328",
        "totalBorrowBalanceUSD": "961762403.7407837122768808045722928",
        "timestamp": "1693785599",
        "dailyLiquidateUSD": "1617.05932822044253425708824",
        "dailyRepayUSD": "14698788.29398902227535678567592052"
      },
      {
        "totalDepositBalanceUSD": "2582052192.799873006867618185809798",
        "totalBorrowBalanceUSD": "961048841.2942060940427013188136356",
        "timestamp": "1693699079",
        "dailyLiquidateUSD": "744.1280242354542405409386743",
        "dailyRepayUSD": "12092662.42738282108038947517742867"
      },
      {
        "totalDepositBalanceUSD": "2545433084.854767515965611337816677",
        "totalBorrowBalanceUSD": "948523115.5938598319612307094861669",
        "timestamp": "1693612571",
        "dailyLiquidateUSD": "1857.78719506207315164100784726",
        "dailyRepayUSD": "18213445.8077150095671719662683205"
      },
      {
        "totalDepositBalanceUSD": "2552711384.425129946111380121124219",
        "totalBorrowBalanceUSD": "953224137.9420230958593722646898033",
        "timestamp": "1693526363",
        "dailyLiquidateUSD": "419.61042514981856517522586128",
        "dailyRepayUSD": "19110122.74490031596929035708528244"
      },
      {
        "totalDepositBalanceUSD": "2603585866.245422720266045188421948",
        "totalBorrowBalanceUSD": "962868199.1388311881109479906574794",
        "timestamp": "1693439963",
        "dailyLiquidateUSD": "1568.543747749594682",
        "dailyRepayUSD": "14350164.88053725485583843156456947"
      },
      {
        "totalDepositBalanceUSD": "2605389945.761290332958729722877648",
        "totalBorrowBalanceUSD": "961060878.957597446134812711903793",
        "timestamp": "1693353515",
        "dailyLiquidateUSD": "11130.90371386180633358096",
        "dailyRepayUSD": "27695429.97115171174561629103908701"
      },
      {
        "totalDepositBalanceUSD": "2480640161.791818429894557155197812",
        "totalBorrowBalanceUSD": "911843339.0405396425984482359338755",
        "timestamp": "1693266983",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "36096536.6245967383973140537557778"
      },
      {
        "totalDepositBalanceUSD": "2362747870.819147965990376813534775",
        "totalBorrowBalanceUSD": "807990647.2527512342990875103032112",
        "timestamp": "1693179803",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "9136622.55019455925981175144453896"
      },
      {
        "totalDepositBalanceUSD": "2357468844.490484113079483311782691",
        "totalBorrowBalanceUSD": "803907654.3637086982948087790047197",
        "timestamp": "1693093979",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "6121997.45192451006226147629618816"
      },
      {
        "totalDepositBalanceUSD": "2350452928.349776150365052096958351",
        "totalBorrowBalanceUSD": "800897557.343616929631925606033967",
        "timestamp": "1693007771",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "18981867.11605434694725448556787275"
      },
      {
        "totalDepositBalanceUSD": "2352094879.867496003818371155635218",
        "totalBorrowBalanceUSD": "802312905.4441376651150139792276978",
        "timestamp": "1692921467",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "21293972.5716642894544126315933906"
      },
      {
        "totalDepositBalanceUSD": "2372219807.899035035734095424149287",
        "totalBorrowBalanceUSD": "798418648.5237999982205491247726704",
        "timestamp": "1692835103",
        "dailyLiquidateUSD": "862.59699372225634328883212998",
        "dailyRepayUSD": "17063012.87541663462534087568617382"
      },
      {
        "totalDepositBalanceUSD": "2314336734.867710792728918229073123",
        "totalBorrowBalanceUSD": "792218152.5742100556503239572278509",
        "timestamp": "1692748775",
        "dailyLiquidateUSD": "21719.56125222577338146211836351",
        "dailyRepayUSD": "34113408.6585456975607081584464359"
      },
      {
        "totalDepositBalanceUSD": "2365851206.653257431609955744286039",
        "totalBorrowBalanceUSD": "808558125.5342176303912766579694089",
        "timestamp": "1692662363",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "14907122.26758413814322069484381016"
      },
      {
        "totalDepositBalanceUSD": "2319376997.569609000402849483062278",
        "totalBorrowBalanceUSD": "810417507.7111357396469731329737812",
        "timestamp": "1692575927",
        "dailyLiquidateUSD": "228.8094431325551199626",
        "dailyRepayUSD": "7616202.51622180692775915091072683"
      },
      {
        "totalDepositBalanceUSD": "2255008722.180323270056141243078376",
        "totalBorrowBalanceUSD": "789048105.6286144138061203630946349",
        "timestamp": "1692489527",
        "dailyLiquidateUSD": "1306.38013673323437359987020548",
        "dailyRepayUSD": "8672651.16829247421327854128156499"
      },
      {
        "totalDepositBalanceUSD": "2251649649.611976434026037696441451",
        "totalBorrowBalanceUSD": "784201641.6090837005261764072524795",
        "timestamp": "1692403103",
        "dailyLiquidateUSD": "54217.75434910824029814715649011",
        "dailyRepayUSD": "38146737.14501193362969987751078332"
      },
      {
        "totalDepositBalanceUSD": "2249977599.202359917393280512591313",
        "totalBorrowBalanceUSD": "791209739.4797071806436468861418029",
        "timestamp": "1692316727",
        "dailyLiquidateUSD": "8776558.37341506346300158954972839",
        "dailyRepayUSD": "33031068.46424656803567581279897536"
      },
      {
        "totalDepositBalanceUSD": "2346645141.251723941326244086636748",
        "totalBorrowBalanceUSD": "817550659.1334694089657262661311351",
        "timestamp": "1692230387",
        "dailyLiquidateUSD": "40248.50787669579397246013006493",
        "dailyRepayUSD": "12149488.37793049032886004397991424"
      },
      {
        "totalDepositBalanceUSD": "2352880444.058103565604950386831892",
        "totalBorrowBalanceUSD": "821027946.4275953089555231162193266",
        "timestamp": "1692143963",
        "dailyLiquidateUSD": "1527.8774620912164893",
        "dailyRepayUSD": "12475224.05283042930254682076898737"
      },
      {
        "totalDepositBalanceUSD": "2345807630.093700536630914316038373",
        "totalBorrowBalanceUSD": "812266821.8936635073407952690782494",
        "timestamp": "1692057503",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "6795250.81311475737592926877814011"
      },
      {
        "totalDepositBalanceUSD": "2314651067.748341965895559815422936",
        "totalBorrowBalanceUSD": "795572969.9030298767231835505680719",
        "timestamp": "1691971091",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "5593448.51196706278857334919890518"
      },
      {
        "totalDepositBalanceUSD": "2320109762.795888175873621395922137",
        "totalBorrowBalanceUSD": "799844263.7017961687318176356458777",
        "timestamp": "1691884595",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "5815485.23344408293678527959677156"
      },
      {
        "totalDepositBalanceUSD": "2310724224.475132180020456054787606",
        "totalBorrowBalanceUSD": "799682561.4305282091560480105830988",
        "timestamp": "1691798387",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "10615701.94132404361853712029205566"
      },
      {
        "totalDepositBalanceUSD": "2297222575.613912896025476362922709",
        "totalBorrowBalanceUSD": "789674848.4007762516674191947202525",
        "timestamp": "1691711927",
        "dailyLiquidateUSD": "16533.0265703396685129",
        "dailyRepayUSD": "21833154.11679533433668191522287255"
      },
      {
        "totalDepositBalanceUSD": "2318435274.218752509648520705335826",
        "totalBorrowBalanceUSD": "794209852.6088423800649200965956675",
        "timestamp": "1691625503",
        "dailyLiquidateUSD": "424460.6421239100894909585854",
        "dailyRepayUSD": "7541991.90078196342181105654535084"
      },
      {
        "totalDepositBalanceUSD": "2339296894.237899238329224869829609",
        "totalBorrowBalanceUSD": "794761592.2534421073070595898776042",
        "timestamp": "1691538827",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "57716944.91363860042342294083029017"
      },
      {
        "totalDepositBalanceUSD": "2334546253.4829438636154944579396",
        "totalBorrowBalanceUSD": "820381350.8068145830614101149170367",
        "timestamp": "1691452643",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "42760882.62876074640810991475381857"
      },
      {
        "totalDepositBalanceUSD": "2315386726.740174937349444378020088",
        "totalBorrowBalanceUSD": "807501498.8421652917972528773152632",
        "timestamp": "1691366087",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "7500661.77124571464953140187308903"
      },
      {
        "totalDepositBalanceUSD": "2285662678.929882754458291561869874",
        "totalBorrowBalanceUSD": "804445381.820916335417017146075333",
        "timestamp": "1691279975",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "7053224.66760474813434681788852587"
      },
      {
        "totalDepositBalanceUSD": "2270071290.47023257474342349456086",
        "totalBorrowBalanceUSD": "803219556.3401972313872665368217873",
        "timestamp": "1691193107",
        "dailyLiquidateUSD": "6419.7900451187288569417946249",
        "dailyRepayUSD": "11372134.57559648863555307874801153"
      },
      {
        "totalDepositBalanceUSD": "2268745372.478887734109408487364976",
        "totalBorrowBalanceUSD": "806685927.8388847243187006858384961",
        "timestamp": "1691107127",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "18788857.7907199186132858779652375"
      },
      {
        "totalDepositBalanceUSD": "2258098139.596717709808088484551969",
        "totalBorrowBalanceUSD": "812189262.3452374358580441355310432",
        "timestamp": "1691020739",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "19899845.83512021475453330548037516"
      },
      {
        "totalDepositBalanceUSD": "2205821858.434160713309418921156264",
        "totalBorrowBalanceUSD": "762663163.6644184492175750934745735",
        "timestamp": "1690934195",
        "dailyLiquidateUSD": "106550.30908051175291003906459022",
        "dailyRepayUSD": "161320890.7342897991527527330604256"
      },
      {
        "totalDepositBalanceUSD": "2196893297.477549877521557388045408",
        "totalBorrowBalanceUSD": "819356779.9812131022703629994422519",
        "timestamp": "1690847927",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "58284491.229940755300808649446496"
      },
      {
        "totalDepositBalanceUSD": "2122795134.144753447075015260417335",
        "totalBorrowBalanceUSD": "772167834.6624573003550480552586405",
        "timestamp": "1690761503",
        "dailyLiquidateUSD": "11864.59529530444613832918759832",
        "dailyRepayUSD": "63315267.60590886231878569543657096"
      },
      {
        "totalDepositBalanceUSD": "2228986853.653728646660969274311635",
        "totalBorrowBalanceUSD": "774527971.5517611231129595237851356",
        "timestamp": "1690675007",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "9040990.53679236948475185932068483"
      },
      {
        "totalDepositBalanceUSD": "2212667318.397075178923447958707254",
        "totalBorrowBalanceUSD": "767972798.8436272659645225081767688",
        "timestamp": "1690588679",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "12478008.5602837367041014093057151"
      },
      {
        "totalDepositBalanceUSD": "2202529295.312445415432605120299881",
        "totalBorrowBalanceUSD": "767733964.4752327414987413610979593",
        "timestamp": "1690502315",
        "dailyLiquidateUSD": "1893.4706418262214391138174",
        "dailyRepayUSD": "6620091.04651881043735260489893252"
      },
      {
        "totalDepositBalanceUSD": "2219602449.322666513946889553118543",
        "totalBorrowBalanceUSD": "769973650.6487564566685421976120278",
        "timestamp": "1690415879",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "1587854.05496820425300249852031956"
      },
      {
        "totalDepositBalanceUSD": "2206282915.977595401133435087768643",
        "totalBorrowBalanceUSD": "765073025.4323470444928258455061232",
        "timestamp": "1690329071",
        "dailyLiquidateUSD": "0",
        "dailyRepayUSD": "792943.03739243385941104335869178"
      }
    ]
  }
}

short_positions = data["data"]["financialsDailySnapshots"]

header = [
    "timestamp",
    "totalDepositBalanceUSD",
    "totalBorrowBalanceUSD",
    "utilizationRate",
    "dailyLiquidateUSD",
    "dailyRepayUSD"
]

with open("123.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for position in short_positions:
        position['timestamp'] = datetime.utcfromtimestamp(int(position['timestamp'])).strftime('%Y-%m-%d')
        position['utilizationRate'] = float(position['totalBorrowBalanceUSD']) / float(position['totalDepositBalanceUSD'])
        writer.writerow(position)