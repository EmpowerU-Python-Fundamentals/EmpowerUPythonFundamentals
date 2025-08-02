"""random color"""
import random
class Ghost(object):
    """color ghost"""
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)
