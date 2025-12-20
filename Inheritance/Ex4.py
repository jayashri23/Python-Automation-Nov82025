""""#4.Multilevel Inheritance

accessing properties of superclass1 and super class 2 in 1 subclass
-if same method classing in super class then 1 class method will call.
what is inheritance
single level
multi level
single level inheritance where used in framework.

"""

class Bedroom1:
    def b1(self):
        print("I am bedroom1 from Super class1")
    def b(self):
        print("I am bedroom1 from Super class1 from b method")


class Bedroom2:
    def b2(self):
        print("I am bedroom2 from Super class2")
    def b(self):
        print("I am bedroom2 from Super class2 from b method")

class Bedroom3:
    def b3(self):
        print("I am bedroom3 from Super class3")

class Home(Bedroom1,Bedroom2,Bedroom3):
    def h(self):
        print("I am kitchen from subclass")

h1= Home()
h1.b1()
h1.b2()
h1.h()
h1.b3()
h1.b()