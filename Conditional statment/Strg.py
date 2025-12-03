#concatenation --means str1 + str 2 =str3
from operator import index

str1="jaya"
str2="shri"
fullstring=str1+str2;
#print(str1+str2)
#Len ----used for access length of string

#index---used for access specific char rang
print(len(str1+str2),fullstring)
print("length of str1 :",len(str1))
name="Poo ja"
print(name[3])
print(len(name) ,index(4),name)
surname="Vadde"
print(surname[1:4])
print(surname[:3])
print(surname[:])


