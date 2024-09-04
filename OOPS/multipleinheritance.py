class Employee:
    def __init__(self, name):
        self.name = name  
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance  

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance  
        self.name = name    

o = DancerEmployee("Kathak", "Shivani")

print(o.name)   # Output: Shivani
print(o.dance)  # Output: Kathak

# Call the show method (inherited from the first class in the MRO, which is Employee)
o.show()  # Output: The name is Shivani

# Print the method resolution order (MRO)
print(DancerEmployee.mro())
# Output: [<class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]


#14th line mai bracket mai jo pehla likha hai uska hi show method call hoga first as per mro
