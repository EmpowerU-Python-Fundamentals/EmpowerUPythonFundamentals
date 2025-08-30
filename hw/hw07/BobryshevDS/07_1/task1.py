#Напишіть функцію, яка повертає найбільше з двох чисел (використовуйте DocStrings для документації функції)
def largest_number(num1, num2):
    """ Функція приймає два числа і повертає найбільше з них."""
    if num1 >= num2:
        return num1
    else:
        return num2

print(f"Найбільше число: {largest_number(3, 2)}")