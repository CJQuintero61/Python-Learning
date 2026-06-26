from abc import ABC, abstractmethod
from importlib import import_module

class IShape(ABC):
    """
    This is the interface for all shapes. All shapes must implement this interface
    to be created by the shape factory.
    """

    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement this method")


def shape_factory(shape_type: str, **kwargs) -> IShape:
    """
    This is the factory method to create shapes. This factory method can be called
    anywhere in the code to create shapes. It will import the shape module dynamically
    based on the shape type requested.

    Args:
        shape_type (str): The type of shape to create
    
    Returns:
        IShape: The shape object created by the factory
    """

    try:
        return getattr(
            import_module(f"shapes.{shape_type}"),      # the module name to import
            shape_type                                  # the class to instantiate from the module
        )(**kwargs)
        """
        the last parenthesis is to call the class constructor and pass **kwargs to it
        """
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f'Failed to import shape module for shape: {shape_type}!')