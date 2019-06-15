# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:51:19 2019

@author: Stella
"""
import pandas as pd
import numpy as np
import scipy.optimize
import datetime
import math
import os
from decimal import Decimal
from fun_local import *


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

q_list = price_to_q()[2]

newq_list = []

for j in range(len(q_list)):
    Q = []
    Name = []
    Ranking = []
    for i in range(q_list[j].shape[0]):
        Ranking.append(q_list[j].iloc[i,2])
        Name.append(name_reconcile(q_list[j].iloc[i,1])[1])
        Q.append(sci_notation(q_list[j].iloc[i,0],4))
    newq_list.append(pd.DataFrame(list(zip(Ranking, Name, Q))))