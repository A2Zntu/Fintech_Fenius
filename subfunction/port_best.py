# -*- coding: utf-8 -*-
"""
Created on Fri May 31 02:49:19 2019

@author: Stella
"""


import pandas as pd
import numpy as np
import scipy.optimize
import math
import os
from fun import *

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
    

testname = "0050 元大台灣50"    

port_qlist = []
indbest_list = best_fund(q_list)

for i in range(len(indbest_list)):
    port_qlist.append(portfolio(testname,indbest_list[i],dflist))

        
best_port(port_qlist)    
