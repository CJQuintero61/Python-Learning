from IShape import IShape

class Triangle(IShape):
    """triangle class that implements the IShape interface"""
    
    def __init__(self, base: float = 0, height: float = 0):
        self.base = base
        self.height = height
    

    def area(self) -> float:
        return 0.5 * self.base * self.height
    
    
    