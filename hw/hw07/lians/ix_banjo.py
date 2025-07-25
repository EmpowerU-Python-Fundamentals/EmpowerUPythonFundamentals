def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name
