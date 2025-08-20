while True:
    try:
        age = int(input('Enter your age: '))
    except ValueError:
        print('Your age should be a natural number')
        continue
    if age < 1:
        print('Your age should be a natural number')
        continue
    if age % 2:
        print('Your age is odd number')
    else:
        print('Your age is even number')
    break
