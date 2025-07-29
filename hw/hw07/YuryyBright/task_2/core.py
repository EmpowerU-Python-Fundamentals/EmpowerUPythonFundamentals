from typing import List
from math import sqrt


# I. Jenny's secret message
def greet(name: str) -> str:
    """
    Returns a special greeting for Jenny, and a normal one for others.
    """
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


# II. Find The Distance Between Two Points
def distance_between_points(p1: complex, p2: complex) -> float:
    """
    Calculates the distance between two points using the distance formula.
    """
    return abs(p1 - p2)


# III. No yelling!
def remove_exclamation_marks(s: str) -> str:
    """
    Removes all exclamation marks from a string.
    """
    return s.replace('!', '')


# IV. Convert a Number to a String
def number_to_string(num: int) -> str:
    """
    Converts a number to its string representation.
    """
    return str(num)


# V. Reversing Words in a String
def reverse_words(text: str) -> str:
    """
    Reverses the order of words in a string.
    """
    return ' '.join(text.split()[::-1])


# VI. Reverse List Order
def reverse_list(lst: List[int]) -> List[int]:
    """
    Reverses the elements of a list.
    """
    return lst[::-1]


# VII. Multiples of 3 or 5
def sum_of_multiples(limit: int) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below the given number.
    """
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


# VIII. Will you make it?
def can_reach(distance: int, mpg: int, fuel_left: int) -> bool:
    """
    Determines if the car can reach the destination.
    """
    return mpg * fuel_left >= distance


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name: str) -> str:
    """
    Returns whether a person plays the banjo depending on the first letter of their name.
    """
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(value: bool) -> str:
    """
    Converts boolean value to 'Yes' or 'No'.
    """
    return "Yes" if value else "No"


# XI. Counting sheep
def count_sheep(sheep: List[bool]) -> int:
    """
    Counts how many 'True' values (sheep) are in the list.
    """
    return sheep.count(True)


# XII. Is this my tail?
def correct_tail(body: str, tail: str) -> bool:
    """
    Checks if the tail character is the same as the last character of the body.
    """
    return body.endswith(tail)
