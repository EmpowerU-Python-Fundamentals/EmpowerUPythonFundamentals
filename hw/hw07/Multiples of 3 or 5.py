def solution(number):
    if number > 0:
        lst = list(range(1,number))
        print(lst)
        mult = []
        for l in lst:
            if l % 3 == 0 or l % 5 == 0:
                mult.append(l)
        return sum(mult)
    else:
        return 0
