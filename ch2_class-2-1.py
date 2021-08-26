# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:47:52 2021

@author: Vivian
"""



'''使用函式前'''
dog1 = '小白'
dog1Point = 0
dog1StepSize = 1

print(dog1,'從位置',dog1Point)
dog1Point += dog1StepSize
print('跑到位置',dog1Point,'了!')

print(dog1,'從位置',dog1Point)
dog1Point += dog1StepSize
print('跑到位置',dog1Point
      ,'了!')

print(dog1,'從位置',dog1Point)
dog1Point += dog1StepSize
print('跑到位置',dog1Point,'了!')










'''使用函式後'''
dog1 = '小白'
dog1Point = 0
dog1StepSize = 1
def dogRun(dogName,currentPoint,stepSize):
    print(dogName,'從位置',currentPoint)
    currentPoint += stepSize
    print('跑到位置',currentPoint,'了!')

dogRun(dog1, dog1Point, dog1StepSize)













'''我們希望狗狗走到位置3，所以我們呼叫函式3次，這樣是對的嗎？'''
dog1 = '小白'
dog1Point = 0
dog1StepSize = 1
def dogRun(dogName,currentPoint,stepSize):
    print(dogName,'從位置',currentPoint)
    currentPoint += stepSize
    print('跑到位置',currentPoint,'了!')

dogRun(dog1, dog1Point, dog1StepSize)
dogRun(dog1, dog1Point, dog1StepSize)
dogRun(dog1, dog1Point, dog1StepSize)











'''使函式return值'''
dog1 = '小白'
dog1Point = 0
dog1StepSize = 1
def dogRun(dogName,currentPoint,stepSize):
    print(dogName,'從位置',currentPoint)
    currentPoint += stepSize
    print('跑到位置',currentPoint,'了!')
    return currentPoint

dog1Point = dogRun(dog1, dog1Point, dog1StepSize)
dog1Point = dogRun(dog1, dog1Point, dog1StepSize)
dog1Point = dogRun(dog1, dog1Point, dog1StepSize)










'''搭配迴圈使用
    讓程式碼更簡潔'''

dog1 = '小白'
dog1Point = 0
dog1StepSize = 1
def dogRun(dogName,currentPoint,stepSize):
    print(dogName,'從位置',currentPoint)
    currentPoint += stepSize
    print('跑到位置',currentPoint,'了!')
    return currentPoint

for i in range(0,3):
    dog1Point = dogRun(dog1, dog1Point, dog1StepSize)






