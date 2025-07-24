def check_play(name: str) -> None:
    name = name.lower()
    if name[0] == 'r':
        print(f"{name} plays banjo")
    else:
        print(f"{name} does not play banjo")

check_play("Sergio")
check_play("Roman")