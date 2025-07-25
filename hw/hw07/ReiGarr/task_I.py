def can_reach_pump(distance_to_pump, mpg, gallons_left):
    max_distance = mpg * gallons_left
    return max_distance >= distance_to_pump

print(can_reach_pump(50, 25, 1))
print(can_reach_pump(50, 25, 3))