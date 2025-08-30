def check_odd_even(number):
    try:
        num = int(number)
        if num % 2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except (ValueError, TypeError):
        return "You entered not a number."

print(check_odd_even(15))
# =========================================


class MyError(Exception):
    pass

def check_positive(number):
    try:
        num = float(number)
        if num >= 0:
            return f"You input positive number: {num}"
        else:
            return MyError(f"You input negative number: {num}. Try again.")
    except ValueError:
        return "Error type: ValueError!"
# =========================================


while True:
    try:
        age = int(input())   
        check_age(age)       
        print(age)           
        break                
    except:
        continue
# =========================================


class InputError(Exception):
    def __init__(self, data):
        self.data = data

def check(text):
    if not isinstance(text, str):
        raise InputError("Type text error")
    if len(text) < 3:
        raise InputError("Short text error")
    if len(text) > 15:
        raise InputError("Long text error")
    return True

# =========================================



def divide(numerator, denominator):
    try:
        result = numerator / denominator
        return f"Result is {result}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except TypeError:
        return "Value Error! You did not enter a number!"
# =========================================


import re

def check(login):
    login_lower = login.lower()

    pattern = r"^(admin|employee)(-?\d+|id\d+|-id\d+)$"

    if re.match(pattern, login_lower):
        return True
    else:
        raise ValueError(f"incorrect login '{login}'")
# =========================================
