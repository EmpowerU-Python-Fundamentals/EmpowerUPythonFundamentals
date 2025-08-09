def process_age(age):
    if age<0:
        raise ValueError("Age can't be negative")
    elif age%2==0:
        print ("Your age is even.")
    else:
        print ("Your age is odd.")


def main():
    try:
        age = int(input("Enter age: \n"))
        process_age(age)
    except ValueError:
        print (f"You inputted age in incorrect format.")

if __name__ == "__main__":
    main()