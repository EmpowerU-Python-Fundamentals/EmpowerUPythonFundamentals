import pygame as pg 
import random
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


class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x, y, w, h)
        self.color = INACTIVE_COLOR
        self.text = text
        self.active = False
        self.font = font1

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(surface, self.color, self.rect, 2)

    def handle_event(self,event):
        
        if event.type == pg.MOUSEBUTTONDOWN:
            self.text = ''
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = ACTIVE_COLOR if self.active else INACTIVE_COLOR
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    # f = self.text
                    try:
                        a = int(self.text)
                        b = random.randint(1, 100)
                        self.text = ''
                        if a != b:
                            self.text = f'You guessed {a}, but the number was {b}. Try again!'
                        else:
                            self.text = f'Congratulations! You guessed the number {b} correctly!'
                    except ValueError:
                        self.text = "Please enter a valid number"
                        return self.text = ''
                elif event.key == pg.K_ESCAPE:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isprintable():
                    self.text += event.unicode
input_box_i = input_box = InputBox(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 16, 610, 32)

while not Done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            input_box_i.handle_event(event)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                Done = True
            print(event)
            a = input_box_i.handle_event(event)
            if a is not None:
                gameDisplay.blit(c, (200, 250))
            else:
                gameDisplay.blit(e, (200, 250))

    gameDisplay.fill(WHITE)
    input_box_i.draw(gameDisplay)
    
    pg.display.update()
    clock.tick(60)

pg.quit()