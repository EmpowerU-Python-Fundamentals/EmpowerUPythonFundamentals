import pygame
import random
import sys

pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вгадайте число")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 87, 183)
YELLOW = (255, 215, 0)

# Шрифти
font = pygame.font.Font(None, 32)
message_font = pygame.font.Font(None, 24)
small_font = pygame.font.Font(None, 19)

# Поле вводу
input_box = pygame.Rect(220, 110, 60, 30)
user_text = ''

# Кнопка
button_rect = pygame.Rect(190, 160, 120, 38)

# Логіка гри
target_number = random.randint(1, 100)
attempts_left = 10
message = "Введіть число від 1 до 100 і натисніть кнопку \"Вгадати\""
head = 1
tail = 100
user_win = False

def check_guess(guess):
    global attempts_left, message, head, tail, user_win
    if not guess.isdigit():
        message = "Введіть ціле число!"
        return
    guess = int(guess)
    attempts_left -= 1
    if guess < target_number:
        message = f"{guess} занадто маленьке. Спроб залишилось: {attempts_left}"
        head = guess
    elif guess > target_number:
        message = f"{guess} занадто велике. Спроб залишилось: {attempts_left}"
        tail = guess
    else:
        message = f"Вітаємо! Ви вгадали число {target_number}!"
        user_win = True
        attempts_left = 0

running = True
while running:
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, WIDTH, HEIGHT / 2))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ввід тексту
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                if attempts_left > 0:
                    check_guess(user_text)
                    user_text = ''
            else:
                if len(user_text) < 3:
                    user_text += event.unicode

        # Натискання кнопки
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if attempts_left > 0:
                    check_guess(user_text)
                    user_text = ''


    if not user_win and attempts_left > 0:
        # Відображення поля вводу
        pygame.draw.rect(screen, GRAY, input_box, 2)
        text_surface = font.render(user_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # Відображення кнопки
        pygame.draw.rect(screen, GREEN if attempts_left > 0 else RED, button_rect)
        button_text = font.render("Вгадати", True, WHITE)
        screen.blit(button_text, (button_rect.x + 15, button_rect.y + 8))

        # Відображення підказки
        msg_range_surface = small_font.render(f"Підказка: Загадане число в межах від {head} до {tail}!", True, BLACK)
        screen.blit(msg_range_surface, (40, 260))

    # Відображення повідомлення
    msg_surface = message_font.render(message, True, BLACK)
    screen.blit(msg_surface, (40, 225))

    pygame.display.flip()

pygame.quit()
sys.exit()
