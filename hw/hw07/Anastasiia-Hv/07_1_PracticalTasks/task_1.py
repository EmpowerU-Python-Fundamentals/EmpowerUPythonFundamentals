def largest_number(a, b):
    """
    Return the largest of two numbers.
    
    Parameters:
    a: The first number.
    b: The second number.
    """
    return a if a > b else b

num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")
print(f"The largest number is: {largest_number(num1, num2)}")