class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

# Example usage
humans = God()
print(isinstance(humans[0], Man))    # True
print(isinstance(humans[1], Woman))  # True
print(isinstance(humans[0], Human))  # True
print(isinstance(humans[1], Human))  # True