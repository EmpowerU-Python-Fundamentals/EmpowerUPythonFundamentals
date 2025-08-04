 # import pygame as pg
# from datetime import datetime

# class InputBox:
    
#     COLOR_BUTTON = (0, 255 , 0)
#     WHITE = (150, 150, 150)
#     BLACK = (0, 0, 0)
#     COLOR_BUTTON_TEXT = (255, 0, 0 )
    
#     def __init__(self, x, y, w, h,):
        
#         self.rect = pg.Rect(x,y,w,h)
#         self.color_text = self.COLOR_BUTTON_TEXT
#         self.keytext = 'EXIT'
#         self.font = pg.font.SysFont('Colibri', 25)
#         self.button = self.font.render(self.keytext, True, self.color_text)
#         # Получаем прямоугольник текста, чтобы разместить его в центре кнопки
#         self.button_text_rect = self.button.get_rect(center=self.rect.center)
        
    
#     def draw(self, screen):
        
#         pg.draw.rect(screen, self.COLOR_BUTTON, self.rect)
#         screen.blit(self.button, self.button_text_rect)
        
# def date_time():
#     current_time = datetime.now()
#     current_time = current_time.strftime("%A:%B:%d:%Y,%H:%M:%S")
#     return current_time

import os
import sys
from datetime import datetime
import pygame as pg
# Клас InputBox залишається тут, як ви його надали
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

# Функція date_time() винесена на рівень модуля
def date_time():
    current_time = datetime.now()
    current_time = current_time.strftime("%A:%B:%d:%Y,%H:%M:%S")
    return current_time

# Нова функція для отримання шляху до лог-файлу
def get_log_file_path(log_file_name):
    """
    Determines the path for the log file and ensures the directory exists.
    Logs will be created in a 'log' subfolder relative to the executable/script.
    """
    log_directory_name = "log"
    
    # Визначаємо базову директорію для логів
    if getattr(sys, 'frozen', False): # Якщо запущено PyInstaller'ом
        # sys.executable - це шлях до EXE. Логи поруч з EXE.
        base_dir = os.path.dirname(sys.executable) 
    else:
        # Для розробки, коли запускається .py файл
        # base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Піднятися на 2 рівні від module.py

    log_dir_path = os.path.join(base_dir, log_directory_name)
    
    # Створюємо директорію, якщо вона не існує
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)
        
    return os.path.join(log_dir_path, log_file_name)