class MyError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data
    

def age_verification(age):
    if age < 0:
        raise MyError("Error! Age cannot be a negative number!")
    

def user_age():
    while True:
        try:
            age = int(input("Enter your age \n"))
            age_verification(age)
            break
        except MyError as e:
            print(e.data)
        except (ValueError, TypeError):
            print ("Input error. Please enter a number.")


user_age()