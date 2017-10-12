import unittest
import urllib
import flask
import json
from panoptes_aggregation.reducers.poly_line_text_reducer import process_data, poly_line_text_reducer
from panoptes_aggregation.reducers.test_utils import extract_in_data

extracted_data = [
    {
        'frame0': {
            'points': {
                'x': [
                    [895.43, 1274.67],
                    [828.96, 1400.76],
                    [807.46, 848.51],
                    [1047.91, 918.89],
                    [942.35, 1130.99],
                    [1160.31, 1254.15],
                    [1284.45, 1128.06],
                    [811.37, 1459.41]
                ],
                'y': [
                    [122.38, 130.2],
                    [273.88, 451.77],
                    [506.51, 508.46],
                    [507.49, 681.47],
                    [678.54, 675.61],
                    [672.67, 849.59],
                    [841.77, 1014.78],
                    [1093.95, 1086.13]
                ]
            },
            'text': [
                ['Pot Pourri'],
                ['Gather as many rose leaves as you can just before the blooms are going to fall'],
                ['I'],
                ['only to use pink or red & to get these when they are'],
                ['goode'],
                ['dry put them on a tray to dry in a conservatory or hot house'],
                ['& turnd them once or twice every day untill dry then'],
                ['a jar with a cover']
            ],
            'slope': [
                1.1812823254847735,
                17.281193838779483,
                2.7196795379737018,
                126.55987346148383,
                -0.88985971075672066,
                62.058108413580193,
                132.11156945725872,
                -0.69136357286282057
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [860.71, 1418.89],
                    [845.09, 1401.32],
                    [839.24, 839.24]
                ],
                'y': [
                    [267.38, 275.19],
                    [341.55, 339.59],
                    [394.24, 509.39]
                ]
            },
            'text': [
                ['Gather as many rose'],
                ['leaves as you can'],
                ['just before the blooms are going to fall &']
            ],
            'slope': [
                0.80162463698921349,
                -0.20189357469900293,
                90.0
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [832.03, 1255.85],
                    [827.46, 1452.51],
                    [816.78, 1121.69],
                    [824.41, 914.35],
                    [944.85, 1176.57],
                    [995.15, 1060.71]
                ],
                'y': [
                    [336.92, 336.92],
                    [394.85, 382.66],
                    [626.58, 622.01],
                    [460.41, 463.46],
                    [457.36, 449.74],
                    [564.08, 561.03]
                ]
            },
            'text': [
                ['leaves as you'],
                ['just before the blooms'],
                ['get them'],
                ['are'],
                ['going to'],
                ['or']
            ],
            'slope': [
                0.0,
                -1.1172658565014391,
                -0.85868652461555584,
                1.9422413385414206,
                -1.8834652410260238,
                -2.663609178056995
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [873.91, 1306.3],
                    [828.05, 1452.62],
                    [821.53, 1430.09],
                    [823.42, 1456.63],
                    [815.84, 1344.78],
                    [812.05, 1407.34],
                    [813.94, 1392.17],
                    [810.15, 1430.09],
                    [812.05, 1437.67],
                    [815.84, 1413.03],
                    [814.12, 1473.88],
                    [817.24, 1448.92],
                    [812.56, 1448.92]
                ],
                'y': [
                    [124.48, 141.95],
                    [283.89, 277.34],
                    [342.87, 340.98],
                    [397.85, 388.37],
                    [466.1, 449.04],
                    [509.71, 500.23],
                    [564.69, 551.41],
                    [634.83, 610.19],
                    [687.91, 678.44],
                    [735.31, 750.48],
                    [800.56, 836.43],
                    [914.42, 928.45],
                    [1090.66, 1092.22]
                ]
            },
            'text': [
                ['Pot Pourri'],
                ['Gather as many rose'],
                ['leaves as you can'],
                ['just before the blooms'],
                ['are going to fall'],
                ['& mind only to use'],
                ['pink or red & to'],
                ['get them where they'],
                ['are quite dry put'],
                ['them on a tray'],
                ['to dry in a conservatory'],
                ['then once or twice'],
                ['a jar with a cover']
            ],
            'slope': [
                2.3136824088760424,
                -0.60085114314415411,
                -0.17794247916532438,
                -0.85773031613913675,
                -1.847331016176694,
                -0.91235881708605293,
                -1.3156602273836577,
                -2.2760675360043101,
                -0.86721907339980431,
                1.4551316905705483,
                3.1120077026469906,
                1.272365186961546,
                0.14045703217215191
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [874.86, 1278.39],
                    [825.65, 1452.74],
                    [818.62, 1433.05],
                    [821.43, 1456.96],
                    [817.21, 918.45],
                    [1130.76, 1175.75],
                    [814.4, 1250.27],
                    [1205.28, 1254.49],
                    [814.4, 1438.68],
                    [811.59, 915.63],
                    [1156.06, 1433.05],
                    [814.4, 1431.65],
                    [810.18, 1182.78],
                    [815.81, 876.26],
                    [1215.12, 1281.2],
                    [821.43, 1123.73],
                    [820.02, 1452.74],
                    [810.18, 1459.77],
                    [582.08, 757.83],
                    [806.16, 898.42],
                    [814.42, 857.09],
                    [1293.2, 1418.09],
                    [1210.97, 1477.42],
                    [931.07, 1254.79],
                    [816.69, 988.26]
                ],
                'y': [
                    [133.57, 142.01],
                    [276.99, 278.39],
                    [340.26, 340.26],
                    [400.72, 388.06],
                    [459.77, 459.77],
                    [447.12, 445.71],
                    [566.63, 562.41],
                    [497.74, 501.95],
                    [629.9, 617.25],
                    [681.93, 680.52],
                    [672.08, 688.96],
                    [740.98, 752.23],
                    [798.63, 795.81],
                    [854.87, 857.68],
                    [901.27, 906.89],
                    [963.13, 956.1],
                    [1016.56, 1020.78],
                    [1084.05, 1091.08],
                    [40.4, 47.73],
                    [78.48, 82.88],
                    [102.12, 102.12],
                    [173.93, 157.28],
                    [795.3, 833.81],
                    [846.59, 849.83],
                    [907.02, 916.73]
                ]
            },
            'text': [
                ['Pot Pourri'],
                ['Gather as many rose'],
                ['leaves as you can'],
                ['that before the blooms'],
                ['are'],
                ['&'],
                ['pink or red'],
                ['&'],
                ['get them when they'],
                ['are'],
                ['dry put'],
                ['them on a tray'],
                ['to dry in a'],
                ['or'],
                ['or'],
                ['every day'],
                ['dry then put in'],
                ['a jar with a cover'],
                ['MS. Add. 369'],
                ['X.d.451'],
                ['(7)'],
                ['1685'],
                ['conservatory'],
                ['hot house'],
                ['them']
            ],
            'slope': [
                1.1981906755751579,
                0.12791458650394247,
                0.0,
                -1.1412028459682639,
                0.0,
                -1.7950792315218822,
                -0.554708135771525,
                4.889845766146161,
                -1.1608451892028007,
                -0.77645236076346968,
                3.4873394465591718,
                1.0441574083189766,
                -0.43363127556971831,
                2.6614611304609408,
                4.8612176190058927,
                -1.3321758002882953,
                0.38213523268205246,
                0.62004280569738002,
                2.3882492426472552,
                2.730441780429457,
                0.0,
                -7.5937418536908448,
                8.2240070808507397,
                0.57343422507612674,
                3.2391978304671274
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [
                    [890.35, 1270.69],
                    [839, 1432.33],
                    [821.89, 1420.92],
                    [827.59, 1451.35],
                    [819.98, 1344.85],
                    [802.87, 1415.22],
                    [812.38, 1392.4],
                    [819.98, 1424.73],
                    [821.89, 1430.43],
                    [816.18, 1411.41],
                    [814.28, 1464.66],
                    [818.08, 1445.64],
                    [818.08, 1110.94],
                    [1164.19, 1396.2],
                    [810.48, 1333.44],
                    [812.38, 1453.25],
                    [814.28, 1327.74]
                ],
                'y': [
                    [128.05, 143.26],
                    [264.97, 268.77],
                    [341.04, 331.53],
                    [390.48, 379.07],
                    [458.94, 447.53],
                    [510.29, 500.78],
                    [567.34, 554.03],
                    [630.1, 607.28],
                    [681.44, 673.84],
                    [742.3, 740.4],
                    [801.25, 816.46],
                    [907.75, 940.08],
                    [962.9, 957.19],
                    [953.39, 972.4],
                    [1014.24, 1006.64],
                    [1086.51, 1082.7],
                    [846.89, 850.7]
                ]
            },
            'text': [
                ['Pot Pourri'],
                ['Gather as many rose'],
                ['leaves as you can'],
                ['just before the blooms'],
                ['are going to fall'],
                ['& mind only to use'],
                ['pink or red & to'],
                ['get them when they'],
                ['are quite dry put'],
                ['them on a tray'],
                ['to dry in a conservatory'],
                ['them once or twice'],
                ['every day'],
                ['untill'],
                ['dry then just'],
                ['a jar with a cover'],
                ['or hot house &']
            ],
            'slope': [
                2.2900685918639829,
                0.36694754243868721,
                -0.90953223253171889,
                -1.0479542497229344,
                -1.2453405471411225,
                -0.88975106150196548,
                -1.3145633046633123,
                -2.1610080858107743,
                -0.71552451288487495,
                -0.18288999435582665,
                1.3396936926683003,
                2.9490987699269864,
                -1.1169755318708467,
                4.6841304161042094,
                -0.83260148559900182,
                -0.34062188619212308,
                0.42514103064765579
            ]
        }
    },
    {
        'frame0': {
            'points': {
                'x': [],
                'y': []
            },
            'text': [],
            'slope': []
        }
    }
]

processed_data = {
    'frame0': {
        'x': [
            [895.43, 1274.67],
            [828.96, 1400.76],
            [807.46, 848.51],
            [1047.91, 918.89],
            [942.35, 1130.99],
            [1160.31, 1254.15],
            [1284.45, 1128.06],
            [811.37, 1459.41],
            [860.71, 1418.89],
            [845.09, 1401.32],
            [839.24, 839.24],
            [832.03, 1255.85],
            [827.46, 1452.51],
            [816.78, 1121.69],
            [824.41, 914.35],
            [944.85, 1176.57],
            [995.15, 1060.71],
            [873.91, 1306.3],
            [828.05, 1452.62],
            [821.53, 1430.09],
            [823.42, 1456.63],
            [815.84, 1344.78],
            [812.05, 1407.34],
            [813.94, 1392.17],
            [810.15, 1430.09],
            [812.05, 1437.67],
            [815.84, 1413.03],
            [814.12, 1473.88],
            [817.24, 1448.92],
            [812.56, 1448.92],
            [874.86, 1278.39],
            [825.65, 1452.74],
            [818.62, 1433.05],
            [821.43, 1456.96],
            [817.21, 918.45],
            [1130.76, 1175.75],
            [814.4, 1250.27],
            [1205.28, 1254.49],
            [814.4, 1438.68],
            [811.59, 915.63],
            [1156.06, 1433.05],
            [814.4, 1431.65],
            [810.18, 1182.78],
            [815.81, 876.26],
            [1215.12, 1281.2],
            [821.43, 1123.73],
            [820.02, 1452.74],
            [810.18, 1459.77],
            [582.08, 757.83],
            [806.16, 898.42],
            [814.42, 857.09],
            [1293.2, 1418.09],
            [1210.97, 1477.42],
            [931.07, 1254.79],
            [816.69, 988.26],
            [890.35, 1270.69],
            [839, 1432.33],
            [821.89, 1420.92],
            [827.59, 1451.35],
            [819.98, 1344.85],
            [802.87, 1415.22],
            [812.38, 1392.4],
            [819.98, 1424.73],
            [821.89, 1430.43],
            [816.18, 1411.41],
            [814.28, 1464.66],
            [818.08, 1445.64],
            [818.08, 1110.94],
            [1164.19, 1396.2],
            [810.48, 1333.44],
            [812.38, 1453.25],
            [814.28, 1327.74]
        ],
        'y': [
            [122.38, 130.2],
            [273.88, 451.77],
            [506.51, 508.46],
            [507.49, 681.47],
            [678.54, 675.61],
            [672.67, 849.59],
            [841.77, 1014.78],
            [1093.95, 1086.13],
            [267.38, 275.19],
            [341.55, 339.59],
            [394.24, 509.39],
            [336.92, 336.92],
            [394.85, 382.66],
            [626.58, 622.01],
            [460.41, 463.46],
            [457.36, 449.74],
            [564.08, 561.03],
            [124.48, 141.95],
            [283.89, 277.34],
            [342.87, 340.98],
            [397.85, 388.37],
            [466.1, 449.04],
            [509.71, 500.23],
            [564.69, 551.41],
            [634.83, 610.19],
            [687.91, 678.44],
            [735.31, 750.48],
            [800.56, 836.43],
            [914.42, 928.45],
            [1090.66, 1092.22],
            [133.57, 142.01],
            [276.99, 278.39],
            [340.26, 340.26],
            [400.72, 388.06],
            [459.77, 459.77],
            [447.12, 445.71],
            [566.63, 562.41],
            [497.74, 501.95],
            [629.9, 617.25],
            [681.93, 680.52],
            [672.08, 688.96],
            [740.98, 752.23],
            [798.63, 795.81],
            [854.87, 857.68],
            [901.27, 906.89],
            [963.13, 956.1],
            [1016.56, 1020.78],
            [1084.05, 1091.08],
            [40.4, 47.73],
            [78.48, 82.88],
            [102.12, 102.12],
            [173.93, 157.28],
            [795.3, 833.81],
            [846.59, 849.83],
            [907.02, 916.73],
            [128.05, 143.26],
            [264.97, 268.77],
            [341.04, 331.53],
            [390.48, 379.07],
            [458.94, 447.53],
            [510.29, 500.78],
            [567.34, 554.03],
            [630.1, 607.28],
            [681.44, 673.84],
            [742.3, 740.4],
            [801.25, 816.46],
            [907.75, 940.08],
            [962.9, 957.19],
            [953.39, 972.4],
            [1014.24, 1006.64],
            [1086.51, 1082.7],
            [846.89, 850.7]
        ],
        'text': [
            ['Pot Pourri'],
            ['Gather as many rose leaves as you can just before the blooms are going to fall'],
            ['I'],
            ['only to use pink or red & to get these when they are'],
            ['goode'],
            ['dry put them on a tray to dry in a conservatory or hot house'],
            ['& turnd them once or twice every day untill dry then'],
            ['a jar with a cover'],
            ['Gather as many rose'],
            ['leaves as you can'],
            ['just before the blooms are going to fall &'],
            ['leaves as you'],
            ['just before the blooms'],
            ['get them'],
            ['are'],
            ['going to'],
            ['or'],
            ['Pot Pourri'],
            ['Gather as many rose'],
            ['leaves as you can'],
            ['just before the blooms'],
            ['are going to fall'],
            ['& mind only to use'],
            ['pink or red & to'],
            ['get them where they'],
            ['are quite dry put'],
            ['them on a tray'],
            ['to dry in a conservatory'],
            ['then once or twice'],
            ['a jar with a cover'],
            ['Pot Pourri'],
            ['Gather as many rose'],
            ['leaves as you can'],
            ['that before the blooms'],
            ['are'],
            ['&'],
            ['pink or red'],
            ['&'],
            ['get them when they'],
            ['are'],
            ['dry put'],
            ['them on a tray'],
            ['to dry in a'],
            ['or'],
            ['or'],
            ['every day'],
            ['dry then put in'],
            ['a jar with a cover'],
            ['MS. Add. 369'],
            ['X.d.451'],
            ['(7)'],
            ['1685'],
            ['conservatory'],
            ['hot house'],
            ['them'],
            ['Pot Pourri'],
            ['Gather as many rose'],
            ['leaves as you can'],
            ['just before the blooms'],
            ['are going to fall'],
            ['& mind only to use'],
            ['pink or red & to'],
            ['get them when they'],
            ['are quite dry put'],
            ['them on a tray'],
            ['to dry in a conservatory'],
            ['them once or twice'],
            ['every day'],
            ['untill'],
            ['dry then just'],
            ['a jar with a cover'],
            ['or hot house &']
        ],
        'slope': [
            1.1812823254847735,
            17.281193838779483,
            2.7196795379737018,
            126.55987346148383,
            -0.88985971075672066,
            62.058108413580193,
            132.11156945725872,
            -0.69136357286282057,
            0.80162463698921349,
            -0.20189357469900293,
            90.0,
            0.0,
            -1.1172658565014391,
            -0.85868652461555584,
            1.9422413385414206,
            -1.8834652410260238,
            -2.663609178056995,
            2.3136824088760424,
            -0.60085114314415411,
            -0.17794247916532438,
            -0.85773031613913675,
            -1.847331016176694,
            -0.91235881708605293,
            -1.3156602273836577,
            -2.2760675360043101,
            -0.86721907339980431,
            1.4551316905705483,
            3.1120077026469906,
            1.272365186961546,
            0.14045703217215191,
            1.1981906755751579,
            0.12791458650394247,
            0.0,
            -1.1412028459682639,
            0.0,
            -1.7950792315218822,
            -0.554708135771525,
            4.889845766146161,
            -1.1608451892028007,
            -0.77645236076346968,
            3.4873394465591718,
            1.0441574083189766,
            -0.43363127556971831,
            2.6614611304609408,
            4.8612176190058927,
            -1.3321758002882953,
            0.38213523268205246,
            0.62004280569738002,
            2.3882492426472552,
            2.730441780429457,
            0.0,
            -7.5937418536908448,
            8.2240070808507397,
            0.57343422507612674,
            3.2391978304671274,
            2.2900685918639829,
            0.36694754243868721,
            -0.90953223253171889,
            -1.0479542497229344,
            -1.2453405471411225,
            -0.88975106150196548,
            -1.3145633046633123,
            -2.1610080858107743,
            -0.71552451288487495,
            -0.18288999435582665,
            1.3396936926683003,
            2.9490987699269864,
            -1.1169755318708467,
            4.6841304161042094,
            -0.83260148559900182,
            -0.34062188619212308,
            0.42514103064765579
        ]
    }
}

reduced_data = {
    'frame0': [
        {
            'clusters_text': [
                ['Pot', 'Pot', 'Pot', 'Pot'],
                ['Pourri', 'Pourri', 'Pourri', 'Pourri']
            ],
            'clusters_x': [883.6374999999999, 1282.5125000000003],
            'clusters_y': [127.12, 139.355],
            'consensus_score': 4.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 4,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['Gather', 'Gather', 'Gather', 'Gather'],
                ['as', 'as', 'as', 'as'],
                ['many', 'many', 'many', 'many'],
                ['rose', 'rose', 'rose', 'rose']
            ],
            'clusters_x': [838.3525, 1439.145],
            'clusters_y': [273.3075, 274.9225],
            'consensus_score': 4.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 4,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['leaves', 'leaves', 'leaves', 'leaves', 'leaves'],
                ['as', 'as', 'as', 'as', 'as'],
                ['you', 'you', 'you', 'you', 'you'],
                ['can', '', 'can', 'can', 'can']
            ],
            'clusters_x': [827.832, 1421.345],
            'clusters_y': [340.52799999999996, 338.09],
            'consensus_score': 4.75,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 5,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['just', 'just', 'that', 'just'],
                ['before', 'before', 'before', 'before'],
                ['the', 'the', 'the', 'the'],
                ['blooms', 'blooms', 'blooms', 'blooms']
            ],
            'clusters_x': [824.975, 1454.3625000000002],
            'clusters_y': [395.975, 384.53999999999996],
            'consensus_score': 3.75,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 4,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['are', '', 'are', 'are', '', 'are'],
                ['', 'going', 'going', '', '', 'going'],
                ['', 'to', 'to', '', '&', 'to'],
                ['', '', 'fall', '', '', 'fall']
            ],
            'clusters_x': [819.36, 1344.815],
            'clusters_y': [461.305, 448.28499999999997],
            'consensus_score': 3.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 6,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['I', '&', '&'],
                ['', 'mind', 'mind'],
                ['', 'only', 'only'],
                ['', 'to', 'to'],
                ['', 'use', 'use']
            ],
            'clusters_x': [807.46, 1411.28],
            'clusters_y': [508.83666666666664, 500.505],
            'consensus_score': 2.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 3,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['', 'pink', 'pink', 'pink'],
                ['or', 'or', 'or', 'or'],
                ['', 'red', 'red', 'red'],
                ['', '&', '', '&'],
                ['', 'to', '', 'to']
            ],
            'clusters_x': [813.5733333333334, 1392.285],
            'clusters_y': [566.2200000000001, 552.72],
            'consensus_score': 2.8,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 4,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['get', 'get', 'get', 'get'],
                ['them', 'them', 'them', 'them'],
                ['', 'where', 'when', 'when'],
                ['', 'they', 'they', 'they']
            ],
            'clusters_x': [815.3275, 1431.1666666666667],
            'clusters_y': [630.3525, 611.5733333333334],
            'consensus_score': 3.25,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 4,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['goode', 'are', 'are', '', 'are'],
                ['', 'quite', '', '', 'quite'],
                ['', 'dry', '', 'dry', 'dry'],
                ['', 'put', '', 'put', 'put']
            ],
            'clusters_x': [815.1766666666666, 1433.716666666667],
            'clusters_y': [683.7599999999999, 680.4133333333334],
            'consensus_score': 2.75,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 5,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['them', 'them', 'them'],
                ['on', 'on', 'on'],
                ['a', 'a', 'a'],
                ['tray', 'tray', 'tray']],
            'clusters_x': [815.4733333333334, 1418.6966666666667],
            'clusters_y': [739.5300000000001, 747.7033333333334],
            'consensus_score': 3.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 3,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['to', 'to', 'to'],
                ['dry', 'dry', 'dry'],
                ['in', 'in', 'in'],
                ['a', 'a', 'a'],
                ['conservatory', '', 'conservatory']
            ],
            'clusters_x': [812.86, 1469.27],
            'clusters_y': [800.1466666666666, 826.4449999999999],
            'consensus_score': 2.8,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 3,
            'slope_label': 0
        },
        {
            'clusters_text': [
                ['or', '', 'or'],
                ['', 'hot', 'hot'],
                ['', 'house', 'house'],
                ['', '', '&']
            ],
            'clusters_x': [815.045, 1327.74],
            'clusters_y': [850.88, 850.7],
            'consensus_score': 1.75,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 3,
            'slope_label': 0},
        {
            'clusters_text': [
                ['then', 'them', 'them'],
                ['once', '', 'once'],
                ['or', '', 'or'],
                ['twice', '', 'twice']
            ],
            'clusters_x': [817.3366666666667, 1447.2800000000002],
            'clusters_y': [909.73, 934.2650000000001],
            'consensus_score': 2.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 3,
            'slope_label': 0},
        {
            'clusters_text': [
                ['every', 'every'],
                ['day', 'day']
            ],
            'clusters_x': [819.755, 1117.335],
            'clusters_y': [963.015, 956.645],
            'consensus_score': 2.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 2,
            'slope_label': 0},
        {
            'clusters_text': [
                ['dry', 'dry'],
                ['then', 'then'],
                ['put', 'just'],
                ['in', '']
            ],
            'clusters_x': [815.25, 1452.74],
            'clusters_y': [1015.4, 1020.78],
            'consensus_score': 1.5,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 2,
            'slope_label': 0},
        {
            'clusters_text': [
                ['a', 'a', 'a', 'a'],
                ['jar', 'jar', 'jar', 'jar'],
                ['with', 'with', 'with', 'with'],
                ['a', 'a', 'a', 'a'],
                ['cover', 'cover', 'cover', 'cover']
            ],
            'clusters_x': [811.6225, 1455.3375],
            'clusters_y': [1088.7925, 1088.0325],
            'consensus_score': 4.0,
            'gutter_label': 1,
            'line_slope': 0.09112619119034585,
            'number_views': 4,
            'slope_label': 0
        }
    ]
}


class TestSWClusterLines(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.kwargs = {
            'eps_slope': 0.5,
            'eps_line': 15,
            'eps_word': 30,
            'dot_freq': 'line',
            'min_samples': 2
        }

    def test_process_data(self):
        result = process_data(extracted_data)
        self.assertDictEqual(dict(result), processed_data)

    def test_cluster_lines(self):
        result = poly_line_text_reducer._original(processed_data, metric='euclidean', gutter_tol=0, **self.kwargs)
        self.assertDictEqual(dict(result), reduced_data)

    def test_poly_line_text_reducer(self):
        result = poly_line_text_reducer(extracted_data, **self.kwargs)
        self.assertDictEqual(dict(result), reduced_data)

    def test_poly_line_text_reducer_request(self):
        app = flask.Flask(__name__)
        request_kwargs = {
            'data': json.dumps(extract_in_data(extracted_data)),
            'content_type': 'application/json'
        }
        url_params = '?{0}'.format(urllib.parse.urlencode(self.kwargs))
        with app.test_request_context(url_params, **request_kwargs):
            result = poly_line_text_reducer(flask.request)
            self.assertDictEqual(dict(result), reduced_data)


if __name__ == '__main__':
    unittest.main()
