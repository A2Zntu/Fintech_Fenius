# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:17:44 2019

@author: Stella
"""

import pandas as pd
import numpy as np
import scipy.optimize
import datetime
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


def extract_q(fundname,theqlist):
    qvalue = None
    for i in theqlist:
        if fundname in i['Name'].tolist():
            qvalue = i.loc[i['Name']== fundname,'Q'].values[0]
        else:
            pass
    if qvalue == None:
        print("輸入基金名稱有誤")
    else:
        return(fundname+" 的風險Q值為: "+ sci_notation(qvalue,4))
        
if __name__ ==  '__main__':        
    extract_q('T0110Y 兆豐豐台灣',q_list)        
