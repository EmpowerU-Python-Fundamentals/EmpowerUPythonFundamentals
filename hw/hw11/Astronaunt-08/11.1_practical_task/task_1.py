'''This is DOC for task_1'''
class NegativeError(Exception):
    '''This is DOC for my Excep.'''
    def __str__(self):
        return 'NegativeError: input the negative number!'

def check_age(age):
    '''This is DOC for check func.'''
    try:
        age = int(age)
        if age > 0 and age % 2 == 0:
            return 'Even'
        elif age > 0 and age % 2 == 1:
            return 'Odd'
        else:
            raise NegativeError()
    except ValueError as valerr:
        return f'{valerr} is not a num, pls enter the number'
    except NegativeError as neerr:
        return neerr

print(check_age(input('Введи значення свого віку: ')))
