def num(st):
    d={}
    for i in st:
        d[i]=d.get(i,0)+1
    return d

st=input("Cтрока: ").lower()
print(num(st))