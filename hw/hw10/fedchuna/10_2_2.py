import random
class Ghost(object):
        def __init__(self):
            colors = ["white", "yellow", "purple", "red"]
            self.color = random.choice(colors)