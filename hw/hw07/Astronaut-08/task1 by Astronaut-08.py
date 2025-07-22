'''homework by Astronaut-08'''

def largest_num(a: int, b: int):
    'The function acces two integer numbers and returns the largest'
    if type(a) in (float, str) or type(b) in (float, str):
        return 'Wrong type, please put integer number'
    if a > b:
        return a
    else:
        return b
