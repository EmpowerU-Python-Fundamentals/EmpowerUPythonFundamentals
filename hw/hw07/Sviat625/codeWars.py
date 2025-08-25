#1
def greet(name):
    return "Hello, my love!" if name.lower() == "johnny" else f"Hello, {name}!"

#2
from math import sqrt

def distance(point1, point2):
    print()
    print(f"Distance between points: {sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2):.2f}\n")
def coordinates():
    return tuple(map(float, input("Enter coordinates (x, y): ").strip().split(',')))

while True:
    try:
        point1 = coordinates()
        point2 = coordinates()
        distance(point1, point2)
        break
    except (ValueError, IndexError):
        print("\n>>>>>>>             Invalid input              >>>>>>>\n>>>>>>>   Please enter numeric X & numeric Y   >>>>>>>\n")
#3
def filter_words(no_yelling):
    return " ".join(no_yelling.split()).capitalize()

#4
def number_to_string(num):
    return str(num) if isinstance(num, (int, float)) else print("Enter a number to function")


#5
def reverse(st):
    st = " ".join(st.split()[::-1])
    return st

#6
def reverse_list(lst):
    return lst[::-1]

#7
def sum_mult_3_or_5(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#8
def get_to_pump():
    while True:
        try:
            distance = float(input("\nEnter distance to the pump (in miles):                  "))
            mpg = float(input("Enter your car's fuel efficiency (in miles per gallon): "))
            fuel = float(input("Enter the amount of fuel in your tank (in gallons):     "))
            print()
            if mpg * fuel < distance:
                print("\n>>>>>>>>>>>       Sorry. Not enough fuel to reach the pump       >>>>>>>>>>>>\n")
            else:
                print(f'Congratulations! You can reach the pump. Your distance: {mpg * fuel} km \n')
        except ValueError:
            print("\n>>>>>>>>>>>       Invalid input       >>>>>>>>>>>>\n>>>>>>>>>>>   Please enter numeric values   >>>>>>>>>>>>\n")
            continue

        return mpg * fuel >= distance

get_to_pump()

#9
def banjo_check():
    name = input("Enter your name: ")
    if not isinstance(name, str):
        return "Invalid input: name must be a string"
    else:
        print(f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo")

banjo_check()

#10
def bool_to_word(boolean: bool) -> str:
    return "Yes" if boolean else "No"

#11
def count_sheeps(sheep):
    return sum(1 for i in sheep if i)

flock_of_sheep = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True]
print(f"Number of sheep: {count_sheeps(flock_of_sheep)}")

#12
def correct_tail(body, tail):
    return 1 if body[-len(tail):] == tail else 0
