# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:29:29 2021

@author: Vivian
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,50)                                     #宣告一個一維陣列，其元素的值在-3到3之間共有50個點
y1 = 2*x+1
y2 = x**2

#畫出y1的圖
plt.figure()                                                 #figure~下一個figure前 的設定  都是屬於一個figure的
plt.plot(x,y1)

#畫出有y1、y2的圖
plt.figure(figsize=(8,5))                                    #準備好畫布，設定寬和高，單位為英吋
plt.plot(x,y2)                                               #畫y1的線
plt.plot(x,y1,color='red',linewidth=10.0,linestyle='--')     #畫y2的線
plt.title('我是圖表標題')                                     #設定圖表標題


plt.show()                                                   #將2張圖產生出來

