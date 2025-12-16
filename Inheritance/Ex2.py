#2.Multilevel Inheritance
#need minimum 3 class for multi level inheritance

#Example of multi level inheritance

class Grandfather:

    def age(self):
        print("I am Granfather")

    def grandfatherName(self):
        print("Grandfather name is Namdev")

class PaPa(Grandfather):

    def name(self):
        print("PaPas name  is Shankar")

    def paAge(self):
        print("PaPa age is 56")
class Daughter(PaPa):

    def bloodgr(self):
        print("Bloodgr of daughter is AB+")


d=Daughter()
d.age()
d.grandfatherName()
d.paAge()
d.name()
d.bloodgr()
