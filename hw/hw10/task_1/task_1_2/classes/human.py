class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."
    
    def info(self):
        return f"{self.name} is a speicies of 'Homosapients'"
    
    def __str__(self):
        return f"Human(name={self.name})"
    
    @staticmethod
    def message():
        return "This is a static method in the Human class."