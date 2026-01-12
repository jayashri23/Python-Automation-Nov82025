class Person:

    # User defined without parameterized constructor

    #initialize object
    def __init__(self):   #constructor declaration(user defined)
        print("--------constructor running----------")

    def m1(self):
        print("--------m1 called------------------")

d1=Person()     #constructor called-->initialize object
d1.m1()         #method called



