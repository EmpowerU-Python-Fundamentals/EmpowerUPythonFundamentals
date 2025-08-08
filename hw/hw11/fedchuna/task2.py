### 2. Напишите программу, которая анализирует введенное число и, в зависимости от числа, выдает день недели, соответствующий этому числу (1 - понедельник, 2 - вторник и т. д.). Учтите случаи ввода чисел от 8 и более, а также случаи ввода нечисловых данных.

def day_of_week(day_number):
    match day_number:
        case 1:
            return "monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "friday"
        case 6:
            return "saturday"
        case 7:
            return "sunday"
        case _:
            raise ValueError("Number must be between 1 and 7.")
        
while True:
    try:
        user_input = int(input("Enter numerical number of the day of the week (1-7): "))
        print(f"Today is {day_of_week(user_input)}")
        break
    except ValueError as e:
        print(f"Error inpt data is not a number: {e}")
