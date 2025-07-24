def calc_multiplies(max_number: int) -> int:
    sum_ = 0
    if max_number <= 0:
        return 0

    for i in range(1, max_number):
        if i % 3 == 0 or i % 5 == 0:
            sum_ += i

    return sum_


sum_ = calc_multiplies(10)
print(sum_)