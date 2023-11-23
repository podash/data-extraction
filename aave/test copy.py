import json
import csv
from datetime import datetime

json_data = {
  "data": {
    "financialsDailySnapshots": [
      {
        "totalDepositBalanceUSD": "3226065049.118704274950340682630601",
        "totalBorrowBalanceUSD": "1009916164.681115600481717675703603",
        "timestamp": "1700653367",
        "blockNumber": "18627050"
      },
      {
        "totalDepositBalanceUSD": "3181449429.860225406939879730915011",
        "totalBorrowBalanceUSD": "999637365.3104989482044910308948028",
        "timestamp": "1700611091",
        "blockNumber": "18623564"
      },
      {
        "totalDepositBalanceUSD": "3263191953.864897865769778093261307",
        "totalBorrowBalanceUSD": "1018326747.432227542576416192152212",
        "timestamp": "1700524043",
        "blockNumber": "18616367"
      },
      {
        "totalDepositBalanceUSD": "3216581716.316181388579130259955906",
        "totalBorrowBalanceUSD": "1014893709.742644441299337003830973",
        "timestamp": "1700438351",
        "blockNumber": "18609279"
      },
      {
        "totalDepositBalanceUSD": "3174972786.138509575404517854757439",
        "totalBorrowBalanceUSD": "1002189241.012575310996175606226705",
        "timestamp": "1700351159",
        "blockNumber": "18602075"
      },
      {
        "totalDepositBalanceUSD": "3171559526.149940598666447019655013",
        "totalBorrowBalanceUSD": "1004105985.190373068317881158714772",
        "timestamp": "1700265467",
        "blockNumber": "18595019"
      },
      {
        "totalDepositBalanceUSD": "3186049685.274653979366355201448248",
        "totalBorrowBalanceUSD": "1005661979.492582329618247934528987",
        "timestamp": "1700178551",
        "blockNumber": "18587828"
      },
      {
        "totalDepositBalanceUSD": "3392435636.638267488269709790932713",
        "totalBorrowBalanceUSD": "1054621105.256654688359914134084564",
        "timestamp": "1700092547",
        "blockNumber": "18580705"
      },
      {
        "totalDepositBalanceUSD": "3347138746.689061312108912314501635",
        "totalBorrowBalanceUSD": "1069811544.887590573009135764845885",
        "timestamp": "1700006255",
        "blockNumber": "18573566"
      },
      {
        "totalDepositBalanceUSD": "3487215632.606618356046495200552031",
        "totalBorrowBalanceUSD": "1096675085.333047745500828165909282",
        "timestamp": "1699919939",
        "blockNumber": "18566413"
      },
      {
        "totalDepositBalanceUSD": "3376659868.18876092208830452986651",
        "totalBorrowBalanceUSD": "1071963831.803064228032492765716424",
        "timestamp": "1699119011",
        "blockNumber": "18500169"
      },
      {
        "totalDepositBalanceUSD": "3370908852.174356351249167815156531",
        "totalBorrowBalanceUSD": "1069715429.111373792808747319891612",
        "timestamp": "1699055903",
        "blockNumber": "18494955"
      },
      {
        "totalDepositBalanceUSD": "3385867871.609626887419484611291516",
        "totalBorrowBalanceUSD": "1082797377.853554739909609663043842",
        "timestamp": "1698969443",
        "blockNumber": "18487811"
      },
      {
        "totalDepositBalanceUSD": "3456369966.701709863693671677593061",
        "totalBorrowBalanceUSD": "1104379629.724748749576915781165483",
        "timestamp": "1698882983",
        "blockNumber": "18480675"
      },
      {
        "totalDepositBalanceUSD": "3414904603.729896570109278314014978",
        "totalBorrowBalanceUSD": "1100113404.032850880599469388665282",
        "timestamp": "1698796727",
        "blockNumber": "18473536"
      },
      {
        "totalDepositBalanceUSD": "3405006000.611491692542106503927591",
        "totalBorrowBalanceUSD": "1106164145.351039791903165687684741",
        "timestamp": "1698710171",
        "blockNumber": "18466388"
      },
      {
        "totalDepositBalanceUSD": "3415071852.03888548025873831998326",
        "totalBorrowBalanceUSD": "1102088841.494641238592701719578905",
        "timestamp": "1698623651",
        "blockNumber": "18459239"
      },
      {
        "totalDepositBalanceUSD": "3389812827.468931001380511798546188",
        "totalBorrowBalanceUSD": "1097517938.766408901819162992608869",
        "timestamp": "1698536999",
        "blockNumber": "18452078"
      },
      {
        "totalDepositBalanceUSD": "3366544550.562489089490039468995516",
        "totalBorrowBalanceUSD": "1092669942.797230230666525577382771",
        "timestamp": "1698451055",
        "blockNumber": "18444970"
      },
      {
        "totalDepositBalanceUSD": "3395642257.015102256508158905964659",
        "totalBorrowBalanceUSD": "1102347051.41122175925921322731371",
        "timestamp": "1698364799",
        "blockNumber": "18437825"
      },
      {
        "totalDepositBalanceUSD": "3411976856.358263858999030253546322",
        "totalBorrowBalanceUSD": "1106445481.283833459201489744414585",
        "timestamp": "1698277775",
        "blockNumber": "18430625"
      },
      {
        "totalDepositBalanceUSD": "3376981505.87230494817448284041072",
        "totalBorrowBalanceUSD": "1109884086.931753269277068011673516",
        "timestamp": "1698191927",
        "blockNumber": "18423543"
      },
      {
        "totalDepositBalanceUSD": "3357757978.495991409705937906977187",
        "totalBorrowBalanceUSD": "1101450030.646850663102657027662325",
        "timestamp": "1698105551",
        "blockNumber": "18416402"
      },
      {
        "totalDepositBalanceUSD": "3175809579.818197071490906877999066",
        "totalBorrowBalanceUSD": "1076940044.756977477504807744579443",
        "timestamp": "1698019103",
        "blockNumber": "18409257"
      },
      {
        "totalDepositBalanceUSD": "3147968878.409934464246832773432194",
        "totalBorrowBalanceUSD": "1070803066.606667217364233396859619",
        "timestamp": "1697932787",
        "blockNumber": "18402120"
      },
      {
        "totalDepositBalanceUSD": "3088387792.851319763213276769221177",
        "totalBorrowBalanceUSD": "1060125973.683231832705855453974044",
        "timestamp": "1697846207",
        "blockNumber": "18394958"
      },
      {
        "totalDepositBalanceUSD": "3019546957.057790133623793450313223",
        "totalBorrowBalanceUSD": "1048685229.066834963232876148263232",
        "timestamp": "1697758547",
        "blockNumber": "18387698"
      },
      {
        "totalDepositBalanceUSD": "2999241371.012699181198143515386567",
        "totalBorrowBalanceUSD": "1030750998.229516172978519956010448",
        "timestamp": "1697673083",
        "blockNumber": "18380628"
      },
      {
        "totalDepositBalanceUSD": "3007707077.914613403194578484044718",
        "totalBorrowBalanceUSD": "1029187459.384133849837938084727581",
        "timestamp": "1697587199",
        "blockNumber": "18373528"
      },
      {
        "totalDepositBalanceUSD": "3105101311.358445324813603659203168",
        "totalBorrowBalanceUSD": "1081483345.749455061137229068208309",
        "timestamp": "1697500751",
        "blockNumber": "18366374"
      },
      {
        "totalDepositBalanceUSD": "3069455048.385181621253918751924469",
        "totalBorrowBalanceUSD": "1070190340.765906357203584533877378",
        "timestamp": "1697414375",
        "blockNumber": "18359210"
      },
      {
        "totalDepositBalanceUSD": "3056453356.314833745540857884183189",
        "totalBorrowBalanceUSD": "1065674417.968336609710174692800884",
        "timestamp": "1697327519",
        "blockNumber": "18352018"
      },
      {
        "totalDepositBalanceUSD": "3064555294.910872706838111146363203",
        "totalBorrowBalanceUSD": "1064687622.460484209478348796041208",
        "timestamp": "1697241011",
        "blockNumber": "18344857"
      },
      {
        "totalDepositBalanceUSD": "3031104135.286281750979902075746178",
        "totalBorrowBalanceUSD": "1059552304.782711095468878926319916",
        "timestamp": "1697154875",
        "blockNumber": "18337741"
      },
      {
        "totalDepositBalanceUSD": "3120581337.015399836604839200769426",
        "totalBorrowBalanceUSD": "1057606305.836529518887681790882636",
        "timestamp": "1697068547",
        "blockNumber": "18330603"
      },
      {
        "totalDepositBalanceUSD": "3129510551.41952074150038957252417",
        "totalBorrowBalanceUSD": "1053810269.129183099037069017173438",
        "timestamp": "1696982219",
        "blockNumber": "18323474"
      },
      {
        "totalDepositBalanceUSD": "3138190215.563338692387895499052831",
        "totalBorrowBalanceUSD": "1055007164.832448375984361129479543",
        "timestamp": "1696895747",
        "blockNumber": "18316318"
      },
      {
        "totalDepositBalanceUSD": "3229951271.816925155415242253881288",
        "totalBorrowBalanceUSD": "1082411706.124210992155276584442753",
        "timestamp": "1696808447",
        "blockNumber": "18309101"
      },
      {
        "totalDepositBalanceUSD": "3224290884.340570418566263846330619",
        "totalBorrowBalanceUSD": "1080087862.421044110989413204862666",
        "timestamp": "1696723019",
        "blockNumber": "18302033"
      },
      {
        "totalDepositBalanceUSD": "3244107008.248023771273621360007208",
        "totalBorrowBalanceUSD": "1086410683.18296848091507900782208",
        "timestamp": "1696636391",
        "blockNumber": "18294860"
      },
      {
        "totalDepositBalanceUSD": "3204741346.732420205743882450955021",
        "totalBorrowBalanceUSD": "1079582212.258826239822862814411533",
        "timestamp": "1696549331",
        "blockNumber": "18287654"
      },
      {
        "totalDepositBalanceUSD": "3257705909.227706030157691716162705",
        "totalBorrowBalanceUSD": "1091984750.126062252875523253721071",
        "timestamp": "1696463843",
        "blockNumber": "18280580"
      },
      {
        "totalDepositBalanceUSD": "3261332833.776688594481620638986899",
        "totalBorrowBalanceUSD": "1089414641.558829105575186429063109",
        "timestamp": "1696377395",
        "blockNumber": "18273419"
      },
      {
        "totalDepositBalanceUSD": "3262838532.25868023640937584016812",
        "totalBorrowBalanceUSD": "1094327363.06654961581449469383809",
        "timestamp": "1696290179",
        "blockNumber": "18266207"
      },
      {
        "totalDepositBalanceUSD": "3333819835.531351538173266476850967",
        "totalBorrowBalanceUSD": "1096886260.432092880648959676379255",
        "timestamp": "1696204799",
        "blockNumber": "18259123"
      },
      {
        "totalDepositBalanceUSD": "3266117284.21893696347442073841337",
        "totalBorrowBalanceUSD": "1090279635.452945220610353441135049",
        "timestamp": "1696118279",
        "blockNumber": "18251954"
      },
      {
        "totalDepositBalanceUSD": "3303611877.378162612540262330728833",
        "totalBorrowBalanceUSD": "1103167664.310330922290605458838247",
        "timestamp": "1696031447",
        "blockNumber": "18244758"
      },
      {
        "totalDepositBalanceUSD": "3282898752.379282841565779401189719",
        "totalBorrowBalanceUSD": "1111567924.783418582023594376504124",
        "timestamp": "1695945335",
        "blockNumber": "18237643"
      },
      {
        "totalDepositBalanceUSD": "3224618394.204496832785175372551758",
        "totalBorrowBalanceUSD": "1099833028.521608306628118990397906",
        "timestamp": "1695857627",
        "blockNumber": "18230399"
      },
      {
        "totalDepositBalanceUSD": "3200421622.629984140042813650444306",
        "totalBorrowBalanceUSD": "1096481597.489178717784570055787646",
        "timestamp": "1695772187",
        "blockNumber": "18223335"
      },
      {
        "totalDepositBalanceUSD": "3219632043.715741932634590971588499",
        "totalBorrowBalanceUSD": "1099967779.166638875666860243493574",
        "timestamp": "1695685787",
        "blockNumber": "18216187"
      },
      {
        "totalDepositBalanceUSD": "3265907394.632600544911009947409786",
        "totalBorrowBalanceUSD": "1114335717.000143277831692410200832",
        "timestamp": "1695599627",
        "blockNumber": "18209059"
      },
      {
        "totalDepositBalanceUSD": "3260289324.674739363913231212907886",
        "totalBorrowBalanceUSD": "1112029175.971599823609435006926386",
        "timestamp": "1695513071",
        "blockNumber": "18201907"
      },
      {
        "totalDepositBalanceUSD": "3262206249.792901644817104579103577",
        "totalBorrowBalanceUSD": "1112153825.342401296290309771707741",
        "timestamp": "1695427175",
        "blockNumber": "18194806"
      },
      {
        "totalDepositBalanceUSD": "3270003295.937486330473430861315204",
        "totalBorrowBalanceUSD": "1123716732.727957909115330703807216",
        "timestamp": "1695340319",
        "blockNumber": "18187641"
      },
      {
        "totalDepositBalanceUSD": "3320632511.935515172877269736764343",
        "totalBorrowBalanceUSD": "1134802692.444754265844854802941565",
        "timestamp": "1695254327",
        "blockNumber": "18180535"
      },
      {
        "totalDepositBalanceUSD": "3346606848.230058753121387391400746",
        "totalBorrowBalanceUSD": "1147457873.482610669485044726063639",
        "timestamp": "1695167759",
        "blockNumber": "18173371"
      },
      {
        "totalDepositBalanceUSD": "3330361259.257782883901739642560544",
        "totalBorrowBalanceUSD": "1150540571.516014373704848267052787",
        "timestamp": "1695081443",
        "blockNumber": "18166241"
      },
      {
        "totalDepositBalanceUSD": "3295271389.245886395872856115997744",
        "totalBorrowBalanceUSD": "1146124670.695545548012879453577888",
        "timestamp": "1694995019",
        "blockNumber": "18159127"
      },
      {
        "totalDepositBalanceUSD": "3315464075.0427796510081634964315",
        "totalBorrowBalanceUSD": "1115780034.839521162121921653513831",
        "timestamp": "1694908427",
        "blockNumber": "18152070"
      },
      {
        "totalDepositBalanceUSD": "3302557279.023792039530266647242192",
        "totalBorrowBalanceUSD": "1112880235.519771276108249562711001",
        "timestamp": "1694821643",
        "blockNumber": "18144956"
      },
      {
        "totalDepositBalanceUSD": "3316249447.519576701794894210803693",
        "totalBorrowBalanceUSD": "1118324543.506654162310076191276332",
        "timestamp": "1694735627",
        "blockNumber": "18137897"
      },
      {
        "totalDepositBalanceUSD": "3260263885.795967485380128271379844",
        "totalBorrowBalanceUSD": "1103151484.379792568836041373712314",
        "timestamp": "1694649503",
        "blockNumber": "18130800"
      },
      {
        "totalDepositBalanceUSD": "3258922970.810702475386659489017214",
        "totalBorrowBalanceUSD": "1098633414.050050666760401047367989",
        "timestamp": "1694563163",
        "blockNumber": "18123674"
      },
      {
        "totalDepositBalanceUSD": "3197558021.441988387807935673320947",
        "totalBorrowBalanceUSD": "1088283612.013127522954224116513865",
        "timestamp": "1694476295",
        "blockNumber": "18116501"
      },
      {
        "totalDepositBalanceUSD": "3295441964.248100750414892953759972",
        "totalBorrowBalanceUSD": "1100428405.619016513706878307831019",
        "timestamp": "1694389907",
        "blockNumber": "18109361"
      },
      {
        "totalDepositBalanceUSD": "3332670263.318279730444140864461015",
        "totalBorrowBalanceUSD": "1114760661.066155122741914353723903",
        "timestamp": "1694302691",
        "blockNumber": "18102156"
      },
      {
        "totalDepositBalanceUSD": "3319801820.142878883474774670949787",
        "totalBorrowBalanceUSD": "1115101636.924509841769143751829998",
        "timestamp": "1694216519",
        "blockNumber": "18095036"
      },
      {
        "totalDepositBalanceUSD": "3362313649.793616834822443512757873",
        "totalBorrowBalanceUSD": "1123933920.348478686280834003941501",
        "timestamp": "1694131175",
        "blockNumber": "18087984"
      },
      {
        "totalDepositBalanceUSD": "3329353677.591042119337248863553082",
        "totalBorrowBalanceUSD": "1115603380.707530467934571248825044",
        "timestamp": "1694044235",
        "blockNumber": "18080788"
      },
      {
        "totalDepositBalanceUSD": "3332863509.09145987276844197148985",
        "totalBorrowBalanceUSD": "1113047036.495668527860813120204956",
        "timestamp": "1693958087",
        "blockNumber": "18073675"
      },
      {
        "totalDepositBalanceUSD": "3307524716.360411033995267689833517",
        "totalBorrowBalanceUSD": "1112441516.334659972020661641837673",
        "timestamp": "1693871891",
        "blockNumber": "18066551"
      },
      {
        "totalDepositBalanceUSD": "3339898526.784772993226162484135223",
        "totalBorrowBalanceUSD": "1114769804.162671855892714514571735",
        "timestamp": "1693785371",
        "blockNumber": "18059379"
      },
      {
        "totalDepositBalanceUSD": "3330969414.544272013441264314406513",
        "totalBorrowBalanceUSD": "1113846664.229356641432438589367753",
        "timestamp": "1693699175",
        "blockNumber": "18052251"
      },
      {
        "totalDepositBalanceUSD": "3301185415.702546845123822520348993",
        "totalBorrowBalanceUSD": "1102435239.77391381665037236649404",
        "timestamp": "1693612595",
        "blockNumber": "18045112"
      },
      {
        "totalDepositBalanceUSD": "3359521200.218554852615066125411445",
        "totalBorrowBalanceUSD": "1120407028.914358788585058399430617",
        "timestamp": "1693526183",
        "blockNumber": "18037969"
      },
      {
        "totalDepositBalanceUSD": "3440848134.388088566204822758408609",
        "totalBorrowBalanceUSD": "1136607924.679656783589114655128193",
        "timestamp": "1693439663",
        "blockNumber": "18030813"
      },
      {
        "totalDepositBalanceUSD": "3509907446.634037941875401487963541",
        "totalBorrowBalanceUSD": "1148953427.784494223054982983461443",
        "timestamp": "1693353383",
        "blockNumber": "18023685"
      },
      {
        "totalDepositBalanceUSD": "3457181054.818719961383839899387525",
        "totalBorrowBalanceUSD": "1142532826.057564086405129156012097",
        "timestamp": "1693266347",
        "blockNumber": "18016502"
      },
      {
        "totalDepositBalanceUSD": "3459488982.846779465544576705266119",
        "totalBorrowBalanceUSD": "1152870546.312610285658060911532682",
        "timestamp": "1693180391",
        "blockNumber": "18009392"
      },
      {
        "totalDepositBalanceUSD": "3434049328.85547852510320848513609",
        "totalBorrowBalanceUSD": "1145792568.538480294955396241645381",
        "timestamp": "1693093679",
        "blockNumber": "18002224"
      },
      {
        "totalDepositBalanceUSD": "3441259667.015954314291637917867989",
        "totalBorrowBalanceUSD": "1144773686.598543611531992897050969",
        "timestamp": "1693007351",
        "blockNumber": "17995085"
      },
      {
        "totalDepositBalanceUSD": "3449648053.781146650266104539470685",
        "totalBorrowBalanceUSD": "1149204107.331492571757425148051795",
        "timestamp": "1692921467",
        "blockNumber": "17987983"
      },
      {
        "totalDepositBalanceUSD": "3493455948.930910293643283157627296",
        "totalBorrowBalanceUSD": "1159304298.168716010585053992309262",
        "timestamp": "1692834023",
        "blockNumber": "17980751"
      },
      {
        "totalDepositBalanceUSD": "3429467989.167933929692884271292653",
        "totalBorrowBalanceUSD": "1142807317.916963360505346205599824",
        "timestamp": "1692748487",
        "blockNumber": "17973665"
      },
      {
        "totalDepositBalanceUSD": "3505828599.110156674376409848972305",
        "totalBorrowBalanceUSD": "1155366107.209748083667379990145324",
        "timestamp": "1692661631",
        "blockNumber": "17966474"
      },
      {
        "totalDepositBalanceUSD": "3528278011.518244618200152765708305",
        "totalBorrowBalanceUSD": "1153879944.421166298472914018687375",
        "timestamp": "1692575039",
        "blockNumber": "17959313"
      },
      {
        "totalDepositBalanceUSD": "3522290397.891397964088677475296432",
        "totalBorrowBalanceUSD": "1152973765.740807632840882739919153",
        "timestamp": "1692488927",
        "blockNumber": "17952195"
      },
      {
        "totalDepositBalanceUSD": "3534840552.668197170181508269723378",
        "totalBorrowBalanceUSD": "1156818166.356523123646441278705263",
        "timestamp": "1692402923",
        "blockNumber": "17945085"
      },
      {
        "totalDepositBalanceUSD": "3679878274.100382789683077689687481",
        "totalBorrowBalanceUSD": "1247646343.273452264517786680313389",
        "timestamp": "1692316799",
        "blockNumber": "17937967"
      },
      {
        "totalDepositBalanceUSD": "3822410646.490844553914270418321129",
        "totalBorrowBalanceUSD": "1273253267.774030246223044296863323",
        "timestamp": "1692229379",
        "blockNumber": "17930742"
      },
      {
        "totalDepositBalanceUSD": "3833864584.921815907474850329813695",
        "totalBorrowBalanceUSD": "1278782805.673034161476381528048994",
        "timestamp": "1692143639",
        "blockNumber": "17923645"
      },
      {
        "totalDepositBalanceUSD": "3918549356.571931848670733240501178",
        "totalBorrowBalanceUSD": "1290140540.636882748532275799931905",
        "timestamp": "1692057395",
        "blockNumber": "17916508"
      },
      {
        "totalDepositBalanceUSD": "3937328683.520864775627100049833713",
        "totalBorrowBalanceUSD": "1300443517.326938977009366033587203",
        "timestamp": "1691970911",
        "blockNumber": "17909349"
      },
      {
        "totalDepositBalanceUSD": "3974682515.494002133499453732483508",
        "totalBorrowBalanceUSD": "1306331406.043085968490768627988164",
        "timestamp": "1691883971",
        "blockNumber": "17902147"
      },
      {
        "totalDepositBalanceUSD": "4078890345.594051065156371435836707",
        "totalBorrowBalanceUSD": "1356836860.97951501580711133198086",
        "timestamp": "1691797943",
        "blockNumber": "17895032"
      },
      {
        "totalDepositBalanceUSD": "3922110621.907549682629889412948638",
        "totalBorrowBalanceUSD": "1298125379.13302316276091767744253",
        "timestamp": "1691711711",
        "blockNumber": "17887898"
      },
      {
        "totalDepositBalanceUSD": "3946757602.063878571348311657621002",
        "totalBorrowBalanceUSD": "1303389317.17648810706452364854318",
        "timestamp": "1691625599",
        "blockNumber": "17880776"
      },
      {
        "totalDepositBalanceUSD": "3969514687.698463557674437167463649",
        "totalBorrowBalanceUSD": "1301872327.699056796093427081388354",
        "timestamp": "1691538683",
        "blockNumber": "17873587"
      },
      {
        "totalDepositBalanceUSD": "3926521117.694722755712829093716134",
        "totalBorrowBalanceUSD": "1293877911.239216992789289972158346",
        "timestamp": "1691452307",
        "blockNumber": "17866446"
      },
      {
        "totalDepositBalanceUSD": "3989913922.065664284190464020906381",
        "totalBorrowBalanceUSD": "1312531578.543983679626794721602873",
        "timestamp": "1691365619",
        "blockNumber": "17859281"
      },
      {
        "totalDepositBalanceUSD": "4014153803.247152906126096951769793",
        "totalBorrowBalanceUSD": "1321878095.156189820023345149668601",
        "timestamp": "1691279555",
        "blockNumber": "17852171"
      },
      {
        "totalDepositBalanceUSD": "4020865954.034340158335782706542116",
        "totalBorrowBalanceUSD": "1328643229.241940496943067655444447",
        "timestamp": "1691192783",
        "blockNumber": "17844984"
      },
      {
        "totalDepositBalanceUSD": "4065583919.372325154183939205073138",
        "totalBorrowBalanceUSD": "1330344728.118655355534780074484322",
        "timestamp": "1691106923",
        "blockNumber": "17837877"
      },
      {
        "totalDepositBalanceUSD": "4138174037.181259675119993439079218",
        "totalBorrowBalanceUSD": "1350160293.77357383372685018825979",
        "timestamp": "1691020343",
        "blockNumber": "17830717"
      },
      {
        "totalDepositBalanceUSD": "4293137048.057799655499378179126585",
        "totalBorrowBalanceUSD": "1417049904.345186808920124412544464",
        "timestamp": "1690934303",
        "blockNumber": "17823586"
      },
      {
        "totalDepositBalanceUSD": "4600270688.287722694453184779237931",
        "totalBorrowBalanceUSD": "1482967904.939171223711472518902707",
        "timestamp": "1690847999",
        "blockNumber": "17816433"
      },
      {
        "totalDepositBalanceUSD": "4895370395.176807921760002746961754",
        "totalBorrowBalanceUSD": "1615298831.313736777240559595364679",
        "timestamp": "1690761443",
        "blockNumber": "17809261"
      },
      {
        "totalDepositBalanceUSD": "5241360541.576745374978395376793568",
        "totalBorrowBalanceUSD": "1663809193.41463594740301428596502",
        "timestamp": "1690675127",
        "blockNumber": "17802124"
      },
      {
        "totalDepositBalanceUSD": "5266427838.628430284957627776487951",
        "totalBorrowBalanceUSD": "1669740950.727310657020329347932441",
        "timestamp": "1690588439",
        "blockNumber": "17794951"
      },
      {
        "totalDepositBalanceUSD": "5201491507.345781135564824285812659",
        "totalBorrowBalanceUSD": "1647857942.614785326401465076671697",
        "timestamp": "1690502111",
        "blockNumber": "17787813"
      },
      {
        "totalDepositBalanceUSD": "5206023563.51768039695617622499142",
        "totalBorrowBalanceUSD": "1644887349.26736941597588189719021",
        "timestamp": "1690415075",
        "blockNumber": "17780614"
      },
      {
        "totalDepositBalanceUSD": "5193113597.76939277401685749830151",
        "totalBorrowBalanceUSD": "1639982234.283134403843780019257733",
        "timestamp": "1690329587",
        "blockNumber": "17773537"
      },
      {
        "totalDepositBalanceUSD": "5179370777.312234194721034158439009",
        "totalBorrowBalanceUSD": "1639965283.17313896292712081644817",
        "timestamp": "1690242191",
        "blockNumber": "17766315"
      },
      {
        "totalDepositBalanceUSD": "5279101214.673597013871546621274332",
        "totalBorrowBalanceUSD": "1659031079.585747582925664097281484",
        "timestamp": "1690156271",
        "blockNumber": "17759206"
      },
      {
        "totalDepositBalanceUSD": "5224500369.465887133452472890744162",
        "totalBorrowBalanceUSD": "1652212852.671824057713635628304269",
        "timestamp": "1690070039",
        "blockNumber": "17752071"
      },
      {
        "totalDepositBalanceUSD": "5251904086.632292289265382366962164",
        "totalBorrowBalanceUSD": "1666112698.673568525359767594642496",
        "timestamp": "1689982691",
        "blockNumber": "17744842"
      },
      {
        "totalDepositBalanceUSD": "5238980444.673014257857751119700117",
        "totalBorrowBalanceUSD": "1675021483.076193812119032249389019",
        "timestamp": "1689896507",
        "blockNumber": "17737719"
      },
      {
        "totalDepositBalanceUSD": "5236300124.773500674014547287454382",
        "totalBorrowBalanceUSD": "1668068236.218074384367257964159056",
        "timestamp": "1689811175",
        "blockNumber": "17730664"
      },
      {
        "totalDepositBalanceUSD": "5263470493.758187708407418542011601",
        "totalBorrowBalanceUSD": "1655866467.995467545122603183485696",
        "timestamp": "1689724595",
        "blockNumber": "17723520"
      },
      {
        "totalDepositBalanceUSD": "5340876696.444512498553432606129501",
        "totalBorrowBalanceUSD": "1658243150.725890574675504415425553",
        "timestamp": "1689638135",
        "blockNumber": "17716387"
      },
      {
        "totalDepositBalanceUSD": "5511922428.04362110420702326584892",
        "totalBorrowBalanceUSD": "1692070267.786177784259407686599436",
        "timestamp": "1689551579",
        "blockNumber": "17709238"
      },
      {
        "totalDepositBalanceUSD": "5558405659.650982153098382726418491",
        "totalBorrowBalanceUSD": "1700688043.985817653941967678750879",
        "timestamp": "1689465191",
        "blockNumber": "17702136"
      },
      {
        "totalDepositBalanceUSD": "5440927624.698813448381849262743841",
        "totalBorrowBalanceUSD": "1701028966.255903242054629334199876",
        "timestamp": "1689378839",
        "blockNumber": "17695081"
      },
      {
        "totalDepositBalanceUSD": "5545007183.880845409735437665202609",
        "totalBorrowBalanceUSD": "1690327947.77408935043230389822171",
        "timestamp": "1689292775",
        "blockNumber": "17687999"
      },
      {
        "totalDepositBalanceUSD": "5377199930.105953819004749806627454",
        "totalBorrowBalanceUSD": "1671795483.266266967055342992845382",
        "timestamp": "1689206207",
        "blockNumber": "17680881"
      },
      {
        "totalDepositBalanceUSD": "5366693143.920008501272124956110297",
        "totalBorrowBalanceUSD": "1671645073.878910266885464322582499",
        "timestamp": "1689119459",
        "blockNumber": "17673743"
      },
      {
        "totalDepositBalanceUSD": "5343462100.386436556327611833358264",
        "totalBorrowBalanceUSD": "1661770694.492022139952566679027699",
        "timestamp": "1689033035",
        "blockNumber": "17666628"
      },
      {
        "totalDepositBalanceUSD": "5352561432.210592881436458876356718",
        "totalBorrowBalanceUSD": "1657601506.612173350951427692115121",
        "timestamp": "1688947127",
        "blockNumber": "17659565"
      },
      {
        "totalDepositBalanceUSD": "5345074236.944215959342408785203801",
        "totalBorrowBalanceUSD": "1660487754.467451690555490771203878",
        "timestamp": "1688860547",
        "blockNumber": "17652438"
      },
      {
        "totalDepositBalanceUSD": "5351096316.93389168846012076827116",
        "totalBorrowBalanceUSD": "1660536318.472434157679031048577084",
        "timestamp": "1688774159",
        "blockNumber": "17645326"
      },
      {
        "totalDepositBalanceUSD": "5319635093.78850549313813801983163",
        "totalBorrowBalanceUSD": "1661046216.914463432733221365050397",
        "timestamp": "1688687939",
        "blockNumber": "17638219"
      },
      {
        "totalDepositBalanceUSD": "5434497608.46671830980549338851571",
        "totalBorrowBalanceUSD": "1669781416.080083625001641426434098",
        "timestamp": "1688600711",
        "blockNumber": "17631033"
      },
      {
        "totalDepositBalanceUSD": "5454663903.91896020412842169723157",
        "totalBorrowBalanceUSD": "1689109321.337631437209661336816323",
        "timestamp": "1688515175",
        "blockNumber": "17623971"
      },
      {
        "totalDepositBalanceUSD": "5476637556.039571156809792338993439",
        "totalBorrowBalanceUSD": "1706273165.257672728480524123523477",
        "timestamp": "1688428607",
        "blockNumber": "17616845"
      },
      {
        "totalDepositBalanceUSD": "5412857669.336182090379111175323787",
        "totalBorrowBalanceUSD": "1686150174.288377149071368764037456",
        "timestamp": "1688342315",
        "blockNumber": "17609742"
      },
      {
        "totalDepositBalanceUSD": "5381551188.413331658041087707453787",
        "totalBorrowBalanceUSD": "1754584751.710179172876144054919264",
        "timestamp": "1688255867",
        "blockNumber": "17602608"
      },
      {
        "totalDepositBalanceUSD": "5426951031.566437522361179527590796",
        "totalBorrowBalanceUSD": "1766195362.311675883812015473678517",
        "timestamp": "1688169503",
        "blockNumber": "17595501"
      },
      {
        "totalDepositBalanceUSD": "5329967387.216629789164870927011227",
        "totalBorrowBalanceUSD": "1751864326.319721579046063135827951",
        "timestamp": "1688082011",
        "blockNumber": "17588287"
      },
      {
        "totalDepositBalanceUSD": "5259875875.701700040334123964702776",
        "totalBorrowBalanceUSD": "1746843549.206602808482689655076604",
        "timestamp": "1687996595",
        "blockNumber": "17581236"
      },
      {
        "totalDepositBalanceUSD": "5381953568.65574067857530535786028",
        "totalBorrowBalanceUSD": "1764129793.016553999475355982649286",
        "timestamp": "1687910387",
        "blockNumber": "17574108"
      },
      {
        "totalDepositBalanceUSD": "5258352788.394263381919712665807082",
        "totalBorrowBalanceUSD": "1743914769.040018257325171426871706",
        "timestamp": "1687823507",
        "blockNumber": "17566971"
      },
      {
        "totalDepositBalanceUSD": "5342862028.054044666839080634797684",
        "totalBorrowBalanceUSD": "1756002917.543879964740711178426563",
        "timestamp": "1687737443",
        "blockNumber": "17559894"
      },
      {
        "totalDepositBalanceUSD": "5265295141.414984632065004559131065",
        "totalBorrowBalanceUSD": "1738388894.545136374630982455076704",
        "timestamp": "1687650911",
        "blockNumber": "17552774"
      },
      {
        "totalDepositBalanceUSD": "5300630945.670552753188070335402198",
        "totalBorrowBalanceUSD": "1739060239.212209055132399462507413",
        "timestamp": "1687564631",
        "blockNumber": "17545674"
      },
      {
        "totalDepositBalanceUSD": "5199060641.898763449299362206863603",
        "totalBorrowBalanceUSD": "1701097242.611105023973986956001397",
        "timestamp": "1687478219",
        "blockNumber": "17538562"
      },
      {
        "totalDepositBalanceUSD": "5196078496.238481541885467563596467",
        "totalBorrowBalanceUSD": "1692634034.774783537002756581902223",
        "timestamp": "1687391939",
        "blockNumber": "17531458"
      },
      {
        "totalDepositBalanceUSD": "4988208224.837021988373037281352948",
        "totalBorrowBalanceUSD": "1632087584.208142617927476877983341",
        "timestamp": "1687305479",
        "blockNumber": "17524318"
      },
      {
        "totalDepositBalanceUSD": "4893817892.439613493359149683728094",
        "totalBorrowBalanceUSD": "1635725075.275864604473814751704808",
        "timestamp": "1687218827",
        "blockNumber": "17517177"
      },
      {
        "totalDepositBalanceUSD": "4920059397.435302866226039932505858",
        "totalBorrowBalanceUSD": "1651292976.260329866058132423049593",
        "timestamp": "1687132439",
        "blockNumber": "17510057"
      },
      {
        "totalDepositBalanceUSD": "4893427150.668576341488425278978472",
        "totalBorrowBalanceUSD": "1658579956.961876368876545610586212",
        "timestamp": "1687045547",
        "blockNumber": "17502890"
      },
      {
        "totalDepositBalanceUSD": "4936266950.776540560904601529246471",
        "totalBorrowBalanceUSD": "1686620424.810594557606775493805598",
        "timestamp": "1686959843",
        "blockNumber": "17495806"
      },
      {
        "totalDepositBalanceUSD": "4797510614.557646252937298842934364",
        "totalBorrowBalanceUSD": "1657799948.15377085777842981846715",
        "timestamp": "1686873359",
        "blockNumber": "17488679"
      },
      {
        "totalDepositBalanceUSD": "4657800079.351634666494698890423235",
        "totalBorrowBalanceUSD": "1591717818.026937007650995147030121",
        "timestamp": "1686787175",
        "blockNumber": "17481590"
      },
      {
        "totalDepositBalanceUSD": "4946262958.230871376288284154692709",
        "totalBorrowBalanceUSD": "1625034008.926075924201701011439582",
        "timestamp": "1686700391",
        "blockNumber": "17474462"
      },
      {
        "totalDepositBalanceUSD": "4957694924.863870181462965486074669",
        "totalBorrowBalanceUSD": "1619924371.691398832702097541016888",
        "timestamp": "1686614063",
        "blockNumber": "17467356"
      },
      {
        "totalDepositBalanceUSD": "5042614958.130696657214628733433427",
        "totalBorrowBalanceUSD": "1671272281.623355694411418147675712",
        "timestamp": "1686527771",
        "blockNumber": "17460261"
      },
      {
        "totalDepositBalanceUSD": "4948340682.919575634974933526640804",
        "totalBorrowBalanceUSD": "1640806425.416582257915427395225505",
        "timestamp": "1686441587",
        "blockNumber": "17453184"
      },
      {
        "totalDepositBalanceUSD": "5181674415.682302651499838305067049",
        "totalBorrowBalanceUSD": "1710337749.197784981746890994576046",
        "timestamp": "1686355175",
        "blockNumber": "17446078"
      },
      {
        "totalDepositBalanceUSD": "5296485966.101607172660027393818235",
        "totalBorrowBalanceUSD": "1748759524.105689200272233421421952",
        "timestamp": "1686268031",
        "blockNumber": "17438917"
      },
      {
        "totalDepositBalanceUSD": "5279879609.518696583639976258940758",
        "totalBorrowBalanceUSD": "1780546946.938106112519989480091236",
        "timestamp": "1686182303",
        "blockNumber": "17431895"
      },
      {
        "totalDepositBalanceUSD": "5407670721.174686806154293898721662",
        "totalBorrowBalanceUSD": "1813434351.418168477961741083095122",
        "timestamp": "1686095387",
        "blockNumber": "17424763"
      },
      {
        "totalDepositBalanceUSD": "5224183336.751645359319652987250937",
        "totalBorrowBalanceUSD": "1753197731.027214372343755844402139",
        "timestamp": "1686009551",
        "blockNumber": "17417715"
      },
      {
        "totalDepositBalanceUSD": "5447895994.458786769314904030854077",
        "totalBorrowBalanceUSD": "1798045723.213734817026923931142729",
        "timestamp": "1685922251",
        "blockNumber": "17410567"
      },
      {
        "totalDepositBalanceUSD": "5488175150.46271274366242914608716",
        "totalBorrowBalanceUSD": "1818584190.256985842809785437544023",
        "timestamp": "1685836667",
        "blockNumber": "17403544"
      },
      {
        "totalDepositBalanceUSD": "5462926988.109500866616682306844004",
        "totalBorrowBalanceUSD": "1806229988.792135680752494281738738",
        "timestamp": "1685750147",
        "blockNumber": "17396433"
      },
      {
        "totalDepositBalanceUSD": "5412917341.661237726270418113111382",
        "totalBorrowBalanceUSD": "1782299349.224186721373727179131326",
        "timestamp": "1685663807",
        "blockNumber": "17389348"
      },
      {
        "totalDepositBalanceUSD": "5345394429.036716731916780293244053",
        "totalBorrowBalanceUSD": "1733561606.44317355490730355984788",
        "timestamp": "1685577527",
        "blockNumber": "17382259"
      },
      {
        "totalDepositBalanceUSD": "5383828708.916135541527468005802431",
        "totalBorrowBalanceUSD": "1740238206.54835464018831633403085",
        "timestamp": "1685491199",
        "blockNumber": "17375164"
      },
      {
        "totalDepositBalanceUSD": "5384178807.121955671476182958297835",
        "totalBorrowBalanceUSD": "1741481101.365751451773581610040232",
        "timestamp": "1685404655",
        "blockNumber": "17368048"
      },
      {
        "totalDepositBalanceUSD": "5389696520.904504854389443161166711",
        "totalBorrowBalanceUSD": "1744013450.89686675241186652685348",
        "timestamp": "1685318351",
        "blockNumber": "17360943"
      },
      {
        "totalDepositBalanceUSD": "5257340386.053985145464420999860707",
        "totalBorrowBalanceUSD": "1718599460.130429645953247959058798",
        "timestamp": "1685231639",
        "blockNumber": "17353788"
      },
      {
        "totalDepositBalanceUSD": "5267161471.562027577858613550800956",
        "totalBorrowBalanceUSD": "1723088845.743171892039935271504653",
        "timestamp": "1685145383",
        "blockNumber": "17346673"
      },
      {
        "totalDepositBalanceUSD": "5232763271.259497396763268011318829",
        "totalBorrowBalanceUSD": "1708911057.71913719591718733731101",
        "timestamp": "1685059187",
        "blockNumber": "17339570"
      },
      {
        "totalDepositBalanceUSD": "5259124902.418340751994243668838368",
        "totalBorrowBalanceUSD": "1701454341.7324407146462828442988",
        "timestamp": "1684972643",
        "blockNumber": "17332448"
      },
      {
        "totalDepositBalanceUSD": "5356428932.592951620097904449729861",
        "totalBorrowBalanceUSD": "1711949229.20874206425918018472426",
        "timestamp": "1684886147",
        "blockNumber": "17325328"
      },
      {
        "totalDepositBalanceUSD": "5247460619.077077365349352466185919",
        "totalBorrowBalanceUSD": "1694897814.200032288709408221724673",
        "timestamp": "1684799915",
        "blockNumber": "17318248"
      },
      {
        "totalDepositBalanceUSD": "5217321446.009612624639371629493806",
        "totalBorrowBalanceUSD": "1694080374.301399078892889297353942",
        "timestamp": "1684712039",
        "blockNumber": "17311016"
      },
      {
        "totalDepositBalanceUSD": "5218831664.827455174280109987562019",
        "totalBorrowBalanceUSD": "1692886514.70942812580358890155666",
        "timestamp": "1684627187",
        "blockNumber": "17304049"
      },
      {
        "totalDepositBalanceUSD": "5206675967.069888331940717135078169",
        "totalBorrowBalanceUSD": "1696594984.144292183139190484063441",
        "timestamp": "1684540751",
        "blockNumber": "17296936"
      },
      {
        "totalDepositBalanceUSD": "5159851824.096397062581391692000877",
        "totalBorrowBalanceUSD": "1686858732.22269114521088043385859",
        "timestamp": "1684453739",
        "blockNumber": "17289801"
      },
      {
        "totalDepositBalanceUSD": "5207327370.747419522022534162106988",
        "totalBorrowBalanceUSD": "1699651158.033089160642904825920728",
        "timestamp": "1684367411",
        "blockNumber": "17282696"
      },
      {
        "totalDepositBalanceUSD": "5190630159.922511739280789154566207",
        "totalBorrowBalanceUSD": "1682841958.54558938529013373764827",
        "timestamp": "1684281395",
        "blockNumber": "17275654"
      },
      {
        "totalDepositBalanceUSD": "5199935104.967521303203245375053496",
        "totalBorrowBalanceUSD": "1682691767.733460752218574487395082",
        "timestamp": "1684194935",
        "blockNumber": "17268565"
      },
      {
        "totalDepositBalanceUSD": "5153632130.853416044415352903488465",
        "totalBorrowBalanceUSD": "1679548954.792715885225437369128359",
        "timestamp": "1684108799",
        "blockNumber": "17261504"
      },
      {
        "totalDepositBalanceUSD": "5115205389.12690133652975042401295",
        "totalBorrowBalanceUSD": "1668488376.701258957487704469541379",
        "timestamp": "1684022363",
        "blockNumber": "17254449"
      },
      {
        "totalDepositBalanceUSD": "5126894809.796033516456986917896187",
        "totalBorrowBalanceUSD": "1658059563.300337129493671524408377",
        "timestamp": "1683935795",
        "blockNumber": "17247355"
      },
      {
        "totalDepositBalanceUSD": "5084127017.733507268358598746950967",
        "totalBorrowBalanceUSD": "1656484045.541253181580743306273522",
        "timestamp": "1683848819",
        "blockNumber": "17240392"
      },
      {
        "totalDepositBalanceUSD": "5183881684.686519811183766653238333",
        "totalBorrowBalanceUSD": "1667032359.284481008367259413732448",
        "timestamp": "1683762959",
        "blockNumber": "17233393"
      },
      {
        "totalDepositBalanceUSD": "5180580104.233244735536740832734013",
        "totalBorrowBalanceUSD": "1658149922.357312073881563233563787",
        "timestamp": "1683673763",
        "blockNumber": "17226054"
      },
      {
        "totalDepositBalanceUSD": "5157508490.801859405176664028107628",
        "totalBorrowBalanceUSD": "1658591408.95592905475385567810769",
        "timestamp": "1683590027",
        "blockNumber": "17219163"
      },
      {
        "totalDepositBalanceUSD": "5423748867.700402016592119594594269",
        "totalBorrowBalanceUSD": "1718064821.441809003149734118131243",
        "timestamp": "1683503975",
        "blockNumber": "17212077"
      },
      {
        "totalDepositBalanceUSD": "5364660974.804970267196983139324178",
        "totalBorrowBalanceUSD": "1671625262.813442921747935757602031",
        "timestamp": "1683417575",
        "blockNumber": "17204965"
      },
      {
        "totalDepositBalanceUSD": "5575079854.088586422717760365736229",
        "totalBorrowBalanceUSD": "1708533822.869551981973253256579069",
        "timestamp": "1683331199",
        "blockNumber": "17197858"
      },
      {
        "totalDepositBalanceUSD": "5316780755.923008010288584601494877",
        "totalBorrowBalanceUSD": "1655916579.446148470232579732517069",
        "timestamp": "1683244247",
        "blockNumber": "17190684"
      },
      {
        "totalDepositBalanceUSD": "5355807524.510249549001256577014991",
        "totalBorrowBalanceUSD": "1650735886.851820777501044821600724",
        "timestamp": "1683158171",
        "blockNumber": "17183588"
      },
      {
        "totalDepositBalanceUSD": "5330704774.335397080624834577955555",
        "totalBorrowBalanceUSD": "1668469547.470705390565656534300729",
        "timestamp": "1683071975",
        "blockNumber": "17176504"
      },
      {
        "totalDepositBalanceUSD": "5265764254.534856638200051410207043",
        "totalBorrowBalanceUSD": "1653899234.405113690279185865560864",
        "timestamp": "1682985407",
        "blockNumber": "17169379"
      },
      {
        "totalDepositBalanceUSD": "5406622630.446441192593430371472442",
        "totalBorrowBalanceUSD": "1717030917.347842276729512580833628",
        "timestamp": "1682899139",
        "blockNumber": "17162281"
      },
      {
        "totalDepositBalanceUSD": "5409626161.658508958930847734935457",
        "totalBorrowBalanceUSD": "1688968451.309272849011948632055622",
        "timestamp": "1682812751",
        "blockNumber": "17155159"
      },
      {
        "totalDepositBalanceUSD": "5364996098.459774999345403229679293",
        "totalBorrowBalanceUSD": "1680115885.844306725144982901538865",
        "timestamp": "1682726171",
        "blockNumber": "17148031"
      },
      {
        "totalDepositBalanceUSD": "5515302327.310048862592133081620623",
        "totalBorrowBalanceUSD": "1700643354.014894980728319836594751",
        "timestamp": "1682639183",
        "blockNumber": "17140862"
      },
      {
        "totalDepositBalanceUSD": "5410768830.371889587649144756057443",
        "totalBorrowBalanceUSD": "1682289924.118099357700867131177001",
        "timestamp": "1682553575",
        "blockNumber": "17133817"
      },
      {
        "totalDepositBalanceUSD": "5394285418.044862339095050084736296",
        "totalBorrowBalanceUSD": "1674678019.954787491669126792090949",
        "timestamp": "1682466923",
        "blockNumber": "17126671"
      },
      {
        "totalDepositBalanceUSD": "5297553165.305846767187548099804484",
        "totalBorrowBalanceUSD": "1656190465.311469337186123580672476",
        "timestamp": "1682380343",
        "blockNumber": "17119534"
      },
      {
        "totalDepositBalanceUSD": "5339678628.893360373238809042838659",
        "totalBorrowBalanceUSD": "1688900359.96243842519698410521599",
        "timestamp": "1682294147",
        "blockNumber": "17112419"
      },
      {
        "totalDepositBalanceUSD": "5338136015.158826968661511429574041",
        "totalBorrowBalanceUSD": "1667188377.103225890233062520172135",
        "timestamp": "1682207555",
        "blockNumber": "17105272"
      },
      {
        "totalDepositBalanceUSD": "5300683249.78942280365540641618829",
        "totalBorrowBalanceUSD": "1677317972.820977211560223508163264",
        "timestamp": "1682121599",
        "blockNumber": "17098172"
      },
      {
        "totalDepositBalanceUSD": "5500969205.19354648543216067487687",
        "totalBorrowBalanceUSD": "1730672037.145363928687103050459919",
        "timestamp": "1682034995",
        "blockNumber": "17091057"
      },
      {
        "totalDepositBalanceUSD": "5720755426.918297725927129569874992",
        "totalBorrowBalanceUSD": "1727442321.046373123181221680624661",
        "timestamp": "1681948535",
        "blockNumber": "17084025"
      },
      {
        "totalDepositBalanceUSD": "6041995636.421109726506212062564802",
        "totalBorrowBalanceUSD": "1803728548.944172637583941416415645",
        "timestamp": "1681862387",
        "blockNumber": "17076965"
      },
      {
        "totalDepositBalanceUSD": "6034607370.688160703995178589139051",
        "totalBorrowBalanceUSD": "1824237586.807446167586208816141817",
        "timestamp": "1681775735",
        "blockNumber": "17069877"
      },
      {
        "totalDepositBalanceUSD": "6240338190.536003168161763347917513",
        "totalBorrowBalanceUSD": "1828949868.609100966232150641277884",
        "timestamp": "1681689491",
        "blockNumber": "17062824"
      },
      {
        "totalDepositBalanceUSD": "6222493181.885701494390927572208043",
        "totalBorrowBalanceUSD": "1823899948.83583121175423070186636",
        "timestamp": "1681603175",
        "blockNumber": "17055789"
      },
      {
        "totalDepositBalanceUSD": "6252234870.1012847886413808579271",
        "totalBorrowBalanceUSD": "1830966845.126545535633972916103514",
        "timestamp": "1681516799",
        "blockNumber": "17048771"
      },
      {
        "totalDepositBalanceUSD": "6027044662.230677813934799727558473",
        "totalBorrowBalanceUSD": "1805385574.238960127039157542971057",
        "timestamp": "1681430159",
        "blockNumber": "17041746"
      },
      {
        "totalDepositBalanceUSD": "5911840254.919348373068019398363326",
        "totalBorrowBalanceUSD": "1768167626.237274638753774080998267",
        "timestamp": "1681343879",
        "blockNumber": "17035248"
      },
      {
        "totalDepositBalanceUSD": "5916503141.770604337419500991353779",
        "totalBorrowBalanceUSD": "1751057242.934014179264528023779945",
        "timestamp": "1681256915",
        "blockNumber": "17028185"
      },
      {
        "totalDepositBalanceUSD": "5897992367.689853106129113082592144",
        "totalBorrowBalanceUSD": "1743501509.501179953629605861392677",
        "timestamp": "1681171091",
        "blockNumber": "17021172"
      },
      {
        "totalDepositBalanceUSD": "5780967462.66775007715353184608401",
        "totalBorrowBalanceUSD": "1739337440.916678761251814379110854",
        "timestamp": "1681084547",
        "blockNumber": "17014095"
      },
      {
        "totalDepositBalanceUSD": "5734608629.946608789755008806618869",
        "totalBorrowBalanceUSD": "1712761519.922257227472298263077349",
        "timestamp": "1680998399",
        "blockNumber": "17007071"
      },
      {
        "totalDepositBalanceUSD": "5728167274.286715103105735396578347",
        "totalBorrowBalanceUSD": "1694785319.735958047459338474053393",
        "timestamp": "1680910463",
        "blockNumber": "16999884"
      },
      {
        "totalDepositBalanceUSD": "5752474903.126937812083411173645305",
        "totalBorrowBalanceUSD": "1693944316.409020209796825669389303",
        "timestamp": "1680825227",
        "blockNumber": "16992922"
      },
      {
        "totalDepositBalanceUSD": "5798640967.222527948523608538702198",
        "totalBorrowBalanceUSD": "1708804838.997554924115238254332815",
        "timestamp": "1680738815",
        "blockNumber": "16985924"
      },
      {
        "totalDepositBalanceUSD": "5749354578.611018583139986817342206",
        "totalBorrowBalanceUSD": "1708066851.405852406771998376588391",
        "timestamp": "1680651575",
        "blockNumber": "16978812"
      },
      {
        "totalDepositBalanceUSD": "5647544993.82427997939053959834569",
        "totalBorrowBalanceUSD": "1696855683.418741342051692260871826",
        "timestamp": "1680566231",
        "blockNumber": "16971879"
      },
      {
        "totalDepositBalanceUSD": "5659227499.77735561434870053061367",
        "totalBorrowBalanceUSD": "1728323996.302609722689167188800468",
        "timestamp": "1680479867",
        "blockNumber": "16964804"
      },
      {
        "totalDepositBalanceUSD": "5665173081.729114645688525977385061",
        "totalBorrowBalanceUSD": "1717366275.281109659489242830341329",
        "timestamp": "1680393455",
        "blockNumber": "16957704"
      },
      {
        "totalDepositBalanceUSD": "5739068452.688879425778201274369989",
        "totalBorrowBalanceUSD": "1766371630.713528365026103614268265",
        "timestamp": "1680307115",
        "blockNumber": "16950595"
      },
      {
        "totalDepositBalanceUSD": "5670010999.17459385165509763750447",
        "totalBorrowBalanceUSD": "1724045419.971815527758121625998662",
        "timestamp": "1680220427",
        "blockNumber": "16943448"
      },
      {
        "totalDepositBalanceUSD": "5747418218.41122481844412929146094",
        "totalBorrowBalanceUSD": "1720321859.845991152460929715734118",
        "timestamp": "1680134267",
        "blockNumber": "16936350"
      },
      {
        "totalDepositBalanceUSD": "5765480168.285074979771544104672253",
        "totalBorrowBalanceUSD": "1693855392.651312725032734790309282",
        "timestamp": "1680047963",
        "blockNumber": "16929244"
      },
      {
        "totalDepositBalanceUSD": "5764401918.841543309798920266134818",
        "totalBorrowBalanceUSD": "1741914496.480158653703723368948281",
        "timestamp": "1679961599",
        "blockNumber": "16922136"
      },
      {
        "totalDepositBalanceUSD": "5883732189.145574957982019715985729",
        "totalBorrowBalanceUSD": "1754519825.785149101021921736357857",
        "timestamp": "1679873843",
        "blockNumber": "16914910"
      },
      {
        "totalDepositBalanceUSD": "5822530389.346145797904713532281312",
        "totalBorrowBalanceUSD": "1729077300.44016192954753065863477",
        "timestamp": "1679788451",
        "blockNumber": "16907870"
      },
      {
        "totalDepositBalanceUSD": "5999503527.284994497717663497764036",
        "totalBorrowBalanceUSD": "1827543891.530524762204460944252731",
        "timestamp": "1679702267",
        "blockNumber": "16900766"
      },
      {
        "totalDepositBalanceUSD": "6213083600.740241851630478696176391",
        "totalBorrowBalanceUSD": "1900268753.357709745993924093985089",
        "timestamp": "1679615891",
        "blockNumber": "16893647"
      },
      {
        "totalDepositBalanceUSD": "6025109313.607221229701561247120753",
        "totalBorrowBalanceUSD": "1848568610.026933324646904970699081",
        "timestamp": "1679529455",
        "blockNumber": "16886540"
      },
      {
        "totalDepositBalanceUSD": "6211209982.807383837380299210334664",
        "totalBorrowBalanceUSD": "1904699233.305127828280622331624889",
        "timestamp": "1679443067",
        "blockNumber": "16879417"
      },
      {
        "totalDepositBalanceUSD": "6047111241.280090156076339962582563",
        "totalBorrowBalanceUSD": "1868008947.41041439199092586950816",
        "timestamp": "1679356607",
        "blockNumber": "16872296"
      },
      {
        "totalDepositBalanceUSD": "6144498413.475784425823413818164489",
        "totalBorrowBalanceUSD": "1902801832.536117838680282378819642",
        "timestamp": "1679270363",
        "blockNumber": "16865177"
      },
      {
        "totalDepositBalanceUSD": "6042518912.453622052855638149358799",
        "totalBorrowBalanceUSD": "1871704597.436681551663598478090018",
        "timestamp": "1679183999",
        "blockNumber": "16858066"
      },
      {
        "totalDepositBalanceUSD": "5921349438.732103087175359024045209",
        "totalBorrowBalanceUSD": "1886018155.872976957053165696124049",
        "timestamp": "1679097587",
        "blockNumber": "16850944"
      },
      {
        "totalDepositBalanceUSD": "5605230527.580447002327142447156696",
        "totalBorrowBalanceUSD": "1828422805.19782626722828995954387",
        "timestamp": "1679011199",
        "blockNumber": "16843829"
      },
      {
        "totalDepositBalanceUSD": "5782834844.099674562788498113465451",
        "totalBorrowBalanceUSD": "1876102787.225957369582676960936389",
        "timestamp": "1678924439",
        "blockNumber": "16836680"
      },
      {
        "totalDepositBalanceUSD": "5896341331.021344973267515990474122",
        "totalBorrowBalanceUSD": "1914572834.186951540403826494881773",
        "timestamp": "1678838327",
        "blockNumber": "16829603"
      },
      {
        "totalDepositBalanceUSD": "6081187590.648099301396163319318773",
        "totalBorrowBalanceUSD": "2035003285.421588170086531269228176",
        "timestamp": "1678751879",
        "blockNumber": "16822482"
      },
      {
        "totalDepositBalanceUSD": "5948821112.755847566927268048518627",
        "totalBorrowBalanceUSD": "2041689670.190054437552104216416358",
        "timestamp": "1678665587",
        "blockNumber": "16815365"
      },
      {
        "totalDepositBalanceUSD": "5384177880.124219869123755939161332",
        "totalBorrowBalanceUSD": "1789833773.696042449722632069651079",
        "timestamp": "1678579199",
        "blockNumber": "16808257"
      },
      {
        "totalDepositBalanceUSD": "4964109644.405477338802422340960167",
        "totalBorrowBalanceUSD": "1575250805.249335419384595361549228",
        "timestamp": "1678492799",
        "blockNumber": "16801143"
      },
      {
        "totalDepositBalanceUSD": "5109262884.398713632943191257426865",
        "totalBorrowBalanceUSD": "1583991376.995807071184172187863742",
        "timestamp": "1678406255",
        "blockNumber": "16794049"
      },
      {
        "totalDepositBalanceUSD": "5263113511.610524452981419435668452",
        "totalBorrowBalanceUSD": "1640327304.839286211941360949235148",
        "timestamp": "1678319963",
        "blockNumber": "16786945"
      },
      {
        "totalDepositBalanceUSD": "5296003134.655425223908160775153762",
        "totalBorrowBalanceUSD": "1694269043.137852277082543370110137",
        "timestamp": "1678233287",
        "blockNumber": "16779817"
      },
      {
        "totalDepositBalanceUSD": "5365676703.944475730799950960255488",
        "totalBorrowBalanceUSD": "1700071870.770522304659293100860089",
        "timestamp": "1678146515",
        "blockNumber": "16772670"
      },
      {
        "totalDepositBalanceUSD": "5344604895.770947215435536833514994",
        "totalBorrowBalanceUSD": "1650236818.420163673309935575968097",
        "timestamp": "1678060547",
        "blockNumber": "16765594"
      },
      {
        "totalDepositBalanceUSD": "5320162940.028365930707922448116626",
        "totalBorrowBalanceUSD": "1644900333.621549152545417732136784",
        "timestamp": "1677974303",
        "blockNumber": "16758487"
      },
      {
        "totalDepositBalanceUSD": "5186504691.223208934022868940565224",
        "totalBorrowBalanceUSD": "1670119816.236843093482633320801227",
        "timestamp": "1677887747",
        "blockNumber": "16751366"
      },
      {
        "totalDepositBalanceUSD": "5388264077.481939112681925972427548",
        "totalBorrowBalanceUSD": "1691409352.358760710623472349068737",
        "timestamp": "1677801263",
        "blockNumber": "16744260"
      },
      {
        "totalDepositBalanceUSD": "5499403644.400002095899669833556248",
        "totalBorrowBalanceUSD": "1757803628.700240970505452553113736",
        "timestamp": "1677714719",
        "blockNumber": "16737150"
      },
      {
        "totalDepositBalanceUSD": "5404978560.814799108834435267369333",
        "totalBorrowBalanceUSD": "1709753392.93236164807657824375677",
        "timestamp": "1677628703",
        "blockNumber": "16730063"
      },
      {
        "totalDepositBalanceUSD": "5529764846.374232284346721161715812",
        "totalBorrowBalanceUSD": "1728033267.184701984951508177806666",
        "timestamp": "1677542399",
        "blockNumber": "16722962"
      },
      {
        "totalDepositBalanceUSD": "5517060599.929079356555357775341233",
        "totalBorrowBalanceUSD": "1756246828.907128530837401496985851",
        "timestamp": "1677455735",
        "blockNumber": "16715807"
      },
      {
        "totalDepositBalanceUSD": "5392732242.874561014333290218578308",
        "totalBorrowBalanceUSD": "1740532785.755210954883898938881143",
        "timestamp": "1677369515",
        "blockNumber": "16708703"
      },
      {
        "totalDepositBalanceUSD": "5460137586.151418492486190601818362",
        "totalBorrowBalanceUSD": "1763895848.888224703917686393790795",
        "timestamp": "1677282839",
        "blockNumber": "16701568"
      },
      {
        "totalDepositBalanceUSD": "5582145737.013384945567007152059938",
        "totalBorrowBalanceUSD": "1793492866.766424359676087680580563",
        "timestamp": "1677196691",
        "blockNumber": "16694504"
      },
      {
        "totalDepositBalanceUSD": "5534548251.203733233560600456902491",
        "totalBorrowBalanceUSD": "1776900869.217398717330036442391124",
        "timestamp": "1677110279",
        "blockNumber": "16687385"
      },
      {
        "totalDepositBalanceUSD": "5574928210.709356762466271746517733",
        "totalBorrowBalanceUSD": "1780433246.165897897540036528287027",
        "timestamp": "1677023927",
        "blockNumber": "16680293"
      },
      {
        "totalDepositBalanceUSD": "5668260657.281159644988503419533202",
        "totalBorrowBalanceUSD": "1791473205.487690174743651052301951",
        "timestamp": "1676937575",
        "blockNumber": "16673182"
      },
      {
        "totalDepositBalanceUSD": "5703906452.407633427551767831122571",
        "totalBorrowBalanceUSD": "1784674092.451454986920278139113949",
        "timestamp": "1676850815",
        "blockNumber": "16666024"
      },
      {
        "totalDepositBalanceUSD": "5746510261.978309816480452694479349",
        "totalBorrowBalanceUSD": "1791991555.050959597572048332551529",
        "timestamp": "1676764667",
        "blockNumber": "16658927"
      },
      {
        "totalDepositBalanceUSD": "5739034118.334613578837971099745009",
        "totalBorrowBalanceUSD": "1772161881.101853315809308677802503",
        "timestamp": "1676678291",
        "blockNumber": "16651820"
      },
      {
        "totalDepositBalanceUSD": "5650856925.090076900038106276131254",
        "totalBorrowBalanceUSD": "1801311977.510970458933041805585388",
        "timestamp": "1676591999",
        "blockNumber": "16644732"
      },
      {
        "totalDepositBalanceUSD": "5662678913.228024397086215185534661",
        "totalBorrowBalanceUSD": "1815302475.99443902896766967620891",
        "timestamp": "1676505395",
        "blockNumber": "16637557"
      },
      {
        "totalDepositBalanceUSD": "5351668744.939897397355360600491974",
        "totalBorrowBalanceUSD": "1740989483.342785247557242726376958",
        "timestamp": "1676419187",
        "blockNumber": "16630421"
      },
      {
        "totalDepositBalanceUSD": "5238501762.518638003755868360396526",
        "totalBorrowBalanceUSD": "1719410848.878448670269185540174656",
        "timestamp": "1676332343",
        "blockNumber": "16623236"
      },
      {
        "totalDepositBalanceUSD": "5042884868.94145823587545566487952",
        "totalBorrowBalanceUSD": "1618387366.622882628833110999408057",
        "timestamp": "1676246351",
        "blockNumber": "16616111"
      },
      {
        "totalDepositBalanceUSD": "5158946704.895052450328467676938892",
        "totalBorrowBalanceUSD": "1661256290.681561956222545347535224",
        "timestamp": "1676159651",
        "blockNumber": "16608928"
      },
      {
        "totalDepositBalanceUSD": "5051865374.266665401805770610472682",
        "totalBorrowBalanceUSD": "1651898967.257134273688504331486378",
        "timestamp": "1676073575",
        "blockNumber": "16601797"
      },
      {
        "totalDepositBalanceUSD": "5212198647.305312690366711270408115",
        "totalBorrowBalanceUSD": "1704720720.638786203299002408931826",
        "timestamp": "1675987043",
        "blockNumber": "16594618"
      },
      {
        "totalDepositBalanceUSD": "5482879923.172046329647524296379084",
        "totalBorrowBalanceUSD": "1782364915.639571302748073214146891",
        "timestamp": "1675900211",
        "blockNumber": "16587427"
      },
      {
        "totalDepositBalanceUSD": "5530347578.094411874976392332020925",
        "totalBorrowBalanceUSD": "1777526754.840773629693127267334007",
        "timestamp": "1675814351",
        "blockNumber": "16580333"
      },
      {
        "totalDepositBalanceUSD": "5428910557.54584212902404530625908",
        "totalBorrowBalanceUSD": "1744484080.890421527293728921462874",
        "timestamp": "1675727915",
        "blockNumber": "16573182"
      },
      {
        "totalDepositBalanceUSD": "5469032237.337303466713882990262203",
        "totalBorrowBalanceUSD": "1775967682.912476303506908192778456",
        "timestamp": "1675641443",
        "blockNumber": "16566009"
      },
      {
        "totalDepositBalanceUSD": "5592432179.352359488604380767496557",
        "totalBorrowBalanceUSD": "1800283026.474358925844185401816906",
        "timestamp": "1675554875",
        "blockNumber": "16558831"
      },
      {
        "totalDepositBalanceUSD": "5614150819.680034510898978286178678",
        "totalBorrowBalanceUSD": "1795402434.645530771684308200130512",
        "timestamp": "1675468367",
        "blockNumber": "16551664"
      },
      {
        "totalDepositBalanceUSD": "5572058787.234558866737278113196729",
        "totalBorrowBalanceUSD": "1776066983.519710853379486835474263",
        "timestamp": "1675382171",
        "blockNumber": "16544528"
      },
      {
        "totalDepositBalanceUSD": "5557498681.175216154281203487733749",
        "totalBorrowBalanceUSD": "1761161050.856472029745225859525172",
        "timestamp": "1675295915",
        "blockNumber": "16537399"
      },
      {
        "totalDepositBalanceUSD": "5431792602.768713381097974656497389",
        "totalBorrowBalanceUSD": "1724383044.8489358606686509986099",
        "timestamp": "1675209587",
        "blockNumber": "16530246"
      },
      {
        "totalDepositBalanceUSD": "5349953237.116928845472190903740027",
        "totalBorrowBalanceUSD": "1710071863.162038167758215659682453",
        "timestamp": "1675122911",
        "blockNumber": "16523060"
      },
      {
        "totalDepositBalanceUSD": "5579153502.372352279770875449622823",
        "totalBorrowBalanceUSD": "1764259004.148061874512369203711263",
        "timestamp": "1675036799",
        "blockNumber": "16515916"
      },
      {
        "totalDepositBalanceUSD": "5431330802.469153612533523357452456",
        "totalBorrowBalanceUSD": "1700035668.180217802327121058117368",
        "timestamp": "1674950267",
        "blockNumber": "16508746"
      },
      {
        "totalDepositBalanceUSD": "5452533603.376760692180581187727173",
        "totalBorrowBalanceUSD": "1724631222.907528643327915280713393",
        "timestamp": "1674863879",
        "blockNumber": "16501578"
      },
      {
        "totalDepositBalanceUSD": "5478783407.245153777496007613117446",
        "totalBorrowBalanceUSD": "1718175257.882805514467466811792",
        "timestamp": "1674777587",
        "blockNumber": "16494434"
      },
      {
        "totalDepositBalanceUSD": "5535621470.15474575107972458286692",
        "totalBorrowBalanceUSD": "1751706892.156712833733990692630802",
        "timestamp": "1674691151",
        "blockNumber": "16487265"
      },
      {
        "totalDepositBalanceUSD": "5455484188.725961965840188255894416",
        "totalBorrowBalanceUSD": "1750896621.135121510521992680993275",
        "timestamp": "1674604775",
        "blockNumber": "16480109"
      },
      {
        "totalDepositBalanceUSD": "5604226830.815979456552093000902666",
        "totalBorrowBalanceUSD": "1762538422.161312345837009009700067",
        "timestamp": "1674518147",
        "blockNumber": "16472924"
      },
      {
        "totalDepositBalanceUSD": "5560203828.74292115489440430796231",
        "totalBorrowBalanceUSD": "1762867337.435775827347932260058307",
        "timestamp": "1674431927",
        "blockNumber": "16465774"
      },
      {
        "totalDepositBalanceUSD": "5552809564.846195896270965804338416",
        "totalBorrowBalanceUSD": "1748757117.164459885534337350314027",
        "timestamp": "1674345479",
        "blockNumber": "16458611"
      },
      {
        "totalDepositBalanceUSD": "5589875507.810316516641911974135802",
        "totalBorrowBalanceUSD": "1738624673.067423528096389390835624",
        "timestamp": "1674259103",
        "blockNumber": "16451449"
      },
      {
        "totalDepositBalanceUSD": "5334367239.718949532793010141678962",
        "totalBorrowBalanceUSD": "1714453670.152966217335537134149137",
        "timestamp": "1674172775",
        "blockNumber": "16444287"
      },
      {
        "totalDepositBalanceUSD": "5268284810.310079119982376539412096",
        "totalBorrowBalanceUSD": "1709990495.461981707604673928866598",
        "timestamp": "1674086387",
        "blockNumber": "16437128"
      },
      {
        "totalDepositBalanceUSD": "5429660384.001996299754110384831571",
        "totalBorrowBalanceUSD": "1733431846.125834334107947544618147",
        "timestamp": "1673999387",
        "blockNumber": "16429913"
      },
      {
        "totalDepositBalanceUSD": "5445698840.09159854905510640535427",
        "totalBorrowBalanceUSD": "1708482451.047250608976490894649335",
        "timestamp": "1673913527",
        "blockNumber": "16422787"
      },
      {
        "totalDepositBalanceUSD": "5381325059.697267865304167137399731",
        "totalBorrowBalanceUSD": "1678856982.688948837023928426208648",
        "timestamp": "1673827055",
        "blockNumber": "16415621"
      },
      {
        "totalDepositBalanceUSD": "5368224046.460755080955975757278142",
        "totalBorrowBalanceUSD": "1690729246.887122180985695697676258",
        "timestamp": "1673740787",
        "blockNumber": "16408486"
      },
      {
        "totalDepositBalanceUSD": "5222337427.855227717963917315038843",
        "totalBorrowBalanceUSD": "1660759131.547352806364318970651012",
        "timestamp": "1673654327",
        "blockNumber": "16401311"
      },
      {
        "totalDepositBalanceUSD": "5129875246.306952262508850088345154",
        "totalBorrowBalanceUSD": "1639591050.284900634576740402519974",
        "timestamp": "1673567879",
        "blockNumber": "16394145"
      },
      {
        "totalDepositBalanceUSD": "5000564861.153122846010314484892027",
        "totalBorrowBalanceUSD": "1612288933.682629065466388376159272",
        "timestamp": "1673481515",
        "blockNumber": "16386992"
      },
      {
        "totalDepositBalanceUSD": "4883393908.271493725485188870620629",
        "totalBorrowBalanceUSD": "1586996679.08350917799488397348142",
        "timestamp": "1673395031",
        "blockNumber": "16379830"
      },
      {
        "totalDepositBalanceUSD": "4842773436.041556743307512946351942",
        "totalBorrowBalanceUSD": "1580361605.98545712857461189855837",
        "timestamp": "1673308427",
        "blockNumber": "16372647"
      },
      {
        "totalDepositBalanceUSD": "4754760199.708436710900297010108917",
        "totalBorrowBalanceUSD": "1560760574.508026577148098131244499",
        "timestamp": "1673222327",
        "blockNumber": "16365505"
      },
      {
        "totalDepositBalanceUSD": "4621773648.221438179651755053890027",
        "totalBorrowBalanceUSD": "1555322758.717013942028957205175421",
        "timestamp": "1673135963",
        "blockNumber": "16358343"
      },
      {
        "totalDepositBalanceUSD": "4625427703.69036835707060707724197",
        "totalBorrowBalanceUSD": "1555660775.289787801979969110857937",
        "timestamp": "1673049503",
        "blockNumber": "16351175"
      },
      {
        "totalDepositBalanceUSD": "4597397653.943328054204731955441851",
        "totalBorrowBalanceUSD": "1538516037.051267512453696750903842",
        "timestamp": "1672963187",
        "blockNumber": "16344022"
      },
      {
        "totalDepositBalanceUSD": "4622783295.506280717562256174937552",
        "totalBorrowBalanceUSD": "1543918285.437811471105270703426908",
        "timestamp": "1672876703",
        "blockNumber": "16336862"
      },
      {
        "totalDepositBalanceUSD": "4555702879.083360369057113996614115",
        "totalBorrowBalanceUSD": "1528166937.172220220866838717984402",
        "timestamp": "1672789943",
        "blockNumber": "16329662"
      },
      {
        "totalDepositBalanceUSD": "4577627586.494081076872649480341683",
        "totalBorrowBalanceUSD": "1541724176.145660860904692594710653",
        "timestamp": "1672703963",
        "blockNumber": "16322529"
      },
      {
        "totalDepositBalanceUSD": "4511430654.780198147314483962394469",
        "totalBorrowBalanceUSD": "1521370275.164689559781367421732338",
        "timestamp": "1672617599",
        "blockNumber": "16315361"
      },
      {
        "totalDepositBalanceUSD": "4508139496.148952517021673007670918",
        "totalBorrowBalanceUSD": "1519474456.461540578437959109221316",
        "timestamp": "1672531151",
        "blockNumber": "16308185"
      },
      {
        "totalDepositBalanceUSD": "4502459092.135246849793650469579545",
        "totalBorrowBalanceUSD": "1527681650.444698567141916456611125",
        "timestamp": "1672444787",
        "blockNumber": "16301022"
      },
      {
        "totalDepositBalanceUSD": "4536234884.768754381434388335571251",
        "totalBorrowBalanceUSD": "1531489016.671809863575297224027541",
        "timestamp": "1672357847",
        "blockNumber": "16293811"
      },
      {
        "totalDepositBalanceUSD": "4514239848.801303228338067556524265",
        "totalBorrowBalanceUSD": "1532008357.459563336358805331097585",
        "timestamp": "1672271927",
        "blockNumber": "16286690"
      },
      {
        "totalDepositBalanceUSD": "4555954780.757508745842253256182639",
        "totalBorrowBalanceUSD": "1547553178.49162179971264409204375",
        "timestamp": "1672185023",
        "blockNumber": "16279475"
      },
      {
        "totalDepositBalanceUSD": "4568097477.044122568555285042043065",
        "totalBorrowBalanceUSD": "1545945697.890510036228304306341595",
        "timestamp": "1672099187",
        "blockNumber": "16272366"
      },
      {
        "totalDepositBalanceUSD": "4519716401.319009321129573950276958",
        "totalBorrowBalanceUSD": "1531583488.195614289560799335695723",
        "timestamp": "1672012787",
        "blockNumber": "16265204"
      },
      {
        "totalDepositBalanceUSD": "4564190803.566635944798901705846741",
        "totalBorrowBalanceUSD": "1546196208.176299412112719878761402",
        "timestamp": "1671926303",
        "blockNumber": "16258029"
      },
      {
        "totalDepositBalanceUSD": "4558542489.691818608756293740340581",
        "totalBorrowBalanceUSD": "1561944624.76479025930979269740473",
        "timestamp": "1671839555",
        "blockNumber": "16250834"
      },
      {
        "totalDepositBalanceUSD": "4586404328.035254852825420509372401",
        "totalBorrowBalanceUSD": "1567072130.532807182596133697577993",
        "timestamp": "1671753563",
        "blockNumber": "16243688"
      },
      {
        "totalDepositBalanceUSD": "4573794029.500086426428084431433434",
        "totalBorrowBalanceUSD": "1582195820.085339155715837244161642",
        "timestamp": "1671667043",
        "blockNumber": "16236500"
      },
      {
        "totalDepositBalanceUSD": "4576285192.851298985325048020964327",
        "totalBorrowBalanceUSD": "1591963862.270117828633395879743704",
        "timestamp": "1671580631",
        "blockNumber": "16229336"
      }
    ]
  }
}

market_daily_snapshots = json_data["data"]["financialsDailySnapshots"]

with open("AAVE-V2-Ethereum.csv", mode="w", newline="") as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=["datetime", "totalBorrowBalanceUSD", "totalDepositBalanceUSD", "blockNumber"])

    writer.writeheader()

    for snapshot in market_daily_snapshots:
        timestamp = datetime.utcfromtimestamp(int(snapshot["timestamp"]))
        datetime_str = timestamp.strftime("%Y-%m-%d")
        writer.writerow({
            "totalBorrowBalanceUSD": snapshot["totalBorrowBalanceUSD"],
            "totalDepositBalanceUSD": snapshot["totalDepositBalanceUSD"],
            "datetime": datetime_str,
            "blockNumber": snapshot["blockNumber"]
        })
