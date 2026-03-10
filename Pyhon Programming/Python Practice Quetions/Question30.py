# Question:
# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

import math   # Used to access the value of π (pi)

class Circle:
    
    def __init__(self, r):
        # Constructor: runs automatically when object is created
        self.radius = r   # Instance variable to store radius
    
    def Area(self):
        # Formula: π × r²
        return math.pi * self.radius ** 2
    
    def Perimeter(self):
        # Formula: 2 × π × r
        return 2 * math.pi * self.radius


# Example usage
c = Circle(5)   # Creating object with radius = 5

print("Area:", c.Area())
print("Perimeter:", c.Perimeter())