# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:33:53 2022

@author: PRAYUKTI
"""

class student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.marks = []
        student.count = student.count+1
    
    def stdMarks(self):
        for i in range(3):
            n = int(input("Enter the Marks of %s in %d subject: "%(self.name,i+1)))
            self.marks.append(n)
            
    def display(self):
        print(self.name,"of age",self.age,"got",self.marks)
        
name = input("Enter the student name: ")
s1=student(name=name,age=0)
age = input("Enter the student age: ")
s1=student(name=name,age=age)
s1.stdMarks()
s1.display()
print("")

name = input("Enter the student name: ")
s2=student(name=name,age=0)
age = input("Enter the student age: ")
s2=student(name=name,age=age)
s2.stdMarks()
s2.display()