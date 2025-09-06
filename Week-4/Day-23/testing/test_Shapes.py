import pytest
import source.Shapes as shapes
import math

# class based testing

class Test_Shapes:
    
    def setup_method(self, method):
        print(f"\nSetting up {method}")
        self.circle = shapes.Circle(5)
    
    def teardown_method(self, method):
        print(f"\ntearing down {method}")
        del self.circle
        
    def test_circle(self):
            assert self.circle.area() == math.pi * self.circle.radius ** 2
            