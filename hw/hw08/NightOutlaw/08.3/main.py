"""Programm that calculates the area of a rectangle, the area of a triangle, the area of a circle"""
from areas import rectangle_area, triangle_area, circle_area

print("Оберіть фігуру, площу якої ви хочете розрахувати:")
print("1 — Прямокутник")
print("2 — Трикутник")
print("3 — Коло")

choice = input("Введіть свій вибір (1-3): ")

if choice == '1':
    a = float(input("Введіть довжину сторони a: "))
    b = float(input("Введіть довжину сторони b: "))
    print("Площа прямокутника:", rectangle_area(a, b))

elif choice == '2':
    a = float(input("Введіть довжину сторони трикутника a: "))
    h = float(input("Введіть висоту трикутника h: "))
    print("Площа трикутника:", triangle_area(a, h))

elif choice == '3':
    r = float(input("Введіть радіус кола r: "))
    print("Площа кола:", circle_area(r))

else:
    print("Невірний вибір. Перезапустіть скрипт, щоб спробувати ще раз.")
