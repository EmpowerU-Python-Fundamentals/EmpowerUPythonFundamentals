def area_of_rectangle(width, height):
    """Розраховує площу прямокутника."""
    return width * height

def area_of_triangle(base, height):
    """Розраховує площу трикутника."""
    return 0.5 * base * height

def area_of_circle(radius):
    """Розраховує площу круга."""
    pi = 3.1416
    return pi * radius * radius

# User choise for calculating area
print("Оберіть фігуру для обчислення площі:")
print("1. Прямокутник")
print("2. Трикутник")
print("3. Круг")

choice = input("Введіть номер фігури (1/2/3): ")

if choice == "1":
    w = float(input("Введіть ширину: "))
    h = float(input("Введіть висоту: "))
    print("Площа прямокутника:", area_of_rectangle(w, h))

elif choice == "2":
    b = float(input("Введіть основу: "))
    h = float(input("Введіть висоту: "))
    print("Площа трикутника:", area_of_triangle(b, h))

elif choice == "3":
    r = float(input("Введіть радіус: "))
    print("Площа круга:", area_of_circle(r))

else:
    print("Невірний вибір. Будь ласка, запустіть програму ще раз.")
