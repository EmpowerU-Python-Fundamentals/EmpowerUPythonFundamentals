def solution(number):
    sum = 0 
    if number <= 0:
        sum = 0
    for n in range(number):
        if n%3==0 or n%5==0:
            sum+=n
    return sum
  