import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

def restrain_movement(desired_position: int, horizontal_axis: bool) -> int:
    if desired_position < 0:
        return 0
    if horizontal_axis and desired_position > WIDTH_DISPLAY - WIDTH_RECTANGLE:
        return WIDTH_DISPLAY - WIDTH_RECTANGLE
    if not horizontal_axis and desired_position > HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        return HEIGHT_DISPLAY - HEIGHT_RECTANGLE

    return desired_position


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        COORD_X = restrain_movement(COORD_X - DELTA_STEP, True)
    if keys[pygame.K_RIGHT]:
        COORD_X = restrain_movement(COORD_X + DELTA_STEP, True)
    if keys[pygame.K_UP]:
        COORD_Y = restrain_movement(COORD_Y - DELTA_STEP, False)
    if keys[pygame.K_DOWN]:
        COORD_Y = restrain_movement(COORD_Y + DELTA_STEP, False)


    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    

