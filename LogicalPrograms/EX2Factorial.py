num=int(input("Enter a number:"))
#num=4
fact = 1      #1  update =2  update fact =6 update fact =25

for i in range(1,num+1):   #1,2,3,4      5<5 false
    fact=fact*i        #1=1*1     2=2*1     6=3*2   24=4*6
print("Factorial of ",num ,"is ::",fact)
 #4*3*2*1