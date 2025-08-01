import pygame

FPS = 100

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    new_x = COORD_X
    new_y = COORD_Y

    if keys[pygame.K_LEFT]:
        new_x = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT]:
        new_x = COORD_X + DELTA_STEP
    if keys[pygame.K_UP]:
        new_y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN]:
        new_y = COORD_Y + DELTA_STEP

# перевірка меж програмного вікна
    if new_x < 0:
        new_x = 0
    elif new_x + WIDTH_RECTANGLE > WIDTH_DISPLAY:
        new_x = WIDTH_DISPLAY - WIDTH_RECTANGLE
    if new_y < 0:
        new_y = 0
    elif new_y + HEIGHT_RECTANGLE > HEIGHT_DISPLAY:
        new_y = HEIGHT_DISPLAY - HEIGHT_RECTANGLE

    COORD_X = new_x
    COORD_Y = new_y

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)