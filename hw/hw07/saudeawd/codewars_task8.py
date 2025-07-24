def zero_fuel(distance_to_pump, mpg, fuel_left):
    if (mpg * fuel_left) >= distance_to_pump:
        return True
    else:
        return False
print(zero_fuel(50, 25, 2))