import csv
import json
from datetime import datetime

data = {
  "data": {
    "vaultDailySnapshots": [
      {
        "timestamp": "1697194171",
        "totalValueLockedUSD": "99786.26583810287440615763573"
      },
      {
        "timestamp": "1697074844",
        "totalValueLockedUSD": "101040.7862310043716124149465236"
      },
      {
        "timestamp": "1696973956",
        "totalValueLockedUSD": "104999.48746605026966456266671846"
      },
      {
        "timestamp": "1696676834",
        "totalValueLockedUSD": "117402.66052896637279969664599416"
      },
      {
        "timestamp": "1696589890",
        "totalValueLockedUSD": "120842.33453895502487104387017188"
      },
      {
        "timestamp": "1696154557",
        "totalValueLockedUSD": "112748.43885788924501930469892864"
      },
      {
        "timestamp": "1696104846",
        "totalValueLockedUSD": "109430.70929501752969365386575104"
      },
      {
        "timestamp": "1695984108",
        "totalValueLockedUSD": "108944.019413908796893707827213"
      },
      {
        "timestamp": "1695934104",
        "totalValueLockedUSD": "108944.019413908796893707827213"
      },
      {
        "timestamp": "1695766486",
        "totalValueLockedUSD": "106006.67780711747345573514931304"
      },
      {
        "timestamp": "1695426861",
        "totalValueLockedUSD": "104319.96107609990429300908319434"
      },
      {
        "timestamp": "1695245351",
        "totalValueLockedUSD": "108573.17124414858841964918074"
      },
      {
        "timestamp": "1695120820",
        "totalValueLockedUSD": "110207.74106639999848024151145404"
      },
      {
        "timestamp": "1694913068",
        "totalValueLockedUSD": "110405.2017513118604707124961184"
      },
      {
        "timestamp": "1694834311",
        "totalValueLockedUSD": "114236.54339772420198034808828544"
      },
      {
        "timestamp": "1694774629",
        "totalValueLockedUSD": "110283.56198657208663734277251844"
      },
      {
        "timestamp": "1694676317",
        "totalValueLockedUSD": "110283.56198657208663734277251844"
      },
      {
        "timestamp": "1694634074",
        "totalValueLockedUSD": "109815.39507857394545695682234668"
      },
      {
        "timestamp": "1694450228",
        "totalValueLockedUSD": "109896.71063069010350621259952422"
      },
      {
        "timestamp": "1694180488",
        "totalValueLockedUSD": "119781.02887036179328136170139418"
      },
      {
        "timestamp": "1693901041",
        "totalValueLockedUSD": "119803.8182088511533917288929448"
      },
      {
        "timestamp": "1693770562",
        "totalValueLockedUSD": "121479.42936611874928751347263626"
      },
      {
        "timestamp": "1693657373",
        "totalValueLockedUSD": "120778.75188835699134408140905645"
      },
      {
        "timestamp": "1693573229",
        "totalValueLockedUSD": "123026.28907391183763404932838584"
      },
      {
        "timestamp": "1693480771",
        "totalValueLockedUSD": "127981.1977668744106890602040567"
      },
      {
        "timestamp": "1693374632",
        "totalValueLockedUSD": "130274.56744587537307519240126422"
      },
      {
        "timestamp": "1693309561",
        "totalValueLockedUSD": "126649.69225420222777662002361123"
      },
      {
        "timestamp": "1693209991",
        "totalValueLockedUSD": "122275.53594301322909811434940792"
      },
      {
        "timestamp": "1693109528",
        "totalValueLockedUSD": "123278.91296530787978423709594305"
      },
      {
        "timestamp": "1693085215",
        "totalValueLockedUSD": "122869.23846625035256289180267203"
      },
      {
        "timestamp": "1692968435",
        "totalValueLockedUSD": "122317.08841939445011416682974748"
      },
      {
        "timestamp": "1692820718",
        "totalValueLockedUSD": "127437.88181317455041504396424841"
      },
      {
        "timestamp": "1692451119",
        "totalValueLockedUSD": "130956.53346789778665666618341699"
      },
      {
        "timestamp": "1692373252",
        "totalValueLockedUSD": "131664.83152106546403027059392096"
      },
      {
        "timestamp": "1692307238",
        "totalValueLockedUSD": "133030.04169042518410390089864951"
      },
      {
        "timestamp": "1692141751",
        "totalValueLockedUSD": "138343.72379706860719875541474222"
      },
      {
        "timestamp": "1691749474",
        "totalValueLockedUSD": "145680.06892099897056507206134064"
      },
      {
        "timestamp": "1691654638",
        "totalValueLockedUSD": "146304.25073022176695608232187175"
      },
      {
        "timestamp": "1691452859",
        "totalValueLockedUSD": "145881.88617930873180242316925812"
      },
      {
        "timestamp": "1691153937",
        "totalValueLockedUSD": "146575.7725289500210181444185906"
      },
      {
        "timestamp": "1691084119",
        "totalValueLockedUSD": "147290.95344197427086826245929295"
      },
      {
        "timestamp": "1690974253",
        "totalValueLockedUSD": "149408.36287971480233348482873212"
      },
      {
        "timestamp": "1690846451",
        "totalValueLockedUSD": "149851.54354414914535549280273232"
      },
      {
        "timestamp": "1690544820",
        "totalValueLockedUSD": "153068.7685486486797056563733789"
      },
      {
        "timestamp": "1690405429",
        "totalValueLockedUSD": "156936.1459911131491868426552087"
      },
      {
        "timestamp": "1690189137",
        "totalValueLockedUSD": "158421.33168816469669692800517816"
      },
      {
        "timestamp": "1690103941",
        "totalValueLockedUSD": "160282.45118874326494096263422277"
      },
      {
        "timestamp": "1689942135",
        "totalValueLockedUSD": "164409.30454724950667599181589272"
      },
      {
        "timestamp": "1689860355",
        "totalValueLockedUSD": "167981.0079757646500846640250966"
      },
      {
        "timestamp": "1689719422",
        "totalValueLockedUSD": "155076.94414696031632764270855816"
      },
      {
        "timestamp": "1689614882",
        "totalValueLockedUSD": "158816.15953422348756729514804534"
      },
      {
        "timestamp": "1689455424",
        "totalValueLockedUSD": "170053.25383669477788907672245707"
      },
      {
        "timestamp": "1689351192",
        "totalValueLockedUSD": "177009.65544335952402011869225656"
      },
      {
        "timestamp": "1689151257",
        "totalValueLockedUSD": "169336.40286094385525097511640184"
      },
      {
        "timestamp": "1689059857",
        "totalValueLockedUSD": "159779.16421413111681552532397772"
      },
      {
        "timestamp": "1688838460",
        "totalValueLockedUSD": "160841.83788637608327132080526222"
      },
      {
        "timestamp": "1688756689",
        "totalValueLockedUSD": "147474.72554521381253516356328934"
      },
      {
        "timestamp": "1688651415",
        "totalValueLockedUSD": "148905.76480560650529113511798244"
      },
      {
        "timestamp": "1688571096",
        "totalValueLockedUSD": "147772.35736959121058112848323734"
      },
      {
        "timestamp": "1688510803",
        "totalValueLockedUSD": "154238.35309567092235772071906862"
      },
      {
        "timestamp": "1688412202",
        "totalValueLockedUSD": "156981.77991525099154750147179213"
      },
      {
        "timestamp": "1688272599",
        "totalValueLockedUSD": "150871.68157293772514571648646806"
      },
      {
        "timestamp": "1688134395",
        "totalValueLockedUSD": "149410.53991692430948894695407904"
      },
      {
        "timestamp": "1688038004",
        "totalValueLockedUSD": "150692.4899757416990790670888122"
      },
      {
        "timestamp": "1687961461",
        "totalValueLockedUSD": "148635.2274271637672650522480928"
      },
      {
        "timestamp": "1687876022",
        "totalValueLockedUSD": "155582.82999351879896715040015607"
      },
      {
        "timestamp": "1687693737",
        "totalValueLockedUSD": "157815.67387905890567196790572285"
      },
      {
        "timestamp": "1687639212",
        "totalValueLockedUSD": "150232.12354340849310645258178158"
      },
      {
        "timestamp": "1687554764",
        "totalValueLockedUSD": "156227.72840500442788703234887379"
      },
      {
        "timestamp": "1687475302",
        "totalValueLockedUSD": "147648.8611429248678043841590832"
      },
      {
        "timestamp": "1687367775",
        "totalValueLockedUSD": "146923.53085985062719162746560746"
      },
      {
        "timestamp": "1687277739",
        "totalValueLockedUSD": "133044.83446117790490291313808055"
      },
      {
        "timestamp": "1687118416",
        "totalValueLockedUSD": "134452.82174708438818730238386785"
      },
      {
        "timestamp": "1686995662",
        "totalValueLockedUSD": "137405.565057911285121162423807"
      },
      {
        "timestamp": "1686932070",
        "totalValueLockedUSD": "142614.2803999606367554509066756"
      },
      {
        "timestamp": "1686763215",
        "totalValueLockedUSD": "147988.05438751462807145583609843"
      },
      {
        "timestamp": "1686609847",
        "totalValueLockedUSD": "143203.56327472131328857046053796"
      },
      {
        "timestamp": "1686487701",
        "totalValueLockedUSD": "144928.10438349181905104649215463"
      },
      {
        "timestamp": "1686369243",
        "totalValueLockedUSD": "162835.10076694934568083761497684"
      },
      {
        "timestamp": "1686318815",
        "totalValueLockedUSD": "175788.5582541580715151599524173"
      },
      {
        "timestamp": "1686240167",
        "totalValueLockedUSD": "177078.3016105901756350371587382"
      },
      {
        "timestamp": "1686135050",
        "totalValueLockedUSD": "178905.98676393563534306120269776"
      },
      {
        "timestamp": "1686086242",
        "totalValueLockedUSD": "181730.5429670838113710574308286"
      },
      {
        "timestamp": "1685823030",
        "totalValueLockedUSD": "180029.08703305625516704304513406"
      },
      {
        "timestamp": "1685741253",
        "totalValueLockedUSD": "178194.19587798069515964754051928"
      },
      {
        "timestamp": "1685387402",
        "totalValueLockedUSD": "179105.0542512484767045383609702"
      },
      {
        "timestamp": "1685265463",
        "totalValueLockedUSD": "168845.1438367806472678717941762"
      },
      {
        "timestamp": "1685111659",
        "totalValueLockedUSD": "163715.70617617470186420328271952"
      },
      {
        "timestamp": "1685003810",
        "totalValueLockedUSD": "162301.4100545103164447174606448"
      },
      {
        "timestamp": "1684964679",
        "totalValueLockedUSD": "162215.00342619603969586749402632"
      },
      {
        "timestamp": "1684877258",
        "totalValueLockedUSD": "167926.76013505779548398798702687"
      },
      {
        "timestamp": "1684765740",
        "totalValueLockedUSD": "166254.74471152766304744803857657"
      },
      {
        "timestamp": "1684670592",
        "totalValueLockedUSD": "163902.05362310342154936050886656"
      },
      {
        "timestamp": "1684540958",
        "totalValueLockedUSD": "164798.75807178971593223217322404"
      },
      {
        "timestamp": "1684539673",
        "totalValueLockedUSD": "165385.7237947633237150656679838"
      },
      {
        "timestamp": "1684407874",
        "totalValueLockedUSD": "168247.65283563753605624371229646"
      },
      {
        "timestamp": "1684337465",
        "totalValueLockedUSD": "164935.42387969888253535735388728"
      },
      {
        "timestamp": "1684260975",
        "totalValueLockedUSD": "163198.43724565430609176262779494"
      },
      {
        "timestamp": "1684150050",
        "totalValueLockedUSD": "167143.47666951592682611244066772"
      },
      {
        "timestamp": "1684016952",
        "totalValueLockedUSD": "163188.01660819533852876924286165"
      },
      {
        "timestamp": "1683902401",
        "totalValueLockedUSD": "163782.17582878163546123477114672"
      },
      {
        "timestamp": "1683818710",
        "totalValueLockedUSD": "198689.77335055601900686017879225"
      },
      {
        "timestamp": "1683727560",
        "totalValueLockedUSD": "206516.32789215831206278380775365"
      },
      {
        "timestamp": "1683612720",
        "totalValueLockedUSD": "203893.7525763100511109225539112"
      },
      {
        "timestamp": "1683578099",
        "totalValueLockedUSD": "202489.12809123050566648083107884"
      },
      {
        "timestamp": "1683502183",
        "totalValueLockedUSD": "217951.987484495770882414196004"
      },
      {
        "timestamp": "1683380175",
        "totalValueLockedUSD": "223136.99413821721758657791038459"
      },
      {
        "timestamp": "1683309415",
        "totalValueLockedUSD": "229224.25768742913870349670466936"
      },
      {
        "timestamp": "1683214814",
        "totalValueLockedUSD": "225097.6190683270910482797023592"
      },
      {
        "timestamp": "1683102517",
        "totalValueLockedUSD": "220489.105835753359785778359216"
      },
      {
        "timestamp": "1683058845",
        "totalValueLockedUSD": "223664.68829632659196536381842535"
      },
      {
        "timestamp": "1682950500",
        "totalValueLockedUSD": "224599.54686982413201299112345984"
      },
      {
        "timestamp": "1682846211",
        "totalValueLockedUSD": "230337.3992715851200823537732232"
      },
      {
        "timestamp": "1682806298",
        "totalValueLockedUSD": "230665.1154440949854181072884976"
      },
      {
        "timestamp": "1682705141",
        "totalValueLockedUSD": "231766.2263463646144355278255647"
      },
      {
        "timestamp": "1682610373",
        "totalValueLockedUSD": "218838.084122826181404973855042"
      },
      {
        "timestamp": "1682516225",
        "totalValueLockedUSD": "224545.46717917813548756493764412"
      },
      {
        "timestamp": "1682373025",
        "totalValueLockedUSD": "209754.97584218589852663242580972"
      },
      {
        "timestamp": "1682171307",
        "totalValueLockedUSD": "210900.5264636428359789159868716"
      },
      {
        "timestamp": "1682101289",
        "totalValueLockedUSD": "215546.97003646866661987500356232"
      },
      {
        "timestamp": "1681738445",
        "totalValueLockedUSD": "251692.94899001264946937677782646"
      },
      {
        "timestamp": "1681680549",
        "totalValueLockedUSD": "244962.8320351073977808576943454"
      },
      {
        "timestamp": "1681575494",
        "totalValueLockedUSD": "232967.71046638481141942683944824"
      },
      {
        "timestamp": "1681514958",
        "totalValueLockedUSD": "233495.08001490396610407473472545"
      },
      {
        "timestamp": "1681365537",
        "totalValueLockedUSD": "234451.8842219554515631575734719"
      },
      {
        "timestamp": "1681318035",
        "totalValueLockedUSD": "229175.0178912428650507972920774"
      },
      {
        "timestamp": "1681236780",
        "totalValueLockedUSD": "233013.0267957056760948176639305"
      },
      {
        "timestamp": "1681165860",
        "totalValueLockedUSD": "233292.6511466608314483300979862"
      },
      {
        "timestamp": "1681052296",
        "totalValueLockedUSD": "225563.96999476076738216682735254"
      },
      {
        "timestamp": "1680970147",
        "totalValueLockedUSD": "229316.66860120875849737167743045"
      },
      {
        "timestamp": "1680904183",
        "totalValueLockedUSD": "228625.72616718114882417494617532"
      },
      {
        "timestamp": "1680775658",
        "totalValueLockedUSD": "225005.80281203682703337587659676"
      },
      {
        "timestamp": "1680681331",
        "totalValueLockedUSD": "229826.56272718066494255743086848"
      },
      {
        "timestamp": "1680631657",
        "totalValueLockedUSD": "210886.71855430799573901361433088"
      },
      {
        "timestamp": "1680557202",
        "totalValueLockedUSD": "203384.37211516186184566574036824"
      },
      {
        "timestamp": "1680440955",
        "totalValueLockedUSD": "210983.48052801934058569619676"
      },
      {
        "timestamp": "1680375527",
        "totalValueLockedUSD": "211632.27182140358638652161182"
      },
      {
        "timestamp": "1680290095",
        "totalValueLockedUSD": "211584.53529458342888779308471099"
      },
      {
        "timestamp": "1680088792",
        "totalValueLockedUSD": "208350.3935389028018241139076324"
      },
      {
        "timestamp": "1680041237",
        "totalValueLockedUSD": "202303.09287680609854116723040488"
      },
      {
        "timestamp": "1679932746",
        "totalValueLockedUSD": "197687.99049846271408212562419395"
      },
      {
        "timestamp": "1679868006",
        "totalValueLockedUSD": "204402.18930468032992463076171088"
      },
      {
        "timestamp": "1679783763",
        "totalValueLockedUSD": "200688.41356881307397592790296"
      },
      {
        "timestamp": "1679671083",
        "totalValueLockedUSD": "203977.17602909055605457955120107"
      },
      {
        "timestamp": "1679558312",
        "totalValueLockedUSD": "206158.01517508901611822018791946"
      },
      {
        "timestamp": "1679465554",
        "totalValueLockedUSD": "212431.9368414718390661257505378"
      },
      {
        "timestamp": "1679411052",
        "totalValueLockedUSD": "207749.53162003841279577277330779"
      },
      {
        "timestamp": "1679255115",
        "totalValueLockedUSD": "196427.8085077282226314130474468"
      },
      {
        "timestamp": "1679149157",
        "totalValueLockedUSD": "192921.38663139035537803945266372"
      },
      {
        "timestamp": "1679089843",
        "totalValueLockedUSD": "183149.18466379929412214950946492"
      },
      {
        "timestamp": "1679007122",
        "totalValueLockedUSD": "172793.13396468631663934394383577"
      },
      {
        "timestamp": "1678872152",
        "totalValueLockedUSD": "170354.03303135294226512687929208"
      },
      {
        "timestamp": "1678833759",
        "totalValueLockedUSD": "168515.1524688222108154422268626"
      },
      {
        "timestamp": "1678554126",
        "totalValueLockedUSD": "139843.3282664928363719108420844"
      },
      {
        "timestamp": "1678487411",
        "totalValueLockedUSD": "146733.58999799651557176259388548"
      },
      {
        "timestamp": "1678387403",
        "totalValueLockedUSD": "151492.52106865909348727757915205"
      },
      {
        "timestamp": "1678319396",
        "totalValueLockedUSD": "151284.8926365184155725181924342"
      },
      {
        "timestamp": "1678229636",
        "totalValueLockedUSD": "159535.2446782918050517290607284"
      },
      {
        "timestamp": "1678139652",
        "totalValueLockedUSD": "163019.5051588377057568218942"
      },
      {
        "timestamp": "1678060181",
        "totalValueLockedUSD": "160315.48496158402225421811530199"
      },
      {
        "timestamp": "1677963214",
        "totalValueLockedUSD": "158895.26261360711586836566039106"
      },
      {
        "timestamp": "1677877664",
        "totalValueLockedUSD": "162681.6870091021508100325425633"
      },
      {
        "timestamp": "1677801173",
        "totalValueLockedUSD": "187838.95596019350588199937313532"
      },
      {
        "timestamp": "1677704739",
        "totalValueLockedUSD": "187995.78991904102270797524699238"
      },
      {
        "timestamp": "1677623099",
        "totalValueLockedUSD": "184411.20809543741968895159034004"
      },
      {
        "timestamp": "1677541500",
        "totalValueLockedUSD": "193092.8988548037651894034781757"
      },
      {
        "timestamp": "1677443663",
        "totalValueLockedUSD": "199183.3777617887884687719035"
      },
      {
        "timestamp": "1677367916",
        "totalValueLockedUSD": "193147.09085378155278561335111254"
      },
      {
        "timestamp": "1677281636",
        "totalValueLockedUSD": "206222.37183669706818752258036935"
      },
      {
        "timestamp": "1677193962",
        "totalValueLockedUSD": "220610.2966687729670118764704344"
      },
      {
        "timestamp": "1677105722",
        "totalValueLockedUSD": "223693.18724241440655893111850076"
      },
      {
        "timestamp": "1677023324",
        "totalValueLockedUSD": "231397.74694453385970245436923438"
      },
      {
        "timestamp": "1676930455",
        "totalValueLockedUSD": "230680.14320785103781761160059274"
      },
      {
        "timestamp": "1676844108",
        "totalValueLockedUSD": "219515.38575264733260037509926825"
      },
      {
        "timestamp": "1676751533",
        "totalValueLockedUSD": "224452.68461951537561665473176113"
      },
      {
        "timestamp": "1676672119",
        "totalValueLockedUSD": "222944.90105977843193842419417755"
      },
      {
        "timestamp": "1676588098",
        "totalValueLockedUSD": "216424.58364656176676196810930675"
      },
      {
        "timestamp": "1676504559",
        "totalValueLockedUSD": "224740.84538595050177685781859212"
      },
      {
        "timestamp": "1676418980",
        "totalValueLockedUSD": "204654.02160080669345710376049936"
      },
      {
        "timestamp": "1676323701",
        "totalValueLockedUSD": "189474.1111853968396550073931923"
      },
      {
        "timestamp": "1676236291",
        "totalValueLockedUSD": "200243.7776360954378142246357187"
      },
      {
        "timestamp": "1676158360",
        "totalValueLockedUSD": "197406.1914104099370189510793116"
      },
      {
        "timestamp": "1676072792",
        "totalValueLockedUSD": "194795.59417191794011229849697595"
      },
      {
        "timestamp": "1675985128",
        "totalValueLockedUSD": "196157.4158931548150405845200378"
      },
      {
        "timestamp": "1675897727",
        "totalValueLockedUSD": "219809.18049783432558594708560667"
      },
      {
        "timestamp": "1675813744",
        "totalValueLockedUSD": "226879.48138421172127614221072"
      },
      {
        "timestamp": "1675726782",
        "totalValueLockedUSD": "210450.3381211634735823923076463"
      },
      {
        "timestamp": "1675635968",
        "totalValueLockedUSD": "215894.81488624375499844839312124"
      },
      {
        "timestamp": "1675553191",
        "totalValueLockedUSD": "226711.72408407950391004679245183"
      },
      {
        "timestamp": "1675466412",
        "totalValueLockedUSD": "235234.16291770874172516402148394"
      },
      {
        "timestamp": "1675381203",
        "totalValueLockedUSD": "233153.50166155651766062196538921"
      },
      {
        "timestamp": "1675293304",
        "totalValueLockedUSD": "228310.68562691687928169141577324"
      },
      {
        "timestamp": "1675198341",
        "totalValueLockedUSD": "220128.13826764308636411552948096"
      },
      {
        "timestamp": "1675120911",
        "totalValueLockedUSD": "215718.18658022087428414422963844"
      },
      {
        "timestamp": "1675036765",
        "totalValueLockedUSD": "231088.70906073678499560871388302"
      },
      {
        "timestamp": "1674949394",
        "totalValueLockedUSD": "226042.97665542417629004884352"
      },
      {
        "timestamp": "1674862502",
        "totalValueLockedUSD": "235175.14940153691849306723778062"
      },
      {
        "timestamp": "1674776137",
        "totalValueLockedUSD": "199717.12089413880286155347580376"
      },
      {
        "timestamp": "1674685387",
        "totalValueLockedUSD": "198153.161128464389688216354901"
      },
      {
        "timestamp": "1674600666",
        "totalValueLockedUSD": "189744.88770490679439241005167505"
      },
      {
        "timestamp": "1674515895",
        "totalValueLockedUSD": "198026.6885901821652698816708832"
      },
      {
        "timestamp": "1674421276",
        "totalValueLockedUSD": "189064.99768475783358532051826442"
      },
      {
        "timestamp": "1674341831",
        "totalValueLockedUSD": "189015.16246193014835240142015888"
      },
      {
        "timestamp": "1674256256",
        "totalValueLockedUSD": "191318.52272477266208191917855081"
      },
      {
        "timestamp": "1674171759",
        "totalValueLockedUSD": "191186.01568000800767418850021248"
      },
      {
        "timestamp": "1674082497",
        "totalValueLockedUSD": "188723.68788126961377668415065516"
      },
      {
        "timestamp": "1673998711",
        "totalValueLockedUSD": "200732.0129044539344799163540315"
      },
      {
        "timestamp": "1673907108",
        "totalValueLockedUSD": "197555.94536296132809758064609664"
      },
      {
        "timestamp": "1673819226",
        "totalValueLockedUSD": "197790.95689201511444778362652078"
      },
      {
        "timestamp": "1673739163",
        "totalValueLockedUSD": "198563.57599005190242195432330276"
      },
      {
        "timestamp": "1673650185",
        "totalValueLockedUSD": "194539.42704143819908359491517772"
      },
      {
        "timestamp": "1673565022",
        "totalValueLockedUSD": "206475.0077786888134644617426604"
      },
      {
        "timestamp": "1673477132",
        "totalValueLockedUSD": "204239.24879589598401614279309288"
      },
      {
        "timestamp": "1673393585",
        "totalValueLockedUSD": "172218.53061301542833565582265058"
      },
      {
        "timestamp": "1673307811",
        "totalValueLockedUSD": "164756.5735527306247735244596974"
      },
      {
        "timestamp": "1673220266",
        "totalValueLockedUSD": "163432.3305607144825579933840171"
      },
      {
        "timestamp": "1673134339",
        "totalValueLockedUSD": "157944.58182425508322412556561224"
      },
      {
        "timestamp": "1673046351",
        "totalValueLockedUSD": "158458.01643571362913625571640332"
      },
      {
        "timestamp": "1672962985",
        "totalValueLockedUSD": "158850.67262386852850597214716328"
      },
      {
        "timestamp": "1672876759",
        "totalValueLockedUSD": "163149.8015577274634050857258396"
      },
      {
        "timestamp": "1672788650",
        "totalValueLockedUSD": "153172.17434557922378095761818558"
      },
      {
        "timestamp": "1672696778",
        "totalValueLockedUSD": "151160.20530998585405914664535648"
      },
      {
        "timestamp": "1672617423",
        "totalValueLockedUSD": "146459.95668259609389286048595968"
      },
      {
        "timestamp": "1672526266",
        "totalValueLockedUSD": "147141.5895617578517423921850823"
      },
      {
        "timestamp": "1672444501",
        "totalValueLockedUSD": "147037.1337507961135329667542597"
      },
      {
        "timestamp": "1672358057",
        "totalValueLockedUSD": "148326.07662732087359196370648832"
      },
      {
        "timestamp": "1672271709",
        "totalValueLockedUSD": "149021.6365303885683359523725713"
      },
      {
        "timestamp": "1672179312",
        "totalValueLockedUSD": "154045.23295921881642256791448029"
      },
      {
        "timestamp": "1672098471",
        "totalValueLockedUSD": "155064.6548836987704421045465193"
      },
      {
        "timestamp": "1672012113",
        "totalValueLockedUSD": "154855.073890411123051841780816"
      },
      {
        "timestamp": "1671916808",
        "totalValueLockedUSD": "154764.10653094906032628641283956"
      },
      {
        "timestamp": "1671839411",
        "totalValueLockedUSD": "156613.22805617908210782441073073"
      },
      {
        "timestamp": "1671750772",
        "totalValueLockedUSD": "157402.7051356318369811866227646"
      },
      {
        "timestamp": "1671661939",
        "totalValueLockedUSD": "155312.6914214434828707126626356"
      },
      {
        "timestamp": "1671580088",
        "totalValueLockedUSD": "159111.3335589054680736089620143"
      },
      {
        "timestamp": "1671489521",
        "totalValueLockedUSD": "149692.5565263206368007119645776"
      },
      {
        "timestamp": "1671407304",
        "totalValueLockedUSD": "158851.48873583385359205199237852"
      },
      {
        "timestamp": "1671321173",
        "totalValueLockedUSD": "158852.8089924895192660773878098"
      },
      {
        "timestamp": "1671234748",
        "totalValueLockedUSD": "155473.18228716201028857271810178"
      },
      {
        "timestamp": "1671146835",
        "totalValueLockedUSD": "170454.15022191202875305408267736"
      },
      {
        "timestamp": "1671062202",
        "totalValueLockedUSD": "177337.31048015244502701644264219"
      },
      {
        "timestamp": "1670975964",
        "totalValueLockedUSD": "176283.14099291733384113692925881"
      },
      {
        "timestamp": "1670889587",
        "totalValueLockedUSD": "165173.28872477530584519667326888"
      },
      {
        "timestamp": "1670802146",
        "totalValueLockedUSD": "160813.08141939894197627251314312"
      },
      {
        "timestamp": "1670716578",
        "totalValueLockedUSD": "166183.50442088075641235672622228"
      },
      {
        "timestamp": "1670628420",
        "totalValueLockedUSD": "165746.69634663538134259951738878"
      },
      {
        "timestamp": "1670543506",
        "totalValueLockedUSD": "165382.46134944004263280113186"
      },
      {
        "timestamp": "1670457414",
        "totalValueLockedUSD": "163561.63022111352948361954514403"
      },
      {
        "timestamp": "1670370493",
        "totalValueLockedUSD": "168071.73107181536575878054763584"
      },
      {
        "timestamp": "1670282861",
        "totalValueLockedUSD": "166689.14716160091748384158586722"
      },
      {
        "timestamp": "1670195720",
        "totalValueLockedUSD": "169739.2356270203124528312469726"
      },
      {
        "timestamp": "1670107733",
        "totalValueLockedUSD": "165880.33865395591580273148538968"
      },
      {
        "timestamp": "1670025399",
        "totalValueLockedUSD": "166901.78863334593975785046040205"
      },
      {
        "timestamp": "1669938676",
        "totalValueLockedUSD": "159233.6895313158420160576409515"
      },
      {
        "timestamp": "1669851800",
        "totalValueLockedUSD": "162446.0308139916146285230910013"
      },
      {
        "timestamp": "1669766184",
        "totalValueLockedUSD": "154222.1352393338415443836400914"
      },
      {
        "timestamp": "1669678972",
        "totalValueLockedUSD": "153788.37841275162094660014521052"
      },
      {
        "timestamp": "1669593126",
        "totalValueLockedUSD": "159306.87557444991793602932607565"
      },
      {
        "timestamp": "1669507064",
        "totalValueLockedUSD": "157380.85006781706139289728317958"
      },
      {
        "timestamp": "1669420750",
        "totalValueLockedUSD": "158242.11464661069172957590764083"
      },
      {
        "timestamp": "1669334320",
        "totalValueLockedUSD": "159891.56703235632604711165117679"
      },
      {
        "timestamp": "1669246333",
        "totalValueLockedUSD": "160216.44206718580497178715317725"
      },
      {
        "timestamp": "1669159316",
        "totalValueLockedUSD": "151981.29676374990764430935656194"
      },
      {
        "timestamp": "1669074661",
        "totalValueLockedUSD": "145908.98668368485413721998677474"
      },
      {
        "timestamp": "1668987809",
        "totalValueLockedUSD": "150204.24977021174661433261785828"
      },
      {
        "timestamp": "1668902389",
        "totalValueLockedUSD": "159134.09748148280822407150042736"
      },
      {
        "timestamp": "1668814346",
        "totalValueLockedUSD": "159898.61394270912052564401649632"
      },
      {
        "timestamp": "1668728994",
        "totalValueLockedUSD": "159885.58216899441490172787301741"
      },
      {
        "timestamp": "1668638514",
        "totalValueLockedUSD": "161074.88387832006288230448525704"
      },
      {
        "timestamp": "1668556154",
        "totalValueLockedUSD": "169674.63346788395323361181970444"
      },
      {
        "timestamp": "1668470164",
        "totalValueLockedUSD": "164599.50979473422283655423719066"
      },
      {
        "timestamp": "1668382009",
        "totalValueLockedUSD": "161734.83666550260391611166181202"
      },
      {
        "timestamp": "1668297523",
        "totalValueLockedUSD": "163483.32135781048451814304489288"
      },
      {
        "timestamp": "1668210700",
        "totalValueLockedUSD": "175362.0657952380518122249073668"
      },
      {
        "timestamp": "1668122193",
        "totalValueLockedUSD": "261012.87346959944173530337736594"
      },
      {
        "timestamp": "1668036416",
        "totalValueLockedUSD": "213878.62976426941838422800950225"
      },
      {
        "timestamp": "1667951093",
        "totalValueLockedUSD": "271455.68073746312460311599897668"
      },
      {
        "timestamp": "1667864918",
        "totalValueLockedUSD": "325693.69358700229170677823964703"
      },
      {
        "timestamp": "1667776989",
        "totalValueLockedUSD": "331213.97669179192220213716833532"
      },
      {
        "timestamp": "1667689670",
        "totalValueLockedUSD": "355990.93537611569151580742547864"
      },
      {
        "timestamp": "1667605275",
        "totalValueLockedUSD": "349109.66610501500050407212831208"
      },
      {
        "timestamp": "1667518743",
        "totalValueLockedUSD": "325671.1570899952019869447542386"
      },
      {
        "timestamp": "1667432026",
        "totalValueLockedUSD": "322587.29694373826132439268638336"
      },
      {
        "timestamp": "1667346555",
        "totalValueLockedUSD": "336970.1955539578276986488019916"
      },
      {
        "timestamp": "1667256452",
        "totalValueLockedUSD": "344567.32906045853739645903800942"
      },
      {
        "timestamp": "1667171005",
        "totalValueLockedUSD": "326500.41199129910855621273731626"
      },
      {
        "timestamp": "1667087767",
        "totalValueLockedUSD": "328002.04099253125641682807272085"
      },
      {
        "timestamp": "1666995206",
        "totalValueLockedUSD": "327217.23917706958066907160331486"
      },
      {
        "timestamp": "1666915028",
        "totalValueLockedUSD": "321069.079383890804984489363991"
      },
      {
        "timestamp": "1666828513",
        "totalValueLockedUSD": "322386.63202722052230461244098838"
      },
      {
        "timestamp": "1666734431",
        "totalValueLockedUSD": "312772.8852215546245328229980637"
      },
      {
        "timestamp": "1666652650",
        "totalValueLockedUSD": "298851.42836808419750544504221296"
      },
      {
        "timestamp": "1666568620",
        "totalValueLockedUSD": "308804.60107773126877759573726132"
      },
      {
        "timestamp": "1666481875",
        "totalValueLockedUSD": "294849.46381490070573936679539663"
      },
      {
        "timestamp": "1666394120",
        "totalValueLockedUSD": "296621.59031639888551550446823948"
      },
      {
        "timestamp": "1666305171",
        "totalValueLockedUSD": "287443.1029917709893688182932351"
      },
      {
        "timestamp": "1666223454",
        "totalValueLockedUSD": "284971.89720205637347267643440988"
      },
      {
        "timestamp": "1666137280",
        "totalValueLockedUSD": "299067.39356886115867572649450503"
      },
      {
        "timestamp": "1666046985",
        "totalValueLockedUSD": "303269.1905423665190254334407625"
      },
      {
        "timestamp": "1665964128",
        "totalValueLockedUSD": "295754.28238660217044454012547905"
      },
      {
        "timestamp": "1665876147",
        "totalValueLockedUSD": "223680.99074099957321790825152064"
      },
      {
        "timestamp": "1665788740",
        "totalValueLockedUSD": "227137.50563162708697630202343074"
      },
      {
        "timestamp": "1665701743",
        "totalValueLockedUSD": "227527.8688695300193793372886687"
      },
      {
        "timestamp": "1665619069",
        "totalValueLockedUSD": "232142.61224470718182758899424475"
      },
      {
        "timestamp": "1665527764",
        "totalValueLockedUSD": "232318.4556214661066183713315654"
      },
      {
        "timestamp": "1665445379",
        "totalValueLockedUSD": "236281.11423687260679415469069708"
      },
      {
        "timestamp": "1665357067",
        "totalValueLockedUSD": "243610.27565267795534563390790285"
      },
      {
        "timestamp": "1665272716",
        "totalValueLockedUSD": "242526.17282610519209660726177207"
      },
      {
        "timestamp": "1665186245",
        "totalValueLockedUSD": "243641.6993854656028121789926476"
      },
      {
        "timestamp": "1665100785",
        "totalValueLockedUSD": "244612.34407819302497052053538939"
      },
      {
        "timestamp": "1665013841",
        "totalValueLockedUSD": "247739.26888595397854789097320248"
      },
      {
        "timestamp": "1664925050",
        "totalValueLockedUSD": "247838.05008673930973888810625454"
      },
      {
        "timestamp": "1664840235",
        "totalValueLockedUSD": "244584.84636575978348871472426016"
      },
      {
        "timestamp": "1664753863",
        "totalValueLockedUSD": "235344.61323395964976619807390872"
      },
      {
        "timestamp": "1664666567",
        "totalValueLockedUSD": "242019.28027315711619295125590044"
      },
      {
        "timestamp": "1664581771",
        "totalValueLockedUSD": "244192.59870186005198145495528516"
      },
      {
        "timestamp": "1664495655",
        "totalValueLockedUSD": "245914.42235251444278458229754096"
      },
      {
        "timestamp": "1664409437",
        "totalValueLockedUSD": "244401.42447950529971313529790684"
      },
      {
        "timestamp": "1664323192",
        "totalValueLockedUSD": "244869.87892875901040139291606823"
      },
      {
        "timestamp": "1664236431",
        "totalValueLockedUSD": "246736.31125193244336694242587832"
      },
      {
        "timestamp": "1664150122",
        "totalValueLockedUSD": "245427.6934531758350996782569984"
      },
      {
        "timestamp": "1664049606",
        "totalValueLockedUSD": "247571.86189501813061175480998869"
      },
      {
        "timestamp": "1663958823",
        "totalValueLockedUSD": "237682.61203318628779793433478874"
      },
      {
        "timestamp": "1663852644",
        "totalValueLockedUSD": "238192.57620586216350133891600894"
      },
      {
        "timestamp": "1663558424",
        "totalValueLockedUSD": "225926.52130527172591407278246368"
      },
      {
        "timestamp": "1663486822",
        "totalValueLockedUSD": "251988.1809558418659763888442968"
      },
      {
        "timestamp": "1663441688",
        "totalValueLockedUSD": "251655.9773728369909306466365504"
      },
      {
        "timestamp": "1663364892",
        "totalValueLockedUSD": "246642.46327651651546206866101848"
      },
      {
        "timestamp": "1663193077",
        "totalValueLockedUSD": "259613.02056509565923790527371555"
      },
      {
        "timestamp": "1663079149",
        "totalValueLockedUSD": "268987.2086059098245496707264687"
      },
      {
        "timestamp": "1662980580",
        "totalValueLockedUSD": "289765.33714195682616588768096974"
      },
      {
        "timestamp": "1662895497",
        "totalValueLockedUSD": "275023.1486302089460684321966656"
      },
      {
        "timestamp": "1662827341",
        "totalValueLockedUSD": "271084.92178509614413226652039178"
      },
      {
        "timestamp": "1662756344",
        "totalValueLockedUSD": "272060.83917240576823858363415424"
      },
      {
        "timestamp": "1662647835",
        "totalValueLockedUSD": "258104.78466477376080723341125266"
      },
      {
        "timestamp": "1662579929",
        "totalValueLockedUSD": "256614.052011895564870324861934"
      },
      {
        "timestamp": "1662452724",
        "totalValueLockedUSD": "273619.93396773141892135978636645"
      },
      {
        "timestamp": "1662386610",
        "totalValueLockedUSD": "255141.81193686535602746065033308"
      },
      {
        "timestamp": "1662292750",
        "totalValueLockedUSD": "258907.7180763789390905838193313"
      },
      {
        "timestamp": "1662166051",
        "totalValueLockedUSD": "260547.62320466556388266169373184"
      },
      {
        "timestamp": "1662154772",
        "totalValueLockedUSD": "259016.6193807791000237741429623"
      },
      {
        "timestamp": "1662071382",
        "totalValueLockedUSD": "264409.13302011544314590996464"
      },
      {
        "timestamp": "1661907830",
        "totalValueLockedUSD": "267769.59028574851630499099945644"
      },
      {
        "timestamp": "1661898464",
        "totalValueLockedUSD": "264961.72787027165964537076730911"
      },
      {
        "timestamp": "1661767107",
        "totalValueLockedUSD": "246577.26758361727499239563940832"
      },
      {
        "timestamp": "1661673767",
        "totalValueLockedUSD": "274268.81524478009137574802089068"
      },
      {
        "timestamp": "1661541641",
        "totalValueLockedUSD": "293088.77637268390411216447825584"
      },
      {
        "timestamp": "1661415740",
        "totalValueLockedUSD": "318480.2151943958420175152771652"
      },
      {
        "timestamp": "1661365991",
        "totalValueLockedUSD": "315325.0679964589560524158579743"
      },
      {
        "timestamp": "1661280889",
        "totalValueLockedUSD": "315371.13808271696275807250762064"
      },
      {
        "timestamp": "1661207400",
        "totalValueLockedUSD": "299986.31739697519778801621667674"
      },
      {
        "timestamp": "1661126316",
        "totalValueLockedUSD": "311421.25063132446046027486693425"
      },
      {
        "timestamp": "1661039697",
        "totalValueLockedUSD": "302476.30937568009075714257074916"
      },
      {
        "timestamp": "1660953273",
        "totalValueLockedUSD": "305270.6229448673499934696493865"
      },
      {
        "timestamp": "1660840727",
        "totalValueLockedUSD": "345535.8812472482892141161174853"
      },
      {
        "timestamp": "1660752367",
        "totalValueLockedUSD": "354443.59802378641564716650175436"
      },
      {
        "timestamp": "1660690795",
        "totalValueLockedUSD": "364051.81002935002770057561268518"
      },
      {
        "timestamp": "1660579584",
        "totalValueLockedUSD": "369850.63980840579132320587356043"
      },
      {
        "timestamp": "1660491629",
        "totalValueLockedUSD": "379715.1026280435832492289977648"
      },
      {
        "timestamp": "1660403175",
        "totalValueLockedUSD": "388666.99962011121320211572563144"
      },
      {
        "timestamp": "1660347469",
        "totalValueLockedUSD": "386277.52162611360540030857993498"
      },
      {
        "timestamp": "1660262397",
        "totalValueLockedUSD": "405081.57490803021876474853213364"
      },
      {
        "timestamp": "1660151250",
        "totalValueLockedUSD": "412820.28060869652539330715835866"
      },
      {
        "timestamp": "1660079299",
        "totalValueLockedUSD": "389687.04036423255715910769373776"
      },
      {
        "timestamp": "1660000286",
        "totalValueLockedUSD": "399071.51675487316379671206848713"
      },
      {
        "timestamp": "1659916788",
        "totalValueLockedUSD": "393734.3420330950323686418436752"
      },
      {
        "timestamp": "1659811204",
        "totalValueLockedUSD": "375834.1745472569487606658642623"
      },
      {
        "timestamp": "1659730511",
        "totalValueLockedUSD": "344900.10349783263856501153598911"
      },
      {
        "timestamp": "1659655702",
        "totalValueLockedUSD": "349018.68525986511841263762783107"
      },
      {
        "timestamp": "1659548871",
        "totalValueLockedUSD": "349031.2605702259490223139686798"
      },
      {
        "timestamp": "1659449515",
        "totalValueLockedUSD": "327128.66620111507641846574157363"
      },
      {
        "timestamp": "1659398389",
        "totalValueLockedUSD": "1972549.9650742219913254984513547"
      },
      {
        "timestamp": "1659309262",
        "totalValueLockedUSD": "1978430.36589810648984888612549934"
      },
      {
        "timestamp": "1659152249",
        "totalValueLockedUSD": "2038546.85815540018416926644406784"
      },
      {
        "timestamp": "1659120354",
        "totalValueLockedUSD": "2062851.67428622852604076117394123"
      },
      {
        "timestamp": "1659015075",
        "totalValueLockedUSD": "1969614.51481655168893457812435677"
      },
      {
        "timestamp": "1658893430",
        "totalValueLockedUSD": "1726940.2909115811711150765014368"
      },
      {
        "timestamp": "1658843223",
        "totalValueLockedUSD": "1739304.12759744177499537561789818"
      },
      {
        "timestamp": "1658719207",
        "totalValueLockedUSD": "1891382.40087489430896459344664965"
      },
      {
        "timestamp": "1658699576",
        "totalValueLockedUSD": "2058050.2185351116445447712074726"
      },
      {
        "timestamp": "1658620021",
        "totalValueLockedUSD": "2017577.64271989581454254780289316"
      },
      {
        "timestamp": "1658533173",
        "totalValueLockedUSD": "2083716.68899830915277097241941889"
      },
      {
        "timestamp": "1658444160",
        "totalValueLockedUSD": "2329351.24343485531691365115662671"
      },
      {
        "timestamp": "1658324331",
        "totalValueLockedUSD": "2444599.91322261731526858580656786"
      },
      {
        "timestamp": "1658262416",
        "totalValueLockedUSD": "2358020.9797973605078524751139342"
      },
      {
        "timestamp": "1658186021",
        "totalValueLockedUSD": "2208837.66401063475627051702956256"
      },
      {
        "timestamp": "1658070292",
        "totalValueLockedUSD": "2003068.99463052443898894665019966"
      },
      {
        "timestamp": "1657947885",
        "totalValueLockedUSD": "1802156.9842200811466401295544799"
      },
      {
        "timestamp": "1657929581",
        "totalValueLockedUSD": "1816381.21576252976296736016805659"
      },
      {
        "timestamp": "1657832687",
        "totalValueLockedUSD": "1849603.4434880091546746253812066"
      },
      {
        "timestamp": "1657740331",
        "totalValueLockedUSD": "1672089.55789654125603665938476255"
      },
      {
        "timestamp": "1657612062",
        "totalValueLockedUSD": "1616516.16217633284912940778459694"
      },
      {
        "timestamp": "1657572728",
        "totalValueLockedUSD": "1694357.47038746487137663267586528"
      },
      {
        "timestamp": "1657459022",
        "totalValueLockedUSD": "1793046.16157235945909537000597081"
      },
      {
        "timestamp": "1657359408",
        "totalValueLockedUSD": "1864596.125333511502921360768716"
      },
      {
        "timestamp": "1657308057",
        "totalValueLockedUSD": "1886210.659901861182954924833919"
      },
      {
        "timestamp": "1657234498",
        "totalValueLockedUSD": "1920978.7445855507056354880395176"
      },
      {
        "timestamp": "1657136943",
        "totalValueLockedUSD": "1816926.1267678649159936199548303"
      },
      {
        "timestamp": "1657037209",
        "totalValueLockedUSD": "1626163.05172891100402203595724651"
      },
      {
        "timestamp": "1656979167",
        "totalValueLockedUSD": "1683071.26679241465077332596614409"
      },
      {
        "timestamp": "1656892235",
        "totalValueLockedUSD": "1559480.31533013319923046111266684"
      },
      {
        "timestamp": "1656800869",
        "totalValueLockedUSD": "1545770.8970649041098959327799696"
      },
      {
        "timestamp": "1656719036",
        "totalValueLockedUSD": "1527329.32400118870713665252082756"
      },
      {
        "timestamp": "1656633333",
        "totalValueLockedUSD": "1575153.27471919452164596896040236"
      },
      {
        "timestamp": "1656547143",
        "totalValueLockedUSD": "1647045.43106958380703738848476"
      },
      {
        "timestamp": "1656455715",
        "totalValueLockedUSD": "1699732.509847950931392966839406"
      },
      {
        "timestamp": "1656369575",
        "totalValueLockedUSD": "1760487.38440631177931905368944"
      },
      {
        "timestamp": "1656277530",
        "totalValueLockedUSD": "1872071.038629257741618971695738"
      },
      {
        "timestamp": "1656168316",
        "totalValueLockedUSD": "1826608.608327609267545356956216"
      },
      {
        "timestamp": "1656085058",
        "totalValueLockedUSD": "1730293.879513441846593410515827"
      },
      {
        "timestamp": "1655972786",
        "totalValueLockedUSD": "1566344.91300551225052447470818"
      },
      {
        "timestamp": "1655906543",
        "totalValueLockedUSD": "1541391.739778880720475149585004"
      },
      {
        "timestamp": "1655771708",
        "totalValueLockedUSD": "1491739.839637044769527866134088"
      },
      {
        "timestamp": "1655721149",
        "totalValueLockedUSD": "1520771.869412904442899938839194"
      },
      {
        "timestamp": "1655681937",
        "totalValueLockedUSD": "1445726.514799102823261456942425"
      },
      {
        "timestamp": "1655565289",
        "totalValueLockedUSD": "1330440.450587924745388690438174"
      },
      {
        "timestamp": "1655503036",
        "totalValueLockedUSD": "1447543.971286948023947031198856"
      },
      {
        "timestamp": "1655411824",
        "totalValueLockedUSD": "1458404.507111765661834108615326"
      },
      {
        "timestamp": "1655301338",
        "totalValueLockedUSD": "1448037.738478169294910939426327"
      },
      {
        "timestamp": "1655234252",
        "totalValueLockedUSD": "1434651.222826276664577774837164"
      },
      {
        "timestamp": "1655161625",
        "totalValueLockedUSD": "1386818.895793883136405776754365"
      },
      {
        "timestamp": "1655072677",
        "totalValueLockedUSD": "1622779.505652898209099200899275"
      },
      {
        "timestamp": "1654991680",
        "totalValueLockedUSD": "1768076.513287160820391552427142"
      },
      {
        "timestamp": "1654880316",
        "totalValueLockedUSD": "2012760.524366572775911648711824"
      },
      {
        "timestamp": "1654814859",
        "totalValueLockedUSD": "2158729.651110230512852987391648"
      },
      {
        "timestamp": "1654685794",
        "totalValueLockedUSD": "2172327.182488977053998424886195"
      },
      {
        "timestamp": "1654556957",
        "totalValueLockedUSD": "2293871.4392769038775613676382"
      },
      {
        "timestamp": "1654435643",
        "totalValueLockedUSD": "2167841.171496866906606434404"
      },
      {
        "timestamp": "1654386299",
        "totalValueLockedUSD": "2168194.886451261932965950475232"
      },
      {
        "timestamp": "1654284992",
        "totalValueLockedUSD": "2027411.653941509650904890976112"
      },
      {
        "timestamp": "1654185626",
        "totalValueLockedUSD": "2165409.0784340766281437262355"
      },
      {
        "timestamp": "1654069451",
        "totalValueLockedUSD": "2279528.862444792788409680828787"
      },
      {
        "timestamp": "1653965981",
        "totalValueLockedUSD": "2537456.109070978343667066182326"
      },
      {
        "timestamp": "1653938107",
        "totalValueLockedUSD": "2409944.123516630922337856130105"
      },
      {
        "timestamp": "1653725261",
        "totalValueLockedUSD": "2030869.967064638724172305508032"
      },
      {
        "timestamp": "1653686657",
        "totalValueLockedUSD": "2019435.938187885092895373494644"
      },
      {
        "timestamp": "1653602364",
        "totalValueLockedUSD": "2139782.226459542364127917243474"
      },
      {
        "timestamp": "1653519372",
        "totalValueLockedUSD": "2451258.864389699096140371143568"
      },
      {
        "timestamp": "1653416588",
        "totalValueLockedUSD": "2536759.140876315353210840579144"
      },
      {
        "timestamp": "1653344492",
        "totalValueLockedUSD": "2619669.383736752834987878429656"
      },
      {
        "timestamp": "1653263296",
        "totalValueLockedUSD": "2833128.311507041892143342636145"
      },
      {
        "timestamp": "1653173699",
        "totalValueLockedUSD": "2615300.140363375063373909082216"
      },
      {
        "timestamp": "1653084140",
        "totalValueLockedUSD": "2593314.869627545218551968937056"
      },
      {
        "timestamp": "1652952988",
        "totalValueLockedUSD": "2516431.961337252442570737751244"
      },
      {
        "timestamp": "1652881577",
        "totalValueLockedUSD": "2823818.989495716122344863875389"
      },
      {
        "timestamp": "1652829739",
        "totalValueLockedUSD": "3078400.56848627489869155667353"
      },
      {
        "timestamp": "1652728640",
        "totalValueLockedUSD": "2947923.28279459431958087435648"
      },
      {
        "timestamp": "1652655301",
        "totalValueLockedUSD": "3268820.48008258537546188722424"
      },
      {
        "timestamp": "1652568140",
        "totalValueLockedUSD": "2903277.00726466868330879584294"
      },
      {
        "timestamp": "1652459834",
        "totalValueLockedUSD": "3047133.951050838759381122983755"
      },
      {
        "timestamp": "1652354349",
        "totalValueLockedUSD": "2797447.902882447080816254353285"
      },
      {
        "timestamp": "1652310430",
        "totalValueLockedUSD": "3078814.456443879704162300534648"
      },
      {
        "timestamp": "1652175952",
        "totalValueLockedUSD": "4694590.780957437682867253525082"
      },
      {
        "timestamp": "1652044903",
        "totalValueLockedUSD": "5256095.51171355568941418226964"
      },
      {
        "timestamp": "1651961401",
        "totalValueLockedUSD": "5557392.45597188157118862836448"
      },
      {
        "timestamp": "1651872146",
        "totalValueLockedUSD": "5796874.708805923154259534131115"
      },
      {
        "timestamp": "1651721007",
        "totalValueLockedUSD": "6787128.924653706452322612303645"
      },
      {
        "timestamp": "1651678170",
        "totalValueLockedUSD": "6032194.21383246133151401781037"
      },
      {
        "timestamp": "1651583649",
        "totalValueLockedUSD": "6101435.32875439216276403996516"
      },
      {
        "timestamp": "1651476259",
        "totalValueLockedUSD": "5933789.38647328394392010207628"
      },
      {
        "timestamp": "1651436928",
        "totalValueLockedUSD": "5764595.717458560937299520958112"
      },
      {
        "timestamp": "1651357604",
        "totalValueLockedUSD": "5729262.138677395113003383975371"
      },
      {
        "timestamp": "1651274809",
        "totalValueLockedUSD": "6312867.91992051049200174645913"
      },
      {
        "timestamp": "1651185056",
        "totalValueLockedUSD": "6724244.07655553701530585385238"
      },
      {
        "timestamp": "1651091370",
        "totalValueLockedUSD": "6974990.92311614394600367432864"
      },
      {
        "timestamp": "1651017059",
        "totalValueLockedUSD": "6882699.029575745578529583008736"
      },
      {
        "timestamp": "1650924182",
        "totalValueLockedUSD": "7183954.053518664353500923827145"
      },
      {
        "timestamp": "1650823166",
        "totalValueLockedUSD": "7142720.691795970794800737597422"
      },
      {
        "timestamp": "1650745141",
        "totalValueLockedUSD": "7345825.38644122267669063918512"
      },
      {
        "timestamp": "1650669025",
        "totalValueLockedUSD": "7428062.312341356720779063434036"
      },
      {
        "timestamp": "1650568701",
        "totalValueLockedUSD": "7654699.170194757880292580581475"
      },
      {
        "timestamp": "1650467831",
        "totalValueLockedUSD": "4522898.15672609825766935442468"
      },
      {
        "timestamp": "1650409572",
        "totalValueLockedUSD": "3900846.564942437964643506509793"
      },
      {
        "timestamp": "1650303274",
        "totalValueLockedUSD": "3619874.442062727338565384776244"
      },
      {
        "timestamp": "1650222018",
        "totalValueLockedUSD": "3689129.455677345583557009250752"
      },
      {
        "timestamp": "1650109175",
        "totalValueLockedUSD": "3690757.38844251857531039776812"
      },
      {
        "timestamp": "1650060018",
        "totalValueLockedUSD": "3671864.584011896766044499170325"
      },
      {
        "timestamp": "1649976917",
        "totalValueLockedUSD": "3636842.279977313869690619829575"
      },
      {
        "timestamp": "1649892098",
        "totalValueLockedUSD": "1707457.728633031992632172362595"
      },
      {
        "timestamp": "1649797214",
        "totalValueLockedUSD": "1499851.306774701003219864354424"
      },
      {
        "timestamp": "1649704126",
        "totalValueLockedUSD": "1498527.59878249110827975547213"
      },
      {
        "timestamp": "1649608668",
        "totalValueLockedUSD": "1639885.411454350625378639319486"
      },
      {
        "timestamp": "1649546426",
        "totalValueLockedUSD": "1616824.00731804466041829740912"
      },
      {
        "timestamp": "1649454381",
        "totalValueLockedUSD": "1564942.021300974270586671010148"
      },
      {
        "timestamp": "1649363837",
        "totalValueLockedUSD": "1661190.073630477689697282313076"
      },
      {
        "timestamp": "1649286283",
        "totalValueLockedUSD": "1618693.330834705613530915464136"
      },
      {
        "timestamp": "1649181042",
        "totalValueLockedUSD": "1693237.086009304394232392972594"
      },
      {
        "timestamp": "1649114832",
        "totalValueLockedUSD": "1705692.960229008224640842451192"
      },
      {
        "timestamp": "1649011392",
        "totalValueLockedUSD": "1692471.653617068071238027204965"
      },
      {
        "timestamp": "1648938671",
        "totalValueLockedUSD": "1705243.346241019101636740647775"
      },
      {
        "timestamp": "1648848139",
        "totalValueLockedUSD": "1740388.218486330733125999482448"
      },
      {
        "timestamp": "1648749614",
        "totalValueLockedUSD": "1695995.578902488834600818546179"
      },
      {
        "timestamp": "1648683729",
        "totalValueLockedUSD": "1687789.957491278327997008037962"
      },
      {
        "timestamp": "1648587837",
        "totalValueLockedUSD": "1683630.637537075784449352301352"
      },
      {
        "timestamp": "1648499614",
        "totalValueLockedUSD": "1686328.820040832411074842522772"
      },
      {
        "timestamp": "1648413108",
        "totalValueLockedUSD": "1519005.00504378954519503346055"
      },
      {
        "timestamp": "1648338622",
        "totalValueLockedUSD": "1535345.8429568418719182025032"
      },
      {
        "timestamp": "1648234570",
        "totalValueLockedUSD": "2018711.031232144360051198357792"
      },
      {
        "timestamp": "1648149187",
        "totalValueLockedUSD": "2165340.03586558490808198960753"
      },
      {
        "timestamp": "1648067071",
        "totalValueLockedUSD": "2013017.463635458162225032867814"
      },
      {
        "timestamp": "1647976593",
        "totalValueLockedUSD": "2051303.739432847556501647830888"
      },
      {
        "timestamp": "1647893457",
        "totalValueLockedUSD": "2080491.470304621836825047141338"
      },
      {
        "timestamp": "1647814457",
        "totalValueLockedUSD": "2038948.67325081279627518179051"
      },
      {
        "timestamp": "1647728230",
        "totalValueLockedUSD": "2112317.69900073893700324434331"
      },
      {
        "timestamp": "1647636280",
        "totalValueLockedUSD": "2104313.355341282531703897899749"
      },
      {
        "timestamp": "1647541036",
        "totalValueLockedUSD": "1926836.555114633519875995625436"
      },
      {
        "timestamp": "1647465379",
        "totalValueLockedUSD": "1808720.087996356507392752970144"
      },
      {
        "timestamp": "1647387088",
        "totalValueLockedUSD": "1628062.76145546266889461336718"
      },
      {
        "timestamp": "1647298478",
        "totalValueLockedUSD": "1550240.463563945900213415252324"
      },
      {
        "timestamp": "1647200857",
        "totalValueLockedUSD": "1589776.11101439095554966756275"
      },
      {
        "timestamp": "1647124787",
        "totalValueLockedUSD": "1565082.681574134404569698567119"
      },
      {
        "timestamp": "1647039092",
        "totalValueLockedUSD": "1437512.44301434129997358607015"
      },
      {
        "timestamp": "1646955259",
        "totalValueLockedUSD": "1127436.08925909924553262729264"
      },
      {
        "timestamp": "1646851098",
        "totalValueLockedUSD": "1175339.810933150498007148264892"
      },
      {
        "timestamp": "1646777631",
        "totalValueLockedUSD": "1092287.086601590307953809190695"
      },
      {
        "timestamp": "1646697191",
        "totalValueLockedUSD": "1037989.493256455336693930445693"
      },
      {
        "timestamp": "1646395872",
        "totalValueLockedUSD": "743976.199534984980112182247445"
      },
      {
        "timestamp": "1646342062",
        "totalValueLockedUSD": "776626.091366423560915971807663"
      },
      {
        "timestamp": "1646265197",
        "totalValueLockedUSD": "592534.938698478220832937678634"
      },
      {
        "timestamp": "1646177320",
        "totalValueLockedUSD": "327247.908232945226011812133356"
      },
      {
        "timestamp": "1646079807",
        "totalValueLockedUSD": "4.31235825"
      },
      {
        "timestamp": "1645648535",
        "totalValueLockedUSD": "0.75951384"
      }
    ]
  }
}

tvl = data["data"]["vaultDailySnapshots"]

header = [
    "timestamp",
    "totalValueLockedUSD"
]

with open("AVAX_TVL.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for position in tvl:
        position['timestamp'] = datetime.utcfromtimestamp(int(position['timestamp'])).strftime('%Y-%m-%d')
        writer.writerow(position)