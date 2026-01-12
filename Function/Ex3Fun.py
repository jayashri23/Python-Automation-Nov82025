#Function with Return type

def swami():
    print("-----------------Swami Smarth-------------")

swami()
swami()

def BaluMama(n1,n2):
    print("---------BaluMama______",n1,n2)
BaluMama("Chang Bhala","Chang bhala")
BaluMama("Admapur","Admapur")


def Akkalkoth():
    name="Swami Smarth"
    return name
Akkalkoth()
#---------Multiple return type----------------
def withReturn():
    NameOFStudent="Jayashri"
    markes=40
    height=5.2

    print("Markes:",markes)
    print("Height:",height)
    print("NameOFStudent:",NameOFStudent)
    return markes,height,NameOFStudent
withReturn()


#store return variable value with variable
def Bhaji():
    veg="Onion"
    veg2="Tomato"
    return veg,veg2

v1,v2=Bhaji()
print("Vegetable:",v1)
print("Vegetable2:",v2)

#function with multi return 
def AddandMulti(a,b):
    add=a+b
    multi=a*b
    return add,multi
a,m=AddandMulti(1,2)
print("Add:",a)
print("Multi:",m)

