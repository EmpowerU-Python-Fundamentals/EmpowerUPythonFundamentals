import pygame as pg
import random
import module as m
pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
a = 0



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
input_box_i = input_box = m.InputBox(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 16, 610, 32)

while not Done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            input_box_i.handle_event(event)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                Done = True
            input_box_i.handle_event(event)

    gameDisplay.fill(WHITE)
    input_box_i.draw(gameDisplay)
    
    pg.display.update()
    clock.tick(60)
if __name__ == "__main__":
    pg.quit()
    exit()
    