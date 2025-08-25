#III. No yelling!

def filter_words(st):
    words = st.split()
    words = [word.lower() for word in words]
    if words:
        words[0] = words[0].capitalize()
        
    return ' '.join(words)
print(filter_words('HELLO CAN YOU HEAR ME'))           
print(filter_words('now THIS is REALLY interesting'))
print(filter_words('THAT was EXTRAORDINARY!'))
