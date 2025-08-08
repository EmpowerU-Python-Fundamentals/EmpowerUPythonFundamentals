import re

class AgeError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")

    return f"Your age is {"odd" if age % 2 else "even"}."

def main():
    while True:
        user_age = input("Enter your age: ")
        if not re.match(r"^[+-]?\d+$", user_age):
            print("Please enter a numeric value")
            continue
        try:
            print(check_age(int(user_age)))
            return
        except AgeError as e:
            print(e.msg)
            continue


if __name__ == "__main__":
    main()