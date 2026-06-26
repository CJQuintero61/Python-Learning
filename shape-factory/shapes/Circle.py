from IShape import IShape
from math import pi

class Circle(IShape):
    """circle shape class that implements the IShape interface"""

    def __init__(self, radius: float = 0.0):
        self.radius = radius

    def area(self) -> float:
        """calculates the area of the circle"""
        return pi * self.radius * self.radius