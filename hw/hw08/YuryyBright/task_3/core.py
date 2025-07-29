"""
core.py
=======
Geometry area formulas.

Functions:
    rectangle_area(a, b)
    triangle_area(h, a)
    circle_area(r)
"""

import math
from typing import Union

Number = Union[int, float]

__all__ = [
    "rectangle_area",
    "triangle_area",
    "circle_area",
]

def rectangle_area(a: Number, b: Number) -> float:
    """Return area of rectangle: S = a * b."""
    _validate_positive(a, b)
    return float(a) * float(b)

def triangle_area(h: Number, a: Number) -> float:
    """Return area of triangle: S = 0.5 * h * a."""
    _validate_positive(h, a)
    return 0.5 * float(h) * float(a)

def circle_area(r: Number) -> float:
    """Return area of circle: S = π * r² using math.pow & math.pi."""
    _validate_positive(r)
    return math.pi * math.pow(float(r), 2)

def _validate_positive(*values: Number) -> None:
    if not all(v > 0 for v in values):
        raise ValueError("All dimensions must be positive numbers.")
