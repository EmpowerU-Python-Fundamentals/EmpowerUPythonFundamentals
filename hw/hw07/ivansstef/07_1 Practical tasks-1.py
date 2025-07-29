a = int(input("First: "))
b = int(input("Second: "))

def max_number(a, b):
    """Функція повертає більше з двох чисел."""
    return a if a > b else b

print(max_number(a, b))
