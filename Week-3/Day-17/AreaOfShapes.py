# Q : Create a Shape base class with an area() method. Subclasses: Circle, Rectangle, Triangle.

import math

class Shape:
    
    def area(self):
        raise NotImplementedError("subclasses must implement area() method !")


class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi *self.radius**2

class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length 
        self.width = width
        
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    

circle = Circle(5)
rectangle = Rectangle(10,5)
triangle = Triangle(5,7)

print("Circle area:", round(circle.area(),2))
print("Rectangle area:", rectangle.area())
print("Triangle area:", triangle.area())