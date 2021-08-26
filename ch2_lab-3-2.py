# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:48:00 2021

@author: Vivian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 從檔案中獲取資料
path = r'C:\Users\Vivian\Desktop\資訊碩士\資訊碩二上\畢業論文研究\workspace\to csv\\'

dataFrame = pd.read_csv(path+'2330_(2020-01-01~2020-12-31)forExercise.csv',encoding='gbk') #encoding = 處理檔案的編碼 
print(dataFrame)

openn = np.array(dataFrame['open'])
close = np.array(dataFrame['close'])

price = np.array([openn, close])
x_ticks = np.arange(0,245)
print(price)
print(price.max())

plt.figure(num=3,figsize=(8,5))
plt.plot(x_ticks,price[1])

plt.show()