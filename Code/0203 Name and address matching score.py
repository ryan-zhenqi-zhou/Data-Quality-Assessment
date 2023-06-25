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

result_yes = pd.read_csv("C:/Users/ryanz/Box Sync/220104-NIAAA/04 Matching/07 Result (with name address and distance) 2/Model 4 result0114.csv")

def WRationame(row):
    name1 = row["name_x"]
    name2 = row["name_y"]
    
    result = fuzz.WRatio(name1, name2)
    return result

def WRatioaddress(row):
    address1 = row["address_x"]
    address2 = row["address_y"]
    
    result = fuzz.WRatio(address1, address2)
    return result

def rationame(row):
    name1 = str(row["name_x"])
    name2 = str(row["name_y"])
    
    result = fuzz.ratio(name1, name2)
    return result

def ratioaddress(row):
    address1 = row["address_x"]
    address2 = row["address_y"]
    
    result = fuzz.ratio(address1, address2)
    return result

def partialname(row):
    name1 = str(row["name_x"])
    name2 = str(row["name_y"])
    
    result = fuzz.partial_ratio(name1, name2)
    return result

def partialaddress(row):
    address1 = row["address_x"]
    address2 = row["address_y"]
    
    result = fuzz.partial_ratio(address1, address2)
    return result

def sortname(row):
    name1 = row["name_x"]
    name2 = row["name_y"]
    
    result = fuzz.token_sort_ratio(name1, name2)
    return result

def sortaddress(row):
    address1 = row["address_x"]
    address2 = row["address_y"]
    
    result = fuzz.token_sort_ratio(address1, address2)
    return result

def setname(row):
    name1 = row["name_x"]
    name2 = row["name_y"]
    
    result = fuzz.token_set_ratio(name1, name2)
    return result

def setaddress(row):
    address1 = row["address_x"]
    address2 = row["address_y"]
    
    result = fuzz.token_set_ratio(address1, address2)
    return result

result_yes['ratio_name1'] = result_yes.apply(lambda result_yes: WRationame(result_yes), axis=1)
result_yes['ratio_address'] = result_yes.apply(lambda result_yes: WRatioaddress(result_yes), axis=1)
# result_yes['ratio_name'] = result_yes.apply(lambda result_yes: rationame(result_yes), axis=1)
# result_yes['ratio_address'] = result_yes.apply(lambda result_yes: ratioaddress(result_yes), axis=1)
# result_yes['partial_name'] = result_yes.apply(lambda result_yes: partialname(result_yes), axis=1)
# result_yes['partial_address'] = result_yes.apply(lambda result_yes: partialaddress(result_yes), axis=1)
# result_yes['sort_name'] = result_yes.apply(lambda result_yes: sortname(result_yes), axis=1)
# result_yes['sort_address'] = result_yes.apply(lambda result_yes: sortaddress(result_yes), axis=1)
# result_yes['set_name'] = result_yes.apply(lambda result_yes: setname(result_yes), axis=1)
# result_yes['set_address'] = result_yes.apply(lambda result_yes: setaddress(result_yes), axis=1)



result_yes.to_csv("C:/Users/ryanz/Box Sync/220104-NIAAA/04 Matching/07 Result (with name address and distance) 2/Model 4 result0115.csv", index = False)
