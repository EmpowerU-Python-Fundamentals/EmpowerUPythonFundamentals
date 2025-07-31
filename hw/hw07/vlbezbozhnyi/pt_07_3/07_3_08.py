def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Determines if there is enough fuel to reach the destination.
    """
    return distance_to_pump <= mpg * fuel_left
