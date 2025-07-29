def hello(name: str = None, is_love: bool = False):
    if name:
        if is_love:
            print(f"Hello, {name}! I love you!")
        else:
            print(f"Hello, {name}!")
    else:
        print("Hello!")

hello()
hello("Steve")
hello("Johny", is_love=True)