import area


def main():
    area_index = input("Enter area index. 1: rectangle, 2: triangle, 3: circle: ")
    match area_index:
        case "1":
            print(area.rectangle(int(input("Enter side a: ")), int(input("Enter side b: "))))
        case "2":
            print(area.triangle(int(input("Enter height: ")), int(input("Enter side: "))))
        case "3":
            print(area.circle(int(input("Enter radius: "))))
        case _:
            print("Figure index is not valid!")
     

if __name__ == "__main__":
    main()