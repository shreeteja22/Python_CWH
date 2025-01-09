# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
    
#     def show(self):
#         print(f"Name : {self.name}")
#         print(f"Species : {self.species}")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species = "Dog")
#         self.breed = breed
#     def show(self):
#             Animal.show(self)
#             print(f"Breed : {self.breed}")

# class Rotwheeler(Dog):
#     def __init__(self,name,color):
#         Dog.__init__(self,name,breed = "Rotwheeler")
#         self.color = color
#     def show(self):
#         Dog.show(self)
#         print(f"Color : {self.color}")

# a1 = Dog("Rocky","Black")
# a1.show()



class Animal:
    
    def __init__(self, name, species):
       
        self.name = name
        self.species = species
  
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    
    def __init__(self, name, breed):
        
        Animal.__init__(self, name, species="Dog")
        
        self.breed = breed
        
    
    def show_details(self):
        
        Animal.show_details(self)
        
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    
    def __init__(self, name, color):
        
        Dog.__init__(self, name, breed="Golden Retriever")
        
        self.color = color
        
    def show_details(self):
        
        Dog.show_details(self)
        
        print(f"Color: {self.color}")

# Create an instance of the 'Dog' class
o = Dog("Tommy", "Rotwheeler")
# Call the 'show_details' method on the instance to display its details
o.show_details()
