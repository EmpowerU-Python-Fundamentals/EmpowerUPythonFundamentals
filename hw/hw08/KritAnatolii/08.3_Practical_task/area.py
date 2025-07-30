from math import pi, pow

def rect_area(length, width):
      """Gives area of a rectangle"""
      return f"The area of this rectangle is {length * width} square units."

def triangle_area(base, height):
      """Gives area of a triangle"""
      return f"The area of this triangle is {0.5 * base * height} square units."

def circle_area(radius):
      """Gives area of a circle"""
      return f"The area of this circle is {pi*pow(radius, 2)} square units."

__all__ = ["rect_area", "triangle_area", "circle_area"]