import re

def is_valid_password(password):
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_character = re.search(r"[$#@]", password)
    valid_len = 6 <= len(password) <= 16
    
    if bool(has_lower and has_upper and has_digit and has_character and valid_len):
        return "Your password is valid!"
    else:
        return "Your password is not valid"

    
password = input("Enter your password to check its validity: ")
print(is_valid_password(password))
    
    
#version with feedback

# def is_valid_password(password):
#     errors = []

#     if len(password) < 6:
#         errors.append("Password must be at least 6 characters.")
#     if len(password) > 16:
#         errors.append("Password must not be more than 16 characters.")
#     if not re.search(r"[a-z]", password):
#         errors.append("Password must include at least one lowercase letter.")
#     if not re.search(r"[A-Z]", password):
#         errors.append("Password must include at least one uppercase letter.")
#     if not re.search(r"\d", password):
#         errors.append("Password must include at least one digit.")
#     if not re.search(r"[$#@]", password):
#         errors.append("Password must include at least one special character: $, #, or @.")

#     if errors:
#         return "Your password is not valid:\n- " + "\n- ".join(errors)
#     else:
#         return "Your password is valid!"


# password = input("Enter your password to check its validity: ")
# print(is_valid_password(password))
