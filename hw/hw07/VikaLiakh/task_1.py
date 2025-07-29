#TASK1

def largest_number( num1, num2):
    '''This function returns the largest numbers of 2 given numbers'''
    result = num1 if num1 > num2 else num2
    return result
    
print(largest_number(9,2))