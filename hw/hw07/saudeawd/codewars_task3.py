def filter_words(st):
    sett = set()
    st = st.strip().split()
    corrected = [item.lower() for item in st]
    for elem in corrected:
        if elem in sett:
            corrected.remove(elem)
        else:
            sett.add(elem)
    return (' '.join(corrected)).capitalize()

print(filter_words('HELLO world!'))