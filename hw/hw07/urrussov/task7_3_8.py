def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Determines if you can reach the fuel pump with the remaining fuel.
    """
    if distance_to_pump <= (mpg*fuel_left):
        return True
    else:
        return False