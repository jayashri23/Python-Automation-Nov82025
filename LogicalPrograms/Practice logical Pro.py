#print even number 1 to 100
num=100
print("Even Numbers from 1 to 10----")
for i in range(1,111):
    if i%2==0:
        print(i)


#Print Factorial of number
fact=1
n=int(input("Enter number for factorial:"))
for i in range (1,n+1):
    fact=fact*i
print(fact)



#Print number Odd
print("Odd Number from 1 to 30----")
n1=30
for i in range(1,n1+1):
    if i%2 !=0:
        print(i)


#Print Prime Number or not
num=67

if num%2==0:
      print("Given number" ,num ,"is not Prime")
else:
      print("Given number" ,num ,"is  Prime")

#Count string  char
str="vishal"
count=0
for i in range (1,len(str)+1):
          count=count+1
print("Count of  string:" ,count)
