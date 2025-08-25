from random import choice


class Ghost(object):
    colors = ["white", "yellow", "blue", "red"]

    def __init__(self):
        self.color = choice(colors)
