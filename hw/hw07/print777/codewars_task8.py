#VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump
print(zero_fuel(50, 25, 2)) 
print(zero_fuel(100, 25, 3))

