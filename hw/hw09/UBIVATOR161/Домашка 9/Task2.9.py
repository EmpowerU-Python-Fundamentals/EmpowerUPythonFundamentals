import pygame
import os

FPS = 60
WIDTH_DISPLAY = 1250
HEIGHT_DISPLAY = 1250

COORD_X = 100
COORD_Y = 100
WIDTH_RECTANGLE = 200
HEIGHT_RECTANGLE = 200
DELTA_STEP = 80

pygame.init()
pygame.mixer.init()

ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

pygame.mixer.music.load(os.path.join(ASSETS_PATH, "BIBI.MP3"))
pygame.mixer.music.play(-1)

background = pygame.image.load(os.path.join(ASSETS_PATH, "33.JPG"))
background = pygame.transform.scale(background, (WIDTH_DISPLAY, HEIGHT_DISPLAY))

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("Домашка UBIVATOR161")

player_image = pygame.image.load(os.path.join(ASSETS_PATH, "yanukovych.JPEG"))
player_image = pygame.transform.scale(player_image, (WIDTH_RECTANGLE, HEIGHT_RECTANGLE))

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X - DELTA_STEP >= 0:
        COORD_X -= DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X + DELTA_STEP <= WIDTH_DISPLAY - WIDTH_RECTANGLE:
        COORD_X += DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y - DELTA_STEP >= 0:
        COORD_Y -= DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y + DELTA_STEP <= HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        COORD_Y += DELTA_STEP

    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(player_image, (COORD_X, COORD_Y))

    pygame.display.update()
    clock.tick(FPS)