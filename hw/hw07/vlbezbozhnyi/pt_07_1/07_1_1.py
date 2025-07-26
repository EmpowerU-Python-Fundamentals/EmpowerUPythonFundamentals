def largest_number(a: int | float, b: int | float) -> int | float:
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): First number.
    b (int or float): Second number.

    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a if a > b else b

    else:
        raise TypeError("Both arguments must be of type int or float.")
