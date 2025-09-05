user_input = input()

def password_validation(password):
    if len(password) >= 6 and len(password) <=16:
        if (any(ch.islower() for ch in password)   
        and any(ch.isupper() for ch in password)   
        and any(ch.isdigit() for ch in password)   
        and any(ch in "$#@" for ch in password)):  
            print("Хороший пароль")
        else:
            print("Поганий пароль")
    else:
        print("Поганий пароль")

password_validation(user_input)