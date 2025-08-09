def play_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
print(play_banjo("Ringo"))
print(play_banjo("rauf"))
print(play_banjo("Kolin"))