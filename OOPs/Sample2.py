#Static method
from stringprep import map_table_b3


class Demo2:

    @staticmethod            #static method
    def m3():
        print("Print static method m3")

    @staticmethod
    def m4():
        print("Print static method m4")

    #Nonstatic method
    def m5(self):
        print("Print Non static method m5")

    #static method call
Demo2().m3()
Demo2().m4()

    #Nonstatic method call
d=Demo2()
d.m5()


