import requests
from requests.auth import _basic_auth_str
import json
import os.path
import sys
import time
ar = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,82,85,86,87,91,92,95,98,104,108,109,110,111,113,114,115,116,117,119,122,125,126,128,129,132,133,134,135,137,140,141,145,149,152,159,165,166,168,174,176,177,188,202,211,212,213,220,221,227,228,229,230,231,232,234,237,242,243,244,245,250,252,262,265,278,280,298,299,302,303,305,310,311,312,313,315,317,326,327,330,331,332,333,334,337,338,341,352,358,359,360,361,364,365,366,367,369,370,371,375,376,377,378,379,380,381,383,384,386,388,390,391,393,396,398,400,401,402,404,408,411,413,414,420,423,429,430,432,439,447,448,449,450,452,457,461,467,469,472,473,474,478,484,487,488,491,492,493,494,498,506,507,508,509,511,512,514,520,521,526,531,536,539,540,541,542,543,544,546,552,554,555,563,566,568,569,570,573,576,579,580,582,583,584,585,587,588,592,596,598,607,609,610,614,615,616,618,620,621,624,630,631,632,636,637,642,643,644,645,656,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,679,680,681,683,684,685,686,687,688,689,691,693,696,697,698,699,700,704,705,706,707,708,709,710,711,712,716,717,719,726,727,728,729,730,731,732,733,734,735,736,737,738,741,742,743,744,746,747,749,752,754,757,758,759,761,762,764,765,766,768,769,770,771,772,774,775,776,777,778,780,785,791,792,793,794,799,800,801,803,805,808,809,810,811,812,813,815,816,818,819,820,821,822,823,824,825,826,827,828,839,840,842,845,851,854,856,859,865,869,870,872,873,874,875,876,877,878,879,880,881,884,887,893,895,896,897,898,899,900,901,902,904,906,908,910,911,912,913,917,919,921,922,924,929,930,933,934,935,936,941,945,956,959,960,961,962,967,969,971,973,976,977,979,982,983,984,988,991,992,995,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1011,1018,1020,1021,1024,1025,1026,1027,1028,1029,1030,1031,1033,1034,1038,1040,1041,1042,1043,1044,1050,1052,1053,1054,1061,1063,1069,1072,1075,1076,1077,1078,1079,1080,1081,1082,1083,1087,1092,1093,1094,1095,1101,1110,1116,1120,1122,1123,1124,1140,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1175,1176,1177,1179,1182,1184,1186,1187,1189,1190,1192,1207,1209,1210,1212,1213,1218,1220,1225,1227,1230,1231,1232,1236,1237,1239,1246,1247,1250,1251,1254,1257,1264,1267,1269,1270,1271,1272,1274,1276,1277,1279,1283,1284,1286,1287,1290,1297,1299,1302,1303,1304,1307,1309,1310,1311,1313,1314,1315,1316,1317,1331,1332,1333,1334,1335,1340,1343,1345,1348,1353,1370,1372,1373,1374,1375,1376,1377,1378,1379,1380,1381,1385,1388,1389,1390,1391,1394,1395,1396,1399,1400,1401,1402,1408,1414,1415,1417,1420,1426,1430,1432,1434,1437,1438,1440,1442,1443,1445,1449,1450,1451,1454,1455,1456,1457,1459,1460,1461,1462,1463,1464,1465,1466,1467,1468,1469,1472,1473,1474,1475,1476,1477,1479,1480,1481,1486,1489,1493,1495,1498,1499,1504,1505,1509,1511,1512,1513,1514,1517,1519,1520,1522,1524,1526,1531,1536,1538,1540,1542,1543,1545,1546,1550,1551,1552,1556,1557,1558,1559,1560,1561,1562,1563,1565,1567,1568,1570,1572,1574,1580,1583,1585,1586,1588,1589,1590,1593,1594,1595,1596,1597,1598,1599,1600,1603,1606,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1619,1620,1621,1623,1624,1625,1628,1629,1631,1632,1633,1634,1635,1636,1637,1638,1640,1641,1642,1643,1644,1645,1647,1648,1649,1650,1651,1653,1655,1656,1658,1661,1667,1672,1674,1679,1680,1681,1682,1683,1684,1686,1690,1691,1692,1693,1694,1695,1697,1702,1703,1704,1706,1712,1713,1717,1718,1719,1721,1728,1730,1731,1739,1740,1741,1742,1745,1747,1748,1749,1752,1753,1754,1756,1758,1759,1760,1761,1762,1763,1764,1766,1769,1770,1771,1772,1773,1774,1775,1777,1778,1779,1780,1782,1789,1794,1797,1800,1801,1803,1805,1806,1809,1810,1811,1812,1816,1817,1821,1822,1826,1827,1829,1833,1837,1842,1844,1848,1856,1857,1858,1862,1863,1864,1865,1866,1868,1869,1871,1873,1877,1878,1879,1882,1883,1884,1885,1894,1895,1896,1897,1899,1902,1904,1906,1907,1908,1911,1913,1915,1916,1927,1928,1930,1931,1939,1942,1944,1948,1949,1950,1956,1961,1966,1968,1969,1970,1973,1974,1987,1990,1991,2018,2021,2022,2025,2031,2032,2033,2036,2039,2040,2041,2054,2057,2058,2059,2063,2064,2069,2070,2071,2074,2076,2078,2083,2087,2088,2089,2090,2095,2096,2099,2111,2116,2117,2118,2122,2123,2138,2144,2145,2148,2151,2152,2154,2155,2156,2157,2158,2159,2161,2162,2163,2168,2170,2181,2195,2197,2198,2204,2209,2210,2212,2217,2218,2219,2220,2223,2227,2228,2229,2235,2239,2241,2249,2253,2256,2260,2261,2262,2263,2264,2265,2266,2267,2268,2274,2282,2286,2287,2288,2289,2290,2291,2293,2294,2295,2298,2303,2305,2306,2308,2309,2310,2312,2313,2314,2316,2319,2320,2321,2323,2324,2325,2326,2328,2329,2332,2333,2338,2339,2341,2343,2345,2347,2348,2356,2357,2358,2359,2360,2361,2363,2364,2365,2370,2373,2374,2383,2386,2389,2390,2392,2393,2394,2396,2397,2398,2407,2409,2410,2413,2418,2426,2431,2433,2434,2443,2446,2448,2449,2450,2451,2454,2459,2460,2463,2464,2466,2468,2471,2480,2485,2490,2497,2505,2506,2508,2509,2510,2512,2513,2514,2516,2517,2518,2520,2525,2526,2527,2533,2535,2536,2539,2540,2541,2552,2553,2555,2557,2560,2562,2569,2571,2573,2577,2578,2591,2598,2599,2600,2602,2603,2604,2605,2606,2607,2608,2610,2611,2612,2613,2614,2615,2616,2618,2619,2620,2621,2622,2623,2624,2625,2626,2627,2628,2629,2630,2631,2632,2633,2636,2637,2639,2640,2641,2643,2649,2662,2663,2664,2665,2667,2668,2670,2671,2672,2678,2679,2680,2686,2688,2692,2694,2696,2697,2700,2701,2702,2704,2713,2714,2718,2720,2721,2723,2727,2730,2732,2733,2735,2737,2753,2756,2757,2758,2763,2765,2768,2769,2770,2774,2777,2778,2784,2786,2793,2795,2800,2803,2805,2807,2822,2825,2828,2829,2838,2839,2840,2858,2859,2866,2868,2871,2877,2878,2879,2881,2889,2890,2892,2893,2896,2902,2905,2909,2919,2924,2937,3058,3070,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3091,3093,3096,3099,3100,3103,3108,3113,3114,3115,3122,3123,3127,3128,3131,3138,3144,3149,3154,3158,3159,3162,3171,3177,3184,3187,3190,3193,3197,3199,3202,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3216,3217,3218,3220,3221,3222,3223,3224,3225,3231,3232,3233,3234,3237,3238,3239,3241,3242,3243,3244,3248,3256,3265,3267,3268,3270,3271,3272,3274,3275,3276,3277,3278,3279,3281,3282,3283,3292,3293,3297,3298,3311,3312,3314,3320,3321,3325,3329,3330,3334,3336,3358,3364,3369,3372,3373,3384,3387,3395,3406,3421,3432,3436,3467,3524,3528,3537,3558,3559,3561,3578,3598,3611,3627,3633,3639,3652,3660,3661,3666,3669,3670,3671,3672,3675,3677,3682,3685,3686,3687,3699,3704,3714,3718,3726,3737,3739,3761,3766,3770,3810,3816,3818,3839,3841,3843,3846,3862,3866,3867,3868,3870,3897,3908,3956,3975,3976,3980,3996,3999]
file1 = open("ham.txt","w", encoding="utf-8")

for rr in range(0,30000):


  well_id = rr
  company_name = 'xinix'
  url = "https://" + company_name + ".happyfox.com/api/1.1/json/ticket/"+str(well_id)

  print(url)
  payload = {

  'category': '1',
  'user': '2',
  'text': 'Testing',
  'subject': 'Subject ',
  }
  api_key = '775da585ae084536ad2e3f2418d68ca7'
  auth_code = '217de79d35624c96944a0e99942b0afb'
  auth = _basic_auth_str(api_key, auth_code) 


  check = ''
  #files = {'attachments': open('file.extension','rb')}
  headers ={
    'Authorization': auth, 
    'Content-Type': 'multipart/form-data; boundary=--------------------------531818130631649698349478'
  }

  try:
    response = requests.request("GET", url, headers=headers)
    #print(response.text)  

    x = response.text
    def func(value):
        return ''.join(value.splitlines())
     

    def rp(val):
      return val.replace("'", "`")


    y = json.loads(x)
    print(x)
    well_id1 = well_id + 35200 

    file1.write("\n\n\n\n")

    if(y['status'] !='null' and y['status'] is not None and y['status']['name']!='Closed'):
    
        file1.write('set @status = 0;' +"\n")
        file1.write("select @status := ticketstatusid from tbltickets_status where name  like " + "'%"+str(y['status']['name'])+ "%';"+"\n")

        if y['assigned_to'] == 'null' or y['assigned_to'] is None:
            file1.write("insert  into tbltickets values ("+str(well_id1) + ",0,"+str(y['user']['id'])+","+str(y['user']['id'])+",0,'"+str(y['user']['email'])+"' ,'', "+ str(y['category']['id']) + "," + str(y['priority']['id']) + "," + "@status,0,'','" + rp(str(y['subject']))+"','"+rp(func(str(y['first_message'])))+"','','"+str(y['last_updated_at']) + "',0,'"+str(y['last_user_reply_at'])+"',0,0,'',0,'');"+"\n")
            file1.write("\n\n\n\n")
        
        else:
            file1.write("insert  into tbltickets values ("+str(well_id1) + ",0,"+str(y['user']['id'])+","+str(y['user']['id'])+",0,'"+str(y['user']['email'])+"' ,'', "+ str(y['category']['id']) + "," + str(y['priority']['id']) + "," + "@status,0,'','" + rp(str(y['subject']))+"','"+rp(func(str(y['first_message'])))+"','','"+str(y['last_updated_at']) + "',0,'"+str(y['last_user_reply_at'])+"',0,0,"+str(y['assigned_to']['id'])+",0,'');"+"\n")
            file1.write("\n\n\n\n")
        for z in y['updates']:
          #print(z)
          if(z['priority_change'] !='null' and z['priority_change'] is not None):
            file1.write('update tbltickets   set priority = ' + str(z['priority_change']['new']) + ' where ticketid = ' + str(well_id1) + ";" +"\n")


          if(z['category_change'] !='null' and z['category_change'] is not None):
            file1.write('update tbltickets   set department = ' + str(z['category_change']['new']) + " where ticketid = " + str(well_id1) + ";" +"\n")

          if(z['message'] !='null' and z['message'] is not None):
              file1.write('insert into tblticket_replies values (' + str(z['update_id']) + "," + str(well_id1)  + "," + str(z['by']['id']) + "," +  str(z['by']['id']) + ",'" + str(z['by']['name']) + "','" + str(z['by']['email']) + "','" + str(z['timestamp']) + "','" +rp(func(str(z['message']['text']))) + "','',0);" +"\n")

              for l in z['message']['attachments']:
                extension = os.path.splitext(str(l['filename']))[1]
                file1.write("insert into tblticket_attachments values (" + str(l['id']) + "," +str(well_id1) +","+ str(z['update_id']) + ",'" + str(l['filename']) + "'," + "'image/" + str(extension) +  "','" + str(z['timestamp']) + "');" +"\n")


    else:
      check = y['status']
    

  except Exception   as e:

      
      print(check)
      print(repr(e))
      s = bytes("Error {0}".format(str(e)), encoding='utf-8')
      st = s.decode("utf-8") ;
      print(st)
      if st == "Error 'status'":
        print("furqan")
      else:
        time.sleep(150)