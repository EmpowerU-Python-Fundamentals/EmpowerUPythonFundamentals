# Your task is to complete this Class,
#   the Person class has been created.
# You must fill in the Constructor method
#   to accept a name as string and an age as number,
#   complete the get Info property and getInfo method/Info getter
#   which should return 'johns age is 34'

class Person:
    def __init__(self, name: str, age: int):
        self._name_ = name
        self._age_ = age
    
    @property
    def info(self):
        return f"{self._name_}s age is {self._age_}"
    