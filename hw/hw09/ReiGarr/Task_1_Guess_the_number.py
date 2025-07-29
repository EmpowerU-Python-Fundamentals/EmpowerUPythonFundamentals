import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Guess the number")

FONT = pygame.font.SysFont(None, 32)
BIG_FONT = pygame.font.SysFont(None, 40)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

secret_num = random.randint(1, 100)
attempts_left = 10
user_num = ''
message = "Guess a number (1-100):"
game_over = False

input_box = pygame.Rect(150, 100, 200, 40)
submit_button = pygame.Rect(200, 160, 100, 40)

def draw_text(text, font, color, surface, x, y):
    txt_obj = font.render(text, True, color)
    surface.blit(txt_obj, (x, y))

clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_num = user_num[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                elif event.unicode.isdigit():
                    user_num += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_button.collidepoint(event.pos):
                    if user_num.isdigit():
                        num = int(user_num)
                        attempts_left -= 1
                        if num == secret_num:
                            message = f"Correct! The number was {secret_num}."
                            game_over = True
                        elif attempts_left == 0:
                            message = f"You failed! The number was {secret_num}."
                            game_over = True
                        elif num < secret_num:
                            message = "Too low!"
                        else:
                            message = "Too high!"
                        user_num = ''

    draw_text("Guess the number", BIG_FONT, BLACK, screen, 120, 30)
    draw_text(message, FONT, RED if game_over else BLACK, screen, 150, 60)
    draw_text(f"Attempts left: {attempts_left}", FONT, BLACK, screen, 180, 250)

    pygame.draw.rect(screen, GRAY, input_box, 2)
    draw_text(user_num, FONT, BLACK, screen, input_box.x + 10, input_box.y + 5)

    pygame.draw.rect(screen, GREEN, submit_button)
    draw_text("Submit", FONT, WHITE, screen, submit_button.x + 15, submit_button.y + 10)

    pygame.display.flip()
    clock.tick(30)


