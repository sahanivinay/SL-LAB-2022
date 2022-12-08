# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:26:40 2022

@author: PRAYUKTI
"""

class rectangle():
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
        
    def area(self):
        print("The area of rectangle is: ",(self.breadth*self.length))
        
length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))

obj = rectangle(breadth, length)
obj.area()