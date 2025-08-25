class NegativeNumberException(Exception):
    pass

class ImpossibleNumberException(Exception):
    pass


age = input("Enter age:")

messages = {
    "odd": f"The age {age} is odd",
    "even": f"The age {age} is even",
    "negative": f"The age {age} is negative number",
    "incorrect": f"The age '{age}' is not correct",
    "impossible": "I think it's impossible, but ok"
            }


def data_processing(age):
    try:
        age = int(age)
        if age>100:
            print(messages["impossible"])
        key = "odd"
        if age<0:
            raise NegativeNumberException
        elif age == 0:
            raise Exception
        elif age%2 == 0:
            key = "even"
    except NegativeNumberException:
        key = "negative"
    except:
        key = "incorrect"
    return messages[key]


print(data_processing(age))