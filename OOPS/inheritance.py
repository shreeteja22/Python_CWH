# Defining a base class 'Employee'
class Employee:
    # Constructor to initialize name and id of the employee
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Method to display employee details
    def details(self):
        print(f"The name of the employee is {self.name} and his id is {self.id}")

# Defining a derived class 'Programmer' that inherits from 'Employee'
class Programmer(Employee):
    # Method specific to the Programmer class to display the default programming language
    def showlanguage(self):
        print("The default language is Python")

# Creating an instance of Employee
e1 = Employee("Shreeram", 31122003)
e1.details()  # This will call the 'details' method from the Employee class

# Creating an instance of Programmer
e2 = Programmer("Harry", 4100)
e2.details()  # Inherited method from Employee class
e2.showlanguage()  # Method specific to Programmer class
