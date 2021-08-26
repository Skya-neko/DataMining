# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:51:36 2021

@author: Vivian
"""
book = ['人生人生','黑夜問白天','看見未來','衛星的秘密','白夜']
author = [['AA','CC'],['EE','FF'],['GG'],['AA','DD'],['EE','DD']]
city = ['微風市','微風市','晴天市','青草市','青草市']
year = [2013, 2020, 2018, 2020, 2014]


# 第一題
for i in range(len(author)):
    for j in range(len(author[i])):
        if author[i][j] == 'AA':
            print(book[i])


# 第二題
min_val = min(year)
min_ind = year.index(min_val)
print(book[min_ind])


# 第三題
book.append('天竺鼠鼠')
author.append(['Gary'])
city.append('微風市')
year.append('2019')
print(book)
print(author)
print(city)
print(year)

#第四題
city_check = []
city_count = []
for i in range(len(city)): #確認城市種類
    if city[i] not in city_check:
        city_check.append(city[i])
        
city_count = [ 0 for i in range(len(city_check)) ] #建立跟城市數量相等的計數list
print('city_count',city_count)
for i in range(len(city)):  
    for j in range(len(city_count)):
        if city[i] == city_check[j]:
            city_count[j] += 1   #如果現在看到的城市跟city_check裡面的城市相等，則計數1
            
print(city_check)
print(city_count)
print(city_check[city_count.index(max(city_count))])

        
