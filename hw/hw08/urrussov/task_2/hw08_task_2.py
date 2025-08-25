import re

condition_checking = {
    "at least 1 letter between a-z": r"[a-z]",
    "at least 1 letter between A-Z": r"[A-Z]",
    "at least 1 number between 0-9": r"[0-9]",
    "at least 1 character[$#@]": r"[$#@]",
    "the lenght from 6 to 16 characters": r"^.{6,16}$"
}


def password_review(new_password):
    """
    Checks the validity of a new password against a set of predefined rules and prints feedback messages.
    """
    approve_conditions_check = []
    for message, rules in condition_checking.items():
        if not re.search(rules,new_password):
            print(f'👎 For new password you need {message}')
            approve_conditions_check.append(0)
        else:
            print(f'👍Your password has {message}')
            approve_conditions_check.append(1)
    return approve_conditions_check


while True:
    checked_password = input('Create new password: ')
    result_of_review = password_review(checked_password)
    flag_approve = sum(result_of_review)
    if flag_approve == 5:
        print(f"Password accepted! Your new password is {checked_password}")
        break
    else:
        print('Try again!')
        continue