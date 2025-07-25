def count_sheep(sheep):
    return sum(1 for s in sheep if s is True)
