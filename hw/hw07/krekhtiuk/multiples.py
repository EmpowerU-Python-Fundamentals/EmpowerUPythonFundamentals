def solution(number):
    if number < 0:
        return 0
    else:
        return sum(x for x in range(number) if x%3 == 0 or x%5 == 0)
print(solution(9))
print(solution(-5))
    