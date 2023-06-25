# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 22:01:10 2022

@author: ryanz
"""

import pandas as pd
import numpy as np

df1 = pd.read_csv("C:/Users/ryanz/Desktop/real_result_yes4.csv")

# df1 = df1[-df1.FIDALCO.isin([1])]
# df1 = df1[-df1.FIDALCO.isin([2])]

safelist = df1['FIDSAFE'].unique()
# df1['key'] = 'b'
lis = []

for m in safelist:
    df_ch = df1[df1['FIDSAFE'] == m]
    df_ch.reset_index(drop = True, inplace = True)
    dic = {}
    if len(df_ch) >= 2:
        for i in range(len(df_ch)):
            fidalco = df_ch['FIDALCO'][i]
            address = df_ch['ratio_address'][i]
            dic[fidalco] = address
        maxkey = max(dic, key = dic.get)
        new = [k for k,v in dic.items() if v == dic[maxkey]]
        dicd = {}
        if len(new) >= 2:
            for d in range(len(new)):
                index = df_ch[df_ch.FIDALCO == new[d]].index.tolist()[0]
                distance = df_ch['distance'][index]
                dicd[new[d]] = distance
            mindis = min(dicd, key = dicd.get)
            lis.append(mindis) 
        else:
            lis.append(maxkey)
    else:
        lis.append(df_ch['FIDALCO'][0])
        
diclis = {"lis" : lis}
data = pd.DataFrame(diclis)

df_mat = df1.merge(data,left_on='FIDALCO',right_on = 'lis', how= 'left')
df_mat.to_csv("C:/Users/ryanz/Desktop/real_result_yes9.csv", index = False)

























##########################################################################################################
edg1 = pd.read_csv("C:/Users/ryanz/Desktop/real_result_yes3.csv")
edglist = edg1['FIDSAFE'].unique()
dsfe = []
for f in edglist:
    df_ch3 = edg1[edg1['FIDSAFE'] == f]
    if len(df_ch3) >= 2:
        dsfe.append(df_ch3)
        
edg2 = pd.concat(dsfe)
edg2.to_csv("C:/Users/ryanz/Desktop/real_result_yes4.csv", index = False)
##########################################################################################################
data1 = pd.read_csv("C:/Users/ryanz/Desktop/real_result_yes4.csv")
data1[["FIDSAFE"]] = data1[["FIDSAFE"]].astype(str)
data1[["ratio_address"]] = data1[["ratio_address"]].astype(str)
data1['fidadd'] = data1['FIDSAFE'] + ' ' + data1['ratio_address']
dalist = data1['fidadd'].unique()
dsfg = []

for n in dalist:
    df_ch2 = data1[data1['fidadd'] == n]
    if len(df_ch2) >= 2:
        dsfg.append(df_ch2)
        
data2 = pd.concat(dsfg)
data2.to_csv("C:/Users/ryanz/Desktop/real_result_yes5.csv", index = False)



































