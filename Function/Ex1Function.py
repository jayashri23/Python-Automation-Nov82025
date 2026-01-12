# Function---function is block of code --one time writen code we can reuse(NO need to rewrite same code again and again)
#def FunctionName():  //user define (any name)
  #  Function body

def f():            #function declaration
    print("hello world") #function body
    print("Jayashri ")
    print("Python Automation Testing")
    print("-----------------------------")
f()

def add():
    a=10
    b=20
    c=a+b
    print(c)



def f():
    print("hello ")  # function body
    print("Jayashri ")
    print("Python Automation Testing")
    print("---Function with out Parameter-")
f()
add()

#function with different types:
#1.Without Parameter
#2.With Parameter
#3.With return

def sub():            #Function Without Parameter
    a=20
    b=30
    print("Substraction:",a-b)
sub()
print("____Function with Parameter----------")
def mul(x,y):    #Function with  Parameter
    print("Multiplication:",x*y)
mul(2,3)
mul(30,2)
mul(0,9)

print("____Function without Parameter String----------")
def name():
    print("Jayashri ")
name()
print("____Function with Parameter String----------")

def kids(c):
    print("Kids Name: ",c)
kids("Vedika")

def studentName(a,b):
    print("Student Name: ",a,b)
studentName("Vishal","Vadde")
studentName("Vadde","Hiiii")
print("____Function without Parameter float----------")
def float():
    f=2.3
    print("Float Number: ",f)
float()


print("____Function with Parameter float----------")
def floatParameter(f1,f2):
   print("Float Number: ",f1+f2)
   print("Float Number: ",f1-f2)
floatParameter(2.3,4.5)
floatParameter(11.3,443)


###############Function with Return type#################

#1.Function with single return type
#2.Function with Multiple return type

print("____Function with single return type----------")

def getStudentName():
    name="Vishal"
    return name   # or print("Student Name: ",name)
s1=getStudentName()   #store return in variable
print(s1)               #print that variable


def divi():
    s=13
    a=33
    return a/s
d=divi()
print("Division:",d)

print(divi())   #or directly print function


def sum(a,v):    #finction with Parameters and Return type
    return a + v
def sub(s1,s2):
   return s1-s2

print("Sum:",sum(2,3))
print("Sum:",sum(33,30))
print("Sum:",sum(30,30))
print("Sub:",sub(400,120))

S3=sub(20,30)  #or
print("Sub:",S3)



