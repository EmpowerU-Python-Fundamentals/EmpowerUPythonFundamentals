def are_you_playing_banjo(name):
    a = str(name).lower()
    a = a[0:1]
    if a == 'r':
        return print(f"{name} plays banjo")
    else:
        return print(f"{name} does not play banjo")

are_you_playing_banjo("Rark")
