def max2(a, b):
    '''return max number of two numbers'''
    res = a
    if b>= res:
        res = b
    print (f"{a}, {b} max =",res)
    return res

max2(8,6)