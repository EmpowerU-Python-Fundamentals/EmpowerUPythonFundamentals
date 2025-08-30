from geometry import rectangle_area, triangle_area, circle_area

print("Оберіть фігуру для обчислення площі:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Коло")

choice = input("Введіть номер: ")

if choice == "1":
    a = float(input("Введіть довжину: "))
    b = float(input("Введіть ширину: "))
    print(f"Площа прямокутника = {rectangle_area(a, b)}")

elif choice == "2":
    base = float(input("Введіть основу: "))
    height = float(input("Введіть висоту: "))
    print(f"Площа трикутника = {triangle_area(base, height)}")

elif choice == "3":
    r = float(input("Введіть радіус: "))
    print(f"Площа кола = {circle_area(r)}")

else:
    print("Невірний вибір!")