"""   Set ---used to store more than 1 values
for 1 value use variable
from operator import index

set declare by {}
set does not store duplicate values
set does not support index
set does not store values in order
set store unique values
Add -to add single value
Multiple data add -update pass in[] bracket
Remove ---single element -  remove --through error in element not present in set.
       ----single element --discard  -does not through error if element not present in set.
      -----pop-re remove any random element /data.
sort -to sort set (increment values)
 del /celar -to delete entire set

 Sort -used to sort set elements and convert it into list

 """

st={"abc","ppp",200,1,39.9,"kkk","abc","abc"}   #if store duplicate values stores only single value.
print(st)
print("Type of set:",type(st))
st.add(33)           #add single values use add method

#print length of set only unique values
print(len(st))
print("Added value:",st)

#adding multiple elements
print("Add multiple elements:")
st.update(["jaya","sarika",3444,"sarika","ppp"])
print(st)

#Remove  elements
print("--Remove Data---")
st.remove(39.9,)
print(st)
st.discard("abc")
st.discard("12")
print("After discard:",st)
st.pop()                    #remove any /random 1 element/data
print(st)

#copy set values on set 2

st1=st.copy()
print("Copied values of st in st1=",st1)

#when set values Sort then it returns into convert into list
jaya={300,900,100,800}
print("Original set:",jaya)
s=sorted(jaya)
print("Sorted set:",s)


#delete entire set  clear and del
jaya.clear()
print("Empty set:",jaya)

ss={43,5,0,3,2,2,"qq"}
print(ss)
del ss
#print("Empty set",ss)   #getting error after deleting set for using del

st2={23,44,11,66,40,11}
print("set:",st2)
ls=list(st2)
print("List :",ls)
print(type(ls))
print(type(st2))

