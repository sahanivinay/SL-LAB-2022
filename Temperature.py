# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:38:53 2022

@author: PRAYUKTI
"""
#Fahrenheit function
def fah():
    F = int(input("Enter Fahrenheit value: "))
    C = (F-32)/1.80
    K = (F-32)/(5/9)+273.15
    
    print("Celsius value: ",round(C,2))
    print("Kelvin value: ",round(K,2))
    
def kel():
    K =int(input("Enter Kelvin value: "))
    C = K-273.15
    F = (K-273)*1.8 + 32
    
    print("Celsius value: ",round(C,2))
    print("Fahrenheit value: ",round(F,2))

def cel():
    C = int(input("Enter Celsius value: "))
    F = C * 1.80 + 32
    K = C + 273
    
    print("Fahrenheit value: ",round(F,2))
    print("Kelvin value: ",round(K,2))
    
    
while(1):
    print("---------------Temperature Menu-----------------")
    print("[1]Fahrenheit to Celsius and Kelvin")
    print("[2]Kelvin to Celsius and Fahrenheit")
    print("[3]Celsius to Fahrenheit and Kelvin")
    print("[4]Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        fah()
    elif choice == 2:
        kel()
    elif choice == 3:
        cel()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
        