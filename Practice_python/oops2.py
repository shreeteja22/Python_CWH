class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def display(self):
        print(f"Name : {self.name} ")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self, name,sound):
        super().__init__(name, species = "Dog")
        self.sound = sound
    def display(self):
        print(f"Name : {self.name} ")
        print(f"Sound : {self.sound}")

class Cat(Animal):
    def __init__(self, name,sound):
        super().__init__(name, species = "Cat")
        self.sound = sound
    def display(self):
        print(f"Name : {self.name} ")
        print(f"Sound : {self.sound}")


a1 = Animal("Dog","Labrador")
a1.display()
a2 = Dog("Dog","Bow-Bow")
a2.display()
a3 = Cat("Cat","Meow-Meow")
a3.display()









class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, species="Dog")
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, species="Cat")
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

# Instantiate objects
a2 = Dog("Buddy", "Bow-Bow")
a3 = Cat("Kitty", "Meow-Meow")

# Call the speak method
print(a2.speak())  # Output: Buddy says Bow-Bow
print(a3.speak())  # Output: Kitty says Meow-Meow
