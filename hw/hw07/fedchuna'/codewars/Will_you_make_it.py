def zero_fuel(distance_to_pump, mpg, fuel_left):
    fd = mpg * fuel_left
    if distance_to_pump <= fd:
        return True
    else:
        return False