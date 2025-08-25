class InvalidNumber(Exception):
    pass


days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}


def check_number(number):
    try:
        number = int(number)
        if number in days:
            print(days[number])
        elif number >= 8 or number <= 0:
            raise InvalidNumber("Entered number must be from 1 to 7.")
    except ValueError:
        print("You've entered non-numerical data.")
    except InvalidNumber as e:
        print(e)


number = input("Enter a number: ")
check_number(number)