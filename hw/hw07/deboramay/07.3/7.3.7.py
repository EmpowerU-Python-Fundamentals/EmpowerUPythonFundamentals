def solution(number):
    """
    Returns the sum of all natural numbers below n that are multiples of 3 or 5.
    If n is negative, returns 0.
    """
    if number < 0:
        return 0

    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

#Test:
print(solution(10))
print(solution(5))
print(solution(6))
print(solution(65))