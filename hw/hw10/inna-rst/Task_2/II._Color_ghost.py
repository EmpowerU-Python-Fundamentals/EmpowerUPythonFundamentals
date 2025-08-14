from random import choice

class Ghost:
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = choice(Ghost.colors)

    def __str__(self):
        return self.color

if __name__ == "__main__":
    ghosts = [Ghost() for _ in range(4)]
    for ghost in ghosts:
       print(ghost)