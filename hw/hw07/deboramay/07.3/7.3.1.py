#Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)



#Tests:

print(greet("Jane"))
print(greet("Jim"))
print(greet("James"))
print(greet("Johnny"))