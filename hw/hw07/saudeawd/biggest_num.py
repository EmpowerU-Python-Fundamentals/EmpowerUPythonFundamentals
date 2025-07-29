"""finds the biggest number of two"""
def bigger(num1, num2):
    """finds the biggest number of two
    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int: the biggest number of two numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2

your_1num = input()
your_2num = input()
print(bigger(your_1num, your_2num))