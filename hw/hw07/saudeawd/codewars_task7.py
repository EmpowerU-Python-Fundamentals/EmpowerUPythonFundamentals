def solution(number):
    count = 0
    if number > 0:
        for i in range(number):
            if (i % 3 == 0) or (i % 5 == 0):
                count += i
        return count
    else:
        return 0
print(solution(4))