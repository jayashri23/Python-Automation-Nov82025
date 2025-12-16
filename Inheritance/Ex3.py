"""3.HierarchicalInheritance
Accessing data of class1 into class 2 and class 3

      class1
      /  \
class2   class3
 """

class Mother:

    def m1(self):
        print("I am a mother")

    def m1(self):
        print("I am a mother")


class Son1(Mother):

    def s1(self):
        print("I am a son1")

class Son2(Mother):

    def s2(self):
        print("I am a son2")

s1= Son1()   #son1 accessing data of mother
s1.m1()
s1.s1()

s2= Son2()    #son2 accessing data of mother class
s2.m1()
s2.s2()


