import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=10   # трішки збільшив швидкість

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
        if rectangle.x <= 0:     # Добавив перевірку на лівий край
            continue
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT]:
        if rectangle.right >= WIDTH_DISPLAY:  # Добавив перевірку на правий край, але координат правої сторони фігури
            continue
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP]:
        if rectangle.y <= 0:     # Добавив перевірку на верх
            continue
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN]:
        if rectangle.bottom >= HEIGHT_DISPLAY: # Добавив перевірку на низ відповідно, але координат нижньої сторони фігури
            continue
        COORD_Y = COORD_Y+DELTA_STEP
# Більше/менше дорівнює поклав тому що швидкість може перескочини 0, тобто стати -5 або що,
# і аналогічно в іншу сторону

    gameDisplay.fill(BLACK_COLOR)
# присвоїв змінну фігурі щоб зручно було використовувати
    rectangle = pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                                          COORD_Y,
                                                          WIDTH_RECTANGLE,
                                                          HEIGHT_RECTANGLE])
# Дістаємо і присвоюємо завжди актуальні розміри вікна що мати змогу зробити перевірку на зіткнення
    HEIGHT_DISPLAY = pygame.display.get_surface().get_rect().bottom
    WIDTH_DISPLAY = pygame.display.get_surface().get_rect().right

    pygame.display.update()
    clock.tick(FPS)
