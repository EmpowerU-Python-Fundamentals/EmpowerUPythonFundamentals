def num_char(st):
    '''calculates the number of characters included in string'''
    d_res={}
    for char in st:
        d_res[char]=d_res.get(char,0)+1
    return d_res

st=input("Введіть слово: ").lower()
print(num_char(st))