class Shape:
    # Constructor to initialize the dimensions of the shape
    def __init__(self, x, y):
        self.x = x  # Dimension 1 (e.g., width or length)
        self.y = y  # Dimension 2 (e.g., height or breadth)

    def area(self):
        return self.x * self.y  # Area formula: width * height
    
class Circle(Shape):
    # Constructor to initialize the radius of the circle
    def __init__(self, radius):
        self.radius = radius  
        super().__init__(radius, radius)  # Call the parent class constructor with radius for both dimensions

    def area(self):
        return 3.14 * super().area()  # super().area() gives radius * radius
    
rec = Shape(3, 5)
print(rec.area())  # Output: 15 (3 * 5)

c = Circle(5)
print(c.area())  # Output: 78.5 (3.14 * 5 * 5)
