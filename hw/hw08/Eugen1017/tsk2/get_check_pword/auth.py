from .validate_pass import validate_password

@validate_password
def authorize_user(password):
    print("Authorize user")
    return 0

def main():
    pass_word = input("Enter password: ")
    authorize_user(pass_word)
    return 0

if __name__ == "__main__":
    main()