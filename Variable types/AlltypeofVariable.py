#All type of variables with same name


a,b=4,5

class Add:

    a,b=6,7
    def addition(self):
        a,b=8,9
        print("Local Variable called")
        print(a+b)    #addtion of local variable
        print("Class variable called")
        print(self.a+self.b)    #addition of class variable
        print("Globle variable called")
        print(globals()['a']+globals()['b'])  #addition of globel variable use globle world if local class and globle varible name same


s=Add()
s.addition()