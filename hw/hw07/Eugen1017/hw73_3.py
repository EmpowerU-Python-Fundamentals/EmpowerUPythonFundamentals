def filter_words(st):
    return " ".join((w.strip() for w in st.lower().capitalize().split(" ") if w != ""))
