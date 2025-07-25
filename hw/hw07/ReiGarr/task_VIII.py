def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
print(are_you_playing_banjo("Bob"))
print(are_you_playing_banjo("Rose"))