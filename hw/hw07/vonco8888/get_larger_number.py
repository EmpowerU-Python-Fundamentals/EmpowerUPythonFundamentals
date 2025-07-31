def get_larger_number(a, b):
    """
    Повертає більше з двох переданих чисел.

    Аргументи:
    a (int або float): перше число
    b (int або float): друге число

    Повертає:
    int або float: більше з двох чисел
    """
    if a > b:
        return a
    else:
        return b
print(get_larger_number(5, 10))   # Виведе: 10
print(get_larger_number(3.5, 2))  # Виведе: 3.5
print(get_larger_number(7, 7))    # Виведе: 7
