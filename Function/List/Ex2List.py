#
ls=[23,44,11,40,10,3]
print(ls)
ls.sort()
print("------After sort-----------")
print(ls)
ls.reverse()
print("------After reverse-----------")
print(ls)
print("-----list using for loop----------")
for num in ls:
    print(num)
print("-----Access specific element in list----------")
print(ls[2])

print("------list using for loop range-----------")
print("Original list:",ls)
#for i in range(ls[0,5]):
 #   print(i)
l2=["abc",10,"efg",90,20,40,33,"xyz"]
print(l2)
l2.insert(2,"jaya")    #insert in any index insert(index,value)
print(l2)
l2.append("LMN")     #append add values at last append(value)
print(l2)
l2.extend("aa")
print(l2)
l2.remove(90)
print(l2)
l2.pop()
print(l2)
l2.pop(2)
print(l2)
print("Count:",l2.count(33))
quit(l2)


l2.clear()    #clear is  to remove all elements from list
print(l2)
