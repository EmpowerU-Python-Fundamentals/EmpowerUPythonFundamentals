def max_num(a, b):
    """
    Returns:
        int or float: The larger of the two numbers. 
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
    """
    if a > b: 
        return a
    return b

print (max_num(3, 5))  # Output: 5
print (max_num(10, 2)) # Output: 10
print (max_num(7.5, 7.5)) # Output: 7.5
print (max_num(-1, 0)) # Output: 0
