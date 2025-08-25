"""My way of solving task 2"""
import random


class Ghost:
    """Base class: Ghost"""

    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
