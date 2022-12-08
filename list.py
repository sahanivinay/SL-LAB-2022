# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:52:45 2022

@author: PRAYUKTI
"""

from functools import reduce

list = [2,4,6,8,10,12]
newList = []
for x in list:
    a = x*3
    newList.append(a)

print("List before comprehension",list)
print("List after comprehension",newList)
oldListSum = reduce(lambda a,b :a+b,list)
print("The sum of old list is: ",oldListSum)
newListSum = reduce(lambda a,b :a+b,newList)
print("The sum of old list is: ",newListSum)