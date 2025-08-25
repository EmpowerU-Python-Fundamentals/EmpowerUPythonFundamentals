def Are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print(Are_you_playing_banjo("Robert"))
print(Are_you_playing_banjo("Monica"))
