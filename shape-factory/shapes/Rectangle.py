from IShape import IShape

class Rectangle(IShape):
    """rectangle shape class that implements the IShape interface"""

    def __init__(self, length: float = 0.0, width: float = 0.0):
        self.length = length
        self.width = width

    def area(self) -> float:
        """calculates the area of the rectangle"""
        return self.length * self.width