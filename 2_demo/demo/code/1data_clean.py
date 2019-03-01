#-*- coding: utf-8 -*-
#数据清洗，过滤掉不符合规则的数据
      
import pandas as pd
import types
import string


datafile= '../data/data.xls' #航空原始数据,第一行为属性标签
cleanedfile = '../tmp/data_cleaned.xls' #数据清洗后保存的文件
data = pd.read_excel(datafile,header=None)

for i in data.columns:
    for j in range(len(data)):
        if i%2!=0:
           # if (type(data[i][j]) != type(1)):
            if(type(data[i][j])!=type(1) or int(data[i][j]) >= 100000):
                data[i][j]=None;
data.to_excel(cleanedfile, header=None)
