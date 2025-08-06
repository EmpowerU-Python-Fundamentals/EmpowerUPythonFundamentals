        
from random import randint
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

width = 600
height = 600

gameDisplay = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Game - Guess a Number")
font = pygame.font.SysFont('Calibri', 20, True, False)

clock = pygame.time.Clock()
FPS = 60

user_input = ""
message = ""
guessed_number = randint(1, 100)

tries = 10
number_try = 0

running = True
won = False

while running:
    gameDisplay.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.isdigit():
                    user_guess = int(user_input)
                    if user_guess > guessed_number:
                        message = "Guessed number is less"
                    elif user_guess < guessed_number:
                        message = "Guessed number is more"
                    else:
                        message = "Congratulations!"
                        won = True
                        running = False
                    number_try += 1
                    user_input = ""
                else:
                    message = "Enter valid number"
                    user_input = ""

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.unicode.isdigit():
                user_input += event.unicode

    # Display elements
    prompt_text = font.render("Enter number from 1 to 100. Then press Enter.", True, BLACK)
    gameDisplay.blit(prompt_text, (80, (height / 2) - 150))

    input_text = font.render(user_input, True, BLACK)
    gameDisplay.blit(input_text, (width / 2, (height / 2) - 97))

    message_text = font.render(message, True, RED)
    gameDisplay.blit(message_text, ((width / 2) - 100, (height / 2) - 67))

    tries_text = font.render(f"Tries left: {tries - number_try}", True, GREEN)
    gameDisplay.blit(tries_text, ((width / 2) - 50, (height / 2) - 20))

    pygame.display.update()
    clock.tick(FPS)

    if number_try >= tries:
        running = False

# Final message screen
gameDisplay.fill(WHITE)
if won:
    final_text = font.render("You guessed the number!", True, GREEN)
else:
    final_text = font.render("You lost! Try again.", True, RED)

gameDisplay.blit(final_text, ((width / 2)- 100, (height / 2) - 10))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
    