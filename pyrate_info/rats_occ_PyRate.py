#!/usr/bin/env python
from numpy import * 


data_1=[array([0.113966,0.010373]),
array([0.618484,1.716413,1.290764,0.662301,0.990407,1.527124,0.86576,1.143509,0.494244,0.394475,0.37465,1.487018,0.026699,0.11144,0.118225,0.065431,0.00454,0.105001,0]),
array([0.120066,2.39116,0]),
array([19.740464,7.448744,12.844591,15.254076,13.851306,14.59086,11.163208,13.622101,13.890594,9.489349,13.939162,10.844776,12.321538,12.716872,12.124336,6.781839,15.24252,14.959604,14.05578,24.3058]),
array([12.674414,12.445126]),
array([5.587339,2.117495,2.391251]),
array([14.174675,20.08284]),
array([12.136916]),
array([14.924756,14.329005,13.751177,15.347422,15.25268,13.783942,15.92113,15.908042,14.03229,13.607239,13.920803,15.496136,14.942853,14.766974,14.425464,15.769323,15.070137,14.688435,14.479391,14.971127,15.052011,14.538285,14.9953,15.544699,15.35468,15.357273,7.433382,14.166415,13.846306,13.806947]),
array([14.564074,14.415617,15.193703,14.514135,14.647161,13.748224,15.012765,14.816707,13.694915,15.291606,14.995367,9.7695,14.364227,15.739988,15.33338,15.951149,14.865959,14.550901,14.46583,13.907851,15.729389,15.10087,14.305004,15.609909,15.337096,15.957129,19.535668,17.378979,18.580851]),
array([5.393286,5.816424,9.657708]),
array([15.071149,15.122648,14.143871,15.75111,14.448244,15.23553,15.688997,14.579016,13.615679,14.06484,14.1644,13.641653,14.464776,16.001455,14.205884,14.18687,15.078289,19.843923,14.398954,15.108476,15.02672,14.950471,13.870273,14.037416,15.5112]),
array([13.158966,11.899612,10.969473]),
array([15.429449]),
array([11.436766,13.188648,12.529018,12.137586,13.364154]),
array([14.339071,15.86188]),
array([9.787156]),
array([22.873473,20.501333,23.353733,18.432496,17.861835,17.723371,17.536339,22.696631,17.418072]),
array([4.814791,4.307834,3.684876,4.658162,4.230794,2.15495,2.274034,3.168587,4.573577,3.468204,4.723193,3.062995,3.853043,4.475959,3.950846,3.768151,3.803221,3.055582,1.078092,0.5299,0.550367,0.923555,0.683668,1.216081,1.660968,0.577368,1.203469,0.805195,0.974681,0.80678,1.152634,1.717853,0.449894,0.495393,0.952567,1.292861,0.762768,0.724213,0.77443,1.429834,1.138394,1.14936,0.884065,0.818104,1.398687,1.208475,0.735244,0.541116,1.348115,1.409466,1.512215,1.344385,1.718644,0.415166,0.351903,1.648723,1.39778,0.481604,0.323646,0.547575,0.367234,1.272662,1.326655,1.765356,0.467354,0.785376,1.448614,0.939523,1.393475,0.600973,1.277928,1.767326,0.687325,0.046055,0.068761,0.082829,0.08893,0.745459,1.595823,0.009856,0.002814,0.008209,3.046094,0.028346,0.105199,0.085744,0.258396]),
array([0.08541]),
array([2.021302,2.945533,2.044961,2.641776,4.540733,4.521481,3.548995,3.01216,1.470747,1.797715,1.65044]),
array([1.531792]),
array([2.431438,3.327079,0.830102,1.748565]),
array([3.449395,4.80525,4.840892,4.779525,4.476634,3.290929,3.686052,4.295324,2.415756,2.400084]),
array([0.600578,0.009257,0.00651,0.053429,0.010321,0.124543,0]),
array([0.054558]),
array([1.807755,4.278622,2.731379,3.948443,4.456535]),
array([1.188013,1.277936,1.653467,0.583296,0.027864,0.080494,0.007588,0.075279,0]),
array([0.025449]),
array([1.096689]),
array([0.017213,0.003329,0.092434,0.112169,0.117643,0]),
array([5.164986]),
array([12.861925,11.447835,12.201722,11.14212,13.298467,15.961045]),
array([8.467058,6.898528]),
array([6.359977,12.672017,6.392446,7.056672,8.041092,13.664599]),
array([15.469303]),
array([20.549055,11.001764,23.70527]),
array([14.529594]),
array([18.206873,16.458792,20.190417,19.035771,17.015273]),
array([27.134102,24.751672,21.584276,22.825308,18.05075,19.814318,17.237812,18.262828,16.583917,19.159334,19.922663,16.183752,19.094445,20.141803]),
array([18.931758,18.675926]),
array([32.501683,27.233697,21.845476,25.734124,30.57209,24.103474,21.81522,15.984954,14.173781,14.25973,12.800216,13.916426,16.93331,15.391704,15.482922,17.197756,13.7112,20.668066,3.012153,0.015952,18.582519,0.006269,0.002242,0.007242,0.002379,0.005614,0.004899,14.572362]),
array([10.001145,5.856764,9.361477,8.948298,7.614876,11.950252,5.983024,18.217783,6.884865]),
array([13.44098,14.92631,12.884959,13.688896,7.824437]),
array([15.556874]),
array([15.090753,14.121679,14.240583,13.885247,14.842611,14.693955]),
array([0.061118,0.107212,0.059228]),
array([7.527814]),
array([15.017022,12.004902,14.071543,14.306168,17.873172,12.938994]),
array([15.787232,14.6153,15.339136,15.23611,13.52714,15.31297,14.195288]),
array([13.702048,15.517169]),
array([14.172236]),
array([22.96705,21.206464,19.682135,18.972487,14.299706]),
array([14.389236]),
array([15.933309,14.442382,13.875549,15.037673,15.715056,15.649614,15.252052]),
array([15.891997,13.836958]),
array([15.195518]),
array([3.06344]),
array([6.628526,6.11364,7.243442,9.497942]),
array([9.956171,3.820826]),
array([14.704678,14.895262]),
array([14.280987]),
array([14.259115,15.314812,13.951499,15.88718]),
array([18.494759,19.038013,15.13882,17.156884]),
array([14.244652,15.29941,13.923359,15.777594]),
array([14.528479,14.180683]),
array([12.46394,13.124547]),
array([12.777335,15.274953,11.118929,6.316585,2.54634,4.356062,1.545662,0.946947,2.880817,12.158206,0.00964,0.01377,0.10737,0.068254,0.032403,0.124357,0.055447,8.568344]),
array([15.023408]),
array([14.731249,14.404869,15.023136,13.87855,15.775083,15.376918]),
array([4.531241]),
array([12.018669,6.752709,3.186517]),
array([6.196219]),
array([0.066075,0.002741,0.085551,0.071498,0]),
array([14.081503,15.759924,15.698616,15.183659,15.192829,12.536585,14.872992,15.819411,13.666465,15.087568,12.457691,14.678422,14.071401,12.331184,13.992618,15.758869,15.625804,14.062145,11.319979,13.96268,14.650986,11.49838,15.060316,15.957876,19.405087,14.215708]),
array([1.876501,4.263913,3.412337,1.894159,1.862856,1.439183]),
array([4.999765]),
array([0.10689]),
array([3.862139,2.185752,2.019249,3.894047]),
array([6.095973,7.522788,3.540556]),
array([10.515423,14.868845,14.553216,12.015173,15.711362,13.47886,15.366952,13.522075,15.251114,15.501557,15.83169,13.902591,13.265934,10.827166,13.141814,13.932279,12.69404,12.551482,14.415943,14.978704,11.93203,15.219425,15.194854,14.888252,15.017694,13.806209,8.778114]),
array([3.497711,4.219093,2.385499,2.667963,4.837811,2.492305,3.776225,2.856482,2.432252,2.864987,1.72149,1.510877]),
array([2.255873,4.409405,4.083445,2.935111,4.335326]),
array([15.218023]),
array([6.872083,9.463067,5.171701]),
array([1.831354]),
array([14.070439,15.66001,14.84013,15.090123,13.630179,13.878414,14.143857,13.979857,11.584848,15.726515,13.98747,13.636606,15.295351]),
array([8.914325,8.304406,9.471702,6.308297,4.605781,2.835715,3.054902,2.690335,3.617446,3.662284,3.831284,3.297707,1.817212,1.85778,3.114164,4.749653,3.845963,3.729964,3.471629,4.652844,1.69792,1.715013,1.293389,0.909991,0.927006]),
array([2.97951,4.127867,3.564366,4.149894,2.920131,4.214635]),
array([3.325973]),
array([8.557232,2.301107,2.950074,3.96436,2.252597,4.089468,4.804949,3.589708,3.087257,1.933079,0.873944,0.559477]),
array([5.555578,8.77304]),
array([4.824597,3.148521]),
array([3.794497]),
array([4.659397,3.749555,3.19731,4.889199,2.208407,3.268259]),
array([28.108167]),
array([28.754241,27.675495,27.841224,30.638019,20.698919,27.893991,27.47476,28.31705,28.013718]),
array([29.304818,29.598852,27.228212,28.550936,29.322077]),
array([30.038118,31.162021]),
array([25.847538,22.899492,24.602616,24.57907,16.221249,16.037555,16.831236,20.272515,17.826568,18.290368,22.285775,20.738587,18.264324,17.265009,25.146684,30.493161,30.361643,23.88525]),
array([22.466584]),
array([30.588866,21.525976,22.429081,29.190819,16.037663,19.355028,20.391664,16.048717]),
array([24.401458,29.036118,30.380178,28.021425,30.065562]),
array([26.477736,26.220872,28.069123,25.309216]),
array([23.243974]),
array([15.884038,18.813032]),
array([21.56312]),
array([19.048908,14.288262,13.877372,15.338431,13.006063,19.706549,16.620708,20.810129]),
array([21.245552]),
array([19.070964,28.253778,23.730252,23.55758,27.219152,23.085656,17.851689,20.202681,26.403483,29.162861,22.224706,26.910851,21.495721,20.853935,25.819663,24.024768,29.997122,24.876346]),
array([18.323335,20.006368,19.335236,15.993004,18.120587,20.123499,17.132626,18.485918,20.299495]),
array([18.24582,23.611297]),
array([25.708681,20.562805,24.365446,19.733387,16.737926,17.526273,18.503966,18.43512,16.473098,19.476161,17.556169,25.258229,22.182245]),
array([23.678487]),
array([19.746026]),
array([17.443262,19.50567,19.542884,18.855605,18.389188]),
array([19.454385,15.205586]),
array([22.923559,19.085629])
]

d=[data_1]
names=[ 'rats_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Chaetodipus_formosus','Chaetodipus_hispidus','Chaetodipus_intermedius','Cupidinimus','Cupidinimus_avawatzensis','Cupidinimus_bidahochiensis','Cupidinimus_boronensis','Cupidinimus_cuyamensis','Cupidinimus_halli','Cupidinimus_lindsayi','Cupidinimus_magnus','Cupidinimus_nebraskensis','Cupidinimus_prattensis','Cupidinimus_smaragdinus','Cupidinimus_tertius','Cupidinimus_whitlocki','Dikkomys','Dikkomys_matthewi','Dipodomys','Dipodomys_agilis','Dipodomys_compactus','Dipodomys_deserti','Dipodomys_gidleyi','Dipodomys_hibbardi','Dipodomys_merriami','Dipodomys_microps','Dipodomys_minor','Dipodomys_ordii','Dipodomys_ordii_montanus','Dipodomys_pattersoni','Dipodomys_spectabilis','Diprionomys','Diprionomys_agrarius','Diprionomys_minimus','Diprionomys_parvus','Harrymyinae','Harrymys','Harrymys_canadensis','Harrymys_irvini','Harrymys_magnus','Harrymys_woodi','Heteromyidae','Heteromyinae','Lignimus','Lignimus_austridakotensis','Lignimus_montis','Liomys_irroratus','Metaliomys_sevierensis','Mioheteromys','Mioheteromys_amplissimus','Mioheteromys_arcarius','Mioheteromys_subterior','Mookomys','Mookomys_altifluminis','Mookomys_formicarum','Mookomys_subtilis','Mookomys_thrinax','Oregonomys_magnus','Oregonomys_pebblespringsensis','Oregonomys_sargenti','Peridiomys_borealis','Peridiomys_halis','Peridiomys_oregonensis','Peridiomys_rusticus','Perognathoides_eurekensis','Perognathoides_kleinfelderi','Perognathoides_quartus','Perognathus','Perognathus_ancenensis','Perognathus_brevidens','Perognathus_carpenteri','Perognathus_coquorum','Perognathus_dunklei','Perognathus_flavus','Perognathus_furlongi','Perognathus_gidleyi','Perognathus_henryredfieldi','Perognathus_huastecensis','Perognathus_maldei','Perognathus_mclaughlini','Perognathus_minutus','Perognathus_pearlettensis','Perognathus_rexroadensis','Perognathus_saskatchewanensis','Perognathus_stevei','Perognathus_strigipredus','Perognathus_trojectioansrum','Prodipodomys','Prodipodomys_centralis','Prodipodomys_griggsorum','Prodipodomys_idahoensis','Prodipodomys_kansensis','Prodipodomys_riversidensis','Prodipodomys_tiheni','Prodipodomys_timoteoensis','Proharrymys','Proharrymys_fedti','Proharrymys_schlaikjeri','Proharrymys_wahlerti','Proheteromys','Proheteromys_cejanus','Proheteromys_floridanus','Proheteromys_gremmelsi','Proheteromys_ironcloudi','Proheteromys_matthewi','Proheteromys_maximus','Proheteromys_sabinensis','Proheteromys_sulculus','Proheteromys_toledoensis','Schizodontomys','Schizodontomys_amnicolus','Schizodontomys_greeni','Schizodontomys_harkseni','Schizodontomys_sulcidens','Stratimus','Stratimus_strobeli','Trogomys','Trogomys_rupinimenthae']
def get_taxa_names(): return taxa_names