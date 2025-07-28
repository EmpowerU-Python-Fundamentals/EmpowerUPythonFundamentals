import pygame as pg
import random
pg.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ACTIVE_COLOR = (173, 215, 235)
INACTIVE_COLOR = (200, 200, 200)  

font1 = pg.font.SysFont('Calibri', 25, True, False)
text = "input a number "


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


    def handle_event(self,event,TRY1: int = 0):
        
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
                    try:
                        a = int(self.text)
                        b = random.randint(1, 100)
                        self.text = ''
                        if a != b and TRY1 <= 10:
                            self.text = f'You guessed {a}, but the number was {b} {10 - TRY1}  attempts left. Try again!'
                            TRY1 = TRY1 + 1
                        elif a != b and TRY1 > 10:
                            self.text = f'You have exceeded the number of attempts. The number was {b}.'
                            self.active = False
                            return int(TRY1)
                        else:
                            self.text = f'Congratulations! You guessed the number {b} from {TRY1} attempts correctly!'
                            self.active = False
                            TRY1 = 0
                            return int(TRY1)
                    except ValueError:
                        self.text = "Please enter a valid number"
                        return None
                elif event.key == pg.K_ESCAPE:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isprintable():
                    self.text += event.unicode
        return int(TRY1)
