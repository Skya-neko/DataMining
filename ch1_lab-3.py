# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:01:50 2021

@author: Vivian
"""




#練習一
for i in range(1,10):
    for j in range(1,10):
        print(i,'*',j,'=',i*j)


#練習二：隔行列印，寫法一
for i in range(0,11):
    print(str(i)*(i%2==0))
    
#練習二：隔行列印，寫法二
for i in range(0,11,2):
    print(i)
    print()
    
#練習二：隔行列印，寫法三
for i in range(0,11):
    if i%2 == 0:
        print(i)
        print()

#練習三
for i in range(0,10):
    print('*'*i)

#練習四

    
#練習四
#先觀察這兩行
for i in range(0,10):
    print('*'*i,i,'*'*i)
    
#再寫出答案
for i in range(0,10):
    print((9-i)*' '+'*'*i,i,'*'*i)












