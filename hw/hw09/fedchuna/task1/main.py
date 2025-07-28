import pygame as pg
import random
import module as m
pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
a = 0
TRY1 = int(1)


gameDisplay = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Guess the number')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ACTIVE_COLOR = (173, 215, 235)
INACTIVE_COLOR = (200, 200, 200)  

font1 = pg.font.SysFont('Calibri', 25, True, False)
text = "input a number "

clock = pg.time.Clock()
Done = False


# Create an instance of InputBox
input_box_i = input_box = m.InputBox(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2 - 16, 710, 32)

while not Done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Done = True
        elif event.type == pg.K_ESCAPE:
            Done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            input_box_i.handle_event(event, TRY1)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                Done = True
            TRY1 = input_box_i.handle_event(event, TRY1)


    gameDisplay.fill(WHITE)
    input_box_i.draw(gameDisplay)
    
    pg.display.update()
    clock.tick(60)
if __name__ == "__main__":
    pg.quit()
    exit()
    