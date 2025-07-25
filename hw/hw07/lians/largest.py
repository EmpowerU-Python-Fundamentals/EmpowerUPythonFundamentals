def largest(a, b):
    """Return largest number of two numbers, if not equal"""
    
    if any(not isinstance(el, (int, float)) for el in (a, b)):
        try:
            a = float(a)
            b = float(b)
        except (ValueError, TypeError):
            exit("Should be integers or floats to compare")
            
    if a == b:
        result = "Equal"
    elif a > b:
        result = a
    else:
        result = b
    return result


# print(largest.__doc__)             # Return largest number of two numbers, if not equal
# print(largest(3, 3))               # Equal
# print(largest(-0.23, 0.17))        # 0.17
# print(largest(5, 2.00005))         # 5
# print(largest("3", "4.5"))         # 4.5
# print(largest("yellow", "blue"))   # Should be integers or floats to compare
