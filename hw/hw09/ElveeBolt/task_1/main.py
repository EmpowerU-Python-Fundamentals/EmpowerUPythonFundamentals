import random

secret_number = random.randint(1, 100)
attempts = 10

def main():
    print(f"Choose number from 1 to 100. You have {attempts} attempts.")

    for i in range(1, attempts + 1):
        try:
            number = int(input(f"Attempt {i}: Enter your number: "))
        except ValueError:
            print("Input the number!")
            continue

        if number == secret_number:
            print(f"Hooooray! {secret_number} with {i} attempts.")
            break
        elif number < secret_number:
            print("Number is higher.")
        else:
            print("Number is lower.")
    else:
        print(f"Quak-quak. The number is {secret_number}.")


if __name__ == '__main__':
    main()