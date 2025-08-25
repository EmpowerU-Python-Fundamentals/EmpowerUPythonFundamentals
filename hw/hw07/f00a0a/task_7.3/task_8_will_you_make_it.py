def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump

