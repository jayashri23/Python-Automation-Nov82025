#Inheritance means reuse code
#access data from Parent class
from symtable import Class

class Animal:
    def dog(self):
        print("I am dog.")
class Dog(Animal):
    def bark(self):
        print("I am bark.")

class Cat(Dog):
    def sound(self):
        print("I am cat.")
a=Cat()
a.dog()
a.bark()
a.sound()


