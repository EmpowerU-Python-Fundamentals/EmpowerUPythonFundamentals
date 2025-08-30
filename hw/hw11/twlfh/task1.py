def user_age():
    try:
        age = int(input('Enter your age:'))
        res = ex(age)
        return res
    except ValueError as e:
        return e

def ex(age):
    if age < 0:
        raise ValueError ('Your age is negative?')
    elif age %2 == 0:
        return 'Your age is even.'
    else:
        return 'Your age is odd.'



print(user_age())