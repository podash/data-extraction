import csv
import json
from datetime import datetime

data = {
  "data": {
    "vaultShortPositions": [
      {
        "mintAmount": "134699675583",
        "openedAt": "1697194187",
        "openTxhash": "0xc321125a134e9dabe4550ab2307191c8fd109c19c39a63bb8fbf30ac2d1583f6",
        "premiumEarned": "2963392862826000000",
        "strikePrice": "7200000000"
      },
      {
        "mintAmount": "135636309712",
        "openedAt": "1696588499",
        "openTxhash": "0xc1a4ccfa0878e4d146b0b04b453ee450dc1a274b5fbbeefd7b2fe522e518a7c4",
        "premiumEarned": "6510542866176000000",
        "strikePrice": "7600000000"
      },
      {
        "mintAmount": "153378814163",
        "openedAt": "1695984119",
        "openTxhash": "0x1aa2390663c2401caa2f9f4e19e6c1affce8944cac31c4bc66632a98ab6a7a75",
        "premiumEarned": "3834470354075000000",
        "strikePrice": "7600000000"
      },
      {
        "mintAmount": "153229135185",
        "openedAt": "1695379427",
        "openTxhash": "0xa38465e88bdab262b9202019f717f933cb9e83cfedd8ed511a4d19e01ed4d654",
        "premiumEarned": "3830728379625000000",
        "strikePrice": "7500000000"
      },
      {
        "mintAmount": "159378839826",
        "openedAt": "1694774231",
        "openTxhash": "0xe304760f2ad4d3b44f2df9cd5ba1e465acc3eeaac6ee8678696d71a6aa5c14c7",
        "premiumEarned": "5259501714258000000",
        "strikePrice": "6100000000"
      },
      {
        "mintAmount": "168349548646",
        "openedAt": "1694165975",
        "openTxhash": "0x5899b476a8d8a04c5306e6a6d5bd16d5dd6eccf0ec8ccda06ddd367fc55ea0c2",
        "premiumEarned": "6733981945840000000",
        "strikePrice": "6200000000"
      },
      {
        "mintAmount": "181857225427",
        "openedAt": "1693563371",
        "openTxhash": "0x5a8277a822a809f82b983247e2bcccb29f0b689f918f6e2dd6ee30d219b8cf91",
        "premiumEarned": "16367150288430000000",
        "strikePrice": "6100000000"
      },
      {
        "mintAmount": "342674373387",
        "openedAt": "1692958223",
        "openTxhash": "0xe5850c1f58c900e7994ee8590ef6c86a70884d084d1f7667c7afafe05b18354d",
        "premiumEarned": "7196161841127000000",
        "strikePrice": "6400000000"
      },
      {
        "mintAmount": "671910040101",
        "openedAt": "1692353135",
        "openTxhash": "0x809b88697e284bb42d4f60804f8c68be6a633dd8a2de8cb66a9b7b153866251b",
        "premiumEarned": "8062920481212000000",
        "strikePrice": "6700000000"
      },
      {
        "mintAmount": "694253513657",
        "openedAt": "1691748095",
        "openTxhash": "0x06fd4f947926f7cf13d7c8772b097481093ee09853d9f83b4c04b8cfce4128e6",
        "premiumEarned": "3471267568285000000",
        "strikePrice": "7800000000"
      },
      {
        "mintAmount": "692194046578",
        "openedAt": "1691143187",
        "openTxhash": "0x18637d8c04770e1f78191536bd780d55e20a199c733161e726b404667a79b88f",
        "premiumEarned": "17304851164450000000",
        "strikePrice": "7750000000"
      },
      {
        "mintAmount": "691588282316",
        "openedAt": "1690538603",
        "openTxhash": "0xf8b018382885441049dff46d8e602f10abfe9f9b758da2c9c7c3542f335b45c7",
        "premiumEarned": "11065412517056000000",
        "strikePrice": "8500000000"
      },
      {
        "mintAmount": "690789483860",
        "openedAt": "1689933947",
        "openTxhash": "0x99ff3ffe45f42401ca5af6cefc3d24d178812a11343b5e9b7979070864f9ce3c",
        "premiumEarned": "14506579161060000000",
        "strikePrice": "9100000000"
      },
      {
        "mintAmount": "677278689532",
        "openedAt": "1689329651",
        "openTxhash": "0x4d2dbf26fbc0d342f03d3f0d5681a2e8e3c8ca97b032c37844c51832f51b3eb8",
        "premiumEarned": "7450065584852000000",
        "strikePrice": "10000000000"
      },
      {
        "mintAmount": "689597721288",
        "openedAt": "1688727095",
        "openTxhash": "0xb2da4515865f8c2b410c09afd91861957c4b4dd066b5086231325d8e291955b2",
        "premiumEarned": "14481552147048000000",
        "strikePrice": "9300000000"
      },
      {
        "mintAmount": "688398679593",
        "openedAt": "1688119607",
        "openTxhash": "0x54673fd311c79a70cc59335d585d5487af8d09aae072a9d1915b96ce06d720b2",
        "premiumEarned": "18586764349011000000",
        "strikePrice": "8200000000"
      },
      {
        "mintAmount": "689773630546",
        "openedAt": "1687514639",
        "openTxhash": "0x505e029aeb379f06e257d33a2c8e0698c0f705daba68c4e2d2a44fde3e5d1c45",
        "premiumEarned": "24831850699656000000",
        "strikePrice": "6500000000"
      },
      {
        "mintAmount": "612855091736",
        "openedAt": "1686909995",
        "openTxhash": "0x928421bdd93f976550addda8961bdef2ad548071c9432e49b9060e851cdfceb7",
        "premiumEarned": "12869956926456000000",
        "strikePrice": "6200000000"
      },
      {
        "mintAmount": "615317054660",
        "openedAt": "1686305063",
        "openTxhash": "0x24efe3d32f1aec141095fa8a9d81d79165fa537efe48e2c829670fd29d8e5ba7",
        "premiumEarned": "14767609311840000000",
        "strikePrice": "6700000000"
      },
      {
        "mintAmount": "614670477310",
        "openedAt": "1685700443",
        "openTxhash": "0xb9d01a251c3e8a5f81a791202d830963459772d08e7f0a9d90fe068ec0eec820",
        "premiumEarned": "12908080023510000000",
        "strikePrice": "7000000000"
      },
      {
        "mintAmount": "808874919385",
        "openedAt": "1685095595",
        "openTxhash": "0x776b19439be5fc2cfadf402f1a2c20e3c9af84a3d5934d7c660baa614fcdd779",
        "premiumEarned": "16986373307085000000",
        "strikePrice": "7000000000"
      },
      {
        "mintAmount": "806499760792",
        "openedAt": "1684490771",
        "openTxhash": "0x7bb20c08515308730342b327d10b0086b7ad7724c28b60de5f3838480830d453",
        "premiumEarned": "33066490192472000000",
        "strikePrice": "7200000000"
      },
      {
        "mintAmount": "816124239517",
        "openedAt": "1683885935",
        "openTxhash": "0x5c3608e7da4357b14fa8b496f06b70cf774fab0f354e14c946d670825b34858f",
        "premiumEarned": "23667602945993000000",
        "strikePrice": "7000000000"
      },
      {
        "mintAmount": "813727794215",
        "openedAt": "1683288203",
        "openTxhash": "0xa63b2c53c294b3e9430662c3aabda85a9f018df54ccac8de81ace8a5ba4d067e",
        "premiumEarned": "33362839562815000000",
        "strikePrice": "7950000000"
      },
      {
        "mintAmount": "812376756913",
        "openedAt": "1682676503",
        "openTxhash": "0x1cddc84e986ba223010db170a5b26deae4c63ed91e021618991946aa56f8c02c",
        "premiumEarned": "21121795679738000000",
        "strikePrice": "8100000000"
      },
      {
        "mintAmount": "810354749525",
        "openedAt": "1682071415",
        "openTxhash": "0xcfd24bf964cb19f0960187236323d4cf137c5510b797d3b06484f94b8061c6f9",
        "premiumEarned": "29172770982900000000",
        "strikePrice": "8300000000"
      },
      {
        "mintAmount": "796755023152",
        "openedAt": "1681466615",
        "openTxhash": "0x23e3d6bea62f13ad0ff1fa5582ac047801c2c69fe339f67b63b29151d287a1fd",
        "premiumEarned": "17528610509344000000",
        "strikePrice": "10000000000"
      },
      {
        "mintAmount": "794783682050",
        "openedAt": "1680861947",
        "openTxhash": "0x4baf644e2772dbe87c8c8aabfa66fe48dfc4ab6dbdf9be1a1a341b969f2bb1c8",
        "premiumEarned": "19869592051250000000",
        "strikePrice": "9200000000"
      },
      {
        "mintAmount": "780665909864",
        "openedAt": "1680257027",
        "openTxhash": "0xbed5215d10f1c666e89501b9d3216514c0bc117ca78ca6d856fb2719e5b6ca24",
        "premiumEarned": "18735981836736000000",
        "strikePrice": "8200000000"
      },
      {
        "mintAmount": "1888962687607",
        "openedAt": "1679652443",
        "openTxhash": "0x8ab1981037914675c132a2dd23c37ad18c5aa3b181b6e54448a41e04967ebee4",
        "premiumEarned": "32112365689319000000",
        "strikePrice": "8800000000"
      },
      {
        "mintAmount": "1913517296194",
        "openedAt": "1679046707",
        "openTxhash": "0x6d1ea316c904c8218717bf45bb1701a2d6f4307ea02bc50ecc43209d33c70ec7",
        "premiumEarned": "59319036182014000000",
        "strikePrice": "9200000000"
      },
      {
        "mintAmount": "2078967575783",
        "openedAt": "1678442279",
        "openTxhash": "0x4f560d776bc49a799cce968a9b2ab4cd681450ca007dbeb3c705f2eb7ee31ed7",
        "premiumEarned": "47816254243009000000",
        "strikePrice": "8000000000"
      },
      {
        "mintAmount": "2105009545372",
        "openedAt": "1677837995",
        "openTxhash": "0x86aff06c3ea2bb091fb3b3753c6e6122cbb39f6cdcd7fbe6ceef5172f8458bfe",
        "premiumEarned": "61045276815788000000",
        "strikePrice": "9250000000"
      },
      {
        "mintAmount": "2990708328862",
        "openedAt": "1677233087",
        "openTxhash": "0x5420c31b6c74082c677bfb83ec95df90343cc8d032f8ef72f668fa42185eeeb9",
        "premiumEarned": "86730541536998000000",
        "strikePrice": "10300000000"
      },
      {
        "mintAmount": "2858987267557",
        "openedAt": "1676628275",
        "openTxhash": "0x658a474e65b65360d31e9c788156fc8976e1d0e5799e2cc2c863f5c098915007",
        "premiumEarned": "88628605294267000000",
        "strikePrice": "10200000000"
      },
      {
        "mintAmount": "2707214665045",
        "openedAt": "1676023511",
        "openTxhash": "0x1b1a800b89366bc6baa7fb3d05d7b453c8c6d92607713bf7f30819f6ee54da6c",
        "premiumEarned": "162432879902700000000",
        "strikePrice": "9400000000"
      },
      {
        "mintAmount": "2699598461780",
        "openedAt": "1675425131",
        "openTxhash": "0x8276f28702be333c5cb4b6261c6e62b18f2b85e6f71727f65ea79596e299786a",
        "premiumEarned": "151177513859680000000",
        "strikePrice": "10600000000"
      },
      {
        "mintAmount": "2701587850934",
        "openedAt": "1674813755",
        "openTxhash": "0x827872ecbabd681bafacae25cb4cd015e7a8056698973cfcb5cb27764a4f6714",
        "premiumEarned": "113466689739228000000",
        "strikePrice": "10400000000"
      },
      {
        "mintAmount": "2742804070729",
        "openedAt": "1674208859",
        "openTxhash": "0x7c02e676a34b4bbfdf3e44465620f0655973bd1322f590367a30822701f01bab",
        "premiumEarned": "74055709909683000000",
        "strikePrice": "10500000000"
      },
      {
        "mintAmount": "2876391581885",
        "openedAt": "1673604395",
        "openTxhash": "0x66937e90bd1de74430f0abed5760a709e8146fe7302bc6dab59466306eedcede",
        "premiumEarned": "117932054857285000000",
        "strikePrice": "8000000000"
      },
      {
        "mintAmount": "3262654331546",
        "openedAt": "1672999403",
        "openTxhash": "0x87a99760d0d3ae0f1d4a1fe099b891e6e34d5bb903ed1e590800207c9ffcb8af",
        "premiumEarned": "68515740962466000000",
        "strikePrice": "6250000000"
      },
      {
        "mintAmount": "3230294224952",
        "openedAt": "1672394651",
        "openTxhash": "0xeb9d9dc1d30dfa2f25206b355ca86eb8637db5b72f7dc8f5f5cce137e95174ed",
        "premiumEarned": "32302942249520000000",
        "strikePrice": "6250000000"
      },
      {
        "mintAmount": "3235015370364",
        "openedAt": "1671789767",
        "openTxhash": "0x221f7a19d9fbc891441646cb8b1584de8157b0d153be23dca3df4e6fe324885e",
        "premiumEarned": "48525230555460000000",
        "strikePrice": "6250000000"
      },
      {
        "mintAmount": "3219554095269",
        "openedAt": "1671184895",
        "openTxhash": "0x1cf099e909e1595174c97e4f26ebf4ed76dd57621c7cef8bb0f3eb68d92a11cc",
        "premiumEarned": "70830190095918000000",
        "strikePrice": "6750000000"
      },
      {
        "mintAmount": "3379337933413",
        "openedAt": "1670580299",
        "openTxhash": "0x276a62facd80039ed2ee1097a991edd427b045de831ff42b3174643d831484d6",
        "premiumEarned": "104759475935803000000",
        "strikePrice": "7250000000"
      },
      {
        "mintAmount": "3371994490566",
        "openedAt": "1669975343",
        "openTxhash": "0xcab25bc11e08aef1f40084cae6db8733d6d4af93238670860032a14032a37575",
        "premiumEarned": "134879779622640000000",
        "strikePrice": "7500000000"
      },
      {
        "mintAmount": "3431193215886",
        "openedAt": "1669370603",
        "openTxhash": "0x35fa15c571e206ca008271ea1bd0c4869597b2f0a0459f94abf7106b6e1d23e5",
        "premiumEarned": "181853240441958000000",
        "strikePrice": "6750000000"
      },
      {
        "mintAmount": "3399137410082",
        "openedAt": "1668765815",
        "openTxhash": "0x8e6100fd8b8d7add8fc4503b68a7d9b97cdf35e03ce7c752ebe98e35db5dc4e8",
        "premiumEarned": "142763771223444000000",
        "strikePrice": "7250000000"
      },
      {
        "mintAmount": "3254876127164",
        "openedAt": "1668161111",
        "openTxhash": "0x11886b86509478094a8c9589f3d4a5d1905dceee0418f91e5b45d8e9e17a003c",
        "premiumEarned": "35803637398804000000",
        "strikePrice": "9000000000"
      },
      {
        "mintAmount": "3388198866301",
        "openedAt": "1667556179",
        "openTxhash": "0x597152d34e03fb760a435049c2dcf3c1820d38db1d2cdc1f8d43c80c7fcb651b",
        "premiumEarned": "237173920641070000000",
        "strikePrice": "10700000000"
      },
      {
        "mintAmount": "3422953660865",
        "openedAt": "1666951139",
        "openTxhash": "0x8896b49c45d8da8353f6ac5f878c1c27465b7be9242bead2120192e8c9b3d84f",
        "premiumEarned": "112957470808545000000",
        "strikePrice": "9500000000"
      },
      {
        "mintAmount": "3628258646119",
        "openedAt": "1666346699",
        "openTxhash": "0xe38836acc82ae2b931bb7b5d8e101317f9d883d7bc3737c42cadd1057531a678",
        "premiumEarned": "159643380429236000000",
        "strikePrice": "9000000000"
      },
      {
        "mintAmount": "3050826046834",
        "openedAt": "1665741263",
        "openTxhash": "0xf28acf14aaa1df3749415fba433a0cc7f40fc8529ca9b4ed89713b90eccc9887",
        "premiumEarned": "42711564655676000000",
        "strikePrice": "8500000000"
      },
      {
        "mintAmount": "2981566947052",
        "openedAt": "1665137027",
        "openTxhash": "0x88241a496d5f9621f8fddfa3474a34dda5ba56e185f0d5f7f6ced8340b90fa2d",
        "premiumEarned": "104354843146820000000",
        "strikePrice": "9000000000"
      },
      {
        "mintAmount": "2988901826104",
        "openedAt": "1664531867",
        "openTxhash": "0x14bf1bc5b81580a29c6957706bb31e66055cdc5151bab6654f4024331dfa6d9d",
        "premiumEarned": "164389600435720000000",
        "strikePrice": "9000000000"
      },
      {
        "mintAmount": "2802327100383",
        "openedAt": "1663927211",
        "openTxhash": "0xa68ee0f952768aeac6487b84fe7475251e6a681e6c23980120e9b53ecf08f69f",
        "premiumEarned": "134511700818384000000",
        "strikePrice": "9000000000"
      },
      {
        "mintAmount": "2680274604424",
        "openedAt": "1663322195",
        "openTxhash": "0x384421600b8d1f83e62f5a893e80b12091786ccb7ed1097d1a959da990b9b78e",
        "premiumEarned": "163496750869864000000",
        "strikePrice": "9500000000"
      },
      {
        "mintAmount": "2465239763450",
        "openedAt": "1662717223",
        "openTxhash": "0xa8bf7c11f8c2800c06ee3d8e53118c5fcf89d1826f7f5c3e7f14fdf1b6fbd9db",
        "premiumEarned": "150379625570450000000",
        "strikePrice": "11500000000"
      },
      {
        "mintAmount": "2422029350312",
        "openedAt": "1662112849",
        "openTxhash": "0x2c290fe4d913e3d48ae184cb65a0901cfd33b4bfe552fe292fddecf2491720c9",
        "premiumEarned": "167120025171528000000",
        "strikePrice": "10500000000"
      },
      {
        "mintAmount": "2304169173179",
        "openedAt": "1661507574",
        "openTxhash": "0xe0eaec2ee27b4b694e2e33fa092a245325f7eb13fdd40a43ff86fd77631967d9",
        "premiumEarned": "198158548893394000000",
        "strikePrice": "11000000000"
      },
      {
        "mintAmount": "1969813938407",
        "openedAt": "1660903437",
        "openTxhash": "0xae94484245a111ceeb4e531c13772e32f20055f237984f8ded81671fbe4e4e00",
        "premiumEarned": "104400138735571000000",
        "strikePrice": "11000000000"
      },
      {
        "mintAmount": "1888074406271",
        "openedAt": "1660298534",
        "openTxhash": "0x57605a68ea4e671b5c8cb4f3d0d13b60adefcfefc33966f062f8919708df2b63",
        "premiumEarned": "179367068595745000000",
        "strikePrice": "13500000000"
      },
      {
        "mintAmount": "1556446692511",
        "openedAt": "1659695997",
        "openTxhash": "0x2066f81703634b3697295f618a919a7937d4e04c00d3cfd5977997c7e148070d",
        "premiumEarned": "110507715168281000000",
        "strikePrice": "13000000000"
      },
      {
        "mintAmount": "1583345109841",
        "openedAt": "1659091571",
        "openTxhash": "0x13025e0f6918ff9cbf8be36ff95c63722dedc9bbbfd51f296053ceadc034c56f",
        "premiumEarned": "126667608787280000000",
        "strikePrice": "12500000000"
      },
      {
        "mintAmount": "1547063564433",
        "openedAt": "1658486475",
        "openTxhash": "0xbcdf695b2e99d5abe85af6789ed4256c7503c76cc8c363e4e919c36579834e01",
        "premiumEarned": "69617860399485000000",
        "strikePrice": "12500000000"
      },
      {
        "mintAmount": "1317880477708",
        "openedAt": "1657882762",
        "openTxhash": "0xc8843d07c6a71f10a9270126490862ce664e06757187e18aa8e5e46bd3718b3d",
        "premiumEarned": "115973482038304000000",
        "strikePrice": "11500000000"
      },
      {
        "mintAmount": "1349060402016",
        "openedAt": "1657277468",
        "openTxhash": "0x59725a46bc377194257b7750194b2513e5c592e200a6e12d5f6be6d4abcb1ffd",
        "premiumEarned": "141651342211680000000",
        "strikePrice": "8500000000"
      },
      {
        "mintAmount": "1418537300003",
        "openedAt": "1656673713",
        "openTxhash": "0x56459e0d12687252abe3732efa71929be6fa55614f0897c100468d718c8e03fb",
        "premiumEarned": "100716148300213000000",
        "strikePrice": "7000000000"
      },
      {
        "mintAmount": "1371968216253",
        "openedAt": "1656070911",
        "openTxhash": "0xae312937c4b14aff9e1561193c9ae241403f1a174dcd7572f1c9382fd9cf5ed5",
        "premiumEarned": "80946124758927000000",
        "strikePrice": "9000000000"
      },
      {
        "mintAmount": "1365351588007",
        "openedAt": "1655463677",
        "openTxhash": "0xd232b83325062aea6538a19416104a197c52d6af533dc159d78d4a5f38e7c48e",
        "premiumEarned": "61440821460315000000",
        "strikePrice": "8000000000"
      },
      {
        "mintAmount": "1436046552148",
        "openedAt": "1654858738",
        "openTxhash": "0xc9b9457ce7558e84b7156674d5befb620ff2ff40c162cb37597c65ba52aadc55",
        "premiumEarned": "81854653472436000000",
        "strikePrice": "11500000000"
      },
      {
        "mintAmount": "1804452493937",
        "openedAt": "1654251558",
        "openTxhash": "0x7287b04621abc6d4b70875a61f772d66d2f2b9e8a31c2255fcea59531563c980",
        "premiumEarned": "55035801065078500000",
        "strikePrice": "13000000000"
      },
      {
        "mintAmount": "1632639612941",
        "openedAt": "1653646763",
        "openTxhash": "0x78a7d67c1ddbc57fb3cff25ee2960a87b9b4391af866b1e9e77bf5c70efa7976",
        "premiumEarned": "48979198619956363264",
        "strikePrice": "13000000000"
      },
      {
        "mintAmount": "840446078201",
        "openedAt": "1653041972",
        "openTxhash": "0x3dd2c6ca1117481c241981ceea96491a69423be12a4603e4f1414844a07de867",
        "premiumEarned": "26263945083188219904",
        "strikePrice": "12500000000"
      },
      {
        "mintAmount": "759775966156",
        "openedAt": "1652443191",
        "openTxhash": "0x6437cb5cb11097c657f816cf9bc4b35bec832ee50d088ef4aa2533140e03a8a7",
        "premiumEarned": "15271497623200651264",
        "strikePrice": "11500000000"
      },
      {
        "mintAmount": "818529578992",
        "openedAt": "1651832960",
        "openTxhash": "0x676014d0e615d867a8bb74afe81f007fcb8873778586b9369b97895762691bb0",
        "premiumEarned": "17189121523782742016",
        "strikePrice": "17500000000"
      },
      {
        "mintAmount": "772979550571",
        "openedAt": "1651228165",
        "openTxhash": "0x09d53f03ed567cb5110bd445e5da330f89c904c5d2c004ccfcb146e69a622b47",
        "premiumEarned": "25508329155891507200",
        "strikePrice": "19500000000"
      },
      {
        "mintAmount": "525294745367",
        "openedAt": "1650623371",
        "openTxhash": "0x8d05582869c8d36ff4c1236fa629bb4da3a2d59aa37c6e576dcc630bc8805e48",
        "premiumEarned": "13657663379542003712",
        "strikePrice": "22000000000"
      },
      {
        "mintAmount": "515181165188",
        "openedAt": "1650018570",
        "openTxhash": "0x3647c8cdeb47225c21bbf994b3556ea2adb1295e767847f13c1488422677678f",
        "premiumEarned": "36500000000000000000",
        "strikePrice": "21000000000"
      },
      {
        "mintAmount": "561456446626",
        "openedAt": "1649413776",
        "openTxhash": "0x3f9d8a9c359af995cf84eb3ff0d6480cb6ff5e97463bb206498779dc81cbbc35",
        "premiumEarned": "22456000000000000000",
        "strikePrice": "25000000000"
      },
      {
        "mintAmount": "534467577082",
        "openedAt": "1648808976",
        "openTxhash": "0xb13a39ce74bf1c1de5d9ef39c5136e747d1a076976b8278b884d275193a51bb7",
        "premiumEarned": "31640432000000000000",
        "strikePrice": "30000000000"
      },
      {
        "mintAmount": "699415113517",
        "openedAt": "1648204168",
        "openTxhash": "0xd9323890fba024c0b3b18f70582bb6289f691618326132449951edfd0eedc2b4",
        "premiumEarned": "29374800000000000000",
        "strikePrice": "21000000000"
      },
      {
        "mintAmount": "744503954223",
        "openedAt": "1647599355",
        "openTxhash": "0xe31ac097e975d9d2f8a088e950fff63110b512a77352d0f5404d9c036194d688",
        "premiumEarned": "40947717482265000000",
        "strikePrice": "18000000000"
      },
      {
        "mintAmount": "711796079474",
        "openedAt": "1646994570",
        "openTxhash": "0xaa29bf61a667a0f4338ae55e1719863edda2cee0f9fc7bbf92a527fd4a6e5690",
        "premiumEarned": "22778898135326948000",
        "strikePrice": "14000000000"
      },
      {
        "mintAmount": "656764832368",
        "openedAt": "1646389810",
        "openTxhash": "0xde7d67392da314bd868ada3aeabb0036d2c1437765799b98033278617bac2f40",
        "premiumEarned": "29554417456560000000",
        "strikePrice": "16000000000"
      },
      {
        "mintAmount": "605549499543",
        "openedAt": "1645785006",
        "openTxhash": "0x407df7a10f0ab08e9027baa9069a4a40863bcdf19701d5ea072c65da2063def9",
        "premiumEarned": "23010880982634000000",
        "strikePrice": "15000000000"
      },
      {
        "mintAmount": "597819236619",
        "openedAt": "1645180208",
        "openTxhash": "0xe38c5563df9a3213526d82c3d0161890cf94e306da547fdf5a0d8f5a3bef0136",
        "premiumEarned": "23912769464760000000",
        "strikePrice": "18000000000"
      },
      {
        "mintAmount": "866944303843",
        "openedAt": "1644575425",
        "openTxhash": "0xa63222e8a42267b94ea7f11f9e859f01f123952dc5214a1684d9a2b4172562d1",
        "premiumEarned": "41000000000000000000",
        "strikePrice": "21000000000"
      },
      {
        "mintAmount": "1049741128319",
        "openedAt": "1643970642",
        "openTxhash": "0x0e909acfd2d6aaceb0b21900f7582a5dc252e332f528db4528d017305a808811",
        "premiumEarned": "40939904004481939904",
        "strikePrice": "19000000000"
      },
      {
        "mintAmount": "1015057474827",
        "openedAt": "1643365839",
        "openTxhash": "0x3e71d49d335d18e7526fc5a3d124e392c02e67e03b06da8675e2165efab9b9aa",
        "premiumEarned": "41617356467939461538",
        "strikePrice": "18000000000"
      },
      {
        "mintAmount": "1023443401859",
        "openedAt": "1642761035",
        "openTxhash": "0x22e9c05fbfaef2f95d7b4fdcdf81741b8a9c1937b66798344fda5316e9899fd8",
        "premiumEarned": "51172170092950000000",
        "strikePrice": "23000000000"
      },
      {
        "mintAmount": "1001030370603",
        "openedAt": "1642156200",
        "openTxhash": "0x1496a445e177f62e3673438b8d0c4f52d52625270bb1eb6eff919e766819ad51",
        "premiumEarned": "35036062971128888224",
        "strikePrice": "26000000000"
      },
      {
        "mintAmount": "951546931023",
        "openedAt": "1641551404",
        "openTxhash": "0xddce1f056b7b57a9ef9d3fb0a3b0e42ba76b1e7594eeb52ee96888f0f7cea2dc",
        "premiumEarned": "23788673275575000000",
        "strikePrice": "27000000000"
      },
      {
        "mintAmount": "826363136906",
        "openedAt": "1640949284",
        "openTxhash": "0xf3a2bb79c5ee14027d137b2410c8d1c5592d22f843b0618a7660cdadec93b928",
        "premiumEarned": "67966800000000000000",
        "strikePrice": "34000000000"
      },
      {
        "mintAmount": "849329779853",
        "openedAt": "1640344364",
        "openTxhash": "0x519181488a7b1fafde2bc3815627a5d5cf93188fde4113fa09c7b3fcc48f5e0f",
        "premiumEarned": "50110457011337071886",
        "strikePrice": "31000000000"
      },
      {
        "mintAmount": "264140978945",
        "openedAt": "1639739721",
        "openTxhash": "0xe96c7a9b706006804256931be6cab19f108d489798037ea1079854cf192e0688",
        "premiumEarned": "27200000000000000000",
        "strikePrice": "20000000000"
      },
      {
        "mintAmount": "257616700757",
        "openedAt": "1639136683",
        "openTxhash": "0x637a25f8cd9bc6378181df389b2776672d7f0dc2c30a1004877dd27a28fd78ee",
        "premiumEarned": "19207500000000000000",
        "strikePrice": "21000000000"
      },
      {
        "mintAmount": "259737232902",
        "openedAt": "1638529598",
        "openTxhash": "0x50a871d617dba90fc7c13fa4f5efd6e850510e6ee6e41373a0b387f42f105da1",
        "premiumEarned": "4075200000000000000",
        "strikePrice": "29000000000"
      },
      {
        "mintAmount": "355491464493",
        "openedAt": "1637924935",
        "openTxhash": "0xd5bd1ad37c6203b22f2bfede9fcd45bf6112a853d80076f2fbc7cc4a4b5a326e",
        "premiumEarned": "8887286612325000000",
        "strikePrice": "28000000000"
      },
      {
        "mintAmount": "353692717351",
        "openedAt": "1637319975",
        "openTxhash": "0x2b74e987eb700c9d3f2d87b059a63b94a42a0819f1686cb64ba69e0e49175212",
        "premiumEarned": "1500000000000000",
        "strikePrice": "33000000000"
      },
      {
        "mintAmount": "325236755451",
        "openedAt": "1636716716",
        "openTxhash": "0x9694eacdf6c02ce13c70687c0a671316ee29a68b28651a1bf64cffaad4e62cc9",
        "premiumEarned": "9001017216392888834",
        "strikePrice": "36000000000"
      },
      {
        "mintAmount": "201607168300",
        "openedAt": "1636369466",
        "openTxhash": "0xc2b64319c90f7c14ded172fbb10cff61a594ec68ed3a5b3fe18729c6868f1222",
        "premiumEarned": "7073640000000000000",
        "strikePrice": "37000000000"
      }
    ]
  }
}

short_positions = data["data"]["vaultShortPositions"]

header = [
    "mintAmount",
    "openedAt",
    "openTxhash",
    "premiumEarned",
    "strikePrice"
]

with open("123T-AAVE-C_otokens.csv", mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for position in short_positions:
        position['openedAt'] = datetime.utcfromtimestamp(int(position['openedAt'])).strftime('%Y-%m-%d')
        position["mintAmount"] = int(position["mintAmount"]) / 10**8
        position["premiumEarned"] = int(position["premiumEarned"]) / 10**18
        position["strikePrice"] = int(position["strikePrice"]) / 10**8
        writer.writerow(position)