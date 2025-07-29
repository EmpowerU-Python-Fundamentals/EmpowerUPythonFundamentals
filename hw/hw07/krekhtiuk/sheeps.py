def count_sheeps(sheeps):
    return sum(1 for sheep in sheeps if sheep is True)
print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))