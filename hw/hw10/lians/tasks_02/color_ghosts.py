from random import randint

class Ghost():
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = self.colors[randint(0, 3)]
        
        
    # def __init__(self):
    #     self.color = random.choice(["white", "yellow", "purple", "red"])
        