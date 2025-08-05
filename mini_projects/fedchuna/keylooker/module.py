import os
import sys
from datetime import datetime
import pygame as pg

class InputBox:
    COLOR_BUTTON = (0, 255 , 0)
    WHITE = (150, 150, 150)
    BLACK = (0, 0, 0)
    COLOR_BUTTON_TEXT = (255, 0, 0 )

    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x,y,w,h)
        self.color_text = self.COLOR_BUTTON_TEXT
        self.keytext = 'EXIT'
        self.font = pg.font.SysFont('Colibri', 25)
        self.button = self.font.render(self.keytext, True, self.color_text)
        self.button_text_rect = self.button.get_rect(center=self.rect.center)

    def draw(self, screen):
        pg.draw.rect(screen, self.COLOR_BUTTON, self.rect)
        screen.blit(self.button, self.button_text_rect)

def date_time():
    current_time = datetime.now()
    current_time = current_time.strftime("%A:%B:%d:%Y,%H:%M:%S")
    return current_time

def get_log_file_path(log_file_name):
    log_directory_name = "log"
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable) 
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    log_dir_path = os.path.join(base_dir, log_directory_name)
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)
        
    return os.path.join(log_dir_path, log_file_name)