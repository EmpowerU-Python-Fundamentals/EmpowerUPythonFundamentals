class NegativeAgeError(Exception):
    """Custom exception for negative age values."""
    pass

def enter_age():
    while True:
        age = input('Enter your age: ')
        try:
            age = int(age)
            if age < 0:
                raise NegativeAgeError("Your age can't be negative")
            else:
                if age % 2 == 0 :
                    print(f'{age} is an even number.')
                else:
                    print(f'{age} is an odd number.')
                break
        except NegativeAgeError as e:
            print(f"Error: {e}. Please enter a valid age.")
        except ValueError:
            print("Invalid input: please enter a number.")

if __name__ == '__main__':
    enter_age()