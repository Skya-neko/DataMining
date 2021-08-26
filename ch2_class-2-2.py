# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:16:38 2021

@author: Vivian
"""

'''遞迴
    以下三種不同程式碼，請想一下輸出結果，再自行打在IDE上檢視輸出結果與自己的想法是否一樣：'''
#第一種
i = 0
while True:
    print(i)
    i+=1
    if i == 11:
        break
print('stop loopp')


#第二種
q = 0
while q <= 10:
    print(q)
    q += 1
print('stop loop')
    
#第三種

def test(j):
    if j <= 10:
        print(j)
        j += 1
        test(j)
        
j = 0
test(0)
print('stop loop')










'''遞迴與迴圈的差異'''
#原本的程式碼
def test(j):
    if j <= 10:
        print(j)
        j += 1
        test(j)
        
j = 0
test(0)
print('stop loop')

#將print換行的程式碼
def test(j):
    if j <= 10:
        j += 1
        test(j)
        print(j)
        
j = 0
test(0)
print('stop loop')









'''以倒數4的程式碼為例'''
def test(j):
    if j <= 2:
        j += 1
        test(j)
        print(j)
        
j = 0
test(0)
print('stop loop')



