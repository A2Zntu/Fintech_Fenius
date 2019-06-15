# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:39:03 2019

@author: Stella
"""

import pandas as pd
import numpy as np
import scipy.optimize
import datetime
import math
import os
import matplotlib.pyplot as plt
from fun import *
import matplotlib.font_manager as font_manager
font_path = 'msjh.ttc'
myfont = font_manager.FontProperties(fname='msjh.ttc',
                                   weight='bold',
                                   style='normal', size=16)


def NAVLists():
    
    namelist = ['China','Common', 'ETF', 'OTC', 'Tech', 'Value']
    namedict = dict({'China':"中概股基金",'Common':"一般股票型基金", "ETF": "指數型基金", "OTC":"店頭市場基金", "Tech":"科技型基金", "Value":"價值型基金"}) 
    dflist = []
    
    for i in range(len(namelist)):
        inputFileName = namelist[i]+".csv"
        dflist.append(formatting(inputFileName))
        
    return dflist

def openJsonfile():
    global fund_dict
    with open('subfunction/data/funds_dictionary.json') as json_file:  
        fund_dict = json.load(json_file) 


def plot_nav(codename, moneydjname, tejname, thedflist = dflist):
    
    thecat = None
    for i in range(len(thedflist)):
        if tejname in thedflist[i].columns:
            thecat = i            
        else:
            pass
    if thecat == None:
        print("輸入基金名稱有誤")
    else:

        plt.rcParams['font.sans-serif'] = ['SimHei','Arial']
        thedflist[thecat][tejname].plot(label = "NAV", figsize = (10,5))
        plt.grid()
        plt.title(moneydjname, fontproperties = myfont)
        plt.savefig("./static/"+ codename +".jpg")
        plt.clf()
        
        return(plt)



if __name__ ==  '__main__':
    dflist = NAVLists()
    openJsonfile()

    for codeName in China_codes: # Replaced by Common_codes, Tech_codes, ....
        moneydjname = fund_dict[codeName]["moneydjname"]
        tejname = fund_dict[codeName]["tejname"]
        plot_nav(codeName, moneydjname, tejname)
    
