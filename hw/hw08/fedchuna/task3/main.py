from input_choise import get_user_choice
from calculate import calculate_area

def main():
    choice, *dimensions = get_user_choice()
    tipe, area = calculate_area(choice, *dimensions)
    print(f"The area of the {tipe} is: {area} m²")

if __name__ == "__main__":
    main()