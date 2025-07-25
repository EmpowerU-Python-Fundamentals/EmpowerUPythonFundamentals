def get_distance(a: tuple, b: tuple) -> float:
    return ((b[0] - a[0])**2 + (b[1] - b[0])**2)**0.5

distance = get_distance(a=(1, 3), b=(4, 5))
print(distance)