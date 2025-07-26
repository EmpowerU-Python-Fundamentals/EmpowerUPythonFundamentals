def reverse(st):
    words = [word for word in st.split() if word]

    rev = words[1] + ' ' + words[0]

    return rev