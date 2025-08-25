def the_largest_number(num1, num2):
    '''Returns the largest number of two numbers'''
    if num1 >= num2:
        return num1
    else:
        return num2

print(the_largest_number(1, 5))
print(the_largest_number(10, 4))
print(the_largest_number(7, 7))
print(the_largest_number(-1, -5))
print(the_largest_number(0, 0))