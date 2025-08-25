# Color Ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute 
#   of "white" or "yellow" or "purple" or "red" when instantiated

from random import randint

class Ghost(object):
    COLORS = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = __class__.COLORS[randint(0, 3)]