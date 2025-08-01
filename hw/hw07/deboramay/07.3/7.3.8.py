def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Determines if the car can reach the pump with the remaining fuel.
    """
    return mpg * fuel_left >= distance_to_pump

#Test:
print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))