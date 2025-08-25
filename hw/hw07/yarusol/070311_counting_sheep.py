# Consider an array/list of sheep where some sheep
#   may be missing from their place.
# We need a function that counts the number of sheep
#   present in the array (true means present).
#
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

def count_sheeps(sheep: list):
    return sum(filter(lambda s: 1 if s else 0, sheep))