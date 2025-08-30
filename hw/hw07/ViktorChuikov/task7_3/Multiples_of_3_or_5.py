def sol(num):
    if num < 0:
        return 0
    sol = list()
    for i in range(num):
        if 0 < i < num and i % 3 == 0:
            sol.append(i)
        elif 0 < i < num and i % 5 == 0:
            sol.append(i)
        return sum(sol)