from Inheritance.Ex1 import Father


class Son(Father):

    def family(self):
        print("Family")
    def bag(self):
        print("Bag")

s=Son()
s.car()
s.home()
s.money()