import random
num_random = random.randint (1,100)
#print (num_random)

def game_random():
    attempt = 10
    steps = 0
    while attempt>0:
        num=int(input("Число: "))
        attempt -= 1
        steps += 1
        if int(num_random)<num:
            print("Меньше")
        elif int(num_random)>num:
            print("Більше")
        else:
            return f"Вгадали за {steps} ходов"
    return f"У вас було {steps} спроб вгадати. Ви програли. Число було: {num_random}"


if __name__=="__main__":
    print(game_random())