#Module2

#from PackageName import ModuleName
#.fn--- >calling function
#obj=ClassName
#obj.fn
from Modulesandpkges1 import Test1
from Modulesandpkges1.Test1 import MyClass

print("-------Calling pkg1 in pkg 2-----------")
Test1.f1()
Test1.f2()
print("Accessing data from other pkg class method")
c=MyClass()
c.mm1()
c.mm2()






