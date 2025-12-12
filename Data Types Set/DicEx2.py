#Dictionary

d={"abhi":1,"nilesh":2}
print(type(d))
print("Dictionary:",d)
print(d["abhi"])
print(d.items())
print(d.keys())
print(d.values())
print(d.get("abhi"))
d.update({"23":"vish"})
print(d)
d.pop("abhi")
print(d)
print(d.__contains__("abhi"))
d.update({"100":"abc"})
print(d)
d2={"1":"a","2":"b","3":"c"}
print("All Keys form d2:")
for i in d2:
    print(i)   #get all keys
print("All Values form d2:")
for i in d2:
    print(i)
for i in d2.values():
    print(i)     #get all values
    #to get all key values
print("All Key values form d2:")
for Key ,Value in d.items():
    print(Key,Value)