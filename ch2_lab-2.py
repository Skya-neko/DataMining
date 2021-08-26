# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:27:29 2021

@author: Vivian
"""
def pyramid(i):
    if i < 10:
        print(i*' '+'*'*(9-i),(9-i),'*'*(9-i))
        i += 1
        pyramid(i)
        
q = 0
pyramid(q)
