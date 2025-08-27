class Human:
    """
    A class representing a human being.
    Contains methods for greeting, determining the species, and a static message.
    """
    def __init__(self, name):
        """
        Constructor for the Human class.
        
        Arguments:
            name (str): The name of the human.
        """
        self.__name = name

    @property
    def name(self):
        """
        A property that allows getting the human's name.
        """
        return self.__name

    @name.setter
    def name(self, name_value):
        """
        A property that allows setting a new name for the human.
        """
        self.__name = name_value

    def greeting(self):
        """
        An instance method that prints a greeting message.
        """
        print(f"Hello, {self.name}!")

    @classmethod
    def get_species(cls):
        """
        A class method that returns the species of the human.
        """
        return "Homosapiens"

    @staticmethod
    def show_default_msg():
        """
        A static method that prints a default message.
        """
        print("This is a default message.")

# Example usage
if __name__ == "__main__":
    leo = Human('Leo')
    
    # Calling the instance method
    leo.greeting()

    # Calling the class method
    print(f"Species of human: {Human.get_species()}")

    # Calling the static method
    Human.show_default_msg()
    
    # Changing the name using the setter
    leo.name = "Olexa"
    leo.greeting()
