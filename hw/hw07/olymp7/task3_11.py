def count_sheeps(sheep):
    if not sheep:
        return 0
    result = 0
    for i in sheep:
        if i == True:
            result += 1
    print(result)
    return result