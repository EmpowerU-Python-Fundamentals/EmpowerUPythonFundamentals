class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

creation = God()
print(isinstance(creation[0], Man))
print(isinstance(creation[1], Woman))
print(isinstance(creation[0], Human))
print(isinstance(creation[1], Human)) 
