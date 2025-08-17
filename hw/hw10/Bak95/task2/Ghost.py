import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost = Ghost()
print("Колір привида:", ghost.color)
