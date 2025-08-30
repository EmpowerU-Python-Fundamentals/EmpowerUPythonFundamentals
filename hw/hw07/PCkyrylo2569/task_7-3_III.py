def no_yell(text):

    words = text.split()
    words = [word.lower() for word in words]
    words[0] = words[0].capitalize()
    return " ".join(words)

print(no_yell('HELLO CAN YOU HEAR ME'))
print(no_yell('now     THIS is REALLY interesting'))
print(no_yell('THAT was EXTRAORDINARY!   '))