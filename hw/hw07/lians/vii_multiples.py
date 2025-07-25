def solution(number):
    sum_multiples = 0
    if number >= 0:
        multiples = [n for n in range (1, number) if n % 3 == 0 or n % 5 == 0]
        sum_multiples = sum(multiples)
    return sum_multiples
