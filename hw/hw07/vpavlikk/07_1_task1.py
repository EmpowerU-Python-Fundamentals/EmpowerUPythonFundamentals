def largest_number(num1, num2):
    """Function that returns the largest of two numbers."""
    return (
        "only numbers allowes"
        if type(num1) not in (int, float) or type(num2) not in (int, float)
        else (num1 if num1 > num2 else "numbers are the same" if num1 == num2 else num2)
    )


print(largest_number(3, 8))
print(largest_number(12, 5))
print(largest_number(1, 1))
print(largest_number(1.1, 1.2))
print(largest_number(-1.1, -1.2))
print(largest_number(-1.1, "test"))
