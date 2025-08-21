try:
    number = int(input("Enter a number: "))
    match number:
        case 1:
            print("1 is Monday")
        case 2:
            print("2 is Tuesday")
        case 3:
            print("3 is Wednesday")
        case 4:
            print("4 is Thursday")
        case 5:
            print("5 is Friday")
        case 6:
            print("6 is Saturday")
        case 7:
            print("7 is Sunday")
        case _:
            print("Invalid number (must be between 1 and 7)")
except ValueError:
    print("Error: Please enter a valid integer.")