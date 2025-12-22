#module 2 Arithmaticoperation

#approach import module
#moduleName.fn()-->calll function
#moduleName.variable-->variable Name

#obj=modulename.classname()        #object create from different module
#obj.methodname()         -->method call
#obj.variableName               --->variable call


import Calculator
print("-------Class variable and Function calling-----")
#calling function
Calculator.addition(10,33)   #calling fn
Calculator.multiply(11,9)   #call global variable
print(Calculator.num)
print("Global variable:",Calculator.name)


print("---------- Function and Variable of other class calling---------")
#class method and variable calling
d1=Calculator.Demo1()
d1.m1()
d1.m2()
d2=Calculator.Demo2()
d2.m3()
print("Function Variable :",d1.car)