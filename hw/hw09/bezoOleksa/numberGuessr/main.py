import pygame
import random

minNum, maxNum = 1, 100
totalAttempts = 10
attempts = totalAttempts

screen_height = 720
screen_width = 1080
fps = 10

targetNum = random.randint(minNum, maxNum)

pygame.init()
font = pygame.font.SysFont('Verdana', 20, False, False)
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('numberGuessr')
clock = pygame.time.Clock()
userInput = 0
text = ['Welcome to numberGuessr!',
        f'Can you guess the secret number I\'m thinking of? It\'s between {minNum} and {maxNum}!',
        f'You have {attempts} attempts to get it right, so choose wisely. I\'ll give you hints along the way!',
        'Enter your first guess below:',
        '']


def guess(num):
    global attempts, targetNum
    if minNum <= num <= maxNum:
        if num == targetNum:
            attempts = 0
            text.append('Congratulations! You guessed the number correctly!')
        else:
            attempts -= 1
            if attempts > 0:
                if num < targetNum:
                    text.append(f'Your guess is too low. Try a higher number. You have {attempts} attempts left.')
                else:
                    text.append(f'Your guess is too high. Try a lower number. You have {attempts} attempts left.')
                text.append('')
            else:
                text.append(f'Game over! You ran out of attempts. The secret number was {targetNum}.')
        if attempts == 0:
            text.append('Press R to replay the game')
    else:
        text.append(f'Your guess must be a number between {minNum} and {maxNum}.')
        text.append('')


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_0 <= event.key <= pygame.K_9 and attempts > 0:
                userInput = userInput * 10 + event.key - pygame.K_0
            elif event.key == pygame.K_RETURN and attempts > 0:
                guess(userInput)
                userInput = 0
            elif event.key == pygame.K_BACKSPACE and attempts > 0:
                userInput = userInput // 10
            elif event.key == pygame.K_r:
                attempts = totalAttempts
                targetNum = random.randint(minNum, maxNum)
                userInput = 0
                text = ['Welcome to numberGuessr!',
                        f'Can you guess the secret number I\'m thinking of? It\'s between {minNum} and {maxNum}!',
                        f'You have {attempts} attempts to get it right, so choose wisely. I\'ll give you hints along the way!',
                        'Enter your first guess below:',
                        '']

    while len(text) > 31:
        text.pop(0)
    if userInput != 0:
        text[-1] = str(userInput)
    if userInput == 0 and attempts > 0:
        text[-1] = ''

    display.fill((20, 20, 20))
    for n in range(len(text)):
        display.blit(font.render('>>> ' + text[n], True, (240, 240, 240)), (2, 2 + 23 * n))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
