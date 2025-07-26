def count_sheeps(sheep):
    lst = []
    for s in sheep:
        if s is True:
            lst.append(1)
        if s is False:
            lst.append(0)
        if s is None:
            lst.append(0)
    return sum(lst)

