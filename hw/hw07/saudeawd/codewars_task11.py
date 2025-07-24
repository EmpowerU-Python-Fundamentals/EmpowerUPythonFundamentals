def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item is True:
            count += 1
    return count
print(count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]))