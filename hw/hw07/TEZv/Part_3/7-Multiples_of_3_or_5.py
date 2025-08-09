def solution(number):
    sum = 0 
    if number <= 0:
        sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

print(solution(10))  # Output: 23
print(solution(20))  # Output: 78