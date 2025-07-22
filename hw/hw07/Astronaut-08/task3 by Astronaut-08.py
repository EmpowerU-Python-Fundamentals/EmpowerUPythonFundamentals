'''homework by Astronaut-08'''

def num_of_char(g_str: str):
    '''This func calculate the number of characters included in given string'''
    calc_char = dict()
    for i in g_str:
        if i not in calc_char:
            calc_char[i] = 1
        else:
            calc_char[i] += 1
    return calc_char

print(num_of_char(input('Write a string: ')))
