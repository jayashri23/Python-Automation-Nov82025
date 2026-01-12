#User Defined with Parameterized constructor
#use1-initialize object
#use2=initialize class variable
#global variable -inside class
#Local variable-inside method
#declaried inside method /constructor
# scope remains within method /constructor
#Class variable access throughout the class means inside every method inside of variable.


class   Demo1:

    #user defined parametrised constructor
    def __init__(self,num):     #local variable
        self.num1=num          #classvariable=local variable     self=current class object

    def squareOfNumber(self):          #local parameter
         print("Square of Number:",self.num1 * self.num1)

    def multiply(self,num2):
        print("Multiplication:",self.num1 * num2)

    def divide(self,num3):
       # print("Division:",num2/ num3)  #for this will get error bcz nu2 is not class variable.
        print("Division:",self.num1 / num3)

d=Demo1(9)  #calling constructor
d.squareOfNumber()
d.multiply(2)
d.divide(3)
