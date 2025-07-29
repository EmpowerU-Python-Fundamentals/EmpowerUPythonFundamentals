def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!".format(name=name)

print(greet('Johnny'))
print(greet('Anastasia'))
