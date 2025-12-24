#to call specific class or specific function in other class
#moduleName:   ArithmeticOperation2

#Approach2:
#from moduleName import variable, Function,classes
#from moduleName import *

#print(variableName)       -->calling variable from other class
#fn()   -->function call from other class
#objectName=className()             -->Object creation

#import  Calculator * #import all data from calculator module

print("---2.1 import specific data from calculator module---")
from Calculator import num ,addition,Demo1
addition(3,6)
d=Demo1()    #function call by creating object
d.m1()    #class method
print(num)    #variable call



