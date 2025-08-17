import pygame

FPS = 60

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

    if keys[pygame.K_LEFT]:
        COORD_X -= DELTA_STEP
    if keys[pygame.K_RIGHT]:
        COORD_X += DELTA_STEP
    if keys[pygame.K_UP]:
        COORD_Y -= DELTA_STEP
    if keys[pygame.K_DOWN]:
        COORD_Y += DELTA_STEP

    current_width, current_height = gameDisplay.get_size()

    if COORD_X < 0:
        COORD_X = 0

    elif COORD_X + WIDTH_RECTANGLE > current_width:
        COORD_X = current_width - WIDTH_RECTANGLE

    if COORD_Y < 0:
        COORD_Y = 0

    elif COORD_Y + HEIGHT_RECTANGLE > current_height:
        COORD_Y = current_height - HEIGHT_RECTANGLE

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(
        gameDisplay, RED_COLOR, [COORD_X, COORD_Y, WIDTH_RECTANGLE, HEIGHT_RECTANGLE]
    )

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
