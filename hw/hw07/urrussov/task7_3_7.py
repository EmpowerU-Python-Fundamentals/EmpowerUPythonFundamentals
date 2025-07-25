def solution(number):
    '''Multiples of 3 or 5'''
    total=0
    if number>0:
        for i in range(0,number):
            if i > 0 and (i%3 == 0 or i%5 == 0):
                total+=i
    else:
        return 0
    return total

