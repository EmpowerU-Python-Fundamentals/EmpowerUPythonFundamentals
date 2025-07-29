def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Will you make it?"""
    return True if mpg*fuel_left >= distance_to_pump else False
