# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:09:17 2022

@author: PRAYUKTI
"""

list = []
n = int(input("Enter the No of Elements: "))
for i in range(0,n):
    element = int(input("Enter Elements: \n"))
    list.append(element)
print(list)
print("The minimum value among the list: ",min(list))
print("The maximum value among the list: ",max(list))
print("*****************Add new element to list******************")
newElement = int(input("Enter new elements\n"))
list.append(newElement)
print("Element after adding new elements: ",list)
delete = int(input("Enter the element to delete: "))
list.remove(delete)
print("Elements after deleting: ",list)
search = int(input("Enter element to search:"))
if search in list:
    print("Element found")
else:
    print("Not found")