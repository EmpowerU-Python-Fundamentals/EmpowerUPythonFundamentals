import calculations

try:
    figure = int(input("Площу якої фігури ви бажаєте розрахувати: 1 - прямокутник, 2 - трикутник, 3 - коло. Введіть номер фігури: "))
except ValueError:
    print(f"Ви ввели недопустиме значення. Введіть, будь ласка, цифру 1, 2 або 3, в залежності від вида фігури (де 1 - прямокутник, 2 - трикутник, " \
"3 - коло). ")
    exit()

match figure:
    case 1:
        a = int(input("Введіть сторону а: "))
        b = int(input("Введіть сторону b: "))
        print(calculations.calculate_rectangle_area(a, b))
    case 2:
        a = int(input("Введіть сторону а: "))
        h = int(input("Введіть висоту h: "))
        print(calculations.calculate_triangle_area(a, h))
    case 3:
        r = int(input("Введіть радіус r: "))
        print(calculations.calculate_circle_area(r))
    case _:
        print(f"Ви ввели недопустиме значення: {figure}. Введіть, будь ласка, цифру 1, 2 або 3, в залежності від вида фігури (де 1 - прямокутник, 2 - трикутник, " \
"3 - коло) ")