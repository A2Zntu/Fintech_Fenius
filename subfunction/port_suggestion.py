# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:43:38 2019

@author: Stella
"""

import pandas as pd
import numpy as np
import scipy.optimize
import datetime
import math
import os
from fun_local import *
from itertools import combinations 

def price_to_q():
    namelist = ['China','Common', 'ETF', 'OTC', 'Tech', 'Value']
    namedict = dict({'China':"中概股基金",'Common':"一般股票型基金", "ETF": "指數型基金", "OTC":"店頭市場基金", "Tech":"科技型基金", "Value":"價值型基金"})

    dflist = []
    return_list=[]
    q_list=[]
    
    for i in range(len(namelist)):
        inputFileName = namelist[i]+".csv"
        dflist.append(formatting(inputFileName))
        return_list.append(return_calculate(dflist[i],1))
        q_list.append(riskiness(return_list[i],1,namelist[i]))
    
    return (dflist, return_list, q_list)

# price_to_q[0] = dflist, [1]=return_list, [2]= q_list


def nav_gen(i, comb_list):
    df = pd.DataFrame()
    df['date'] = dflist[0]['date']
    for m in comb_list:
        for k in range(i):
            if k==0:
                colname = str(m[k])+"."
            elif k==max(range(i)):
                colname = colname + str(m[k])
            else:
                colname = colname + str(m[k])+"."
        
        nav_list = []
        for n in m:
            nav_list.append(extract_nav(indbest_list[n], dflist))
        sum_list = sum(map(np.array, nav_list))
        avg_list = [x/i for x in sum_list]
        df[colname] = avg_list
    return df


def equal_portfolio():
    #from nav to q
    port_ret = []
    port_q =[]
    fullnav = {}
    for i in range(2,6):
        comb = combinations([0,1,2,3,4,5],i)
        comb = list(comb)
        fullnav[i] = nav_gen(i,comb)
        port_ret.append(return_calculate(fullnav[i],1))
        port_q.append(riskiness(port_ret[i-2],1, i))        
    return (port_ret, port_q)


q_list = price_to_q()[2]

indbest_list = best_fund(q_list)
call_the_best_p(equal_portfolio()[1], indbest_list)



