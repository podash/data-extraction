import json
import csv
from datetime import datetime

json_data = {
  "data": {
    "financialsDailySnapshots": [
      {
        "totalDepositBalanceUSD": "244922359.6781883232883995358426999",
        "totalBorrowBalanceUSD": "81119980.30615253931407499720622643",
        "timestamp": "1700590541",
        "blockNumber": "38063284"
      },
      {
        "totalDepositBalanceUSD": "247349187.1176382917102232675775331",
        "totalBorrowBalanceUSD": "81455277.95877531535540927311346",
        "timestamp": "1700524734",
        "blockNumber": "38030864"
      },
      {
        "totalDepositBalanceUSD": "251926193.2005108744361310600377986",
        "totalBorrowBalanceUSD": "83197847.70123681918080880942231855",
        "timestamp": "1700438161",
        "blockNumber": "37988237"
      },
      {
        "totalDepositBalanceUSD": "245173609.8870558553422850549975464",
        "totalBorrowBalanceUSD": "81942523.94431777476859441465580845",
        "timestamp": "1700351866",
        "blockNumber": "37945772"
      },
      {
        "totalDepositBalanceUSD": "244513648.9900251298834885787758698",
        "totalBorrowBalanceUSD": "82116083.17860466932317201941228549",
        "timestamp": "1700265543",
        "blockNumber": "37903265"
      },
      {
        "totalDepositBalanceUSD": "254326129.5413832072828118894543348",
        "totalBorrowBalanceUSD": "85653018.91029441574326376292967628",
        "timestamp": "1700179163",
        "blockNumber": "37859866"
      },
      {
        "totalDepositBalanceUSD": "255604072.394194697351231282364811",
        "totalBorrowBalanceUSD": "84731454.4280110730693360585615132",
        "timestamp": "1700092768",
        "blockNumber": "37816278"
      },
      {
        "totalDepositBalanceUSD": "234328021.3359507754660023908769352",
        "totalBorrowBalanceUSD": "78574561.69353991500254474086881664",
        "timestamp": "1700006347",
        "blockNumber": "37772951"
      },
      {
        "totalDepositBalanceUSD": "243984767.5256436381532968984493655",
        "totalBorrowBalanceUSD": "80690179.45027809455533131764785324",
        "timestamp": "1699919995",
        "blockNumber": "37730066"
      },
      {
        "totalDepositBalanceUSD": "258455067.3346424971830028801141113",
        "totalBorrowBalanceUSD": "84832338.35333495944643751877427279",
        "timestamp": "1699833579",
        "blockNumber": "37687061"
      },
      {
        "totalDepositBalanceUSD": "253504033.4887574199744093382710915",
        "totalBorrowBalanceUSD": "84554786.33222650344581836219195653",
        "timestamp": "1699747190",
        "blockNumber": "37643432"
      },
      {
        "totalDepositBalanceUSD": "244836331.5227396379978776731983699",
        "totalBorrowBalanceUSD": "80441992.54078597067362815961373025",
        "timestamp": "1699660799",
        "blockNumber": "37600502"
      },
      {
        "totalDepositBalanceUSD": "235962181.9860235202742373716407307",
        "totalBorrowBalanceUSD": "77575359.12701402541798568277066841",
        "timestamp": "1699574154",
        "blockNumber": "37557597"
      },
      {
        "totalDepositBalanceUSD": "230982441.7218545783086130344148288",
        "totalBorrowBalanceUSD": "77306818.8085122102905844236416882",
        "timestamp": "1699487014",
        "blockNumber": "37514567"
      },
      {
        "totalDepositBalanceUSD": "228569607.8294889046338022011124942",
        "totalBorrowBalanceUSD": "76993038.4096460532788030211461462",
        "timestamp": "1699401379",
        "blockNumber": "37472638"
      },
      {
        "totalDepositBalanceUSD": "229593841.7615645032732638580949083",
        "totalBorrowBalanceUSD": "77467181.9213621417037344480041739",
        "timestamp": "1699314492",
        "blockNumber": "37429882"
      },
      {
        "totalDepositBalanceUSD": "227362301.2357280054473456787851211",
        "totalBorrowBalanceUSD": "76317598.57278058213728063611946934",
        "timestamp": "1699228776",
        "blockNumber": "37387633"
      },
      {
        "totalDepositBalanceUSD": "228483448.3671156446030935479750257",
        "totalBorrowBalanceUSD": "76659911.8821442180794409336015337",
        "timestamp": "1699142212",
        "blockNumber": "37345143"
      },
      {
        "totalDepositBalanceUSD": "230630973.0187240227637578448345591",
        "totalBorrowBalanceUSD": "78414674.51074563622722162285130803",
        "timestamp": "1699055806",
        "blockNumber": "37302875"
      },
      {
        "totalDepositBalanceUSD": "228759409.9558430001327682382343734",
        "totalBorrowBalanceUSD": "77475006.20837351244756861759950205",
        "timestamp": "1698968976",
        "blockNumber": "37260579"
      },
      {
        "totalDepositBalanceUSD": "235319137.0482727399341999740507726",
        "totalBorrowBalanceUSD": "78280846.15324834234403000172951368",
        "timestamp": "1698883112",
        "blockNumber": "37218391"
      },
      {
        "totalDepositBalanceUSD": "226399279.0690988932844141446376093",
        "totalBorrowBalanceUSD": "76528035.71740579369282678703711065",
        "timestamp": "1698796754",
        "blockNumber": "37176162"
      },
      {
        "totalDepositBalanceUSD": "231194841.883183474436472881477028",
        "totalBorrowBalanceUSD": "76318896.43968084981363372438385456",
        "timestamp": "1698710193",
        "blockNumber": "37134042"
      },
      {
        "totalDepositBalanceUSD": "230338871.1567123114067625243707714",
        "totalBorrowBalanceUSD": "79054433.07535723665461348754182135",
        "timestamp": "1698623900",
        "blockNumber": "37091639"
      },
      {
        "totalDepositBalanceUSD": "224755831.1803731599501780873769343",
        "totalBorrowBalanceUSD": "76568957.61918791531186545050581018",
        "timestamp": "1698537216",
        "blockNumber": "37049102"
      },
      {
        "totalDepositBalanceUSD": "219326451.2313041785327870951884959",
        "totalBorrowBalanceUSD": "75523089.48095099559021008335843102",
        "timestamp": "1698451042",
        "blockNumber": "37007182"
      },
      {
        "totalDepositBalanceUSD": "223677323.4254062542692826033719187",
        "totalBorrowBalanceUSD": "76669819.98108470031508956975286198",
        "timestamp": "1698364758",
        "blockNumber": "36964787"
      },
      {
        "totalDepositBalanceUSD": "223229857.6150654745452647407368761",
        "totalBorrowBalanceUSD": "75670410.42793716146393666249551635",
        "timestamp": "1698278334",
        "blockNumber": "36922279"
      },
      {
        "totalDepositBalanceUSD": "219233274.2715461133419368934057126",
        "totalBorrowBalanceUSD": "74131588.93932668052573618815005224",
        "timestamp": "1698191786",
        "blockNumber": "36880279"
      },
      {
        "totalDepositBalanceUSD": "230679758.0122478441643058576832693",
        "totalBorrowBalanceUSD": "75162324.26576783831379744834618081",
        "timestamp": "1698105555",
        "blockNumber": "36837814"
      },
      {
        "totalDepositBalanceUSD": "220642541.5063213174242453425743858",
        "totalBorrowBalanceUSD": "71921475.55525954970889269958108254",
        "timestamp": "1698019185",
        "blockNumber": "36795250"
      },
      {
        "totalDepositBalanceUSD": "217627513.0935713318703498586359891",
        "totalBorrowBalanceUSD": "71521186.90121258188630504954821939",
        "timestamp": "1697932722",
        "blockNumber": "36752704"
      },
      {
        "totalDepositBalanceUSD": "217549715.9333403335086089441032538",
        "totalBorrowBalanceUSD": "71974872.64643879375434480680119558",
        "timestamp": "1697846391",
        "blockNumber": "36710305"
      },
      {
        "totalDepositBalanceUSD": "211836488.7782492605304382407651374",
        "totalBorrowBalanceUSD": "70419145.95100189364595124836172409",
        "timestamp": "1697759861",
        "blockNumber": "36668235"
      },
      {
        "totalDepositBalanceUSD": "210667448.6813216651271330178733014",
        "totalBorrowBalanceUSD": "70330232.98217808109311288796073589",
        "timestamp": "1697673190",
        "blockNumber": "36625691"
      },
      {
        "totalDepositBalanceUSD": "211550958.2852199561982162352953151",
        "totalBorrowBalanceUSD": "70278504.04953352443204900162759361",
        "timestamp": "1697587097",
        "blockNumber": "36583448"
      },
      {
        "totalDepositBalanceUSD": "211543588.614479084034554817917316",
        "totalBorrowBalanceUSD": "70678636.75608423778441695494820154",
        "timestamp": "1697500412",
        "blockNumber": "36541487"
      },
      {
        "totalDepositBalanceUSD": "206204941.4654835263656730121428032",
        "totalBorrowBalanceUSD": "69040981.946144641517095832337039",
        "timestamp": "1697414387",
        "blockNumber": "36500374"
      },
      {
        "totalDepositBalanceUSD": "204613642.6920577241906864381916175",
        "totalBorrowBalanceUSD": "69126426.84350233525359507312127534",
        "timestamp": "1697327259",
        "blockNumber": "36458865"
      },
      {
        "totalDepositBalanceUSD": "205693443.5905620665002224341561591",
        "totalBorrowBalanceUSD": "69647957.35496640519834727412457912",
        "timestamp": "1697240804",
        "blockNumber": "36418470"
      },
      {
        "totalDepositBalanceUSD": "208431792.3724214269554609406678894",
        "totalBorrowBalanceUSD": "69669361.51498029548270453789187794",
        "timestamp": "1697154820",
        "blockNumber": "36377406"
      },
      {
        "totalDepositBalanceUSD": "211790306.0573101765451137944002896",
        "totalBorrowBalanceUSD": "70257498.87676687977233810130277362",
        "timestamp": "1697068488",
        "blockNumber": "36335366"
      },
      {
        "totalDepositBalanceUSD": "215907506.5746647105000611554753916",
        "totalBorrowBalanceUSD": "71635519.10398873088410116217105909",
        "timestamp": "1696982232",
        "blockNumber": "36293699"
      },
      {
        "totalDepositBalanceUSD": "216242588.2574475373540162785540399",
        "totalBorrowBalanceUSD": "72112398.7593541047754967788994451",
        "timestamp": "1696895542",
        "blockNumber": "36252440"
      },
      {
        "totalDepositBalanceUSD": "221414911.9276185478193889788647281",
        "totalBorrowBalanceUSD": "73141099.00325568895892241241977907",
        "timestamp": "1696809441",
        "blockNumber": "36210843"
      },
      {
        "totalDepositBalanceUSD": "222618997.2665175628851207475615049",
        "totalBorrowBalanceUSD": "73925474.74696873243600430043942956",
        "timestamp": "1696722434",
        "blockNumber": "36168902"
      },
      {
        "totalDepositBalanceUSD": "216302427.9630013476849389247625208",
        "totalBorrowBalanceUSD": "74001332.1867080374771894630260299",
        "timestamp": "1696636769",
        "blockNumber": "36126717"
      },
      {
        "totalDepositBalanceUSD": "212150502.0300628455748758513902324",
        "totalBorrowBalanceUSD": "72457716.42572772584712928087039973",
        "timestamp": "1696550395",
        "blockNumber": "36083574"
      },
      {
        "totalDepositBalanceUSD": "212596733.9323715546849057839222005",
        "totalBorrowBalanceUSD": "72118132.97775203801866899987262341",
        "timestamp": "1696463989",
        "blockNumber": "36040937"
      },
      {
        "totalDepositBalanceUSD": "206405590.4319398351931421464466689",
        "totalBorrowBalanceUSD": "70514037.15219907049729216395538463",
        "timestamp": "1696377516",
        "blockNumber": "35998160"
      },
      {
        "totalDepositBalanceUSD": "211608566.8396468216434030054217422",
        "totalBorrowBalanceUSD": "69437471.3075271383271429935846172",
        "timestamp": "1696290650",
        "blockNumber": "35955418"
      },
      {
        "totalDepositBalanceUSD": "207916095.0595031920154227581225975",
        "totalBorrowBalanceUSD": "68825344.84514265720615613206689736",
        "timestamp": "1696204425",
        "blockNumber": "35912934"
      },
      {
        "totalDepositBalanceUSD": "201900138.3288950011486198642390323",
        "totalBorrowBalanceUSD": "67756360.05842466210304391969442574",
        "timestamp": "1696118307",
        "blockNumber": "35871113"
      },
      {
        "totalDepositBalanceUSD": "201371427.1068137723108586871910717",
        "totalBorrowBalanceUSD": "67852592.96679538035061405510705044",
        "timestamp": "1696031854",
        "blockNumber": "35829195"
      },
      {
        "totalDepositBalanceUSD": "202169155.7663047149387934267736974",
        "totalBorrowBalanceUSD": "67930712.55492013992692456829338249",
        "timestamp": "1695945144",
        "blockNumber": "35787125"
      },
      {
        "totalDepositBalanceUSD": "197950786.7588177958424156155906654",
        "totalBorrowBalanceUSD": "66620190.0647894949621679922342108",
        "timestamp": "1695859042",
        "blockNumber": "35745344"
      },
      {
        "totalDepositBalanceUSD": "197677505.3667608592434854763194049",
        "totalBorrowBalanceUSD": "66830748.9033125739980831017714849",
        "timestamp": "1695772626",
        "blockNumber": "35702876"
      },
      {
        "totalDepositBalanceUSD": "197449614.0105306228127205891627645",
        "totalBorrowBalanceUSD": "66689752.92442734072903759928751488",
        "timestamp": "1695686306",
        "blockNumber": "35660348"
      },
      {
        "totalDepositBalanceUSD": "196434243.6111829249558224232843531",
        "totalBorrowBalanceUSD": "66228693.71254956386837047345551092",
        "timestamp": "1695599902",
        "blockNumber": "35617688"
      },
      {
        "totalDepositBalanceUSD": "197639857.5809089066136000025380442",
        "totalBorrowBalanceUSD": "66451668.78909663963913243971471421",
        "timestamp": "1695512465",
        "blockNumber": "35575061"
      },
      {
        "totalDepositBalanceUSD": "197742748.0424986051718553260079191",
        "totalBorrowBalanceUSD": "66556412.30793074246262134630687022",
        "timestamp": "1695426918",
        "blockNumber": "35533117"
      },
      {
        "totalDepositBalanceUSD": "197413006.8148058321201691411443392",
        "totalBorrowBalanceUSD": "66372622.90271845580455964854463589",
        "timestamp": "1695340256",
        "blockNumber": "35490785"
      },
      {
        "totalDepositBalanceUSD": "200412272.016823601523980231709683",
        "totalBorrowBalanceUSD": "66528452.575354127869395547717081",
        "timestamp": "1695254311",
        "blockNumber": "35448688"
      },
      {
        "totalDepositBalanceUSD": "202706397.3323603954442704317395586",
        "totalBorrowBalanceUSD": "67236038.97002539996747821450817273",
        "timestamp": "1695167822",
        "blockNumber": "35406083"
      },
      {
        "totalDepositBalanceUSD": "201167205.4863753224455998444491493",
        "totalBorrowBalanceUSD": "66328709.47885768622487194231344059",
        "timestamp": "1695081184",
        "blockNumber": "35363700"
      },
      {
        "totalDepositBalanceUSD": "199815482.9815992082266194309800607",
        "totalBorrowBalanceUSD": "65982680.00412398353414020204669219",
        "timestamp": "1694995095",
        "blockNumber": "35321436"
      },
      {
        "totalDepositBalanceUSD": "200590032.5830769861938012325647419",
        "totalBorrowBalanceUSD": "66011952.41437217026480082583998553",
        "timestamp": "1694908521",
        "blockNumber": "35279411"
      },
      {
        "totalDepositBalanceUSD": "200004124.5966367452858202267348093",
        "totalBorrowBalanceUSD": "66487131.12409356922884435524470571",
        "timestamp": "1694822198",
        "blockNumber": "35237251"
      },
      {
        "totalDepositBalanceUSD": "200628837.319410398820511328564499",
        "totalBorrowBalanceUSD": "66011894.96367608031738410718772336",
        "timestamp": "1694734868",
        "blockNumber": "35194716"
      },
      {
        "totalDepositBalanceUSD": "198456283.4306776058404319432234948",
        "totalBorrowBalanceUSD": "66369249.41187002278135064363004017",
        "timestamp": "1694649484",
        "blockNumber": "35152971"
      },
      {
        "totalDepositBalanceUSD": "199094340.1350780475590152664949743",
        "totalBorrowBalanceUSD": "66092361.31210276440407729244705937",
        "timestamp": "1694562893",
        "blockNumber": "35110533"
      },
      {
        "totalDepositBalanceUSD": "194908547.3297736481471292332461561",
        "totalBorrowBalanceUSD": "67180474.30734273597535321745611638",
        "timestamp": "1694476525",
        "blockNumber": "35067985"
      },
      {
        "totalDepositBalanceUSD": "199786251.9978803512777771061316436",
        "totalBorrowBalanceUSD": "67635382.00182409063207582218034352",
        "timestamp": "1694390270",
        "blockNumber": "35025487"
      },
      {
        "totalDepositBalanceUSD": "201751602.6717700463106620197122518",
        "totalBorrowBalanceUSD": "68837777.91467844381805005127973517",
        "timestamp": "1694303891",
        "blockNumber": "34983054"
      },
      {
        "totalDepositBalanceUSD": "202681610.479069152317723212369347",
        "totalBorrowBalanceUSD": "68697628.55822537784976919903518809",
        "timestamp": "1694217557",
        "blockNumber": "34940952"
      },
      {
        "totalDepositBalanceUSD": "204334869.6080037872710929916276687",
        "totalBorrowBalanceUSD": "68914812.69992786797741469856896058",
        "timestamp": "1694131012",
        "blockNumber": "34899555"
      },
      {
        "totalDepositBalanceUSD": "200740310.686048881211484816837397",
        "totalBorrowBalanceUSD": "68503505.01407967080676071651284375",
        "timestamp": "1694044125",
        "blockNumber": "34859039"
      },
      {
        "totalDepositBalanceUSD": "201503414.7225321668217073238058305",
        "totalBorrowBalanceUSD": "68379592.36063748938893699856104952",
        "timestamp": "1693958150",
        "blockNumber": "34819075"
      },
      {
        "totalDepositBalanceUSD": "201894816.1454965938023940588593295",
        "totalBorrowBalanceUSD": "68359111.19625502345325279525006611",
        "timestamp": "1693871962",
        "blockNumber": "34779362"
      },
      {
        "totalDepositBalanceUSD": "202693655.8791853472434999604245036",
        "totalBorrowBalanceUSD": "67941122.779676727386153723547301",
        "timestamp": "1693785361",
        "blockNumber": "34739254"
      },
      {
        "totalDepositBalanceUSD": "201590990.1521479825744384052428858",
        "totalBorrowBalanceUSD": "67997589.23597340741765559391682229",
        "timestamp": "1693698849",
        "blockNumber": "34699205"
      },
      {
        "totalDepositBalanceUSD": "201236204.6882905073150442083540221",
        "totalBorrowBalanceUSD": "68056921.83127424099707207932996305",
        "timestamp": "1693612583",
        "blockNumber": "34659329"
      },
      {
        "totalDepositBalanceUSD": "202733285.4340929777822317763139284",
        "totalBorrowBalanceUSD": "68329546.49876346150845990811085812",
        "timestamp": "1693526336",
        "blockNumber": "34619203"
      },
      {
        "totalDepositBalanceUSD": "211883154.3052821802256173033944039",
        "totalBorrowBalanceUSD": "71472289.66145649262722368843520535",
        "timestamp": "1693439676",
        "blockNumber": "34578472"
      },
      {
        "totalDepositBalanceUSD": "214721661.2195384386092323717515954",
        "totalBorrowBalanceUSD": "72293493.98269062365871752406767534",
        "timestamp": "1693353589",
        "blockNumber": "34538862"
      },
      {
        "totalDepositBalanceUSD": "211728441.6819115820352293108983868",
        "totalBorrowBalanceUSD": "70977933.12919038067035268731451176",
        "timestamp": "1693267087",
        "blockNumber": "34498538"
      },
      {
        "totalDepositBalanceUSD": "212209960.4301686656793224620026718",
        "totalBorrowBalanceUSD": "70654204.66673253225493700601978763",
        "timestamp": "1693180793",
        "blockNumber": "34458750"
      },
      {
        "totalDepositBalanceUSD": "211553143.8262178760482404726893337",
        "totalBorrowBalanceUSD": "70787716.56717343929747482767217575",
        "timestamp": "1693094375",
        "blockNumber": "34418744"
      },
      {
        "totalDepositBalanceUSD": "210780880.1003475501998950336402518",
        "totalBorrowBalanceUSD": "69967958.95434508117835580261658471",
        "timestamp": "1693007201",
        "blockNumber": "34378121"
      },
      {
        "totalDepositBalanceUSD": "211579623.0970104817504466859679919",
        "totalBorrowBalanceUSD": "69708175.32418970233743915569898314",
        "timestamp": "1692921556",
        "blockNumber": "34338308"
      },
      {
        "totalDepositBalanceUSD": "215147807.9881285305302739741876827",
        "totalBorrowBalanceUSD": "69837807.30534776701932193266161964",
        "timestamp": "1692835195",
        "blockNumber": "34298086"
      },
      {
        "totalDepositBalanceUSD": "215514567.3538818834215902535864319",
        "totalBorrowBalanceUSD": "68969229.5487368195493821421399815",
        "timestamp": "1692748636",
        "blockNumber": "34257898"
      },
      {
        "totalDepositBalanceUSD": "219550281.0041487458117795007020776",
        "totalBorrowBalanceUSD": "69595332.30077338732368869294806444",
        "timestamp": "1692662388",
        "blockNumber": "34217638"
      },
      {
        "totalDepositBalanceUSD": "226374964.1602452487599043650587432",
        "totalBorrowBalanceUSD": "73387926.45730201415066955936746241",
        "timestamp": "1692575998",
        "blockNumber": "34177635"
      },
      {
        "totalDepositBalanceUSD": "225077298.5416418006710501271223251",
        "totalBorrowBalanceUSD": "72839628.35906899639767221769291283",
        "timestamp": "1692489239",
        "blockNumber": "34137455"
      },
      {
        "totalDepositBalanceUSD": "224479004.4115259972003478146630063",
        "totalBorrowBalanceUSD": "72912284.14268730313276705520905891",
        "timestamp": "1692403097",
        "blockNumber": "34097568"
      },
      {
        "totalDepositBalanceUSD": "223494342.3019229460819374591992268",
        "totalBorrowBalanceUSD": "72381132.88063008023453527443191742",
        "timestamp": "1692316774",
        "blockNumber": "34057330"
      },
      {
        "totalDepositBalanceUSD": "235629698.2671026982376057070012904",
        "totalBorrowBalanceUSD": "77578723.92585393049433781407701141",
        "timestamp": "1692230380",
        "blockNumber": "34014746"
      },
      {
        "totalDepositBalanceUSD": "235150191.7476860040503346993533521",
        "totalBorrowBalanceUSD": "75904243.58233818041835377147028134",
        "timestamp": "1692143859",
        "blockNumber": "33971927"
      },
      {
        "totalDepositBalanceUSD": "246528018.3238598034605078864887797",
        "totalBorrowBalanceUSD": "76803707.88792589135542853644686165",
        "timestamp": "1692057386",
        "blockNumber": "33929199"
      },
      {
        "totalDepositBalanceUSD": "246283477.9350010415889410741273488",
        "totalBorrowBalanceUSD": "79782308.93229630085082897808162126",
        "timestamp": "1691971063",
        "blockNumber": "33886520"
      },
      {
        "totalDepositBalanceUSD": "247119261.8612367608992474698404081",
        "totalBorrowBalanceUSD": "80094057.66445225658163495411554104",
        "timestamp": "1691884591",
        "blockNumber": "33844258"
      },
      {
        "totalDepositBalanceUSD": "246957935.0673910884955758629529755",
        "totalBorrowBalanceUSD": "80282081.29289060749580655529404429",
        "timestamp": "1691798191",
        "blockNumber": "33801625"
      },
      {
        "totalDepositBalanceUSD": "238570627.1403890991899640973503342",
        "totalBorrowBalanceUSD": "76915455.1054466305532122656258493",
        "timestamp": "1691711942",
        "blockNumber": "33759067"
      },
      {
        "totalDepositBalanceUSD": "240316630.4349633854029248954322055",
        "totalBorrowBalanceUSD": "77000438.90864629387964990965814036",
        "timestamp": "1691625392",
        "blockNumber": "33716234"
      },
      {
        "totalDepositBalanceUSD": "240824246.4475124667354147419444387",
        "totalBorrowBalanceUSD": "76268548.96749370721177269670023343",
        "timestamp": "1691539128",
        "blockNumber": "33673538"
      },
      {
        "totalDepositBalanceUSD": "246364329.8088159865960366176812181",
        "totalBorrowBalanceUSD": "80099360.09018342980206274184165933",
        "timestamp": "1691452789",
        "blockNumber": "33631060"
      },
      {
        "totalDepositBalanceUSD": "236902688.4817400884503668329375521",
        "totalBorrowBalanceUSD": "76677280.33817209271805208182435515",
        "timestamp": "1691366290",
        "blockNumber": "33588626"
      },
      {
        "totalDepositBalanceUSD": "234658194.7109772058455041870285851",
        "totalBorrowBalanceUSD": "75856022.80987094151599751410255057",
        "timestamp": "1691279958",
        "blockNumber": "33546011"
      },
      {
        "totalDepositBalanceUSD": "241423975.1410894526682167037139233",
        "totalBorrowBalanceUSD": "79572563.60835651284461550051036688",
        "timestamp": "1691193392",
        "blockNumber": "33503086"
      },
      {
        "totalDepositBalanceUSD": "243511128.1670389571591372085821299",
        "totalBorrowBalanceUSD": "79791250.32340582858465735503860537",
        "timestamp": "1691106991",
        "blockNumber": "33460440"
      },
      {
        "totalDepositBalanceUSD": "235422384.8651587324828947084612896",
        "totalBorrowBalanceUSD": "76149329.85679675979666745534372529",
        "timestamp": "1691020594",
        "blockNumber": "33417890"
      },
      {
        "totalDepositBalanceUSD": "235727006.3754185732251468789489948",
        "totalBorrowBalanceUSD": "76657810.51638402747448453340570578",
        "timestamp": "1690934374",
        "blockNumber": "33375320"
      },
      {
        "totalDepositBalanceUSD": "235227832.6682865246016507611057091",
        "totalBorrowBalanceUSD": "76416071.38289235030891870029011055",
        "timestamp": "1690847988",
        "blockNumber": "33332824"
      },
      {
        "totalDepositBalanceUSD": "244315412.5034034711656223484018359",
        "totalBorrowBalanceUSD": "78244502.42403099871987202027934611",
        "timestamp": "1690761420",
        "blockNumber": "33290428"
      },
      {
        "totalDepositBalanceUSD": "251405748.6581278636046183112484505",
        "totalBorrowBalanceUSD": "78877705.04181043905236842016415166",
        "timestamp": "1690674848",
        "blockNumber": "33247758"
      },
      {
        "totalDepositBalanceUSD": "250349347.5621143837097517535446705",
        "totalBorrowBalanceUSD": "78903780.02432907777850827331234241",
        "timestamp": "1690588797",
        "blockNumber": "33205683"
      },
      {
        "totalDepositBalanceUSD": "248547585.9362766123320528322200722",
        "totalBorrowBalanceUSD": "78201177.26438495645380832356865229",
        "timestamp": "1690502393",
        "blockNumber": "33163945"
      },
      {
        "totalDepositBalanceUSD": "249807682.0564063488804207636301175",
        "totalBorrowBalanceUSD": "78156079.30151237947814540240367939",
        "timestamp": "1690415914",
        "blockNumber": "33122647"
      },
      {
        "totalDepositBalanceUSD": "249261055.2137427831897912999492875",
        "totalBorrowBalanceUSD": "78170602.28023263061605638577611611",
        "timestamp": "1690329055",
        "blockNumber": "33080172"
      },
      {
        "totalDepositBalanceUSD": "250094254.8035084517262433504655587",
        "totalBorrowBalanceUSD": "77777489.81955622481114072469361196",
        "timestamp": "1690243184",
        "blockNumber": "33037436"
      },
      {
        "totalDepositBalanceUSD": "255397058.1630282284857722461448282",
        "totalBorrowBalanceUSD": "79154195.8020443678972607038221881",
        "timestamp": "1690156510",
        "blockNumber": "32994584"
      },
      {
        "totalDepositBalanceUSD": "253576949.8795531682859177857237667",
        "totalBorrowBalanceUSD": "78788941.47244181561096145819503915",
        "timestamp": "1690070364",
        "blockNumber": "32952091"
      },
      {
        "totalDepositBalanceUSD": "256346541.9925453435687894809769966",
        "totalBorrowBalanceUSD": "79394529.90691148372236381826688806",
        "timestamp": "1689983910",
        "blockNumber": "32909797"
      },
      {
        "totalDepositBalanceUSD": "255899885.9710118014184564671066339",
        "totalBorrowBalanceUSD": "78922467.0370771612616872672011149",
        "timestamp": "1689897512",
        "blockNumber": "32867634"
      },
      {
        "totalDepositBalanceUSD": "252030570.7115720581772863719672512",
        "totalBorrowBalanceUSD": "78834224.47330651416725339708307764",
        "timestamp": "1689810889",
        "blockNumber": "32824699"
      },
      {
        "totalDepositBalanceUSD": "250790299.7680061988869362201857549",
        "totalBorrowBalanceUSD": "78693548.38563542512789888428507406",
        "timestamp": "1689724758",
        "blockNumber": "32782222"
      },
      {
        "totalDepositBalanceUSD": "254986113.3113396940517159688235887",
        "totalBorrowBalanceUSD": "79783398.04347688280051756305766987",
        "timestamp": "1689638397",
        "blockNumber": "32739458"
      },
      {
        "totalDepositBalanceUSD": "257655604.032015278471708205735597",
        "totalBorrowBalanceUSD": "79972500.21971431007836519566871447",
        "timestamp": "1689551875",
        "blockNumber": "32696987"
      },
      {
        "totalDepositBalanceUSD": "289539776.0361780477192395296029443",
        "totalBorrowBalanceUSD": "88072582.40028039707123601144639058",
        "timestamp": "1689465557",
        "blockNumber": "32654656"
      },
      {
        "totalDepositBalanceUSD": "292044879.2493737503438943650251749",
        "totalBorrowBalanceUSD": "87335461.64761678520615350676009084",
        "timestamp": "1689379199",
        "blockNumber": "32611882"
      },
      {
        "totalDepositBalanceUSD": "298264340.0228788427117786674054575",
        "totalBorrowBalanceUSD": "87513971.6313221278934611723188124",
        "timestamp": "1689292775",
        "blockNumber": "32569000"
      },
      {
        "totalDepositBalanceUSD": "290826268.9546277110497897769331218",
        "totalBorrowBalanceUSD": "89091974.37028115014761428030608361",
        "timestamp": "1689206373",
        "blockNumber": "32526142"
      },
      {
        "totalDepositBalanceUSD": "293843437.2075474876462411271992602",
        "totalBorrowBalanceUSD": "89377656.0032559272160606741726443",
        "timestamp": "1689119974",
        "blockNumber": "32483335"
      },
      {
        "totalDepositBalanceUSD": "294179552.1437887990496610825682749",
        "totalBorrowBalanceUSD": "90048539.33628383816702443472575611",
        "timestamp": "1689033598",
        "blockNumber": "32441619"
      },
      {
        "totalDepositBalanceUSD": "293048276.8576956054073132924200139",
        "totalBorrowBalanceUSD": "89479194.92437699774518826060002638",
        "timestamp": "1688947178",
        "blockNumber": "32399377"
      },
      {
        "totalDepositBalanceUSD": "293484273.9391951710798812991497553",
        "totalBorrowBalanceUSD": "89357507.18503204814176605018903748",
        "timestamp": "1688860778",
        "blockNumber": "32357275"
      },
      {
        "totalDepositBalanceUSD": "289196919.5747702702597310649692416",
        "totalBorrowBalanceUSD": "87268790.8567756202119164988970461",
        "timestamp": "1688774378",
        "blockNumber": "32314582"
      },
      {
        "totalDepositBalanceUSD": "286279364.8468102304059105573107936",
        "totalBorrowBalanceUSD": "86699808.84744760715955874528451977",
        "timestamp": "1688687979",
        "blockNumber": "32272006"
      },
      {
        "totalDepositBalanceUSD": "290381826.0928413762726272554277913",
        "totalBorrowBalanceUSD": "86953890.76705716964705262661062019",
        "timestamp": "1688601596",
        "blockNumber": "32229473"
      },
      {
        "totalDepositBalanceUSD": "293870888.9639403103006757884336973",
        "totalBorrowBalanceUSD": "87803139.38389910587952132167422514",
        "timestamp": "1688515178",
        "blockNumber": "32186812"
      },
      {
        "totalDepositBalanceUSD": "296711002.1972837263675937831531349",
        "totalBorrowBalanceUSD": "88561326.70433706784614973579152347",
        "timestamp": "1688428775",
        "blockNumber": "32144127"
      },
      {
        "totalDepositBalanceUSD": "295685556.7854875554991702588408889",
        "totalBorrowBalanceUSD": "89402133.01154987391158847321154582",
        "timestamp": "1688342295",
        "blockNumber": "32101800"
      },
      {
        "totalDepositBalanceUSD": "295573502.2809377768231229004001439",
        "totalBorrowBalanceUSD": "90020743.71526025653063037882069108",
        "timestamp": "1688255896",
        "blockNumber": "32059241"
      },
      {
        "totalDepositBalanceUSD": "292537268.5551129264259913028035095",
        "totalBorrowBalanceUSD": "87832500.10644325536982377302330582",
        "timestamp": "1688169574",
        "blockNumber": "32016913"
      },
      {
        "totalDepositBalanceUSD": "288424926.4777372332605974338129204",
        "totalBorrowBalanceUSD": "85861846.60846866477348639121073065",
        "timestamp": "1688083173",
        "blockNumber": "31974511"
      },
      {
        "totalDepositBalanceUSD": "283357178.9746462638189788977673211",
        "totalBorrowBalanceUSD": "84698181.48594761279356439957693456",
        "timestamp": "1687996786",
        "blockNumber": "31932046"
      },
      {
        "totalDepositBalanceUSD": "291634332.136128716638675237835251",
        "totalBorrowBalanceUSD": "86731989.23759593461305419884695333",
        "timestamp": "1687910374",
        "blockNumber": "31889583"
      },
      {
        "totalDepositBalanceUSD": "289141344.3824118135431409692395752",
        "totalBorrowBalanceUSD": "86352542.92412613429768269556785272",
        "timestamp": "1687823973",
        "blockNumber": "31847470"
      },
      {
        "totalDepositBalanceUSD": "294876148.3625445468138338330994419",
        "totalBorrowBalanceUSD": "88740724.43543917544351779146051742",
        "timestamp": "1687737573",
        "blockNumber": "31804901"
      },
      {
        "totalDepositBalanceUSD": "295080528.8244829104156837818907549",
        "totalBorrowBalanceUSD": "90513443.97452058461428551012322356",
        "timestamp": "1687651172",
        "blockNumber": "31762350"
      },
      {
        "totalDepositBalanceUSD": "294945398.688882102871577553876568",
        "totalBorrowBalanceUSD": "89351780.39400078731340467218320265",
        "timestamp": "1687564773",
        "blockNumber": "31720175"
      },
      {
        "totalDepositBalanceUSD": "296128672.5852663252798493894683207",
        "totalBorrowBalanceUSD": "91996610.86342590934789282792567226",
        "timestamp": "1687478386",
        "blockNumber": "31678047"
      },
      {
        "totalDepositBalanceUSD": "298065390.8530120185008692276044286",
        "totalBorrowBalanceUSD": "91961012.38434509304150926133794752",
        "timestamp": "1687391960",
        "blockNumber": "31635642"
      },
      {
        "totalDepositBalanceUSD": "286155844.2791016431613876148948532",
        "totalBorrowBalanceUSD": "87622687.23351820535225210472056506",
        "timestamp": "1687305419",
        "blockNumber": "31594006"
      },
      {
        "totalDepositBalanceUSD": "273543881.9153953641415753894432317",
        "totalBorrowBalanceUSD": "85406156.16166782811557154755276247",
        "timestamp": "1687219183",
        "blockNumber": "31551387"
      },
      {
        "totalDepositBalanceUSD": "267762452.6845364343253794893548563",
        "totalBorrowBalanceUSD": "83983881.35711262949758122598019658",
        "timestamp": "1687132720",
        "blockNumber": "31508866"
      },
      {
        "totalDepositBalanceUSD": "269131992.5518692865001777710656977",
        "totalBorrowBalanceUSD": "84003075.91672863979818516025787106",
        "timestamp": "1687046287",
        "blockNumber": "31466435"
      },
      {
        "totalDepositBalanceUSD": "269794995.0371295836215872620194313",
        "totalBorrowBalanceUSD": "85156799.71303275415528863537508556",
        "timestamp": "1686959921",
        "blockNumber": "31424217"
      },
      {
        "totalDepositBalanceUSD": "264489442.0574809481011296841552358",
        "totalBorrowBalanceUSD": "84651413.11070384282595666651389686",
        "timestamp": "1686873515",
        "blockNumber": "31381628"
      },
      {
        "totalDepositBalanceUSD": "256699849.822599568595547718212184",
        "totalBorrowBalanceUSD": "78488885.31234622202732678204085873",
        "timestamp": "1686787022",
        "blockNumber": "31339602"
      },
      {
        "totalDepositBalanceUSD": "262300205.3629173195898865458015632",
        "totalBorrowBalanceUSD": "79790591.88299045301412494561803591",
        "timestamp": "1686700777",
        "blockNumber": "31297717"
      },
      {
        "totalDepositBalanceUSD": "262259060.4191766371754949800964514",
        "totalBorrowBalanceUSD": "80095198.68380134175010089896950225",
        "timestamp": "1686614317",
        "blockNumber": "31255744"
      },
      {
        "totalDepositBalanceUSD": "263739980.4276111106541675300187615",
        "totalBorrowBalanceUSD": "80328013.03034814103682822539428264",
        "timestamp": "1686527994",
        "blockNumber": "31213546"
      },
      {
        "totalDepositBalanceUSD": "263098360.6259455579299289229879001",
        "totalBorrowBalanceUSD": "80009342.34423548089209007686435313",
        "timestamp": "1686441589",
        "blockNumber": "31171125"
      },
      {
        "totalDepositBalanceUSD": "279242719.4864049638806938562617347",
        "totalBorrowBalanceUSD": "87677081.7849436840527014946207122",
        "timestamp": "1686355151",
        "blockNumber": "31129007"
      },
      {
        "totalDepositBalanceUSD": "284897948.857385795425610097423516",
        "totalBorrowBalanceUSD": "90504876.37957786602014930463961778",
        "timestamp": "1686268785",
        "blockNumber": "31086680"
      },
      {
        "totalDepositBalanceUSD": "283339023.1292097787545531320654453",
        "totalBorrowBalanceUSD": "86283383.25959604624326244427434906",
        "timestamp": "1686181265",
        "blockNumber": "31044469"
      },
      {
        "totalDepositBalanceUSD": "295007512.8219465433870499305681363",
        "totalBorrowBalanceUSD": "91962327.20155473983751073164949418",
        "timestamp": "1686095970",
        "blockNumber": "31002422"
      },
      {
        "totalDepositBalanceUSD": "277318845.6399682938409378038848608",
        "totalBorrowBalanceUSD": "83660192.87592770204132888836938469",
        "timestamp": "1686009401",
        "blockNumber": "30960363"
      },
      {
        "totalDepositBalanceUSD": "290783666.9238486094299597273804622",
        "totalBorrowBalanceUSD": "87796549.66928526612203130945917377",
        "timestamp": "1685923170",
        "blockNumber": "30918252"
      },
      {
        "totalDepositBalanceUSD": "282667082.5011048049673888296604296",
        "totalBorrowBalanceUSD": "87185410.13742443023340466690977148",
        "timestamp": "1685836675",
        "blockNumber": "30875763"
      },
      {
        "totalDepositBalanceUSD": "291493866.2467776578688403934753904",
        "totalBorrowBalanceUSD": "87848070.44154530337883521422920584",
        "timestamp": "1685750315",
        "blockNumber": "30833303"
      },
      {
        "totalDepositBalanceUSD": "284484525.7984522113025000107059188",
        "totalBorrowBalanceUSD": "87532285.5981096974748457812043166",
        "timestamp": "1685663987",
        "blockNumber": "30790979"
      },
      {
        "totalDepositBalanceUSD": "283050681.7248798123738042126018626",
        "totalBorrowBalanceUSD": "86128671.16994382904199270303516316",
        "timestamp": "1685577574",
        "blockNumber": "30749200"
      },
      {
        "totalDepositBalanceUSD": "293791565.2044612297452503775813633",
        "totalBorrowBalanceUSD": "93254156.19660745855495743980838207",
        "timestamp": "1685491022",
        "blockNumber": "30706604"
      },
      {
        "totalDepositBalanceUSD": "288291439.1202702535137098640653833",
        "totalBorrowBalanceUSD": "87625952.06195065201506236412415906",
        "timestamp": "1685404146",
        "blockNumber": "30663856"
      },
      {
        "totalDepositBalanceUSD": "291346345.6842824972250900953659544",
        "totalBorrowBalanceUSD": "88270086.42844920954239791673929593",
        "timestamp": "1685318353",
        "blockNumber": "30621535"
      },
      {
        "totalDepositBalanceUSD": "283356321.3134239726674849762824735",
        "totalBorrowBalanceUSD": "87197541.52653383470857746522322596",
        "timestamp": "1685231917",
        "blockNumber": "30578900"
      },
      {
        "totalDepositBalanceUSD": "285937049.419771510943133441986199",
        "totalBorrowBalanceUSD": "86844281.04661481722747267715739953",
        "timestamp": "1685145592",
        "blockNumber": "30536784"
      },
      {
        "totalDepositBalanceUSD": "278590165.1209784019925548370893797",
        "totalBorrowBalanceUSD": "86272141.13882785496588466165092982",
        "timestamp": "1685059187",
        "blockNumber": "30495154"
      },
      {
        "totalDepositBalanceUSD": "277468878.2631742005519908762592546",
        "totalBorrowBalanceUSD": "86065846.90962418628292589085173975",
        "timestamp": "1684971423",
        "blockNumber": "30452347"
      },
      {
        "totalDepositBalanceUSD": "288251995.8267434770924440243640975",
        "totalBorrowBalanceUSD": "89813775.52660402344868989925755823",
        "timestamp": "1684886341",
        "blockNumber": "30410370"
      },
      {
        "totalDepositBalanceUSD": "285141974.3609191149937664286436994",
        "totalBorrowBalanceUSD": "88441575.84689662976502160728724641",
        "timestamp": "1684799892",
        "blockNumber": "30367749"
      },
      {
        "totalDepositBalanceUSD": "283319427.3932677875754987157007492",
        "totalBorrowBalanceUSD": "87715095.96306598526897371923892123",
        "timestamp": "1684713538",
        "blockNumber": "30325198"
      },
      {
        "totalDepositBalanceUSD": "286232997.8456876336958432414823941",
        "totalBorrowBalanceUSD": "88430264.31964386029601076220728558",
        "timestamp": "1684627159",
        "blockNumber": "30283097"
      },
      {
        "totalDepositBalanceUSD": "287071727.9742695145332073591185649",
        "totalBorrowBalanceUSD": "89147211.20767411182705422182573759",
        "timestamp": "1684540737",
        "blockNumber": "30240541"
      },
      {
        "totalDepositBalanceUSD": "286446474.4622224601623631778958739",
        "totalBorrowBalanceUSD": "89157739.09946588954658850727518869",
        "timestamp": "1684454397",
        "blockNumber": "30197891"
      },
      {
        "totalDepositBalanceUSD": "291513406.5875514671603971785028277",
        "totalBorrowBalanceUSD": "90138054.42688884556796594941125183",
        "timestamp": "1684367993",
        "blockNumber": "30155613"
      },
      {
        "totalDepositBalanceUSD": "294386226.3677358562300717657388301",
        "totalBorrowBalanceUSD": "91266891.58960366635042787266344976",
        "timestamp": "1684281456",
        "blockNumber": "30113495"
      },
      {
        "totalDepositBalanceUSD": "300222426.7690096723804465794276076",
        "totalBorrowBalanceUSD": "93930197.99767484374038810112171589",
        "timestamp": "1684194823",
        "blockNumber": "30071211"
      },
      {
        "totalDepositBalanceUSD": "298127707.7225322100633354214156614",
        "totalBorrowBalanceUSD": "94110600.57887415531927178893615988",
        "timestamp": "1684108743",
        "blockNumber": "30028724"
      },
      {
        "totalDepositBalanceUSD": "296192540.9480887210501753583447542",
        "totalBorrowBalanceUSD": "94530180.7026879969315985138549641",
        "timestamp": "1684022360",
        "blockNumber": "29986328"
      },
      {
        "totalDepositBalanceUSD": "294386354.6935725386608202899912925",
        "totalBorrowBalanceUSD": "93951063.03434000063140051638439407",
        "timestamp": "1683935997",
        "blockNumber": "29943840"
      },
      {
        "totalDepositBalanceUSD": "290034634.616070533972162706595324",
        "totalBorrowBalanceUSD": "89394477.17627596441682159864554077",
        "timestamp": "1683849560",
        "blockNumber": "29901178"
      },
      {
        "totalDepositBalanceUSD": "288820561.6724244055028930822549509",
        "totalBorrowBalanceUSD": "85647452.26538660683225424167472485",
        "timestamp": "1683763023",
        "blockNumber": "29858817"
      },
      {
        "totalDepositBalanceUSD": "287945754.5570443834048619788514554",
        "totalBorrowBalanceUSD": "85011268.56685840666256264339854228",
        "timestamp": "1683676747",
        "blockNumber": "29816347"
      },
      {
        "totalDepositBalanceUSD": "288800909.5882028602720149389471019",
        "totalBorrowBalanceUSD": "85190502.56361779781105186266044818",
        "timestamp": "1683590398",
        "blockNumber": "29773824"
      },
      {
        "totalDepositBalanceUSD": "297837450.2034530523929993971339909",
        "totalBorrowBalanceUSD": "87249167.02707960982184639203508911",
        "timestamp": "1683503988",
        "blockNumber": "29731232"
      },
      {
        "totalDepositBalanceUSD": "300328303.9855978464168381858433309",
        "totalBorrowBalanceUSD": "87641814.06546009762043964740724056",
        "timestamp": "1683417597",
        "blockNumber": "29688946"
      },
      {
        "totalDepositBalanceUSD": "307351193.884985410866501256096153",
        "totalBorrowBalanceUSD": "88379513.74647909118853740136079329",
        "timestamp": "1683331160",
        "blockNumber": "29646543"
      },
      {
        "totalDepositBalanceUSD": "305725225.8240942724936893641427423",
        "totalBorrowBalanceUSD": "86476700.65318941688425587052243118",
        "timestamp": "1683244501",
        "blockNumber": "29604089"
      },
      {
        "totalDepositBalanceUSD": "305640207.4657042000876243651116948",
        "totalBorrowBalanceUSD": "86752698.10523285060686146641085728",
        "timestamp": "1683158344",
        "blockNumber": "29561663"
      },
      {
        "totalDepositBalanceUSD": "301554518.7557067060186748047074908",
        "totalBorrowBalanceUSD": "85743064.55851721452029215857212246",
        "timestamp": "1683071944",
        "blockNumber": "29519121"
      },
      {
        "totalDepositBalanceUSD": "297229135.2703677698998458688411292",
        "totalBorrowBalanceUSD": "85018588.7805848068005494960503176",
        "timestamp": "1682985544",
        "blockNumber": "29476788"
      },
      {
        "totalDepositBalanceUSD": "306049742.5254338228110515924341684",
        "totalBorrowBalanceUSD": "86911899.57652336368624876680415641",
        "timestamp": "1682899160",
        "blockNumber": "29434883"
      },
      {
        "totalDepositBalanceUSD": "308580023.3886560467492667362587645",
        "totalBorrowBalanceUSD": "87713361.21282695095877767476238528",
        "timestamp": "1682812793",
        "blockNumber": "29392802"
      },
      {
        "totalDepositBalanceUSD": "308519835.1096521887434455776642918",
        "totalBorrowBalanceUSD": "87609910.82583546065538773515294144",
        "timestamp": "1682726344",
        "blockNumber": "29350692"
      },
      {
        "totalDepositBalanceUSD": "308517539.7820493506639032133005585",
        "totalBorrowBalanceUSD": "88567893.10210113850426165125362632",
        "timestamp": "1682639942",
        "blockNumber": "29308476"
      },
      {
        "totalDepositBalanceUSD": "299446713.2280622292244342595887592",
        "totalBorrowBalanceUSD": "87051567.23229662674587879746706337",
        "timestamp": "1682553596",
        "blockNumber": "29266202"
      },
      {
        "totalDepositBalanceUSD": "304526833.3234984281682623287149806",
        "totalBorrowBalanceUSD": "87111590.27385150084523472377115635",
        "timestamp": "1682467145",
        "blockNumber": "29223905"
      },
      {
        "totalDepositBalanceUSD": "302725909.8846619613385924131848007",
        "totalBorrowBalanceUSD": "86267859.27442051119853884725040851",
        "timestamp": "1682380743",
        "blockNumber": "29181538"
      },
      {
        "totalDepositBalanceUSD": "305102528.9705566457314533453012876",
        "totalBorrowBalanceUSD": "88319690.41120224910214406103031855",
        "timestamp": "1682294358",
        "blockNumber": "29139226"
      },
      {
        "totalDepositBalanceUSD": "307196582.6156994767662090755583367",
        "totalBorrowBalanceUSD": "89069458.78890055351942812360375454",
        "timestamp": "1682207783",
        "blockNumber": "29096942"
      },
      {
        "totalDepositBalanceUSD": "306733433.7951567859412146716845127",
        "totalBorrowBalanceUSD": "87362736.54954411351369712006013259",
        "timestamp": "1682121546",
        "blockNumber": "29054541"
      },
      {
        "totalDepositBalanceUSD": "325190797.4389911342316350108643492",
        "totalBorrowBalanceUSD": "95964547.89852079952982636879010821",
        "timestamp": "1682035150",
        "blockNumber": "29011899"
      },
      {
        "totalDepositBalanceUSD": "333089201.8941169796362173351787632",
        "totalBorrowBalanceUSD": "98293549.88748949077929436662761",
        "timestamp": "1681948751",
        "blockNumber": "28969443"
      },
      {
        "totalDepositBalanceUSD": "353283887.2286991533977910172773105",
        "totalBorrowBalanceUSD": "102944599.2093454472461221156019057",
        "timestamp": "1681862377",
        "blockNumber": "28926576"
      },
      {
        "totalDepositBalanceUSD": "347447595.2083212059149828107004862",
        "totalBorrowBalanceUSD": "102327941.5675910922625379927954885",
        "timestamp": "1681775944",
        "blockNumber": "28883729"
      },
      {
        "totalDepositBalanceUSD": "346894263.8704646921601517321972412",
        "totalBorrowBalanceUSD": "97964800.20788774802760813897124132",
        "timestamp": "1681689434",
        "blockNumber": "28841523"
      },
      {
        "totalDepositBalanceUSD": "346803199.5990971482346034226925501",
        "totalBorrowBalanceUSD": "96508362.18151367113355648255614744",
        "timestamp": "1681603147",
        "blockNumber": "28798559"
      },
      {
        "totalDepositBalanceUSD": "347668341.0886547555285695095057627",
        "totalBorrowBalanceUSD": "96925070.56395876883105984287008842",
        "timestamp": "1681516797",
        "blockNumber": "28755766"
      },
      {
        "totalDepositBalanceUSD": "345846644.9807186216283642731473113",
        "totalBorrowBalanceUSD": "95719277.91636556839274224159083531",
        "timestamp": "1681430344",
        "blockNumber": "28712866"
      },
      {
        "totalDepositBalanceUSD": "337117568.599630960265957620869025",
        "totalBorrowBalanceUSD": "94089372.02258501024465961215967768",
        "timestamp": "1681343999",
        "blockNumber": "28669929"
      },
      {
        "totalDepositBalanceUSD": "337578496.5174774956876442107769874",
        "totalBorrowBalanceUSD": "94719181.88437427250354566254337378",
        "timestamp": "1681257560",
        "blockNumber": "28626935"
      },
      {
        "totalDepositBalanceUSD": "338236103.7903352371201555956798811",
        "totalBorrowBalanceUSD": "94420435.51369307654837162093291435",
        "timestamp": "1681171152",
        "blockNumber": "28584103"
      },
      {
        "totalDepositBalanceUSD": "341830060.9192634025085165829540923",
        "totalBorrowBalanceUSD": "101430301.2283262377571458294517868",
        "timestamp": "1681084745",
        "blockNumber": "28541407"
      },
      {
        "totalDepositBalanceUSD": "338660032.8097966110400230053806347",
        "totalBorrowBalanceUSD": "101162620.4736556727889037656337882",
        "timestamp": "1680998125",
        "blockNumber": "28498461"
      },
      {
        "totalDepositBalanceUSD": "340116607.2194037461982281914233716",
        "totalBorrowBalanceUSD": "101743104.7422206384811043994635397",
        "timestamp": "1680911685",
        "blockNumber": "28455582"
      },
      {
        "totalDepositBalanceUSD": "341971216.1329096935427994880588177",
        "totalBorrowBalanceUSD": "102379872.1517880023576666620232777",
        "timestamp": "1680825526",
        "blockNumber": "28412900"
      },
      {
        "totalDepositBalanceUSD": "334991768.8253209529894583154007323",
        "totalBorrowBalanceUSD": "95703622.76008348904307893295435951",
        "timestamp": "1680739101",
        "blockNumber": "28369996"
      },
      {
        "totalDepositBalanceUSD": "323575984.7074411884393978346159529",
        "totalBorrowBalanceUSD": "87845448.8521802130637977251270283",
        "timestamp": "1680652603",
        "blockNumber": "28327120"
      },
      {
        "totalDepositBalanceUSD": "347233015.7067447666363938539101297",
        "totalBorrowBalanceUSD": "97637157.54885027944106285156367376",
        "timestamp": "1680565908",
        "blockNumber": "28284260"
      },
      {
        "totalDepositBalanceUSD": "354351993.151454154593765621597023",
        "totalBorrowBalanceUSD": "97934355.35556220794409250735605046",
        "timestamp": "1680479912",
        "blockNumber": "28241595"
      },
      {
        "totalDepositBalanceUSD": "372332515.599866888229244636359936",
        "totalBorrowBalanceUSD": "110447320.6543872499088941012865339",
        "timestamp": "1680393559",
        "blockNumber": "28198819"
      },
      {
        "totalDepositBalanceUSD": "372417606.4986327530027087750251471",
        "totalBorrowBalanceUSD": "109923242.3709773869822912520856254",
        "timestamp": "1680307009",
        "blockNumber": "28155893"
      },
      {
        "totalDepositBalanceUSD": "361156164.604779794038220977530866",
        "totalBorrowBalanceUSD": "102990491.2012045864922919555674701",
        "timestamp": "1680220589",
        "blockNumber": "28112960"
      },
      {
        "totalDepositBalanceUSD": "366803195.5396016387162748289448019",
        "totalBorrowBalanceUSD": "103658429.5407210090633755069265032",
        "timestamp": "1680134127",
        "blockNumber": "28069598"
      },
      {
        "totalDepositBalanceUSD": "356795146.9855779856454479184485721",
        "totalBorrowBalanceUSD": "101047361.3677975205828603559965926",
        "timestamp": "1680047946",
        "blockNumber": "28027916"
      },
      {
        "totalDepositBalanceUSD": "352330079.4259814170553969622575611",
        "totalBorrowBalanceUSD": "99361668.4133640367613110405384373",
        "timestamp": "1679961544",
        "blockNumber": "27986004"
      },
      {
        "totalDepositBalanceUSD": "360495935.198803458971288251023103",
        "totalBorrowBalanceUSD": "99309218.34262536687256730303361529",
        "timestamp": "1679875198",
        "blockNumber": "27944718"
      },
      {
        "totalDepositBalanceUSD": "355191730.6976364463857208807137556",
        "totalBorrowBalanceUSD": "98178292.47513725635477238976461625",
        "timestamp": "1679788744",
        "blockNumber": "27907661"
      },
      {
        "totalDepositBalanceUSD": "356770152.6720780050540784943047725",
        "totalBorrowBalanceUSD": "98558528.43778495815314200125930958",
        "timestamp": "1679702343",
        "blockNumber": "27866181"
      },
      {
        "totalDepositBalanceUSD": "364312211.3521761048219321428983416",
        "totalBorrowBalanceUSD": "99971509.9854208623166220781183904",
        "timestamp": "1679615943",
        "blockNumber": "27825003"
      },
      {
        "totalDepositBalanceUSD": "356361608.877226121457483788279537",
        "totalBorrowBalanceUSD": "99093880.26556054641155499920126945",
        "timestamp": "1679528783",
        "blockNumber": "27788357"
      },
      {
        "totalDepositBalanceUSD": "363210720.4111052543725468844226346",
        "totalBorrowBalanceUSD": "96130813.21369025888822406545171177",
        "timestamp": "1679442971",
        "blockNumber": "27746524"
      },
      {
        "totalDepositBalanceUSD": "360594762.0739805360423172642976823",
        "totalBorrowBalanceUSD": "96026437.71273670945209033657042058",
        "timestamp": "1679356745",
        "blockNumber": "27703881"
      },
      {
        "totalDepositBalanceUSD": "358228441.4982843343945514735644017",
        "totalBorrowBalanceUSD": "92699888.64457138511670552839518599",
        "timestamp": "1679270355",
        "blockNumber": "27661015"
      },
      {
        "totalDepositBalanceUSD": "347138098.3795607777843336752205457",
        "totalBorrowBalanceUSD": "91630258.4992334078085114766489562",
        "timestamp": "1679183993",
        "blockNumber": "27618178"
      },
      {
        "totalDepositBalanceUSD": "342539879.3621485335750489583982688",
        "totalBorrowBalanceUSD": "89860848.45928504796000116089187893",
        "timestamp": "1679097474",
        "blockNumber": "27574930"
      },
      {
        "totalDepositBalanceUSD": "334728040.1372765862526687731728665",
        "totalBorrowBalanceUSD": "92223707.1907119180443373530799358",
        "timestamp": "1679011145",
        "blockNumber": "27532494"
      },
      {
        "totalDepositBalanceUSD": "330268160.1871145611701081100878705",
        "totalBorrowBalanceUSD": "91130513.57625094659321614888368808",
        "timestamp": "1678924748",
        "blockNumber": "27490324"
      },
      {
        "totalDepositBalanceUSD": "345117506.6939506498654994520311581",
        "totalBorrowBalanceUSD": "91427512.73684629626337436906218837",
        "timestamp": "1678838362",
        "blockNumber": "27447852"
      },
      {
        "totalDepositBalanceUSD": "342024973.3239388610241594727412592",
        "totalBorrowBalanceUSD": "91297654.41412917763753951140047467",
        "timestamp": "1678751943",
        "blockNumber": "27405226"
      },
      {
        "totalDepositBalanceUSD": "359231826.9081950323397975585352338",
        "totalBorrowBalanceUSD": "91459789.67376898064938189860327553",
        "timestamp": "1678665530",
        "blockNumber": "27362896"
      },
      {
        "totalDepositBalanceUSD": "344722658.9188203102497241243739471",
        "totalBorrowBalanceUSD": "94660825.05681157752711834751715576",
        "timestamp": "1678579198",
        "blockNumber": "27320306"
      },
      {
        "totalDepositBalanceUSD": "366993621.1827089376183339925527356",
        "totalBorrowBalanceUSD": "112062579.1843723311702512823810265",
        "timestamp": "1678492750",
        "blockNumber": "27276247"
      },
      {
        "totalDepositBalanceUSD": "380441174.3199491257615730392707191",
        "totalBorrowBalanceUSD": "114057302.978279686556185831937896",
        "timestamp": "1678406398",
        "blockNumber": "27233323"
      },
      {
        "totalDepositBalanceUSD": "413625586.249753035328924233075739",
        "totalBorrowBalanceUSD": "117941065.6477967337399592027360742",
        "timestamp": "1678319944",
        "blockNumber": "27191177"
      },
      {
        "totalDepositBalanceUSD": "415362260.2838815862855653197904329",
        "totalBorrowBalanceUSD": "122757924.6693875021036857090792493",
        "timestamp": "1678233599",
        "blockNumber": "27149510"
      },
      {
        "totalDepositBalanceUSD": "404492935.4509809543851086946198609",
        "totalBorrowBalanceUSD": "113848519.3947836372185661657860866",
        "timestamp": "1678146962",
        "blockNumber": "27108434"
      },
      {
        "totalDepositBalanceUSD": "400123190.0907812667597958181134855",
        "totalBorrowBalanceUSD": "110271274.2378410578173754551235956",
        "timestamp": "1678060736",
        "blockNumber": "27067760"
      },
      {
        "totalDepositBalanceUSD": "398010165.5927962059792698092994027",
        "totalBorrowBalanceUSD": "107924360.0398664418783069731563234",
        "timestamp": "1677974350",
        "blockNumber": "27027051"
      },
      {
        "totalDepositBalanceUSD": "400567757.1973623613378324279662903",
        "totalBorrowBalanceUSD": "108273538.9446107228898439668672041",
        "timestamp": "1677887945",
        "blockNumber": "26986879"
      },
      {
        "totalDepositBalanceUSD": "399783778.5082863803023720835263991",
        "totalBorrowBalanceUSD": "115516667.3433929144000822689351959",
        "timestamp": "1677801544",
        "blockNumber": "26944611"
      },
      {
        "totalDepositBalanceUSD": "406726775.5585924641444656548871818",
        "totalBorrowBalanceUSD": "143058575.7260947591345648026591021",
        "timestamp": "1677715144",
        "blockNumber": "26903542"
      },
      {
        "totalDepositBalanceUSD": "406634888.1102046850570253415767918",
        "totalBorrowBalanceUSD": "138538538.8725650107097294564587196",
        "timestamp": "1677628746",
        "blockNumber": "26862089"
      },
      {
        "totalDepositBalanceUSD": "417677165.5063800025548826129432153",
        "totalBorrowBalanceUSD": "142827091.3590552947862429983489109",
        "timestamp": "1677542349",
        "blockNumber": "26820635"
      },
      {
        "totalDepositBalanceUSD": "439853959.6657077919908064696050623",
        "totalBorrowBalanceUSD": "161652445.707430700273716402959379",
        "timestamp": "1677455946",
        "blockNumber": "26778506"
      },
      {
        "totalDepositBalanceUSD": "435620184.5594001376264716992013651",
        "totalBorrowBalanceUSD": "161587203.8597376092257231197682018",
        "timestamp": "1677369509",
        "blockNumber": "26736401"
      },
      {
        "totalDepositBalanceUSD": "438679573.0872099897969508596643101",
        "totalBorrowBalanceUSD": "161878350.0709309455729867479033211",
        "timestamp": "1677283168",
        "blockNumber": "26694342"
      },
      {
        "totalDepositBalanceUSD": "479562432.4907168139070669716504278",
        "totalBorrowBalanceUSD": "193582847.96559065635321876458046",
        "timestamp": "1677196612",
        "blockNumber": "26651697"
      },
      {
        "totalDepositBalanceUSD": "475663138.9222742703201976092993935",
        "totalBorrowBalanceUSD": "187333788.3206561655568819507458245",
        "timestamp": "1677110338",
        "blockNumber": "26608818"
      },
      {
        "totalDepositBalanceUSD": "480676276.2215272260243558792133451",
        "totalBorrowBalanceUSD": "189912393.5073476082150687752070612",
        "timestamp": "1677023789",
        "blockNumber": "26565538"
      },
      {
        "totalDepositBalanceUSD": "487360456.3379282621555645727270411",
        "totalBorrowBalanceUSD": "193472004.283777002488109479048633",
        "timestamp": "1676937318",
        "blockNumber": "26522622"
      },
      {
        "totalDepositBalanceUSD": "492872127.4081144880588342756070162",
        "totalBorrowBalanceUSD": "195101749.6243172721556940663214118",
        "timestamp": "1676851143",
        "blockNumber": "26479769"
      },
      {
        "totalDepositBalanceUSD": "493547335.7705883223464217990198688",
        "totalBorrowBalanceUSD": "194151697.8194591524838238674126534",
        "timestamp": "1676764745",
        "blockNumber": "26437451"
      },
      {
        "totalDepositBalanceUSD": "480769175.7215134915120211811967332",
        "totalBorrowBalanceUSD": "187162710.6724312391291694713160319",
        "timestamp": "1676678345",
        "blockNumber": "26394900"
      },
      {
        "totalDepositBalanceUSD": "474434169.712502326472440979302915",
        "totalBorrowBalanceUSD": "184926197.2434635575771392612153216",
        "timestamp": "1676591995",
        "blockNumber": "26352168"
      },
      {
        "totalDepositBalanceUSD": "483124167.2691780104793871891831988",
        "totalBorrowBalanceUSD": "186113843.5078825133792617571700317",
        "timestamp": "1676505579",
        "blockNumber": "26309301"
      },
      {
        "totalDepositBalanceUSD": "459484709.7299492652254675671270883",
        "totalBorrowBalanceUSD": "176764293.9225706432667316471374169",
        "timestamp": "1676419163",
        "blockNumber": "26267008"
      },
      {
        "totalDepositBalanceUSD": "461912832.882906356634504442177552",
        "totalBorrowBalanceUSD": "182287656.3069764693965070329602506",
        "timestamp": "1676332762",
        "blockNumber": "26224706"
      },
      {
        "totalDepositBalanceUSD": "467317811.4040148755156535947885421",
        "totalBorrowBalanceUSD": "187251758.1479507632539498139977599",
        "timestamp": "1676246343",
        "blockNumber": "26182311"
      },
      {
        "totalDepositBalanceUSD": "470858514.7963009490650668461520503",
        "totalBorrowBalanceUSD": "187674943.477487491649634354427615",
        "timestamp": "1676159982",
        "blockNumber": "26140516"
      },
      {
        "totalDepositBalanceUSD": "472648423.5206148734671868870780375",
        "totalBorrowBalanceUSD": "191637683.5144195628099575353439416",
        "timestamp": "1676073559",
        "blockNumber": "26098789"
      },
      {
        "totalDepositBalanceUSD": "475353119.0746962695870844683078819",
        "totalBorrowBalanceUSD": "192602974.2459061378109956881868028",
        "timestamp": "1675987143",
        "blockNumber": "26056288"
      },
      {
        "totalDepositBalanceUSD": "491193976.540137558157445491198628",
        "totalBorrowBalanceUSD": "195827323.3223917769408864174818536",
        "timestamp": "1675900746",
        "blockNumber": "26013538"
      },
      {
        "totalDepositBalanceUSD": "511335553.1363054876939159102672315",
        "totalBorrowBalanceUSD": "209799083.1574172300495267925616139",
        "timestamp": "1675814372",
        "blockNumber": "25971221"
      },
      {
        "totalDepositBalanceUSD": "498912237.1706814257540391579486993",
        "totalBorrowBalanceUSD": "203753961.1088584698559826095222065",
        "timestamp": "1675727990",
        "blockNumber": "25928414"
      },
      {
        "totalDepositBalanceUSD": "496526091.8460332719677441301463193",
        "totalBorrowBalanceUSD": "192868240.5439791204816344360477633",
        "timestamp": "1675641546",
        "blockNumber": "25885591"
      },
      {
        "totalDepositBalanceUSD": "503230260.8610363895245459488130426",
        "totalBorrowBalanceUSD": "192879752.1326468279818728340720635",
        "timestamp": "1675555163",
        "blockNumber": "25842898"
      },
      {
        "totalDepositBalanceUSD": "501238806.3772671969272174534970466",
        "totalBorrowBalanceUSD": "192222087.7525703244005396072472589",
        "timestamp": "1675468748",
        "blockNumber": "25800300"
      },
      {
        "totalDepositBalanceUSD": "498392194.2502402221959918846419959",
        "totalBorrowBalanceUSD": "203936547.550463450442353944188066",
        "timestamp": "1675382399",
        "blockNumber": "25757525"
      },
      {
        "totalDepositBalanceUSD": "496450216.2677290449222348548209263",
        "totalBorrowBalanceUSD": "195105837.892972253682054494306403",
        "timestamp": "1675295957",
        "blockNumber": "25714190"
      },
      {
        "totalDepositBalanceUSD": "492567100.1357553717575014675396957",
        "totalBorrowBalanceUSD": "199520350.2327582007711156898881128",
        "timestamp": "1675209583",
        "blockNumber": "25670924"
      },
      {
        "totalDepositBalanceUSD": "486098684.909257029170135302973523",
        "totalBorrowBalanceUSD": "194397095.2517656540648254788154359",
        "timestamp": "1675123174",
        "blockNumber": "25628885"
      },
      {
        "totalDepositBalanceUSD": "500243821.5496769491363949249052879",
        "totalBorrowBalanceUSD": "202374996.3134639021898119070753235",
        "timestamp": "1675036777",
        "blockNumber": "25586007"
      },
      {
        "totalDepositBalanceUSD": "498209199.641066428892949922471789",
        "totalBorrowBalanceUSD": "200157913.7700555597097435450959161",
        "timestamp": "1674950346",
        "blockNumber": "25543227"
      },
      {
        "totalDepositBalanceUSD": "502427853.88855880282102109121751",
        "totalBorrowBalanceUSD": "199483293.9619123388939892651947269",
        "timestamp": "1674863973",
        "blockNumber": "25500728"
      },
      {
        "totalDepositBalanceUSD": "494891253.9606747464069804964339653",
        "totalBorrowBalanceUSD": "199349268.3332852120941791032458304",
        "timestamp": "1674777544",
        "blockNumber": "25458317"
      },
      {
        "totalDepositBalanceUSD": "496295649.6946029250640267741627305",
        "totalBorrowBalanceUSD": "199877452.3620126665795096769875217",
        "timestamp": "1674691144",
        "blockNumber": "25415890"
      },
      {
        "totalDepositBalanceUSD": "491875095.3025717048301498387979167",
        "totalBorrowBalanceUSD": "202735340.5337292784936152076958128",
        "timestamp": "1674604764",
        "blockNumber": "25373629"
      },
      {
        "totalDepositBalanceUSD": "487459967.4820482713764745143228018",
        "totalBorrowBalanceUSD": "190506050.3932133016413739133597503",
        "timestamp": "1674518346",
        "blockNumber": "25331322"
      },
      {
        "totalDepositBalanceUSD": "498796803.4206425824077718403734333",
        "totalBorrowBalanceUSD": "200686185.9098441978595578570482",
        "timestamp": "1674431977",
        "blockNumber": "25289189"
      },
      {
        "totalDepositBalanceUSD": "502015596.1983993515662524476053847",
        "totalBorrowBalanceUSD": "199249458.1433943381066576201304743",
        "timestamp": "1674345595",
        "blockNumber": "25246632"
      },
      {
        "totalDepositBalanceUSD": "512359160.9502685346482267694064938",
        "totalBorrowBalanceUSD": "199935224.5165391783675452811040721",
        "timestamp": "1674259192",
        "blockNumber": "25204589"
      },
      {
        "totalDepositBalanceUSD": "495383977.7385446746007632208503213",
        "totalBorrowBalanceUSD": "195874208.3861886359812925682326617",
        "timestamp": "1674172795",
        "blockNumber": "25162087"
      },
      {
        "totalDepositBalanceUSD": "493249035.0849216516147837894987265",
        "totalBorrowBalanceUSD": "200967668.6918926041843200176509949",
        "timestamp": "1674086385",
        "blockNumber": "25120152"
      },
      {
        "totalDepositBalanceUSD": "504486819.9285217472149062062016413",
        "totalBorrowBalanceUSD": "202736894.5796828769288797663539812",
        "timestamp": "1673999603",
        "blockNumber": "25077584"
      },
      {
        "totalDepositBalanceUSD": "499552618.1807378742178927145595033",
        "totalBorrowBalanceUSD": "201124513.0543539800364946432687116",
        "timestamp": "1673913501",
        "blockNumber": "25035525"
      },
      {
        "totalDepositBalanceUSD": "497070006.9819970143402327535170553",
        "totalBorrowBalanceUSD": "197305652.0066604686767666922656949",
        "timestamp": "1673827163",
        "blockNumber": "24993153"
      },
      {
        "totalDepositBalanceUSD": "495302230.8525851593405057438785006",
        "totalBorrowBalanceUSD": "193863972.6346061606039433598181791",
        "timestamp": "1673740794",
        "blockNumber": "24950765"
      },
      {
        "totalDepositBalanceUSD": "465484747.2942016919343620678147016",
        "totalBorrowBalanceUSD": "174082745.8244150880601152122762411",
        "timestamp": "1673653822",
        "blockNumber": "24907290"
      },
      {
        "totalDepositBalanceUSD": "444601977.1831788822894115246231347",
        "totalBorrowBalanceUSD": "171208808.4905948063567945067583241",
        "timestamp": "1673567940",
        "blockNumber": "24864973"
      },
      {
        "totalDepositBalanceUSD": "431337629.6973017020453754145352179",
        "totalBorrowBalanceUSD": "158634924.2856543034900438538177062",
        "timestamp": "1673481588",
        "blockNumber": "24822028"
      },
      {
        "totalDepositBalanceUSD": "414880611.2833174618486914978500517",
        "totalBorrowBalanceUSD": "157970595.6213952726130959257121574",
        "timestamp": "1673395059",
        "blockNumber": "24779714"
      },
      {
        "totalDepositBalanceUSD": "411003562.7404026501844239392008292",
        "totalBorrowBalanceUSD": "154501781.6071683230078942820804669",
        "timestamp": "1673308773",
        "blockNumber": "24737432"
      },
      {
        "totalDepositBalanceUSD": "406455390.8456050285144749338157233",
        "totalBorrowBalanceUSD": "154821184.3324046098564559745806336",
        "timestamp": "1673222179",
        "blockNumber": "24694845"
      },
      {
        "totalDepositBalanceUSD": "407162142.8412585933266128859039766",
        "totalBorrowBalanceUSD": "154528238.4399147525081777174146496",
        "timestamp": "1673135847",
        "blockNumber": "24653403"
      },
      {
        "totalDepositBalanceUSD": "403513473.7041336667650940530532755",
        "totalBorrowBalanceUSD": "152672559.0344576044623185761457213",
        "timestamp": "1673049551",
        "blockNumber": "24611773"
      },
      {
        "totalDepositBalanceUSD": "402017940.8195012932932153539363364",
        "totalBorrowBalanceUSD": "152387721.3804185053308403353745959",
        "timestamp": "1672963179",
        "blockNumber": "24569908"
      },
      {
        "totalDepositBalanceUSD": "393714195.4635653902566857831974171",
        "totalBorrowBalanceUSD": "148659690.921649250265989580084195",
        "timestamp": "1672876795",
        "blockNumber": "24527726"
      },
      {
        "totalDepositBalanceUSD": "390500104.5075721051257628535135411",
        "totalBorrowBalanceUSD": "148074846.2293109763069315115054851",
        "timestamp": "1672790190",
        "blockNumber": "24485320"
      },
      {
        "totalDepositBalanceUSD": "390485211.1803841871735778087771759",
        "totalBorrowBalanceUSD": "148206295.5367107504575968215391374",
        "timestamp": "1672703856",
        "blockNumber": "24443754"
      },
      {
        "totalDepositBalanceUSD": "388290022.8001650690848199513052254",
        "totalBorrowBalanceUSD": "148138313.7042953923195717983990125",
        "timestamp": "1672617585",
        "blockNumber": "24401937"
      },
      {
        "totalDepositBalanceUSD": "389069054.2757417110497825502656169",
        "totalBorrowBalanceUSD": "148221164.9983576820582097360743995",
        "timestamp": "1672531175",
        "blockNumber": "24360257"
      },
      {
        "totalDepositBalanceUSD": "395599465.525881588620160183000975",
        "totalBorrowBalanceUSD": "148044023.3279770298071501544222039",
        "timestamp": "1672444767",
        "blockNumber": "24319111"
      },
      {
        "totalDepositBalanceUSD": "414628731.0513402511005740660857312",
        "totalBorrowBalanceUSD": "166763212.7078628756714464386536993",
        "timestamp": "1672358398",
        "blockNumber": "24277155"
      },
      {
        "totalDepositBalanceUSD": "414863383.3706356207401816316680211",
        "totalBorrowBalanceUSD": "166775961.0843707929991900805508837",
        "timestamp": "1672271981",
        "blockNumber": "24234498"
      },
      {
        "totalDepositBalanceUSD": "421106535.5860462113257694889180148",
        "totalBorrowBalanceUSD": "173046560.3982163576465930962838833",
        "timestamp": "1672185497",
        "blockNumber": "24192281"
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
