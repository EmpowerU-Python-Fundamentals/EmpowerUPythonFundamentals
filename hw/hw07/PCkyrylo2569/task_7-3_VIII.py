def can_you(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump
print(can_you(50, 25, 2))
print(can_you(40, 20, 3))
print(can_you(55, 26, 1))