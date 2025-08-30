from area import rectangle_area, triangle_area, circle_area


print("Оберіть фігуру для обчислення площі ")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Круг")

choice = input("Ваш вибір (1/2/3): ")
if choice == "1":
    a = float(input("Введіть висоту: "))
    b = float(input("Введіть ширину: "))
    print("Площа прямокутника:", rectangle_area(a, b))

elif choice == "2":
    a = float(input("Введіть основу a: "))
    h = float(input("Введіть висоту h: "))
    print("Площа трикутника:", triangle_area(a, h))

elif choice == "3":
    r = float(input("Введіть радіус r: "))
    print("Площа круга:", circle_area(r))

else:
    print("Некоректний вибір, спробуйте ще раз.")