"""07.1 Practical tasks. Task 2 'Largest Number" """

def largest_number(a, b):
    """Function returns the largest of two number"""
    if isinstance(a, int | float) and isinstance(a, int | float):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return "Numbers are equal"
    else:
        raise TypeError(f"Both parameters must be numbers: 'a' is {type(a).__name__}, 'b' is {type(b).__name__}")


print(largest_number(1, 2))
