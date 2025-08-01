def count_sheeps(sheep):
    sum = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            sum += 1
        else:
            sum += 0
    return sum