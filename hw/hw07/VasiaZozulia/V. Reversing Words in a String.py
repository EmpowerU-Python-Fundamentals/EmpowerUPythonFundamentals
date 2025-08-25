def reverse(st):
    s = st.strip()
    words = s.split(" ")
    words = words[::-1]
    return " ".join(words)