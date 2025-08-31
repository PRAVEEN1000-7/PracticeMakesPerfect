from math_utils import MathWorks
from mypackage import finance, geometry

print("factorial of 5 :",MathWorks.factorial(5))
print("is 5 prime number ?",MathWorks.checkPrime(5))
print("square of 5 :",MathWorks.square(5))
print("cube of 5 :",MathWorks.cube(5))

print("Simple Interest :",finance.simple_interest(10,5,5))
print("compound Interest :",finance.compound_interest(10,5,5,3))

print("Area of Circle:", geometry.area_circle(5))
print("Perimeter of Circle:", geometry.perimeter_circle(5))
print("Area of Rectangle:", geometry.area_rectangle(4, 6))
print("Perimeter of Rectangle:", geometry.perimeter_rectangle(4, 6))
print("Area of Square:", geometry.area_square(4))
print("Perimeter of Square:", geometry.perimeter_square(4))
