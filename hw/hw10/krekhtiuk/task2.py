class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        return f"Welcome {self.name}"
    
    @classmethod
    def class_method(cls):
        return "Species: Homosapiens"


    @staticmethod
    def static_method():
        return "I don`t know what to write"
