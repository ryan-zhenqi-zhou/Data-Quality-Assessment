# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:03:33 2022

@author: ryanz
"""

import pandas as pd
import numpy as np

# df = pd.read_csv("C:/Users/ryanz/Desktop/Alcohol NY - NO NA.csv")

# # groupby with License Type Code/License Class Code/Method of Operation_1
# df1 = df.groupby(['License Type Code','License Class Code','Method of Operation_1']).size()
# df1.reset_index()
# df1.to_csv("C:/Users/ryanz/Desktop/1.csv")

# df2 = pd.read_csv("C:/Users/ryanz/Desktop/Alcohol List All.csv")
# df2['All'] = df2['License Type Code'] + df2['License Class Code'] + ' ' + df2['Method of Operation_1']
# df2.to_csv("C:/Users/ryanz/Desktop/Alcohol List All_2.csv")

df = pd.read_csv("C:/Users/ryanz/Desktop/Alcohol List All_2.csv")

# delete
delete = df[df["All"].str.contains('grocery|gorcery|grocerty|grocerty|groceery|grocer|groccery|drug|convenience|airline|restaurant|gas|deli|theater|supermarket|snack|gerocery|grcoery|grcoery|grocey|grocrecy|grocry|groery|groery|groery|groveru|ball|marina|market|breakfast|beverage|arena|vessel servng|vessel serving|vessel selling|theatrical|theatre|sandwich|pizzeria|event space|coffee|café|cafe|cabaret|gallery|comedy|museum|food truck|paint classes|billiard|spa serving|ski lodge|restaruant|railroad|raceway|package|music|museum|motel|golf|caterer|amusement park|art studio|bowling|catering|concert|eating|hotel|game|racetrack|recreation|restarant|sports|stadium')]
df1 = df[~df["All"].str.contains('grocery|gorcery|grocerty|grocerty|groceery|grocer|groccery|drug|convenience|airline|restaurant|gas|deli|theater|supermarket|snack|gerocery|grcoery|grcoery|grocey|grocrecy|grocry|groery|groery|groery|groveru|ball|marina|market|breakfast|beverage|arena|vessel servng|vessel serving|vessel selling|theatrical|theatre|sandwich|pizzeria|event space|coffee|café|cafe|cabaret|gallery|comedy|museum|food truck|paint classes|billiard|spa serving|ski lodge|restaruant|railroad|raceway|package|music|museum|motel|golf|caterer|amusement park|art studio|bowling|catering|concert|eating|hotel|game|racetrack|recreation|restarant|sports|stadium')]
delete.to_csv("C:/Users/ryanz/Desktop/delete.csv")

# remain
remain = df1[df1["All"].str.contains('club|tavern|wholesale|wholesaler|beer store|combined craft|wine product permit|adult entertainment|bar|craft|distiller|farm|liquor store|tenant|winery retail')]
df2 = df1[~df1["All"].str.contains('club|tavern|wholesale|wholesaler|beer store|combined craft|wine product permit|adult entertainment|bar|craft|distiller|farm|liquor store|tenant|winery retail')]
remain.to_csv("C:/Users/ryanz/Desktop/remain.csv")
df2.to_csv("C:/Users/ryanz/Desktop/notsure.csv")