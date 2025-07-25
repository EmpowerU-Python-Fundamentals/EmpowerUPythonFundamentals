def count_sheep(sheep_list):
    return sum(1 for sheep in sheep_list if sheep is True)

sheep = [True, True, True, False,
         True, False, True, True,
         True, False, True, False,
         True, None, None, True,
         True, True, False, True,
         False, False, True, True]

print(count_sheep(sheep))