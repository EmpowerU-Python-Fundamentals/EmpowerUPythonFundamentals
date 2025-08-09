import random

class Ghost(object):
    """
    Color-ghost
    """
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])