"""
This module is the client for the shape factory. Do not call any other module directly
"""
from IShape import IShape, shape_factory

def main():
    c = shape_factory("Circle", radius=5)
    t = shape_factory("Triangle", base=5, height=10)
    r = shape_factory("Rectangle", length=5, width=10)

    shapes = [c, t, r]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")
    


if __name__ == "__main__":
    main()