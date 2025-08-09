def the_largest_number(num1, num2):
    """
    Порівнює два числа та повертає більше.

    Аргументи:
        num1 (int або float): Перше число для порівняння.
        num2 (int або float): Друге число для порівняння.

    Повертає:
        int або float: Найбільше з двох введених чисел.
    """
    # Найкращий спосіб - вбудована функція max().
    return max(num1, num2)
    # Кастомно через if-else:
    # if num1 >= num2:
    #     return num1
    # else:
    #     return num2

print(f"The largest number between 4 and 5 >> {the_largest_number(4, 5)}")
print(f"The largest number between 12 and 11 >> {the_largest_number(12, 11)}")
print(f"The largest number between 10 and 10 >> {the_largest_number(10, 10)}")
print(f"The largest number between -25 and -5 >> {the_largest_number(-25, -5)}")
print(f"The largest number between -125 and 1250 >> {the_largest_number(-125, 1250)}")
print(f"The largest number between 0 and 0 \-0-/ >> {the_largest_number(0, 0)}")