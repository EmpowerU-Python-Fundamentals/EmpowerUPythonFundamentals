#XI. Counting sheep

def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

