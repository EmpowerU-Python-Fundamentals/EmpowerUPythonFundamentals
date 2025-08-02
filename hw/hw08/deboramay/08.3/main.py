import calculations

figure = int(input("Площу якої фігури ви бажаєте розрахувати: 1 - прямокутник, 2 - трикутник," \
"3 - коло. Введіть номер фігури: "))

match figure:
    case 1:
        a = int(input("Введіть сторону а: "))
        b = int(input("Введіть сторону b: "))
        calculations.area_rect(a, b)
    case 2:
        a = int(input("Введіть сторону а: "))
        h = int(input("Введіть висоту h: "))
        calculations.area_tri(a, h)
    case 3:
        r = int(input("Введіть радіус r: "))
        calculations.area_circle(r)
    case _:
        print("Помилка вводу, спробуйте ще раз.")