class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e1 = Employee("Teja",12000)
print(e1.name,e1.salary)
string = "Ram-15000"
e2 = Employee.fromStr(string)
print(e2.name, e2.salary)