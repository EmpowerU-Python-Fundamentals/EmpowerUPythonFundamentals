from math import pi
from typing import Dict

class NumberComparer:
    """Handles number comparison logic."""

    @staticmethod
    def max_of_two(a: float, b: float) -> float:
        """
        Return the maximum of two numbers.
        
        Parameters:
        a (float): First number
        b (float): Second number
        
        Returns:
        float: The larger of the two numbers
        """
        return a if a > b else b


class ShapeAreaCalculator:
    """Handles area calculations for different shapes."""

    @staticmethod
    def rectangle_area(length: float, width: float) -> float:
        """Return the area of a rectangle."""
        return length * width

    @staticmethod
    def triangle_area(base: float, height: float) -> float:
        """Return the area of a triangle."""
        return 0.5 * base * height

    @staticmethod
    def circle_area(radius: float) -> float:
        """Return the area of a circle."""
        return pi * radius ** 2


class CharacterCounter:
    """Counts characters in a given string."""

    @staticmethod
    def count_characters(text: str) -> Dict[str, int]:
        """
        Count frequency of each character in the string.

        Parameters:
        text (str): The input string

        Returns:
        Dict[str, int]: Dictionary of character counts
        """
        counts: Dict[str, int] = {}
        for char in text:
            counts[char] = counts.get(char, 0) + 1
        return counts
