class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

# Derived class Dog inheriting from the Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call to the Animal constructor to initialize the name
        Animal.__init__(self, name)
        self.breed = breed

    # Method to display the dog's details (name, species, and breed)
    def show_details(self):
        # Call to Animal's show_details to display the name
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

# Derived class Cat inheriting from the Animal class
class Cat(Animal):
    def __init__(self, name, color):
        # Call to the Animal constructor to initialize the name
        Animal.__init__(self, name)
        self.color = color

    # Method to display the cat's details (name, species, and color)
    def show_details(self):
        # Call to Animal's show_details to display the name
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

# Create a Dog object with name and breed
dog = Dog("Max", "Golden Retriever")
# Display the details of the dog
dog.show_details()

# Create a Cat object with name and color
cat = Cat("Luna", "Black")
# Display the details of the cat
cat.show_details()
