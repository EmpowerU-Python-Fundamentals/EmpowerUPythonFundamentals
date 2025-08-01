from areas import AREAS

PROMPTS = {
    1: "rectangle",
    2: "triangle",
    3: "square",
}

def area(figure):
    match figure:
        case "rectangle":
            return AREAS["rectangle"]
        case "triangle":
            return AREAS["triangle"]
        case "triangle":
            return AREAS["triangle"]

    return NotImplemented

def get_prompt():
    print("Enter the number of figures which area should be calculated: "
          "1: rectangle, 2: triangle, 3: square: ", end=""
    )

    while True:
        figure = int(input())
        if figure in PROMPTS:
            return area(PROMPTS[figure])

def main():
    pass

if __name__ == "__main__":
    main()

