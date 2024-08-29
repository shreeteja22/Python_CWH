class Employee:
    companyName = "Apple" #this is called class variable
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.3
    def showDetails(self):
        print(f"The name of the employee is {self.name}  and the company which he works is {self.companyName} and his raise is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.5 #this is called instance variable
emp1.showDetails()