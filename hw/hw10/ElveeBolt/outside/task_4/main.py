class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def get_info(self):
        return f"{self._name} age is {self._name}"

    def get_info_method(self):
        return f"{self._name} age is {self._age}"


if __name__ == '__main__':
    person = Person("ElveeBolt", 20)
    print(person.get_info)
    print(person.get_info_method())