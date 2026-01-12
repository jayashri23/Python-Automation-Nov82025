# Local Variable -Defined inside in method ,function and constructor
#  scope only inside method

def name():
    print("Local variable")
    n="Jayashri"
    print(n)    #only access in method

name()


class home():
    def h1(self):
            print("trying to accessing local variable in class failed")
    # print(n)      #if call this variable will get error

h=home()
h.h1()

