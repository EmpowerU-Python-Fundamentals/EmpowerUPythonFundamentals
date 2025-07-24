def get_large_number(a: int, b: int) -> int:
    """
    Function that returns the largest of two numbers.
    """
    if a == b:
        raise ValueError("Both numbers are equal")

    return a if a > b else b


larger_number = get_large_number(20, 20)
print(larger_number)