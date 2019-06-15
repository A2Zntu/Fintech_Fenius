# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 00:09:48 2019

@author: Evan
"""

import pandas as pd
import numpy as np 
import os 
import json


#%% import Json

with open('./data/funds_dictionary.json') as json_file:  
    fund_dict = json.load(json_file) 

#%% import data

#path_tech = categoryCsv(category = "Tech").replace("subfunction", ".")
#df_tech = pd.read_csv(path_tech, encoding = "cp950") 
#
#path_index = categoryCsv(category = "Index").replace("subfunction", ".")
#df_index = pd.read_csv(path_index, encoding = "cp950") 
#
#path_otc = categoryCsv(category = "OTC").replace("subfunction", ".")
#df_otc = pd.read_csv(path_otc, encoding = "cp950") 
#
#path_common = categoryCsv(category = "Common").replace("subfunction", ".")
#df_common = pd.read_csv(path_common, encoding = "cp950") 
#
#path_value = categoryCsv(category = "Value").replace("subfunction", ".")
#df_value = pd.read_csv(path_value, encoding = "cp950") 
#
#path_china = categoryCsv(category = "China").replace("subfunction", ".")
#df_china = pd.read_csv(path_china, encoding = "cp950") 


path_codeName = os.path.join(os.getcwd(), "data", "schemecode.csv")
df_codeName = pd.read_csv(path_codeName, encoding = "cp950") 

#%%
staticPicAddress = 'https://hello-ym-world.herokuapp.com/static/'
# create nested dict 
#fund_dict = {}
for i in range(len(df_codeName)):
    dict_key = df_codeName["codename"][i]
    historyPicName = dict_key + ".jpg"
    dict_content = {}
#    dict_content["moneydjname"] = df_codeName["moneydjname"][i]
#    dict_content["tejname"] = df_codeName["tejname"][i]
#    dict_content["category"] = df_codeName["category"][i]
#    dict_content["history"] = staticPicAddress + historyPicName

#    if df_codeName["category"][i] == "Tech":
#        df_temp = df_tech
#    elif df_codeName["category"][i] == "Value":
#        df_temp = df_value
#    elif df_codeName["category"][i] == "OTC":
#        df_temp = df_otc
#    elif df_codeName["category"][i] == "China":
#        df_temp = df_china
#    elif df_codeName["category"][i] == "Common":
#        df_temp = df_common
#    elif df_codeName["category"][i] == "ETF":
#        df_temp = df_index
#    
#    # attach basic info
#    if df_codeName["moneydjname"][i] in df_temp.columns:
#        list_info = []
#        for j in range(19): # only need to include 19 rows in basic_info 
#            list_info.append(df_temp[df_codeName["moneydjname"][i]][j])
#    dict_content["info"] = list_info
    
    # attach riskiness q
#    q_value = extract_q(df_codeName["tejname"][i], q_list)
#    dict_content["riskiness"] = q_value             
    
    
    fund_dict[dict_key]["history"] = staticPicAddress + historyPicName
    fund_dict[dict_key]["1monthChange (%)"] = df_codeName["1monthChange (%)"][i]
    fund_dict[dict_key]["3monthChange (%)"] = df_codeName["3monthChange (%)"][i]
    fund_dict[dict_key]["6monthChange (%)"] = df_codeName["6monthChange (%)"][i]
    fund_dict[dict_key]["1yearChange (%)"] = df_codeName["1yearChange (%)"][i]

    
#%% write in Json
with open('./data/funds_dictionary.json', 'w') as f:
    json.dump(fund_dict, f, sort_keys=True, indent=4)

#%% rewrite the txt list
ETF_codes = ["A{}".format(i) if i > 9 else "A0{}".format(i) for i in np.arange(1,15)]
ETFFundList = []
for code in ETF_codes:
    ETFFundList.append(code + ". "+ fund_dict[code]["moneydjname"])
    
Tech_codes = ["B{}".format(i) if i > 9 else "B0{}".format(i) for i in np.arange(1,26)]
TechFundList = []
for code in Tech_codes:
    TechFundList.append(code + ". "+ fund_dict[code]["moneydjname"])
    
China_codes = ["D{}".format(i) if i > 9 else "D0{}".format(i) for i in np.arange(1,7)]
ChinaFundList = []
for code in China_codes:
    ChinaFundList.append(code + ". "+ fund_dict[code]["moneydjname"])

Value_codes = ["E{}".format(i) if i > 9 else "E0{}".format(i) for i in np.arange(1,6)]
ValueFundList = []
for code in Value_codes:
    ValueFundList.append(code + ". "+ fund_dict[code]["moneydjname"])
    
OTC_codes = ["F{}".format(i) if i > 9 else "F0{}".format(i) for i in np.arange(1,6)]
OTCFundList = []
for code in OTC_codes:
    OTCFundList.append(code + ". "+ fund_dict[code]["moneydjname"])
    
Common_codes = ["C{}".format(i) if i > 9 else "C0{}".format(i) for i in np.arange(1,74)]
CommonFundList = []
for code in Common_codes:
    CommonFundList.append(code + ". "+ fund_dict[code]["moneydjname"])
    
#%% write in new List
with open('./data/Fund_info/ETFFundList.txt', 'w') as f:
    for item in ETFFundList:
        f.write("%s\n" % item)
        
with open('./data/Fund_info/TechFundList.txt', 'w') as f:
    for item in TechFundList:
        f.write("%s\n" % item)
        
with open('./data/Fund_info/ChinaFundList.txt', 'w') as f:
    for item in ChinaFundList:
        f.write("%s\n" % item)
        
with open('./data/Fund_info/CommonFundList.txt', 'w') as f:
    for item in CommonFundList:
        f.write("%s\n" % item)
        
with open('./data/Fund_info/ValueFundList.txt', 'w') as f:
    for item in ValueFundList:
        f.write("%s\n" % item)
        
with open('./data/Fund_info/OTCFundList.txt', 'w') as f:
    for item in OTCFundList:
        f.write("%s\n" % item)

#%%



        