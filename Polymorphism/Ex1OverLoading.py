"""#Overloading-
-declaring Same method  name with different parameter /argument/input to perform different task


"""
class Add:

    def add(self,a=0,b=0,c=0,d=0,e=0,f=0):
        print(a+b+c+d+e+f)


class CustomerIfo:

    def serviceCustomer(self,name="sarika",customerId=1223,mobile=64748468):
        print("Name:",name,"Customer ID:",customerId,"mobile:",mobile)


a=Add()
a.add()    #without parameter
a.add(2,4)    #2 parameter
a.add(1,2,3) #3 parameter
a.add(1,2,3,4,5,5)
print("---------------------------------------------")
customer = CustomerIfo()
customer.serviceCustomer()   #default value taking
customer.serviceCustomer("jaya",2324,4767587)    #parameter value passed