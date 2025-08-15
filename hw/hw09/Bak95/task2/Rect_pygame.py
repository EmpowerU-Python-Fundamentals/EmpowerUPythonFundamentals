import pygame
import sys

# Ініціалізація pygame
pygame.init()

# Константи
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 100, 200)
BLACK = (0, 0, 0)

# Створення вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Boundary Control")

# Параметри прямокутника
rect_width = 50
rect_height = 50
rect_x = WIDTH // 2 - rect_width // 2
rect_y = HEIGHT // 2 - rect_height // 2
rect_speed = 5

# Створення об'єкта прямокутника
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

clock = pygame.time.Clock()

# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання натиснутих клавіш
    keys = pygame.key.get_pressed()

    # Рух прямокутника з перевіркою меж
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        rect.x -= rect_speed
        # Перевірка лівої межі
        if rect.x < 0:
            rect.x = 0

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        rect.x += rect_speed
        # Перевірка правої межі
        if rect.x + rect_width > WIDTH:
            rect.x = WIDTH - rect_width

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        rect.y -= rect_speed
        # Перевірка верхньої межі
        if rect.y < 0:
            rect.y = 0

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        rect.y += rect_speed
        # Перевірка нижньої межі
        if rect.y + rect_height > HEIGHT:
            rect.y = HEIGHT - rect_height

    # Очищення екрану
    screen.fill(WHITE)

    # Малювання прямокутника
    pygame.draw.rect(screen, BLUE, rect)

    # Малювання рамки вікна для наочності
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 2)

    # Відображення змін
    pygame.display.flip()
    clock.tick(60)

# Завершення роботи
pygame.quit()
sys.exit()