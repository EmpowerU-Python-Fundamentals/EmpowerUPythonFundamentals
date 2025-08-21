class IncorrectAge(ValueError):
    pass

def askNatural(msg='Enter a natural number: ', error=ValueError):
    try:
        num = int(input(msg))
        if num > 0:
            return num
        else:
            raise error
    except (error, ValueError):
        return None

def evenOrOdd(num):
    if num % 2:
        return 'odd'
    else:
        return 'even'

def run():
    age = askNatural('Enter your age: ', error=IncorrectAge)
    while not age:
        print('Your age should be a natural number')
        age = askNatural('Enter your age: ', error=IncorrectAge)
    print('Your age is', evenOrOdd(age), 'number')

if __name__ == '__main__':
    run()
