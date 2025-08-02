import random

class Ghost:
    def __init__(self):
        self.color = self.random_color()

    def random_color(self):
        colors = ['white', 'yellow', 'purple', 'red']
        return random.choice(colors)

    def __str__(self):
        return f'Ghost color: {self.color}'