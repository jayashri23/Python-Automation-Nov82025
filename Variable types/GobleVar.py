#Globle variable-the variable defined in outside function and class
#scope throughout the class ,method and function


num=3
def   add():
    print(num+num)

print("----Accessing global variable in method or function ------")
add()


class A:
    def sub(self):
        print(num-1)


print("----Accessing global variable in  class ------")
a=A()
a.sub()




