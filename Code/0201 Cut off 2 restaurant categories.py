# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:19:34 2022

@author: ryanz
"""

import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from geopy.distance import geodesic

df2 = pd.read_csv("C:/Users/ryanz/Box Sync/220104-NIAAA/04 Matching/2022-01-07-21-core_poi.csv",encoding = "ISO-8859-1")
df3 = df2[~(df2['sub_category'] == 'Limited-Service Restaurants')]
df4 = df3[~(df3['sub_category'] == 'Snack and Nonalcoholic Beverage Bars')]
df4.to_csv("C:/Users/ryanz/Desktop/2022-01-07-21-core_poi2.csv")