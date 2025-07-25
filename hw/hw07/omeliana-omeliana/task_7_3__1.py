def greet(name):
    """Jenny's secret message"""
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)