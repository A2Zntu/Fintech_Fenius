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
from subfunction.fun import *

namelist = ['China','Common', 'ETF', 'OTC', 'Tech', 'Value']
namedict = dict({'China':"中概股基金",'Common':"一般股票型基金", "ETF": "指數型基金", "OTC":"店頭市場基金", "Tech":"科技型基金", "Value":"價值型基金"})

def best5Caller():
	dflist = []
	return_list=[]
	q_list=[]

	for i in range(len(namelist)):
		inputFileName = namelist[i]+".csv"
		dflist.append(formatting(inputFileName))
		return_list.append(return_calculate(dflist[i],1))
		q_list.append(riskiness(return_list[i],1,namelist[i]))
		

		   
	return call_the_best(q_list)  	


if __name__ ==  '__main__':

	dflist = []
	return_list=[]
	q_list=[]

	for i in range(len(namelist)):
		inputFileName = namelist[i]+".csv"
		dflist.append(formatting(inputFileName))
		return_list.append(return_calculate(dflist[i],1))
		q_list.append(riskiness(return_list[i],1,namelist[i]))
		

		   
	call_the_best(q_list)
