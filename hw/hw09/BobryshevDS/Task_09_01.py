import pygame
import random

pygame.init()

# Вікно гри
width, height = 800, 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Відгадай число")
font = pygame.font.SysFont('Calibri', 32, True, False)
clock = pygame.time.Clock()
FPS = 30

# Логіка гри
secret = random.randint(1, 100)
attempts = 10
message = "Я загадав число від 1 до 100!"
input_text = ""

done = False
cursor_visible = True
cursor_timer = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    guess = int(input_text)
                    attempts -= 1
                    if guess < secret:
                        message = f"{guess} < секретного числа. Спробуй більше!"
                    elif guess > secret:
                        message = f"{guess} > секретного числа. Спробуй менше!"
                    else:
                        message = f"Вітаю! Ти вгадав {secret}!"
                input_text = ""

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Відображення гри
    gameDisplay.fill((255, 255, 255))  # білий фон

    # повідомлення
    msg_surface = font.render(message, True, (0, 0, 0))
    msg_rect = msg_surface.get_rect(center=(width // 2, height // 3))
    gameDisplay.blit(msg_surface, msg_rect)

    # поле вводу
    input_rect = pygame.Rect(0, 0, 200, 40)
    input_rect.center = (width // 2, height // 2)
    pygame.draw.rect(gameDisplay, (200, 200, 200), input_rect, 2)

    # курсор
    cursor_timer += 1
    if cursor_timer % 60 < 30:  # блимає
        cursor_visible = True
    else:
        cursor_visible = False

    txt_surface = font.render(input_text, True, (0, 0, 0))
    txt_rect = txt_surface.get_rect(midleft=(input_rect.x + 5, input_rect.centery))
    gameDisplay.blit(txt_surface, txt_rect)

    if cursor_visible:
        cursor_x = txt_rect.right + 2
        cursor_y_top = txt_rect.top
        cursor_y_bottom = txt_rect.bottom
        pygame.draw.line(gameDisplay, (0, 0, 0), (cursor_x, cursor_y_top), (cursor_x, cursor_y_bottom), 2)

    # спроби
    attempts_surface = font.render(f"Залишилось спроб: {attempts}", True, (0, 0, 255))
    attempts_rect = attempts_surface.get_rect(center=(width // 2, height // 2 + 80))
    gameDisplay.blit(attempts_surface, attempts_rect)

    # якщо спроби закінчились
    if attempts <= 0 and "Вітаю" not in message:
        message = f"Програш! Число було {secret}"

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
print("end game")
