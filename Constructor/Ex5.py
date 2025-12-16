class Arithmaticoperations:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("Addition:",self.num1+self.num2)
    def sub(self):
        print("Subtraction:",self.num1-self.num2)
    def mul(self):
        print("Multiplication:",self.num1*self.num2)
    def div(self):
        print("Division:",self.num1/self.num2)

a=Arithmaticoperations(1,2)
a2=Arithmaticoperations(5,4)
a3=Arithmaticoperations(5,6)
a4=Arithmaticoperations(16,8)

a.add()
a2.sub()
a3.mul()
a4.div()