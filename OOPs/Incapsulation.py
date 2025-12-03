#OOPs in Python-
#1.Incapuslation---binding data + method
#Protect data
#_init_ ->Constructor to initialize object

#2.Abstract --abstract class contains methods of abstract only
#abstract method does not contain body

#3.Inheritance---Purpose is reuse data
#Access Parent class methods in children class child(parent):
#variable =child
#variable.parent class methods

#4.Polymorphism--same function name but different function in different classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
c=Car()
c.start()

#example of polymorphism
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

# Polymorphism
print("Sound method called from Cat class:",Cat().sound())
print("Sound method called from Dog class:",Dog().sound())


class family():
    def member(self):
        print("Family members are 4 ")

class jointfamily():
    def member(self):
        print("My Family is my world")
f=family()
f1=jointfamily()
f.member()
f1.member()
