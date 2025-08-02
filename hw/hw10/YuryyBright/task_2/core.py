
# ------------------------- Так, я знаю що цей код згенерував ШІ, однак якби я не вказав, 
# що треба використати слоти (звісно для економії пам'яті) він би і не здогадавс що я хочу.
# Я зрозумів завдання, однак виріштв трішки ускладнити 

from abc import ABC, abstractmethod
import random
import math
from typing import List

# Task I: Ball-super-ball
class Ball:
    """Base class for a ball, demonstrating basic attributes and encapsulation"""
    def __init__(self, ball_type: str = "regular"):
        self._ball_type = ball_type

    @property
    def ball_type(self) -> str:
        """Getter for ball type - encapsulation"""
        return self._ball_type

class SuperBall(Ball):
    """SuperBall subclass, demonstrating inheritance"""
    def __init__(self):
        super().__init__("super")

# Task II: Color-ghost
class Ghost:
    """Ghost class that randomly assigns a color, demonstrating encapsulation"""
    _colors = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self._color = random.choice(self._colors)

    @property
    def color(self) -> str:
        """Getter for color - encapsulation"""
        return self._color

# Task III: Basic-subclasses-Adam-and-Eve
class Human(ABC):
    """Abstract base class for humans, demonstrating abstraction"""
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        """Getter for name - encapsulation"""
        return self._name

    @abstractmethod
    def gender(self) -> str:
        """Abstract method for gender - must be implemented"""
        pass

class Man(Human):
    """Man class, demonstrating inheritance and polymorphism"""
    def gender(self) -> str:
        return "male"

class Woman(Human):
    """Woman class, demonstrating inheritance and polymorphism"""
    def gender(self) -> str:
        return "female"

def create_humans() -> List[Human]:
    """Factory function to create Adam and Eve"""
    return [Man("Adam"), Woman("Eve")]

# Task IV: Classy-classes
class Person:
    """Person class with name and age, demonstrating encapsulation"""
    def __init__(self, name: str, age: int):
        self._name = self._validate_name(name)
        self._age = self._validate_age(age)

    def _validate_name(self, name: str) -> str:
        """Private validation method - encapsulation"""
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        return name.strip()

    def _validate_age(self, age: int) -> int:
        """Private validation method - encapsulation"""
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        return age

    @property
    def name(self) -> str:
        """Getter for name - encapsulation"""
        return self._name

    @property
    def age(self) -> int:
        """Getter for age - encapsulation"""
        return self._age

    def get_info(self) -> str:
        """Return formatted info string - polymorphism"""
        return f"{self.name} is {self.age} year{'s' if self.age != 1 else ''} old"

# Task V: Building Spheres
class Sphere:
    """Sphere class for volume and surface area calculations, demonstrating encapsulation"""
    def __init__(self, radius: float, mass: float):
        self._radius = self._validate_dimension(radius, "radius")
        self._mass = self._validate_dimension(mass, "mass")

    def _validate_dimension(self, value: float, dimension: str) -> float:
        """Private validation method - encapsulation"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{dimension.capitalize()} must be positive")
        return float(value)

    @property
    def radius(self) -> float:
        """Getter for radius - encapsulation"""
        return self._radius

    @property
    def mass(self) -> float:
        """Getter for mass - encapsulation"""
        return self._mass

    def get_volume(self) -> float:
        """Calculate sphere volume"""
        return (4/3) * math.pi * (self._radius ** 3)

    def get_surface_area(self) -> float:
        """Calculate sphere surface area"""
        return 4 * math.pi * (self._radius ** 2)

    def get_density(self) -> float:
        """Calculate density (mass/volume)"""
        return self._mass / self.get_volume()

# Task VI: Dynamic Classes
class ClassFactory:
    """Factory class for creating dynamic classes with __slots__, demonstrating dynamic class creation and memory efficiency"""
    @staticmethod
    def create_dynamic_class(class_name: str, attributes: List[str]):
        """Create a dynamic class with specified attributes using __slots__ for memory efficiency"""
        # Define slots for memory efficiency
        slots = [f"_{attr}" for attr in attributes]

        def init(self, *args):
            if len(args) != len(attributes):
                raise ValueError(f"Expected {len(attributes)} arguments, got {len(args)}")
            for attr, value in zip(attributes, args):
                setattr(self, f"_{attr}", value)

        def str_method(self):
            return f"{class_name}({', '.join(f'{attr}={getattr(self, f'_{attr}')}' for attr in attributes)})"

        # Create dictionary for class attributes and methods
        class_dict = {
            '__slots__': slots,
            '__init__': init,
            '__str__': str_method
        }
        # Add properties for each attribute
        for attr in attributes:
            class_dict[f"{attr}"] = property(lambda self, a=attr: getattr(self, f"_{a}"))

        return type(class_name, (), class_dict)