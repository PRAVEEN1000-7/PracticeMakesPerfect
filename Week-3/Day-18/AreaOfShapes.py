 # Q : Demonstrate polymorphism by iterating over different shapes and calling area().

from abc import ABC, abstractmethod
 
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    def description(self):
        return "This is a shape."
    
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi *self.radius**2
    
    def description(self):
        return super().description()+" called Circle !"

class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length 
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def description(self):
        return super().description()+" called Rectangle !"

class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
    def description(self):
        return super().description()+" called Triangle !"
    

shapes = [Circle(5), Rectangle(10,5), Triangle(5,7)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area : {shape.area()}")
    print(shape.description())