# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:40:10 2019

@author: Stella
"""

import pandas as pd
import numpy as np
import scipy.optimize
import datetime
import math
import os
from decimal import Decimal

namelist = ['China','Common', 'ETF', 'OTC', 'Tech', 'Value']
namedict = dict({'China':"中概股基金",'Common':"一般股票型基金", "ETF": "指數型基金", "OTC":"店頭市場基金", "Tech":"科技型基金", "Value":"價值型基金"})


def formatting(csvname):
    working_dir = os.getcwd()
    dateparse = lambda x: pd.datetime.strptime(x, '%Y/%m/%d')
    # os.path.join(working_dir, 'data','NAV',csvname)
    df = pd.read_csv("subfunction/data/NAV/"+csvname, parse_dates=['date'], date_parser=dateparse, encoding='utf_8_sig')
    #df = pd.read_csv('subfunction/data/NAV/'+csvname, parse_dates=['date'], date_parser=dateparse, encoding='utf_8_sig')
    
    df = pd.pivot_table(df,index=["name"],columns=["date"], values=["name"])
    
    namelist = list(df)
    
    
    goodlist = list()
    for i in namelist:
        goodlist.append(i[1].date())
        
    df.columns = goodlist
    df = df.T
    df = df.sort_index(ascending=False)
    df.insert(loc=0,column='date', value = df.index)
    return(df)


def return_calculate(data,datasource):
    # datasource=1 means python df, then we should enter df name in data
    # datasource=2 means reading from csv file, then we should enter filename.csv
    
    # setting number of weeks
    numofw = 157
    
    if datasource==2:
        working_dir = os.getcwd()
        df = pd.read_csv(os.path.join(working_dir,'data','NAV',data), encoding='utf_8_sig')
        df = df.rename({'Unnamed: 0': 'date'}, axis=1) 
        startdate = df["date"][0].split("-")
        startdate = datetime.date(int(startdate[0]),int(startdate[1]),int(startdate[2]))
    else:
        df = data
        startdate = df["date"][0]
    
    
    # extracting (t-7) list of dates
    c1 = [startdate]
    for i in range(numofw):
        oneweek = datetime.timedelta(weeks = 1)
        startdate = startdate - oneweek 
        c1.append(startdate)
    
    
    
    namelist = list(df.columns) 
    namelist.remove('date')

    
    #calculate return
    newDF = pd.DataFrame()
    for j in namelist:
        rtlist =[]
        for i in range(numofw):
            try:
                latter = df.loc[df['date'] == c1[i], j].iloc[0]
                former = df.loc[df['date'] == c1[i+1], j].iloc[0]
                ret = latter/former - 1
                rtlist.append(ret)
                
            except:
                rtlist.append('no value')
        newDF[j]=rtlist
    
    
    finalwd = c1[1:]
    newDF.index = finalwd
    return(newDF)



def riskiness(data,datasource,category):
    # datasource=1 means python df(date as index), then we should enter df name in data
    # datasource=2 means reading from csv file, then we should enter filename.csv
    if datasource==2:
        working_dir = os.getcwd()
        df = pd.read_csv(os.path.join(working_dir, 'data','NAV',data), encoding='utf_8_sig')
        df = df.rename({'Unnamed: 0': 'date'}, axis=1) 
        df = df.set_index('date')
    else:
        
        df = data
        
    # extract fund name
    namelist = list(df.columns) 
     
    
    r =list()
    
    # iterate through fund returns
    for col in namelist:
        ret_list = df[col].values.tolist()
        ret_list = list(filter(lambda a: a != 'no value', ret_list))
        ret_list = [float(i) for i in ret_list]
        
        initial_r = np.var(ret_list) / (2 * np.mean(ret_list)) 
        def F(x):
            newlist = [-n / x for n in ret_list]
            return np.mean(np.exp(newlist))-1
        try:
            x = scipy.optimize.fsolve(F,initial_r)
            r.append(np.asscalar(x)) 
        except:
            r.append('nan')
        
        
    Q_list = list()
    for i in r:
        if i!='nan':
            temp = np.exp(-(1/i))
            Q_list.append(temp) 
        else:
            Q_list.append(np.nan)
    
    
    table = pd.DataFrame(list(zip(Q_list, namelist)), columns =['Q', 'Name']) 
    sorted_table = table.sort_values(by=['Q'],na_position='last')
    sorted_table['Ranking'] = np.arange(len(sorted_table))+1
    sorted_table['Category'] = str(category)
    riskiness_m = sorted_table
    
    return(riskiness_m)



def call_the_best(thelist):
    output = []
    for i in range(len(thelist)):
        tempdf = thelist[i]
        name = tempdf.loc[tempdf["Ranking"]==1,"Name"].values[0]
        q = tempdf.loc[tempdf["Ranking"]==1,"Q"].values[0]
        cat = tempdf.loc[tempdf["Ranking"]==1,"Category"].values[0]
        
        # print(namedict[cat]+": "+str(name)+" 最佳，風險Q值為"+str(q))
        output.append(namedict[cat]+": "+str(name)+" 最佳，風險Q值為"+ sci_notation(q,4))
    return output


def best_fund(thelist):
    best_list=[]
    for i in range(len(thelist)):
        tempdf = thelist[i]
        name = tempdf.loc[tempdf["Ranking"]==1,"Name"].values[0]
        best_list.append(name)
    return(best_list)


def extract_nav(fundname,thedflist):
    nav = None
    for i in thedflist:
        if fundname in i.columns:
            nav = i.loc[:,fundname].tolist()
        else:
            pass
    if nav == None:
        print("輸入基金名稱有誤")
    else:
        return(nav)
        


def portfolio(fund_self, fund_benchmark, thedflist):
    # the argument here both are fund names
    comb_nav = pd.DataFrame()
    nav_self = extract_nav(fund_self, thedflist)
    nav_benchmark = extract_nav(fund_benchmark, thedflist)
    weight = [x/10 for x in range(0,11)]
    comb_nav['date']= thedflist[0]['date']
    for i in weight:
        w_self = [i*x for x in nav_self]
        w_benchmark = [(1-i)*x for x in nav_benchmark]
        comb_nav[str(int(i*10))+"to"+str(int(10-i*10))] = [sum(x) for x in zip(w_self, w_benchmark)]
    port_ret = return_calculate(comb_nav,1)
    port_q = riskiness(port_ret,1,str(fund_benchmark))
    return(port_q)
    
def best_port(thelist):
     for i in range(len(thelist)):
        tempdf = thelist[i]
        name = tempdf.loc[tempdf["Ranking"]==1,"Name"].values[0]
        q = tempdf.loc[tempdf["Ranking"]==1,"Q"].values[0]
        cat = tempdf.loc[tempdf["Ranking"]==1,"Category"].values[0]
        
        print("最佳搭配是跟: "+str(cat)+" 之"+str(name)+" 為最佳，風險Q值為"+ sci_notation(q,4))
        
def name_reconcile(tejname):
    filename="schemecode.csv"
    df = pd.read_csv('data/'+filename, encoding='utf_8_sig')
    codename = df.loc[df['tejname']==tejname,'codename'].values[0]
    infoname = df.loc[df['tejname']==tejname,'infoname'].values[0]
    return(codename, infoname)
    

def sci_notation(number, sig_fig=2):
    ret_string = "{0:.{1:d}e}".format(number, sig_fig)
    a,b = ret_string.split("e")
    b = int(b) #removed leading "+" and strips leading zeros too.
    return a + " * 10^" + str(b)

