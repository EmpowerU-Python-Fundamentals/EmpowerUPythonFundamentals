def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

print(count_sheeps([True, True, True, False,
                    True, False, True, True,
                    False, True, False, True,
                    True, True, False]))
print(count_sheeps([True, True, 1, False, True,
                    "z", True, True, False,
                    True, False, 0, True,
                    True, False]))
print(count_sheeps([True,  True,  True,  False,
                    True,  True,  True,  True ,
                    True,  False, True,  False,
                    True,  False, False, True ,
                    True,  True,  True,  True ,
                    False, False, True,  True]))