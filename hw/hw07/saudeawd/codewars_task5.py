def reverse(st):
    st = st.strip().split()
    reversed_lst = list(reversed(st))
    return ' '.join(reversed_lst)
print(reverse('Hello World'))