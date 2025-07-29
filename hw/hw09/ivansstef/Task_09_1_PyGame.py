import pygame
import random
import sys

# Initialize
pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Guess the Number")
font = pygame.font.SysFont(None, 36)

# Game variables
secret_number = random.randint(1, 100)
guess = ''
message = "Guess a number between 1 and 100"
attempts = 0
max_attempts = 10
input_active = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def draw_text(text, x, y, color=BLACK):
    txt = font.render(text, True, color)
    screen.blit(txt, (x, y))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw input box
    pygame.draw.rect(screen, GRAY, (50, 200, 400, 40))
    draw_text(guess, 60, 205)

    # Draw message and tries
    draw_text(message, 50, 50)
    draw_text(f"Attempt: {attempts}/{max_attempts}", 50, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if input_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if guess.isdigit():
                    user_guess = int(guess)
                    attempts += 1
                    if user_guess < secret_number:
                        message = "Too low!"
                    elif user_guess > secret_number:
                        message = "Too high!"
                    else:
                        message = f"Correct! The number was {secret_number}"
                        input_active = False
                    if attempts >= max_attempts and user_guess != secret_number:
                        message = f"You lost! The number was {secret_number}"
                        input_active = False
                guess = ''
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            elif event.unicode.isdigit():
                guess += event.unicode

    pygame.display.flip()

pygame.quit()
sys.exit()
