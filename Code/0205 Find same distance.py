# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 22:01:10 2022

@author: ryanz
"""

import pandas as pd
import numpy as np

# df1 = pd.read_csv("C:/Users/ryanz/Desktop/real_result_yes3.csv")

# addlist = df1['distance'].unique()
# dsf = []
# for m in addlist:
#     df_ch = df1[df1['distance'] == m]
#     if len(df_ch) >= 2:
#         dsf.append(df_ch)

# result_yes = pd.concat(dsf)
# result_yes.to_csv("C:/Users/ryanz/Desktop/3.csv")
# ###########################################################################################
# data1 = pd.read_csv("C:/Users/ryanz/Desktop/real_result_yes3.csv")
# data2 = pd.read_csv("C:/Users/ryanz/Desktop/3.csv")
# df_mat = data1.merge(data2,left_on='FIDALCO',right_on = 'SAMEDIS', how= 'left')
# df_mat.to_csv("C:/Users/ryanz/Desktop/real_result_yes4.csv")
###########################################################################################
sure1 = pd.read_csv("C:/Users/ryanz/Desktop/real_result_yes9.csv")
surelist = sure1['distance'].unique()
# dsfs = []
for m in surelist:
    df_sure = sure1[sure1['distance'] == m]
    df_sure.reset_index(drop = True, inplace = True)
    if len(df_sure) >= 2:
        if pd.isna(df_sure['lis'][0]) == False:
            for x in range(len(df_sure)):
                index = sure1[sure1.FIDALCO == df_sure['FIDALCO'][x]].index.tolist()[0]
                sure1["lis"][index] = sure1['FIDALCO'][index]
sure1.to_csv("C:/Users/ryanz/Desktop/real_result_yes10.csv")

# match safegraph data
df1 = pd.read_csv("C:/Users/ryanz/Desktop/2022-01-07-21-core_poi4.csv")
df2 = pd.read_csv("C:/Users/ryanz/Desktop/yes3.csv")   
df_mat = df1.merge(df2,left_on='FIDSAFE',right_on = 'FIDSAFE', how= 'left')
df_mat.to_csv("C:/Users/ryanz/Desktop/2022-01-07-21-core_poi5.csv")

# match alcohol data
df1 = pd.read_csv("C:/Users/ryanz/Desktop/NY alcohol_0107_all_5_yesco.csv")
df2 = pd.read_csv("C:/Users/ryanz/Desktop/no3.csv")   
df_mat = df1.merge(df2,left_on='FIDALCO',right_on = 'FIDALCO', how= 'left')
df_mat.to_csv("C:/Users/ryanz/Desktop/NY alcohol_0107_all_11_yesco.csv")