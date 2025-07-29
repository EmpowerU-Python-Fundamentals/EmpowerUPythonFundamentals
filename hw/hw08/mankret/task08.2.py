import re


def validate_password(password):
    """
    Function checks:
    1. At least 1 letter bentween [a-z] and 1 letter between [A-Z]
    2. At least 1 number bentween [0-9]
    3. At least 1 character from [$#@]
    4. Minimum length 6 characters
    5. Maximum length 16 characters

    """

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"

    if re.fullmatch(pattern, password):
        return True
    else:
        return False


# # --- Tests ---
# print(f"Test@123: {validate_password('Test@123')}")
# print(f"test@123: {validate_password('test@123')}")
# print(f"TEST@123: {validate_password('TEST@123')}")
# print(f"Test@abc: {validate_password('Test@abc')}")
# print(f"Test1234: {validate_password('Test1234')}")
# print(f"T@1: {validate_password('T@1')}")
# print(f"LongPassword12345678@: {validate_password('LongPassword12345678@')}")
# print(f"Abc@1: {validate_password('Abc@1')}")
# print(f"Abc@1234567890: {validate_password('Abc@1234567890')}")

input_from_user = input("Enter password : ")

print(validate_password(input_from_user))
