def my_func(a, b):
    """
    Finds the largest of two numbers.

    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The larger of the two input numbers.
    """
    return a if a > b else b



x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(my_func(x, y))


