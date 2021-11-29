# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:59:22 2021

@author: tchon
"""

def main():
    num = input("Enter a number: ")
    while type(num) != int:
        try:
            num = int(num)
            divisibleby11(num)
        except ValueError:
            print("Error: That's not an integer!")
            num = input("Enter a number: ")

def divisibleby11(num):
    sum=0
    numStr = str(num)
    if numStr[0] == '-':
        numStr = numStr.replace('-','')
        
    for digitplace in range(len(numStr)):
        if (digitplace % 2) == 0:
            sum += int(numStr[digitplace])
        else:
            sum = sum - int(numStr[digitplace])
    
    if sum % 11 == 0:
        print("This is divisible by 11")
    else:
        print("This is not divisible by 11")

main()