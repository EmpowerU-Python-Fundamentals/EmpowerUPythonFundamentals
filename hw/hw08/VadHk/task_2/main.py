from password import *


def main():
    password = input("Enter a password to validate: ")
    
    if is_valid_password(password):
        print(f'Password {password} is valid')
    else:
        print(f'Password {password} is not valid')

if __name__ == "__main__":
    main()