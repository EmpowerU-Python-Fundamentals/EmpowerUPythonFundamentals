def count_sheep(sheeps: list[bool]) -> str:
    count = 0
    for sheep in sheeps:
        if sheep:
            count += 1
    return count


sheeps = count_sheep(
    [
        True, True, True, False,
        True, True, True, True,
        True, False, True, False,
        True, False, False, True,
        True, True, True, True,
        False, False, True, True
    ]
)
print(sheeps)
