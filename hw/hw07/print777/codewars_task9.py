#IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    print(are_you_playing_banjo("Roman"))
    print(are_you_playing_banjo("Andrew"))

