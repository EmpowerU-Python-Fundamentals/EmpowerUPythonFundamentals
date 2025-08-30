import pygame
import random
import time
import os

pygame.init()
pygame.mixer.init()

base_path = os.path.dirname(__file__)
music_path = os.path.join(base_path, "assets", "music.mp3")
move_sound_path = os.path.join(base_path, "assets", "move.wav")

pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

move_sound = pygame.mixer.Sound(move_sound_path)
move_sound.set_volume(0.3)

# --- Налаштування ---
WIDTH, HEIGHT = 20, 15
TILE_SIZE = 32
SCREEN_WIDTH = WIDTH * TILE_SIZE
SCREEN_HEIGHT = HEIGHT * TILE_SIZE
SWITCH_INTERVAL = 2000  # мс
MUSHROOM_INTERVAL = 10000  # мс
INVINCIBILITY_DURATION = 10000  # мс
WALL_DENSITY = 0.12

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Trip")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# --- Кольори ---
GREEN_BG = (0, 100, 0)
PURPLE_BG = (50, 0, 50)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
MUSHROOM_COLOR = (255, 255, 0)
WALL_COLOR = (100, 100, 100)
EXIT_COLOR = (255, 255, 0)
SAFE_ZONE = [(x, y) for x in range(4, 7) for y in range(4, 7)]

# --- Змійка ---
snake = [(5, 5)]
direction = (0, 0)
grow_snake = False
invincible = False
invincible_start_time = 0

# --- Гра ---
current_color = "green"
last_switch_time = pygame.time.get_ticks()
last_mushroom_time = pygame.time.get_ticks()
in_trip_mode = False
trip_maze_exit = (WIDTH - 2, HEIGHT - 2)

# --- Яблука ---
apple_positions = {
    "green": (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)),
    "purple": (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
}

# --- Стінки ---
def generate_random_walls():
    wall_count = int(WIDTH * HEIGHT * WALL_DENSITY)
    green = set()
    purple = set()
    while len(green) < wall_count:
        x, y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
        if (x, y) not in SAFE_ZONE:
            green.add((x, y))
    while len(purple) < wall_count:
        x, y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
        if (x, y) not in SAFE_ZONE:
            purple.add((x, y))
    return list(green), list(purple)

green_walls, purple_walls = generate_random_walls()

# --- Лабіринт Trip режиму ---
trip_green_walls = green_walls.copy()
trip_purple_walls = purple_walls.copy()
trip_exit = trip_maze_exit

# --- Гриб ---
mushroom = None

# --- Game Over ---
game_over = False

# --- Малювання ---
def draw_tile(pos, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw():
    global invincible  # додано для зміни змінної
    # Фон
    screen.fill(GREEN_BG if current_color == "green" else PURPLE_BG)

    # Стіни
    if in_trip_mode:
        walls = trip_green_walls if current_color == "green" else trip_purple_walls
    else:
        walls = green_walls if current_color == "green" else purple_walls

    for wall in walls:
        draw_tile(wall, WALL_COLOR)

    # Яблуко
    if not in_trip_mode:
        draw_tile(apple_positions[current_color], APPLE_COLOR)

    # Гриб
    if mushroom:
        draw_tile(mushroom, MUSHROOM_COLOR)

    # Вихід з лабіринту
    if in_trip_mode:
        draw_tile(trip_exit, EXIT_COLOR)

    # Змійка
    for segment in snake:
        draw_tile(segment, SNAKE_COLOR)

    # Невразливість
    if invincible:
        elapsed = pygame.time.get_ticks() - invincible_start_time
        if elapsed < INVINCIBILITY_DURATION:
            text = font.render(f"Invulnerable: {max(0, (INVINCIBILITY_DURATION - elapsed) // 1000)}", True, (255, 255, 0))
            screen.blit(text, (10, 10))
        else:
            invincible = False  # зміна змінної тут - потрібен global

    # Game Over
    if game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)  # прозорість від 0 до 255
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        text1 = font.render("Game Over!", True, (255, 0, 0))
        text2 = font.render("Press SPACE to restart", True, (255, 255, 255))
        screen.blit(text1, (SCREEN_WIDTH // 2 - text1.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    pygame.display.flip()


# --- Рух змійки ---
def move_snake():
    global grow_snake, invincible, invincible_start_time, in_trip_mode, mushroom, game_over
    if direction == (0, 0) or game_over:
        return

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # Межі
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        if not invincible:
            game_over = True
            return

    walls = trip_green_walls if (in_trip_mode and current_color == "green") else \
            trip_purple_walls if (in_trip_mode and current_color == "purple") else \
            green_walls if current_color == "green" else purple_walls

    if new_head in walls and not invincible:
        game_over = True
        return

    if new_head in snake and not invincible:
        game_over = True
        return

    snake.insert(0, new_head)
    if grow_snake:
        grow_snake = False
    else:
        snake.pop()

    if not in_trip_mode:
        if new_head == apple_positions[current_color]:
            grow_snake = True
            # Нова позиція яблука
            while True:
                new_pos = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
                if new_pos not in snake and new_pos not in walls:
                    apple_positions[current_color] = new_pos
                    break

        if mushroom and new_head == mushroom:
            enter_trip_mode()

    if in_trip_mode and new_head == trip_exit:
        exit_trip_mode()

# --- Логіка Trip режиму ---
def enter_trip_mode():
    global in_trip_mode, mushroom, snake, direction, current_color, grow_snake
    in_trip_mode = True
    mushroom = None
    # Поміщаємо змійку в безпечну зону
    snake = [(4, 4)]
    direction = (0, 0)
    current_color = "green"
    grow_snake = False

def exit_trip_mode():
    global in_trip_mode, invincible, invincible_start_time, game_over, snake, direction, current_color
    in_trip_mode = False
    invincible = True
    invincible_start_time = pygame.time.get_ticks()
    # Повертаємося до стартових налаштувань
    snake = [(5, 5)]
    direction = (0, 0)
    current_color = "green"

# --- Зміна кольору ---
def switch_color():
    global current_color, last_switch_time, game_over
    if game_over:
        return
    now = pygame.time.get_ticks()
    if now - last_switch_time >= SWITCH_INTERVAL:
        current_color = "purple" if current_color == "green" else "green"
        last_switch_time = now

# --- Поява гриба ---
def spawn_mushroom():
    global mushroom, last_mushroom_time, game_over
    if game_over or in_trip_mode or mushroom is not None:
        return
    now = pygame.time.get_ticks()
    if now - last_mushroom_time >= MUSHROOM_INTERVAL:
        while True:
            pos = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
            walls_set = set(green_walls if current_color == "green" else purple_walls)
            if pos not in walls_set and pos not in snake and pos not in SAFE_ZONE:
                mushroom = pos
                break
        last_mushroom_time = now

# --- Перезапуск гри ---
def reset_game():
    global snake, direction, grow_snake, invincible, invincible_start_time, current_color
    global last_switch_time, last_mushroom_time, in_trip_mode, mushroom, game_over
    snake = [(5, 5)]
    direction = (0, 0)
    grow_snake = False
    invincible = False
    invincible_start_time = 0
    current_color = "green"
    last_switch_time = pygame.time.get_ticks()
    last_mushroom_time = pygame.time.get_ticks()
    in_trip_mode = False
    mushroom = None
    game_over = False

# --- Головний цикл ---
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP:
                    direction = (0, -1)
                    move_sound.play()
                    move_snake()
                elif event.key == pygame.K_DOWN:
                    direction = (0, 1)
                    move_sound.play()
                    move_snake()
                elif event.key == pygame.K_LEFT:
                    direction = (-1, 0)
                    move_sound.play()
                    move_snake()
                elif event.key == pygame.K_RIGHT:
                    direction = (1, 0)
                    move_sound.play()
                    move_snake()
            else:
                if event.key == pygame.K_SPACE:
                    reset_game()

    if not game_over:
        switch_color()
        spawn_mushroom()

    draw()

pygame.quit()
