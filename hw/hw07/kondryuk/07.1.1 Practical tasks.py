# 07.1.1 Practical Tasks
# Write a function that returns the largest numer of two numbers. 
# Use DocStrings documentation strings in the function.

def largest_numb(a: float,b: float) -> float:
    """
    Returns the largest number
    
    Parameters:
    a (int or float): first number
    b (int or float): second number

    Returns:
    int or float: the larger number

    Example:
    >>>largest_numb(5,13)
    13
    >>>largest_numb(-12,-15)
    -12
    >>>largest_numb(8.1,7.9)
    8.1
    >>>largest_numb(0,0)
    0
    """
    if not all(isinstance(x, (int, float)) for x in (a,b)):
        raise TypeError("Both arguments must be numbers")
    return a if a > b else b

# Demonstration of access to documentation via __doc__
print("Demonstration of access to documentation via __doc__:")
print(largest_numb.__doc__)
# Demonstration of access to documentation via help()
print("Demonstration of access to documentation via help():")
help(largest_numb)
 
# Example of use
print("Example of use:")
print(largest_numb(5,13)) # 13
print(largest_numb(-12,-15)) # -12
print(largest_numb(8.1,7.9)) # 8.1
print(largest_numb(0,0)) # 0 