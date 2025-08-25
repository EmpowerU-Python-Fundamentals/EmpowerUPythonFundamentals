class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def creation():
    return [Man(), Woman()]

humans = creation()
print("Створено людину типу:", type(humans[0]).__name__)
print("Створено людину типу:", type(humans[1]).__name__)
