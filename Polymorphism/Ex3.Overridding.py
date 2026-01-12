#Variable overriding or variable reinitialization with super kay word


class D:

    def name(self):
        n="jaya"
        print(n)

    def age(self):
        a=5
        print(a)

class E(D):

    def name(self):
        print("Original")
        super().name()
        h="JAYA"
        print("Overridden method")
        print(h)

    def age(self):
        print("calling super class method using super key word")
        super().age()
        a=33

        print("Overridden method")
        print(a)
d=E()
d.name()
d.age()
