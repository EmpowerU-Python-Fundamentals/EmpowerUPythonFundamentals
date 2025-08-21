import random

class Ghost:

    def __init__(self):
        self.color = random.choice(['white','red','purple','yellow'])

g = Ghost()
print(g.color)