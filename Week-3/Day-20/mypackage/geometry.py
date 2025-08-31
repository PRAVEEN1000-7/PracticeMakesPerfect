import math

def area_circle(radius):
    """Calculate area of a circle. Formula: π * r^2"""
    return math.pi * radius ** 2

def perimeter_circle(radius):
    """Calculate perimeter (circumference) of a circle. Formula: 2 * π * r"""
    return 2 * math.pi * radius

def area_rectangle(length, width):
    """Calculate area of a rectangle. Formula: length * width"""
    return length * width

def perimeter_rectangle(length, width):
    """Calculate perimeter of a rectangle. Formula: 2 * (length + width)"""
    return 2 * (length + width)

def area_square(side):
    """Calculate area of a square. Formula: side^2"""
    return side ** 2

def perimeter_square(side):
    """Calculate perimeter of a square. Formula: 4 * side"""
    return 4 * side
