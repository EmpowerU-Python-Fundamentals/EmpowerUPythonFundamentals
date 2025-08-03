from unittest import case

from .areas import AREAS

PROMPTS = {
    1: "rectangle",
    2: "triangle",
    3: "circle",
}

def get_prompt():
    print("Enter the number of figures which area should be calculated: "
          "1: rectangle, 2: triangle, 3: circle: ", end=""
    )

    while True:
        try:
            figure = int(input())
            if figure in PROMPTS:
                return PROMPTS[figure]
        except ValueError:
            print("Please make a valid figure: ", end="")
            continue

def get_figure_params(n):
    params = []
    i = 0
    while i < n:
        try:
            params.append(int(input("Enter parameter: ")))
            i += 1
        except ValueError:
            continue

    return params

def calculate_area():
    choice = get_prompt()

    match choice:
        case "rectangle":
            params_num = 2
        case "triangle":
            params_num = 2
        case "circle":
            params_num = 2
        case _:
            print("Unknown shape.")
            return 0

    return AREAS[choice](params_num)

def main():
    result = calculate_area()
    print(f"The area is: {result:.2f}")

if __name__ == "__main__":
    main()

