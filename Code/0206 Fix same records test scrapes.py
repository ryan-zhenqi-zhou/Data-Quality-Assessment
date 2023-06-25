# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 12:43:56 2022

@author: ryanz
"""

import pandas as pd
import numpy as np

dic = {"a" : 100, "b" : 100, "c" : 80}
# dic1 = {"a" : [124], "b" : [32]}
# df1 = pd.DataFrame(dic1) 
# df2 = pd.DataFrame.stack(df1)
# df2.reset_index()
# df2.to_csv("C:/Users/ryanz/Desktop/test.csv")
#####################################################################
lis = []
df3 = pd.read_csv("C:/Users/ryanz/Desktop/test.csv")
maxkey = max(dic, key = dic.get)

new = [k for k,v in dic.items() if v == dic[maxkey]]
if len(new) >= 2:
    for d in range(len(new)):
        index = df3[df3.FIDSAFE == new[d]].index.tolist()[0]