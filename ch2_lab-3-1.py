# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:45:09 2021

@author: Vivian
"""

import pandas as pd
import numpy as np

#從檔案中讀取資料
path = r'C:\Users\Vivian\Desktop\資訊碩士\資訊碩二上\暑期資料科學\Python 資料探勘\\'
dataFrame = pd.read_csv(path + '2330_(2020-01-01~2020-12-31)forExercise.csv', encoding='gbk') #encoding = 處理檔案的編碼
print(dataFrame)

openn = np.array(dataFrame['open'])
close = np.array(dataFrame['close'])

price = np.array([openn, close])

print(price)
price = np.append(price,[[544],[533]],axis = 1)