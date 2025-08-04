import sys
from pathlib import Path
import os
import pygame as pg
from . import module as m



# --- Новая функция для получения пути к ресурсам ---
def get_resource_path(relative_path):
    """
    Determines the correct path for a resource,
    working both in development and after PyInstaller compilation.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # For development, use the script's directory
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

# --- Функція для логування, щоб уникнути дублювання коду ---
def log_message(message, log_file_path):
    """ Writes a timestamped message to the specified log file. """
    try:
        with open(log_file_path, 'a', encoding='utf-8') as log_f:
            log_f.write(f"{m.date_time()}:{message}\n")
    except Exception as e:
        print(f"Error writing to log file {log_file_path}: {e}")

# --- Головна функція, яка містить логіку Pygame ---
def run_key_looker():
    pg.init()
    pg.mixer.init()
    sound_path = get_resource_path(os.path.join("sound", "zvuk.wav"))
    sound = pg.mixer.Sound(sound_path)

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Получаем пути к ресурсам
    image_path = get_resource_path(os.path.join("img", "scr.jpg"))
    # sound_path = get_resource_path(os.path.join("sound", "zvuk.wav"))
    log_file_name = "log_keylooker.log"
    # m.get_log_file_path теперь будет создавать папку logs рядом с .exe
    keylooker_log_path = m.get_log_file_path(log_file_name)

    gameDisplay = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('KEY')

    try:
        background_image = pg.image.load(image_path)
        background_image = pg.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except FileNotFoundError:
        log_message(f"ERROR: Background image not found at {image_path}", keylooker_log_path)
        print(f"Error: Background image not found at {image_path}")
        pg.quit()
        sys.exit(1)

    KEY_TEXT = ''
    TEXT_SURFACE = "Press keys to check your keyboard"
    BLACK = (0, 0, 0)
    SPEC_SYMBOLS = (' ', '\x1b', '\t', '', '\r', '\x08', '\x7f')

    input_box = m.InputBox(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT -80, 200, 60)

    font = pg.font.SysFont('Calibri', 40, True, False)
    font_l = pg.font.SysFont('Aerial', 50, True, False)
    font_exit = pg.font.SysFont('Aerial', 100,True, False)
    key_code = 0

    clock = pg.time.Clock()
    Done = False

    log_message("\n-------Program Initialized-------\n", keylooker_log_path)

    try:
        while not Done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Done = True
                    log_message(f"{event} = EXIT --- Program---", keylooker_log_path)

                elif event.type == pg.KEYDOWN:
                    key_code = event.key
                    sound.play()
                    if event.key == pg.K_z and (event.mod & pg.KMOD_CTRL):
                        Done = True
                        log_message(f"{event} = EXIT (Ctrl+Z) --- Program---", keylooker_log_path)
                    else:
                        KEY_TEXT = event.unicode
                        log_message(f"{event} = KEYDOWN ({KEY_TEXT}) ---", keylooker_log_path)
                        if KEY_TEXT in SPEC_SYMBOLS:
                            KEY_TEXT = pg.key.name(key_code)
                        else:
                            KEY_TEXT = event.unicode
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.rect.collidepoint(event.pos):
                        Done = True
                        log_message(f"{event} = EXIT (Mouse Click) --- Program---", keylooker_log_path)
                    sound.play()

            gameDisplay.blit(background_image, (0, 0))
            input_box.draw(gameDisplay)

            feedback_text = font_l.render(TEXT_SURFACE, True, BLACK)
            feedback_text_surface_rect = feedback_text.get_rect(center=(SCREEN_WIDTH // 2 , 100))
            gameDisplay.blit(feedback_text , feedback_text_surface_rect)

            if not Done and KEY_TEXT != '':
                TEXT = font.render(f"Нажата клавиша {KEY_TEXT}",True, BLACK)
                attempts_text_rect = TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2))
                gameDisplay.blit(TEXT, attempts_text_rect)
            elif not Done and KEY_TEXT == '':
                TEXT = font.render("Ничего не нажато",True, BLACK)
                attempts_text_rect = TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2))
                gameDisplay.blit(TEXT, attempts_text_rect)
            else:
                TEXT = font_exit.render("EXIT",True, BLACK)
                attempts_text_rect = TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2))
                gameDisplay.blit(TEXT, attempts_text_rect)

            pg.display.flip()
            clock.tick(30)

    except Exception as e:
        log_message(f"ERROR: Unexpected exception: {type(e).__name__} - {e}", keylooker_log_path)
        print(f"ERROR: Unexpected exception: {type(e).__name__} - {e}")
        sys.exit(1)
    finally:
        if 'gameDisplay' in locals():
            log_message("\nPROGRAM EXIT", keylooker_log_path)
            pg.quit()

# --- КЛЮЧЕВОЙ БЛОК: Запуск программы только если скрипт запускается напрямую ---
if __name__ == '__main__':
    # Теперь мы не используем sys.argv, так как все ресурсы находятся внутри пакета
    run_key_looker()