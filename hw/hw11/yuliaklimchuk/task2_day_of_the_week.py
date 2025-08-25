class MyError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data
    

def day_verification(day):
    if day < 1 or day > 7:
        raise MyError("Error! Enter a number from 1 to 7")
    

def day_of_the_week():
    while True:
        try:
            day_number = int(input("Enter the day of the week number \n"))
            day_verification(day_number)
            break
        except MyError as e:
            print(e.data)
        except (ValueError, TypeError):
            print ("Input error. Please enter a integer number.")

    match(day_number):
        case 1: 
            print(f"{day_number} is Monday")
        case 2: 
            print(f"{day_number} is Tuesday")
        case 3: 
            print(f"{day_number} is Wednesday")
        case 4: 
            print(f"{day_number} is Thursday")
        case 5: 
            print(f"{day_number} is Friday")
        case 6: 
            print(f"{day_number} is Saturday")
        case 7: 
            print(f"{day_number} is Sunday")


day_of_the_week()