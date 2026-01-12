class A:

    @staticmethod
    def f():
        print("Static Method CLASS  a Inheritance")


class B(A):
    @staticmethod
    def g():
        print("Static Method cLASS b Inheritance")


#static method classing without object creating 
B.g()
B.f()


