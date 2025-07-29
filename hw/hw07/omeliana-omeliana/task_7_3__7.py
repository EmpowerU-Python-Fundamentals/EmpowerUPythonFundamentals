def solution(number):
    """Multiples of 3 or 5"""
    if number < 0:
        return 0
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum