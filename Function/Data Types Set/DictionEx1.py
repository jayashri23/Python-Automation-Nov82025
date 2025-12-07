'''Dictionary---store key value
-we can store key unique
-values should be duplicate.
declaration:
dict={key:value ,key:value}
-to get specific key value use get method
dic.get(key) and dictionary.item()
-Add key value after dictionary create

Delete/Remove  ----
 #pop (key )delete passed key value
#popitem delete last item of dictionaries
        '''

dict={"jaya":22,"sarika":10,"vish":30}
print(dict)
print("Length of dictionary:",len(dict))
print("Specific Key value:",dict.get("jaya"))

dict.items()
print("Specific Key value:",dict.get("sarika"))

dict2={"abc":100,"cba":100,"def":300}    #store duplicate value does not store
print(dict2)


dict2.pop("abc")                        #pop (key )delete passed key value
print(dict2)
dict2.popitem()                        #popitem delete last item of dictionaries
print(dict2)