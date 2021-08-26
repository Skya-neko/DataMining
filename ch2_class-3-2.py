# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:28:25 2021

@author: Vivian
"""

import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)

#陣列的axis(維)的數量。在Python中，維的數量被稱作rank。
print('陣列的axis(維)的數量')
print(a.ndim)

# 顯示陣列各維度中所含之元素數量
print('顯示陣列各維度中所含之元素數量')
print(a.shape)

#陣列所有元素總數量。
print('陣列所有元素總數量。')
print(a.size)

#陣列的資料型別
print('陣列的資料型別')
print(type(a))

#陣列中元素的資料型別
print('陣列中元素的資料型別')
print(a.dtype.name)


#陣列各元素的佔多少位元組(bytes)。
print('陣列各元素的佔多少位元組(bytes)')
print(a.itemsize)

#此陣列佔記憶體的空間有多少位元組(bytes)
print('此陣列佔記憶體的空間有多少位元組(bytes)')
print(a.size*a.itemsize)




