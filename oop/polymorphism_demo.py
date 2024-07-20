import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape): 
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length** 2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius