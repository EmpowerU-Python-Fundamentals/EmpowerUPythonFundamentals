def solution(number):
    a = 0
    i = 0
    if number <= 0:
        a = 0
    else:
        while i < number:
            if i % 3 == 0 and i % 5 == 0:
                a = a + i
            elif i % 3 == 0:
                a = a + i
            elif i % 5 == 0:
                a = a + i
            i += 1
    number = a
    return number