from Practical import area_rectangle, area_triangle, area_circle


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("1) Rectangle\n2) Triangle\n3) Circle")
    choice = input("Figure (1–3): ")

    if choice == "1":
        w = ask_float("Width  : ")
        h = ask_float("Height : ")
        print("Area =", area_rectangle(w, h))

    elif choice == "2":
        b = ask_float("Base   : ")
        h = ask_float("Height : ")
        print("Area =", area_triangle(b, h))

    elif choice == "3":
        r = ask_float("Radius : ")
        print("Area =", area_circle(r))

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()