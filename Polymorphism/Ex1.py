"""One object multiple form called Polymorphism.
-one method multiple behaviour
1.Method Over ridding---
Sub derived  class provide a specific implementation of method that is already defined in parent class is called over ridding.
method name and parameter should be same then only over ridding happens

"""
class Father:

    def car(self):
        print("Car :Tata")
    def house(self):
     print("House :1bkh")

class Son(Father):

      def mobile(self):
           print("Mobile method called")
      def house(self):            #house method override in son class
          print("House:2bhk")

      def car(self):            #car method override in son class
       print("Car:Kia")


f=Father()
f.car()
f.house()
print("---------------------------")

s= Son()
s.mobile()
print("--------------Method Overridden-------------")
s.car()
s.house()




#2.Method Over Loading

