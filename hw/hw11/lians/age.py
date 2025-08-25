class NegativeNumberError(Exception):
    pass


def main():
    age = input("Enter your age: ")
    try:
        age = int(age)
        if age < 0:
            raise NegativeNumberError()
    except (ValueError, TypeError):
        exit("What you've entered is not valid. Please, use only integers.")
    except NegativeNumberError:
        exit("Incorrect age.")
    
    check_age(age)


def check_age(age):
    if age % 2:
        print("Your age is odd.")
    else:
        print("Your age is even.")
     

if __name__ == "__main__":
    main()