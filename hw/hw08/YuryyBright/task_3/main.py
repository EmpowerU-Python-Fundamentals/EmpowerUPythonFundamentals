"""
main.py
=======
Interactive program that calculates area of geometric figures.

Run:
    python main.py
"""

from core import rectangle_area, triangle_area, circle_area

MENU = {
    "1": ("Rectangle", rectangle_area, ("length a", "width b")),
    "2": ("Triangle", triangle_area, ("height h", "base a")),
    "3": ("Circle", circle_area, ("radius r",)),
}

def _get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(f"Enter {prompt}: "))
        except ValueError:
            print("⚠️  Not a number, try again.")

def main() -> None:
    print("Choose figure to calculate area:")
    for key, (name, _, _) in MENU.items():
        print(f"  {key}. {name}")
    
    choice = input("Your option [1–3]: ").strip()
    
    if choice not in MENU:
        print("❌ Invalid choice.")
        return

    name, func, params = MENU[choice]
    values = [_get_float(p) for p in params]

    try:
        area = func(*values)
    except ValueError as err:
        print(f"Error: {err}")
        return

    print(f"✅ Area of the {name.lower()}: {area:.4f}")

if __name__ == "__main__":
    main()
