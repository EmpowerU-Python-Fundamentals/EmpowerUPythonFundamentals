from math import pi, pow
import area_figures


def main():
    menu = (
        "Which area do you want to calculate?\n"
        "1 - Rectangle (S = a * b)\n"
        "2 - Triangle  (S = 0.5 * a * h)\n"
        "3 - Circle    (S = pi * r^2)\n"
        "Choice: "
    )

    choice = input(menu).strip()

    if choice == "1":
        a = input("Enter a: ")
        b = input("Enter b: ")
        if a.isdigit() and b.isdigit():
            s = area_figures.rectangle_area(float(a), float(b))
            print(f"Rectangle area: {s}")
        else:
            print("Please enter a valid number.")
    elif choice == "2":
        a = input("Enter base a: ")
        h = input("Enter height h: ")
        if a.isdigit() and h.isdigit():
            s = area_figures.triangle_area(float(a), float(h))
            print(f"Triangle area: {s}")
        else:
            print("Please enter a valid number.")
    elif choice == "3":
        r = input("Enter radius r: ")
        if r.isdigit():
            s = area_figures.circle_area(float(r), pi, pow)  # pass pi and pow as required
            print(f"Circle area: {s}")
        else:
            print("Please enter a valid number.")
    else:
        print("Unknown choice. Please run the program again and pick 1, 2, or 3.")


if __name__ == "__main__":
    main()

