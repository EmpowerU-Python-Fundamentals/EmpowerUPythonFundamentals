num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if num1 > num2:
    largest = num1
else:
    largest = num2

print(f"Найбільше число з {num1} та {num2} є: {largest}")