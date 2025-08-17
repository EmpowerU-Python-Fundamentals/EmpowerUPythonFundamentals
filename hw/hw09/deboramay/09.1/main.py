import pygame
import random
import sys

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вгадай число")

FONT = pygame.font.SysFont(None, 36)
BIG_FONT = pygame.font.SysFont(None, 48)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)

def start_new_game():
    global secret_number, attempts, input_text, message, game_over
    secret_number = random.randint(1, 100)
    attempts = 10
    input_text = ''
    message = f'Вгадайте число від 1 до 100. У вас {attempts} спроб.'
    game_over = False

start_new_game()

def draw_text(text, y, font=FONT, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (20, y))

def draw_button(text, rect, active=False):
    color = LIGHT_GREEN if active else GREEN
    pygame.draw.rect(screen, color, rect)
    text_surf = FONT.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

button_rect = pygame.Rect(WIDTH//2 - 80, HEIGHT - 70, 160, 50)

running = True
while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        guess = int(input_text)
                        attempts -= 1

                        if guess < secret_number:
                            message = f"{guess} — занадто маленьке. Спроб залишилось: {attempts}"
                        elif guess > secret_number:
                            message = f"{guess} — занадто велике. Спроб залишилось: {attempts}"
                        else:
                            message = f"Вітаю! Ви вгадали {secret_number}!"
                            game_over = True
                    else:
                        message = "Будь ласка, введіть число."

                    input_text = ''

                    if attempts == 0 and not game_over:
                        message = f"Спроби закінчились. Число було {secret_number}."
                        game_over = True

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    draw_text(message, 50)
    if not game_over:
        draw_text("Ваше припущення: " + input_text, 150)

    if game_over:
        active = button_rect.collidepoint(mouse_pos)
        draw_button("Нова гра", button_rect, active)

        if active and mouse_clicked:
            start_new_game()

    pygame.display.flip()

pygame.quit()
sys.exit()
