

class Human:


    def __init__(self, name):
        self.name = name


    def hello(self):
        return f"Hello {self.name}."


    @classmethod
    def homosapiens_info(cls):
        return "Humans or modern humans belong to the biological" \
            " family of great apes, characterized by hairlessness," \
            " bipedality, and high intelligence."
    

    @staticmethod
    def static_info():
        return "Humans are the only living species of the genus Homo."
    


if __name__ == "__main__":
    human = Human("Alice")
    print(human.hello())
    print(Human.homosapiens_info())
    print(Human.static_info())