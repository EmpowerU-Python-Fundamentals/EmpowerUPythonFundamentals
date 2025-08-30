# Create a decorator that adds a "tag" to a string. The tag will be specified as an argument to the decorator.
def add_tag(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{tag}{result}{tag}"
        return wrapper
    return decorator
# =================================================


# Write a function celsius_to_fahrenheit(temps) using map function whose input parameter 
# is a list of temperatures in Celsius. The function returns new array where temps in Farenheit.
def celsius_to_fahrenheit(temps):
    return list(map(lambda c: (c * 9/5) + 32, temps))
# =================================================


# Write fibonacci_numbers function which returns a generator that yields the Fibonacci sequence.
def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# =================================================


# Write a generator function that returns all combinations of two lists.
def combinations(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)
# =================================================


# Write a list comprehension function celsius_to_fahrenheit(temps) whose input parameter is a 
# list of temperatures in Celsius. The function returns new array where temps in Farenheit.
def celsius_to_fahrenheit(temps):
    return [(c * 9/5) + 32 for c in temps]