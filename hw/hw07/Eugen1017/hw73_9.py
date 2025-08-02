def are_you_playing_banjo(name):
    match name[0].lower():
        case "r":
            return name + " plays banjo"
        case _:
            return name + " does not play banjo"
