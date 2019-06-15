# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:44:51 2019

@author: Evan
"""

import pandas as pd 
import os 
import json

work_dir = os.getcwd()
data_path = os.path.join(work_dir, "data")

## open Json file
with open('subfunction/data/funds_dictionary.json') as json_file:  
    fund_dict = json.load(json_file) 
    
index_list = pd.read_csv("subfunction/data/Fund_info/index_list.csv", 
                         encoding = "cp950", header = None)[0].tolist()

def info_generate(codeName):
    '''
    @param: fund_name should be the name on the list
    @post: The function would return a string of the specific fund information
    '''
    if codeName in fund_dict:
        firstLine = u'\u2022' + " " + "基金名稱" + " : " + fund_dict[codeName]["moneydjname"] + "\n"
        line = [firstLine]
        
        for i, info in enumerate(fund_dict[codeName]["info"]):
            try:
                string = u'\u2022' + " " + index_list[i] + " : " + info + "\n"
            except TypeError:
                string = u'\u2022' + " " + index_list[i] + " : " + "Nan" + "\n"
            line.append(string)
            
        return line
    
    else:
        return ["不好意思，找不到相關基金。請您檢查基金代碼是否在基金列表中，謝謝。"]
    
def ret_generate(codeName):
    '''
    @param: fund_name should be the name on the list
    @post: The function would return a string of the specific fund information
    '''
    if codeName in fund_dict:
        firstLine = u'\u2022' + " " + "基金名稱" + " : " + fund_dict[codeName]["moneydjname"] + "\n"
        line = [firstLine]
    
        string1 = u'\u2022' + " " + "近一個月變動率%" + " : " + str(fund_dict[codeName]["1monthChange (%)"]) + "\n"
        string2 = u'\u2022' + " " + "近三個月變動率%" + " : " + str(fund_dict[codeName]["3monthChange (%)"]) + "\n"
        string3 = u'\u2022' + " " + "近六個月變動率%" + " : " + str(fund_dict[codeName]["6monthChange (%)"]) + "\n"
        string4 = u'\u2022' + " " + "近一年變動率%" + " : " + str(fund_dict[codeName]["1yearChange (%)"]) + "\n"
        
        line.append(string1)
        line.append(string2)
        line.append(string3)
        line.append(string4)
            
        return line
    
    else:
        return ["不好意思，找不到相關基金。請您檢查基金代碼是否在基金列表中，謝謝。"]

def onTheFundList(fundName, category):
    findTheFund = False
    data_path = categoryTxt(category)
    FundList = pd.read_csv(data_path, encoding = "cp950", header = None)
    FundList = list(FundList[0]) #pull into list
    if fundName in FundList:
        findTheFund = True
        
    return findTheFund

def categoryCsv(category):
    if category == "Tech":
        data_csv = "subfunction/data/Fund_info/Tech/Tech_basic_info.csv"
    elif category == "Index":
        data_csv = "subfunction/data/Fund_info/ETF/ETF_basic_info.csv"
    elif category == "OTC":
        data_csv = "subfunction/data/Fund_info/OTC/OTC_basic_info.csv"
    elif category == "Value":
        data_csv = "subfunction/data/Fund_info/Value/Value_basic_info.csv"       
    elif category == "China":
        data_csv = "subfunction/data/Fund_info/China/China_basic_info.csv" 
    elif category == "Common":
        data_csv = "subfunction/data/Fund_info/Common/Common_basic_info.csv" 
    
    return data_csv


def categoryTxt(category):
    if category == "Tech":
        data_txt = "subfunction/data/Fund_info/TechFundList.txt"
    elif category == "Index":
        data_txt = "subfunction/data/Fund_info/ETFFundList.txt"
    elif category == "OTC":
        data_txt = "subfunction/data/Fund_info/OTCFundList.txt"
    elif category == "Value":
        data_txt = "subfunction/data/Fund_info/ValueFundList.txt"       
    elif category == "China":
        data_txt = "subfunction/data/Fund_info/ChinaFundList.txt" 
    elif category == "Common":
        data_txt = "subfunction/data/Fund_info/CommonFundList.txt" 
    
    return data_txt
    

def allFund(category):
    data_path = categoryTxt(category)
    FundList = pd.read_csv(data_path, encoding = "cp950", header = None)    
    FundList = list(FundList[0]) #pull into list
    # FundListString = "\n".join(s for s in FundList)
    return FundList

    
if __name__ ==  '__main__':
    line = info_generate("A01")

    