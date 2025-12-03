#################PYTHON######################################
#Python program run through 4 different ways
#1.cmd promt
#2.python idel
#3.notpad
#4.Pycharm

#**************************************************


#data types in Python Int,float,string,boolean
#int -stores only integer value
#String-stores word or sentence.
#float -store digit values
#boolean- gives out put with true or false value



a="Jayashri"
b=23
c=5.3
print("My name is: " ,a ,"Age is :",b, "height is:", c,)
print(type(a))
print(type(b))
print(type(c))
#converter

q=23
r=1.9
t=float("2.44")
e=q+r
x=int(2.6)
y=str("20")
print(type(x))
print(type(e), e)
print(q+t)

#Python Input from keyboard from user
print (input("My name is : "))
print (input("My age is:" ))
print(input("Address: "))

# input 2 numbers and print output

first =int(input("enter first number:"))
second=int (input("enter second number:"))
sum=first+second;
print(sum)

#2.wap to input side and print square area

side=float(input("enter square side:"))
area=side **2
print("Area of square is :" ,area)

#WAP take  input and print average

l=2
m=4
n=(l+m)/2
print("Average:" ,n)


#Take input a and b print output if a is grater than or equal else false

k=input("k:")
h=input("h:")
if k>=h :
    print("True")
else:
    print("False")
# another simple ans of above question

print(k>=h)

