def max_of_two_numbers(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a: The first number.
    b: The second number.
    """
    return a if a > b else b


#Перевірка:
print(max_of_two_numbers(1, 2))
print(max_of_two_numbers.__doc__)