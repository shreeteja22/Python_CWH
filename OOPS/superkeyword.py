class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id) #child se parent ko contact karne 
        self.lang = lang

a =Employee("Harry" ,"23H")
b = Programmer("Ram" , "24R" , "Python")
print(a.name)
print(b.name)
print(b.id)
print(b.lang)