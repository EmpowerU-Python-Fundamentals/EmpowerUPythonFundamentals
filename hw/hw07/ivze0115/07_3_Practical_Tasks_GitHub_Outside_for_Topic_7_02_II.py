import math

def distance(p1, p2):
    # Check if both points have the same number of dimensions and are not both empty
    if len(p1) != len(p2) or len(p1) == 0:
        return -1

    # Compute Euclidean distance
    squared_diffs = [(a - b) ** 2 for a, b in zip(p1, p2)]
    return math.sqrt(sum(squared_diffs))
