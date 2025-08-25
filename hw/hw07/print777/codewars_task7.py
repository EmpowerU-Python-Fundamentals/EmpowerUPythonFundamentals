#VII. Multiples of 3 or 5

def solution(n):
    if n < 0:
        return 0
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
print(solution(10))   
print(solution(0))    
print(solution(-5))  
print(solution(20))

