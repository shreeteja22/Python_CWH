class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  # Method to display human's details (name and age)
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)

# Derived class Person inheriting from Human
class Person(Human):
  def __init__(self, name, age, address):
    # Call to the Human class constructor to initialize name and age
    Human.__init__(self, name, age)
    self.address = address
    
  # Method to display person's details (name, age, and address)
  def show_details(self):
    # Call to Human's show_details method to display name and age
    Human.show_details(self)
    # Display the address
    print("Address:", self.address)

# Class Program to represent a study program with its name and duration
class Program:
  # Constructor to initialize program name and duration
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  # Method to display program details (program name and duration)
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)

# Derived class Student inheriting from Person
class Student(Person):
  # Constructor to initialize name, age, address, and the program they are enrolled in
  def __init__(self, name, age, address, program):
    # Call to the Person class constructor to initialize name, age, and address
    Person.__init__(self, name, age, address)
    # Assign the program to the student
    self.program = program
    
  # Method to display student details, including their program details
  def show_details(self):
    # Call to Person's show_details method to display name, age, and address
    Person.show_details(self)
    # Call to Program's show_details method to display the program details
    self.program.show_details()

program = Program("Computer Science", 4)

student = Student("John Doe", 25, "123 Main St.", program)

student.show_details()
