import random

def hello():
    print("\t\t Hello, let's test your luck.")
    print("="*59)
    print("\t\t Gess a number, from 1 to 100")
    print("="*59)
    print("\t\t\t Good luck")
    print("="*59)


def gess_number():
    random_number = random.randint(1,100)
    try_number = 10

    while True:
        print(f"You have {try_number} atempts")
        print("="*59)
        input_number = int(input("Enter a number "))
        difference = abs(input_number - random_number)
        percent = difference / random_number
        
        if input_number == random_number:
            
            print("\t\t You guessed it")
            print("="*59)
            break
        if percent > 0.75:
            print("Too cold")
        elif percent > 0.5:
            print("Cold")
        elif percent > 0.25:
            print("Warmer")
        elif percent > 0.1:
            print("Hot")
        elif percent > 0.05:
            print("Very hot")
        else:
            print("You're almost there!")
         
        try_number -= 1
        
        if try_number == 0:
            print("Game over")
            return
            

def game():
    hello()
    gess_number()

game()