import library as tasks

# tasks part 1
def part_1():
    task = int(input("Enter a task number (1 - 3): "))

    match task:
        case 1:
            print("Executing Task 1 (largest digit between two numbers):")
            print("--------------------------")
            a = int(input('Enter first number: '))
            b = int(input('Enter second number: '))
            tasks.task_p1_1(a=a, b=b)
            print("=======================")
        case 2:
            print("Executing Task 2 (area of figures):")
            print("--------------------------")
            a = int(input('Enter side: '))
            h = int(input('Enter height: '))
            tasks.task_p1_2(a=a, h=h)
            print("=======================")
        case 3:
            print("Executing Task 3 (calculates the number of cgarecters):")
            print("--------------------------")
            word = input('Enter the word: ')
            tasks.task_p1_3(word=word)
            print("=======================")
        case _:
            print("Invalid task number. Please enter 1, 2, or 3.")
            part_1()
            print("=======================")

# tasks part 2
def part_2():
    task = int(input("Enter a task number (1 - 12): "))
    match task:
        case 1:
            name=input("Enter name: ")
            tasks.task_p2_1(name)
        case 2:
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))
            tasks.task_p2_2(x1, y1, x2, y2)
        case 3:
            string = input("Enter a string: ")
            tasks.task_p2_3(string)
        case 4:
            number = int(input("Enter a number: "))
            tasks.task_p2_4(number)
        case 5:
            string = input("Enter a string: ")
            tasks.task_p2_5()
        case 6:
            list_input = input("Enter a list of numbers separated by spaces: ")
            list_input = list(map(int, list_input.split()))
            tasks.task_p2_6(list_input)
        case 7:
            number = int(input("Enter a number: "))
            tasks.task_p2_7(number)
        case 8:
            distance_to_pump = input("Enter distance to pump: ")
            mpg = input("Enter miles per gallon: ")
            fuel_left = input("Enter fuel left: ")
            tasks.task_p2_8(distance_to_pump, mpg, fuel_left)
        case 9:
            name = input("Enter a name: ")
            tasks.task_p2_9()
        case 10:
            boolean = input("Enter a boolean value (True/False): ")
            boolean = boolean.lower() == 'true'
            tasks.task_p2_10()
        case 11:
            tasks.task_p2_11()
        case 12:
            body = input("Enter the body: ")
            tail = input("Enter the tail: ")
            tasks.task_p2_12(body, tail)
        case _:
            print("Invalid task number. Please enter a number between 1 and 12.")
            part_2()

