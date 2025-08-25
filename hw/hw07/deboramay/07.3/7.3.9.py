def are_you_playing_banjo(name):
    """
    Function answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!
    """
    if name[0] == "R" or name[0] == "r":
        result = name + " plays banjo"
    else:
        result = name + " does not play banjo"
    return result


#Test:
print(are_you_playing_banjo("Adam"))
print(are_you_playing_banjo("ruby"))
print(are_you_playing_banjo("james"))
print(are_you_playing_banjo("Ricardo"))