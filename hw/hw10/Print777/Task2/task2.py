#II. Color-ghost

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost1 = Ghost()
ghost2 = Ghost()

print(ghost1.color)  # Output: "white" or "yellow" or "purple" or "red"
print(ghost2.color)  # Output: "white" or "yellow" or "purple" or "red"
