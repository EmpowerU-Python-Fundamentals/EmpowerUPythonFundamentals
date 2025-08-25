import pygame as pg



class InputBox:

    COLOR_INACTIVE = (200, 200, 200)
    COLOR_ACTIVE = (173, 215, 235)
    COLOR_TEXT = (0, 0, 0)

    def __init__(self, x, y, w, h, initial_text=''):

        self.rect = pg.Rect(x,y,w,h)
        self.color = self.COLOR_INACTIVE
        self.text = initial_text
        self.font = pg.font.SysFont('Colibri',25)
        self.txt_surface = self.font.render(self.text, True, self.COLOR_TEXT)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:
            
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    
                    entered_text = self.text
                    self.clear_text() 
                    return entered_text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1] 
                else:
                    
                    if event.unicode.isdigit():
                        self.text += event.unicode
                
                self.txt_surface = self.font.render(self.text, True, self.COLOR_TEXT)
        return None 

    def update(self):
        
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        
        pg.draw.rect(screen, self.color, self.rect, 2) 

    def get_text(self):
        
        return self.text

    def clear_text(self):
        
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.COLOR_TEXT)