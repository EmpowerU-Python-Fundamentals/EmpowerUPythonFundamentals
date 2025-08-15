from areas import rectangle_area, triangle_area, circle_area
import math

def main():
    print("Калькулятор площ фігур")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("\nОберіть фігуру для обчислення площі (1-3): ")

    if choice == "1":
        a = float(input("Введіть довжину прямокутника (a): "))
        b = float(input("Введіть ширину прямокутника (b): "))
        area = rectangle_area(a, b)
        print(f"Площа прямокутника: {area}")

    elif choice == "2":
        h = float(input("Введіть висоту трикутника (h): "))
        a = float(input("Введіть основу трикутника (a): "))
        area = triangle_area(h, a)
        print(f"Площа трикутника: {area}")

    elif choice == "3":
        r = float(input("Введіть радіус кола (r): "))
        area = circle_area(r)
        print(f"Площа кола: {area}")

    else:
        print("Невірний вибір!")


if __name__ == "__main__":
    main()