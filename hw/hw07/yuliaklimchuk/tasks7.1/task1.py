def bigger_number(a,b):

    """
    This function returns the largest of two numbers or zero if the numbers are equal.
    """

    if a>b:
        return a
    elif b>a:
        return b
    else:
        return 0
    
number1 = int(input("Input number 1: "))
number2 = int(input("Input number 2: "))

print(bigger_number(number1,number2))