import pygame
import random
import sys

# ініціалізація PyGame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вгадай число")

# шрифти
font = pygame.font.SysFont(None, 36)
input_font = pygame.font.SysFont(None, 28)

# кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)

# константи
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10

clock = pygame.time.Clock()


def reset_game():
    """Повертає нові значення при старті або перезапуску."""
    return (
        random.randint(MIN_NUMBER, MAX_NUMBER),
        MAX_ATTEMPTS,
        "",
        f"Вгадай число від {MIN_NUMBER} до {MAX_NUMBER}",
        False
    )


def render_text(text, y, font_obj, color=BLACK, center=True):
    """Відображає текст на екрані."""
    surf = font_obj.render(text, True, color)
    rect = surf.get_rect()
    if center:
        rect.center = (WIDTH // 2, y)
    else:
        rect.topleft = (20, y)
    screen.blit(surf, rect)


# стартові змінні гри
target, attempts, input_text, message, game_over = reset_game()

running = True
while running:
    screen.fill(WHITE)

    if not game_over:
        render_text(f"Спроб залишилось: {attempts}", 80, font)
        render_text(message, 40, font)
        render_text(f"Введено: {input_text}", 320, input_font, center=False)
    else:
        # режим GAME OVER
        render_text(message, HEIGHT//2 - 20, font, color=RED)
        render_text(
            "Натисни R, щоб грати ще, або ESC, щоб вийти.",
            HEIGHT//2 + 30,
            input_font
        )

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if not game_over:
                # обробка вводу в режимі гри
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if input_text.isdigit():
                        guess = int(input_text)
                        if MIN_NUMBER <= guess <= MAX_NUMBER:
                            if guess == target:
                                message = f"Вітаю! Число {target} вгадано."
                                game_over = True
                            else:
                                attempts -= 1
                                message = "Занадто маленьке!" if guess < target else "Занадто велике!"
                                if attempts <= 0:
                                    message = f"Гру завершено. Було число {target}"
                                    game_over = True
                        else:
                            message = f"Число має бути між {MIN_NUMBER} та {MAX_NUMBER}"
                    else:
                        message = "Введи дійсне число!"
                    input_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                elif event.unicode.isdigit() and len(input_text) < 3:
                    input_text += event.unicode

            else:
                # обробка після GAME OVER
                if event.key == pygame.K_r:
                    target, attempts, input_text, message, game_over = reset_game()
                elif event.key == pygame.K_ESCAPE:
                    running = False

    clock.tick(30)

pygame.quit()
sys.exit()
