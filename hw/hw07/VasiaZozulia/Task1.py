def largest_number (first_number, second_number):
    """Returns the largest number
    
    Parameters:
    first_number (int or float): The first number.
    second_number (int or float): The second number.

    Returns:
    int or float: The larger of the two numbers."""
    if type(first_number) in (int, float) and type(second_number) in (int, float):
        return first_number if first_number > second_number else second_number
    else:
        return None

print(largest_number.__doc__)
print(f"The largest numbber is {largest_number(10, 20) = }")
print(f"The largest numbber is {largest_number(40, 60) = }")
print(f"The largest numbber is {largest_number(-5.4, -8.3) = }")
print(f"The largest numbber is {largest_number(74.2, 34.8) = }")
print(f"The largest numbber is {largest_number(-4, 'z') = }")
