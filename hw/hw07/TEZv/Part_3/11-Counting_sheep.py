def count_sheeps(sheep):
    sum = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            sum += 1
        else:
            sum += 0
    return sum

print(count_sheeps([True, True, False, True, False, True]))  # Output: 4
print(count_sheeps([True, False, True, False, True]))  # Output: 3
print(count_sheeps([False, False, False]))  # Output: 0