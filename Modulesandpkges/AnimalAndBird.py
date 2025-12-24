#Approach 1
#import moduleName1,moduleName2
#modulename.fn

print("---Function calling using Approach 1--")

import Animal,Bird

Animal.fly()
Animal.colour()


Bird.fly()
Bird.colour()

#Approvach 2
#from moduleName1 import *
#from moduleName2 import
print("---Function calling using Approach 2--")
from Animal import *
from Bird import *

Animal.fly(),colour()
print("Other class Variable Calling:",name)


Bird.fly()
Bird.colour()