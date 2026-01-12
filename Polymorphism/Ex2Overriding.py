#if you want to print super class method body and new body then use super word

class Add:

    def add(self):
        print("Method From super class Add")


class Sub(Add):

    def add(self):
        print("-------Existing body-------")
        super().add()     #super world dot method name of super class write body of super class of same method
        print("-----New body--------------")
        print("Method from Sub class Sub")


s=Sub()
s.add()
