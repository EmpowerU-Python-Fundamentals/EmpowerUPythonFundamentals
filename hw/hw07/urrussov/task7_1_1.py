def largest_num(a, b):
    """This function returns the largest number of two.
    If numbers are equal, function will return "equal"
    """

    if a == b:
        return "equal"
    if a < b:
        return f"{b} is larger than {a}"
    return f"{a} is larger than {b}"


def check_num():
    """This function checks if the input is int or float"""

    while True:
        try:
            x = float(input("Enter number: "))
            return x
        except ValueError:
            print("You didn't write a number")


num1 = check_num()
num2 = check_num()

result_a = largest_num(num1, num2)
print(result_a)
