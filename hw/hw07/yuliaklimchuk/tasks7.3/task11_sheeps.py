# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    sum = 0
    for i in sheep:
        if i:
            sum += 1
    return sum
