from inp_pass import input_pass
from validation import validate_password

def main():
    password = input_pass()
    is_valid, message = validate_password(password)
    print(message)



if __name__ == "__main__":
    
    main()
    