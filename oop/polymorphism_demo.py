import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape): 
    def __init__(self, length,width):
        self.radius = length
        self.radius = width
    def area(self):
        return math.pi * self.length* self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius