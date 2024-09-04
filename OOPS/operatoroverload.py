class Vector:
    # Constructor to initialize the vector components
    def __init__(self, i, j, k):
        self.i = i  # x-component
        self.j = j  # y-component
        self.k = k  # z-component

    # String representation of the vector in the form "i + j + k"
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    # Overloading the addition operator to add two vectors
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

v1 = Vector(3, 5, 6)
print(v1) 

v2 = Vector(1, 2, 9)
print(v2)  

# Adding two vectors using the overloaded + operator
print(v1 + v2)  # Output: 4i + 7j + 15k

# Printing the type of the resulting vector
print(type(v1 + v2))  # Output: <class '__main__.Vector'>
