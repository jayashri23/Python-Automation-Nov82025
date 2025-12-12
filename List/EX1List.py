#list data type
#list declaration --->variable name=[ value ,value2,value 4]
#list store dublicate values
#
name=["jayashri","vishal","vedika","jeevika"]
S=name.index("vedika")
print(S)
print(name)
s2=name.index("jayashri")
print(s2)
s3=name.insert(2,"sarika")
print(name)
name.remove("jayashri")
print(name)
print(type(name))
s5=name.reverse()
print(name)
name.count("jayashri")
print("Count:",name.count("jayashri"))
print("Length:",len(name))

Studentdetail=["vishal","marathi",88,43,88,"vishal"]
print(Studentdetail)
print(len(Studentdetail))
print(Studentdetail[0])
print(Studentdetail.index(88))
Studentdetail.insert(3,"marathi")
print(Studentdetail)
#if need to add multiple add then use extend and add in last
Studentdetail.remove(43)
print(Studentdetail)
print("43 removed:",Studentdetail)
print(Studentdetail.extend([12,"abc",9]))
print("Extend function used to extend:",Studentdetail)

#get specific data
print(Studentdetail[2])


