# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

import random

class Ghost(object):
    colors = [ "white","yellow","purple", "red"]
    def __init__(self):
        random_number = random.randint(0, len(Ghost.colors)-1)
        self.color = Ghost.colors[random_number]