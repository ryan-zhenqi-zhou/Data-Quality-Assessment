# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:52:50 2022

@author: ryanz
"""

# import packages
import pandas as pd
import numpy as np

# select NY
df1 = pd.read_csv("C:/Users/ryanz/Desktop/Liquor_Authority_Current_List_of_Active_Licenses.csv")
df2 = df1[df1['Premise State'] == 'NY']

# select alcohol with license (no OP)
df2["code"] = df2['License Type Code'] + df2['License Class Code']
df3 = df2[(df2['code'] == 'TW344') | (df2['code'] == 'L222') | (df2['code'] == 'WA305') | (df2['code'] == 'W322') | (df2['code'] == 'D101') | (df2['code'] == 'MI101') | (df2['code'] == 'BR102') | (df2['code'] == 'C103') | (df2['code'] == 'BC104') | (df2['code'] == 'CO105') | (df2['code'] == 'LL203') | (df2['code'] == 'DW301') | (df2['code'] == 'WW303') | (df2['code'] == 'NC252')]
# select alcohol with license (OP)
df_op = df2[df2['code'] == 'OP252']
df_op1 = df_op[(df_op['Method of Operation'].str[:9] == "BA/TAVERN") | (df_op['Method of Operation'].str[:3] == "BAR") | (df_op['Method of Operation'].str[:10] == "BAT/TAVERN") | (df_op['Method of Operation'].str[:10] == "NIGHT CLUB") | (df_op['Method of Operation'].str[:9] == "NIGHTCLUB") | (df_op['Method of Operation'].str[:4] == "PUB/") | (df_op['Method of Operation'].str[:6] == "TAVERN") | (df_op['Method of Operation'].str[:7] == "TAVERNT")]

dff = [df3, df_op1]
df_final = pd.concat(dff)
df_final.to_csv("C:/Users/ryanz/Desktop/NY alcohol.csv")

# select alcohol others
df_other = df2[(df2['code'] == 'MW307') | (df2['code'] == 'WW353')]
df_other1 = df_op[(df_op['Method of Operation'].str[:7] == "BREWERY") | (df_op['Method of Operation'].str[:6] == "HOOKAH") | (df_op['Method of Operation'].str[:10] == "LOUNGE/BAR")]

dff_other = [df_other, df_other1]
df_other_final = pd.concat(dff_other)
df_other_final.to_csv("C:/Users/ryanz/Desktop/NY alcohol_other.csv")
