import pygame

FPS = 60
WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("My first game")

def get_new_position(current_pos, change, max_pos, rect_size):
    """
    Обчислює нову позицію, перевіряючи,
    чи не виходить вона за межі екрану.
    """
    new_pos = current_pos + change
    if new_pos < 0:
        return 0
    if new_pos + rect_size > max_pos:
        return max_pos - rect_size
    return new_pos

run = True
clock = pygame.time.Clock()

coord_x = 50
coord_y = 50

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # Використання допоміжної функції для руху та перевірки меж
    if keys[pygame.K_LEFT]:
        coord_x = get_new_position(coord_x, -DELTA_STEP, WIDTH_DISPLAY, WIDTH_RECTANGLE)
    if keys[pygame.K_RIGHT]:
        coord_x = get_new_position(coord_x, DELTA_STEP, WIDTH_DISPLAY, WIDTH_RECTANGLE)
    if keys[pygame.K_UP]:
        coord_y = get_new_position(coord_y, -DELTA_STEP, HEIGHT_DISPLAY, HEIGHT_RECTANGLE)
    if keys[pygame.K_DOWN]:
        coord_y = get_new_position(coord_y, DELTA_STEP, HEIGHT_DISPLAY, HEIGHT_RECTANGLE)

    gameDisplay.fill(BLACK_COLOR)
    
    pygame.draw.rect(gameDisplay, RED_COLOR, [
        coord_x, 
        coord_y, 
        WIDTH_RECTANGLE, 
        HEIGHT_RECTANGLE
    ])
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
