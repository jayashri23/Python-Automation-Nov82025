#-------String-----------
#string is data type and inbuilt class

s1="Jayashri"
print(len(s1))
print(s1.upper())
print(s1)
s1=s1.upper()     #permenant changed into upper case called initialization
print(s1)

s2="VISHAL"
print(len(s2))
print(s2.lower())
print(s2)

s2=s2.lower()    #permenant changed into lowe case
print(s2)

s3="Sarika"
print(s3.endswith("s"))   #if string end with given then true or false output comes

print(s3.startswith("S"))

#compare string
st1="JAYASHRI"
st2="Jayashri"
st3="My name is Vedika"
#1 approach
print("Comparing Approach 1:",st1==st2)

#2 approach
print("Comparing Approach 2:",st1.__eq__(st2))

#3 approach compare only data
print("Comparing Approach 3:",st1.lower()==st2.lower())

#4 approach check specific character

print("Checking specific Characters:",st1.__contains__("S"))
print("Checking specific Characters:",st2.__contains__("JAYA"))
print(st3.__contains__("My name IS"))

print("Comparing 2 string:",st1.__contains__(st2))

#check string start with  and end with--
print("String start with:",st3.startswith('My name'))
print("String end with:",st3.endswith('Vedik'))

#single char print
print("Specific characters print:",st2[2])
st4="Jeevika vadde"

#Print multiple char
print("Print multiple char:",st4[2:6])    #start index:end index+1

#Index of specific char
print("Index of specific char:",st4.index("v"))
print("Index of specific char:",st4.index("e"))  #from left side check and then giving index no.
print("Index of specific char:",st4.find("d"))
print("Index of specific char:",st4.rfind("v"))   #count index from right side
print(st1+st2+st3+st4)
s=st1+st2+st3+st4
print(s)