def are_you_playing_banjo(name):
    """
    Determines if a person plays banjo based on their name.
    """
    if name[0] == 'R' or name[0] == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'