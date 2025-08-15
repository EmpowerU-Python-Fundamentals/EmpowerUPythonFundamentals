def input_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        return "Your age is even" if age % 2 == 0 else "Your age is odd"
    except ValueError as e:
        return str(e)
            
print(input_age())  