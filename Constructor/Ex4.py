class Demo4:
    def __init__(self,name,empid,designation,emppkg):      #constructor
        self.name=name
        self.empid=empid
        self.designation=designation
        self.emppkg=emppkg
        

    def empInfo(self):               #method
        print("Name of employee:",self.name,"\nEmployee ID:",self.empid,"\nEmployee Designation:",self.designation,"\nEmployee Package:",self.emppkg)


emp=Demo4("jaya",4065,"manualTester",52000)   #constructor calling
print("-------Information of Employee---------")

emp2=Demo4("Sarika",4066,"AutomationTester",92000)   #again constructor calling
emp.empInfo()
print("---------------")
emp2.empInfo()