#Nonstatic / Instance method
#for this need to create object name and call method using object name.method name

class Demo1:
    def m1(self):
        print("Print method m1")

    def m2(self):
        print("Print method m2")

    def add(self,num1,num2):
        print(" method add:",num1+num2)

    def square(self,n):                     #self by default rahega
        print(" method square:",n*n)


s1=Demo1()    #created object of class objectName=class name()
s1.m1()       #calling method objectName.methodName
s1.m2()
s1.square(2)
s2=Demo1()
s2.add(2,4)  #second object of class created
