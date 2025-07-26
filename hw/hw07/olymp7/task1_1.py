a = input("First number: ")
b = input("Second number: ")

def large_num(a, b):
    '''Return largest number of two numbers'''
    if a > b:
        print(a)
    else:
        print(b)

large_num(a, b)