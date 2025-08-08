# Counting sheep...

def count_sheeps(sheep):
    sum = 0
    for s in sheep:
        if s == True:
            sum += 1
    return sum