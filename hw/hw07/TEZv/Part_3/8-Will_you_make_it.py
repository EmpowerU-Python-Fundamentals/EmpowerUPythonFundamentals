def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <=  mpg * fuel_left if True else False

print(zero_fuel(50, 25, 2))  # Output: True
print(zero_fuel(100, 50, 1))  # Output: False