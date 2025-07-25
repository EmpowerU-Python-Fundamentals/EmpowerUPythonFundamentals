def calculate_of_char(word):
    d = {}
    for w in word:
        d[w] = d.get(w, 0) + 1
    return d