class Human:
    """
    A class representing a human being.

    Attributes:
        species (str): The species of the human, default is 'Homosapiens'.
        name (str): The name of the human instance.

    Methods:
        __init__(name):
            Initializes a Human instance with a given name.

        greeting():
            Returns a greeting message including the human's name.

        spec():
            Class method that returns the species of the human.

        random_message():
            Static method that returns a random message.

        __str__():
            Returns a string representation combining the greeting, species, and random message.
    """
    species = 'Homosapiens'
    
    def __init__(self, name):
        self.name = name 
    
    def greeting(self):
        """
        Returns a personalized greeting message using the instance's name.
        """
        return f'Hi, {self.name}, nice to meet you!'
    
    @classmethod
    def spec(cls):
        """
        Returns a string indicating the species of the human.
        """
        return f'You are {cls.species}.'
    
    @staticmethod
    def random_message():
        """
        Returns a random message as a string.
        """
        return 'This is a random message ;)'
    
    def __str__(self):
        return f'{self.greeting()}\n{self.spec()}\n{self.random_message()}'


while True:
    n = input('Write your name: ')
    if n.isalpha():
        break
    else:
        print("You didn't write a valid name. Try again (letters only).")

hum = Human(n)
print(hum)