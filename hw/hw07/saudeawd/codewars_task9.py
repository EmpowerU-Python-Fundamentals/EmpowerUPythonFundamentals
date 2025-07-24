def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return f'{name} plays banjo'
    return f'{name} does not play banjo'
print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("Rikke"))