# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:10:31 2022

@author: ryanz
"""
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import os
from scipy.optimize import curve_fit

# Select NY region
df1 = pd.read_csv("C:/Users/ryanz/Box Sync/220104-Alcohol/01 NYS Alcohol outlet data/01 CSV/Liquor_Authority_Current_List_of_Active_Licenses - Copy.csv")
df2 = df1[df1['Premise State'] == 'NY']
df2['Method of Operation_1'] = df2['Method of Operation'].str.lower()
df2.to_csv("C:/Users/ryanz/Box Sync/220104-Alcohol/01 NYS Alcohol outlet data/01 CSV/Liquor_Authority_Current_List_of_Active_Licenses_NY.csv")

# Fliter with License Type Code/License Class Code/Method of Operation
# Delete - A: grocery/convenience store, gas station
# Delete - AL: airline serving
# Delete - AW 122: grocery store
# Notsure - 2470-2476 AW 141-441
# Delete - AX: grocery/convenience store, gas station
# Delete - BB: Bed and Breakfast
# Remain - BC: wholesale cider
# Notsure - 14760-14765 BL: bottle club, seems delete https://www.pnj.com/story/news/2019/05/17/what-bottle-club-bedlam/3706508002/
# Delete - BP: Ball park
# Delete - BW: bed and breakfast
# Remain - C: wholesale beer
# Notsure - CB: Club
# Remain - CD: cider producer
# Remain - CF: farm cidery
# Notsure - CL: Club
# Remain - CD: cider producer
# Remain - CM: combined craft manufacturer
# Remain - CO: wholesale beer
# Notsure - CR: Club, some of them are night club...
# Delete - CT: Catering Establishment
# Notsure - CW: Club
# Remain - CX/CZ: custom beermakers' center
# Remain - D: brewer
# Remain - DA/DB/DC/DD: distiller
# Remain - DA/DB/DC/DD: distiller
# Delete - DS/DX: drug store
# Remain - DW: winery
# Notsure - EB: Eating Place Beer, some of them are bar
# Notsure - EL: Eating Place Beer, some of them are tavern
# Remain - FD: farm brewer
# Remain - FP: TEMPORARY WINERY/FARM WINERY
# Remain - FW: farm winery
# Remain - FY: farm meadery
# Delete - GC: golf club
# Delete - HL/HW: hotel
# Remain - IL: liquor importer
# Remain - L/LL: liquor and wine store
# Delete - MD: mead producer
# Remain - MI: micro brewer
# Delete - MR: restaurant brewer
# Notsure - MU: MIXED USE ON-PREMISES LIQUOR
# Remain - MW: micro farm winery
# Remain - NC: night club
# Notsure - OP: ON-PREMISES LIQUOR some of them not so sure
# Notsure - RL: Restaurant, not so sure, some of them are tavern - restaurant
# Delete - RR: railroad car serving beer, cider, wine and liquor
# Delete - RS: roadside farm market
# Notsure - RW: RESTAURANT WINE not so sure, some of them are tavern - restaurant
# Remain - SB: summer beer
# Notsure - SL: SUMMER (O.P.) FOOD & BEV  SUMMER (0. P.) ENTERTAINMENT
# Notsure - TL: O.P. FOOD AND BEV not so sure, some of them are tavern - restaurant
# Delete - VL: Vessels
# Remain - W/WA: wine store
# Delete - WC: caterer serving beer wine & cider
# Remain - WO: bar/tavern
# Remain - WS: direct wine shipper
# Remain - WW: wine wholesaler
# Notsure - ZL/ZT/ZW: Mix/Winter or something




df3 = pd.read_csv("C:/Users/ryanz/Box Sync/220104-Alcohol/01 NYS Alcohol outlet data/01 CSV/Liquor_Authority_Current_List_of_Active_Licenses_NY.csv")
df3['License'] = df3['License Type Code'] + ' ' + df3['License Class Code']
