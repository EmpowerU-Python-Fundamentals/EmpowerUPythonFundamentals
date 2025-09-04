from area_calculator import *

def main():
    print("Choose what type of area you need to calculate: \n" \
    "1. Rectangle\n" \
    "2. Triangle\n" \
    "3. Circle")
    choice = input()
    match choice:
        case "1":
            user_input = input("Enter the two sides of rectangle separated by spaces: ")
            string_parameters = user_input.split()
            try:
                parameters_list = [float(num_str) for num_str in string_parameters]
                print(calculate_area_rectangle(*parameters_list))
            except ValueError:
                print("Invalid input. Make sure you input the numbers separated by spaces.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        case "2":
            user_input = input("Enter the height and side of triangle separated by spaces: ")
            string_parameters = user_input.split()
            try:
                parameters_list = [float(num_str) for num_str in string_parameters]
                print(calculate_area_triangle(*parameters_list))
            except ValueError:
                print("Invalid input. Make sure you input the numbers separated by spaces.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        case "3":
            user_input = input("Enter the radius of circle: ")
            try:
                print(calculate_area_circle(float(user_input)))
            except ValueError:
                print("Invalid input. Make sure you input the number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        case _:
            print("Invalid input. Try again.")


main()