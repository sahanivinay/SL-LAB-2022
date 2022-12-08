# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:00:41 2022

@author: PRAYUKTI
"""

Element = {'Hydrogen':'H','Helium':'He'}
print("Elements in Dictionary",Element)
newElement = {}

def AtomicDict():
    while(1):
        print("Enter  1 to insert element or 0 to Stop? ")
        number = int(input())
        if( number == 0):
                break
        else:
                name = input("Enter Atomic Element Name: ")
                symbol = input("Enter Atomic Element Symbol: ")
                newElement[name] = symbol
                Element.update(newElement)
                print(Element)
       
    print("Number of element",len(Element))
    search = str(input("Enter the element to search: "))
    flag = 0
    for i in Element:
            if(Element[i].lower()==search.lower()):
                print("Search Found")
                print({i,Element[i]})
                flag = 1;
                break
            
    if flag != 1:
        print("Not Found")
            
AtomicDict()