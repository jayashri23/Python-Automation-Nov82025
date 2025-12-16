"""Inheritance -use to reuse code
#if same method need in subclass then use inheritance
#types of inheritance-
1.single level
2.multi level
3.Hierarchical
#this is single level inheritance-2 class only involve    """

class Father:

    def car(self):
        print("I am Car")

    def home(self):
        print("I am Home")

    def money(self):
        print("I am Money")

class Child(Father):

    def mobile(self):
        print("I am Mobile")

c=Child()
c.car()
c.home()
c.money()
c.mobile()