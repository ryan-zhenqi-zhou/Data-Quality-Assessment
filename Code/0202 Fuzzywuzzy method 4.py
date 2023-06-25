# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:01:19 2022

@author: ryanz
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:03:52 2022

@author: ryanz
"""

import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from geopy.distance import geodesic

def matching(df_al, df_sa):
    for a in range(len(df_al)):
        naad_al = df_al['naad'][a]
        longitude_x = df_al['longitude_x'][a]
        latitude_x = df_al['latitude_x'][a]
        dic = {}
        if len(df_sa) < 5:
            extra = process.extract(naad_al, df_sa.naad, limit = len(df_sa))
            for i in range(len(df_sa)):
                index_sa = extra[i][2]
                index_sa1 = df_sa['FIDSAFE'][index_sa]
                longitude_y = df_sa['longitude_y'][index_sa]
                latitude_y = df_sa['latitude_y'][index_sa]
                g1 = (latitude_x, longitude_x)
                g2 = (latitude_y, longitude_y)
                distance = geodesic(g1, g2).meters
                dic[index_sa1] = distance
        else:
            extra = process.extract(naad_al, df_sa.naad, limit = 5)
            for i in range(5):
                index_sa = extra[i][2]
                index_sa1 = df_sa['FIDSAFE'][index_sa]
                longitude_y = df_sa['longitude_y'][index_sa]
                latitude_y = df_sa['latitude_y'][index_sa]
                g1 = (latitude_x, longitude_x)
                g2 = (latitude_y, longitude_y)
                distance = geodesic(g1, g2).meters
                dic[index_sa1] = distance
        minkey = min(dic, key = dic.get)
        df_al['key'][a] = minkey
        # df_sa = df_sa[-df_sa.FIDSAFE.isin([minkey])]
        
    global df_mat 
    df_mat = df_al.merge(df_sa,left_on='key',right_on = 'FIDSAFE', how= 'left')
    return df_mat

def matchname(row):
    naad1 = row["naad_x"]
    naad2 = row["naad_y"]
    
    result = fuzz.WRatio(naad1, naad2)
    return result

def cal_distance(row):
    long1 = row['longitude_x']
    lat1 = row['latitude_x']
    long2 = row['longitude_y']
    lat2 = row['latitude_y']
    g1 = (lat1, long1)
    g2 = (lat2, long2)

    distance = geodesic(g1, g2).meters
    return distance

# main 
if __name__ == '__main__':
    df1 = pd.read_csv("C:/Users/ryanz/Desktop/NY alcohol_0107_all_11_yesco.csv")
    df2 = pd.read_csv("C:/Users/ryanz/Desktop/2022-01-07-21-core_poi5.csv",encoding = "ISO-8859-1")
    
    df1['naad'] = df1['name'] + ' ' + df1['address1']
    df2['naad'] = df2['name'] + ' ' + df2['address']
    
    df1[["zip"]] = df1[["zip"]].astype(str)
    df2[["zip"]] = df2[["zip"]].astype(str)
    df1['key'] = 'b'
    
    ziplist = df1['zip'].unique()
    num = len(ziplist)
    
    dfsy = []
    dfsn = []
    index = 1
    for m in ziplist:
        df_al = df1[df1['zip'] == m]
        df_sa = df2[df2['zip'] == m]
        df_al.reset_index(drop = True, inplace = True) # that is the reson why I get an error: Keyerror 1
        df_sa.reset_index(drop = True, inplace = True) # that is the reson why I get an error: Keyerror 1
        if df_sa.empty == False:
            matching(df_al, df_sa)
            dfsy.append(df_mat)
        else:
            dfsn.append(df_al)
        print(str(num) + ":" + str(index))
        index += 1
        
    result_yes = pd.concat(dfsy)
    result_no = pd.concat(dfsn)
    
    result_yes['ratio_name'] = result_yes.apply(lambda result_yes: matchname(result_yes), axis=1)
    result_yes['distance'] = result_yes.apply(lambda result_yes: cal_distance(result_yes), axis=1)
    
    result_yes.to_csv("C:/Users/ryanz/Desktop/real_result_yes11.csv", index = False)
    result_no.to_csv("C:/Users/ryanz/Desktop/real_result_no11.csv", index = False)
    
    # df_al.to_csv("C:/Users/ryanz/Desktop/df_al.csv", index = False)
    # df_sa.to_csv("C:/Users/ryanz/Desktop/df_sa.csv", index = False)