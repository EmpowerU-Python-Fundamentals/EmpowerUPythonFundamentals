def count_sheeps(sheep):
    """
    Function counts the number of sheep present in the array (true means present)
    """
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count


#Test:
print(count_sheeps([True,  True,  True,  False, True, True, True, True, True, False, True,
                    False, True, False, False, True, True,  True,  True,  True, False, False, True,  True ]))