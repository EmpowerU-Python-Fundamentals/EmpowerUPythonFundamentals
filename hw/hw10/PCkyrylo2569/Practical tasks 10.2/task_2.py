import random
class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost1 = Ghost()
ghost2 = Ghost()

print(ghost1.color)
print(ghost2.color)