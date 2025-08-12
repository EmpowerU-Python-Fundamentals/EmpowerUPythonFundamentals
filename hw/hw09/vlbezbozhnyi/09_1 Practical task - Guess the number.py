import pygame as pg
import random

pg.init()

WINDOW_SIZE = (800, 600)
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("09.1 Practical task - Guess the number")

big_font = pg.font.SysFont(None, 36)
font_obj = pg.font.SysFont(None, 30)

clock = pg.time.Clock()
fps = 30

white = (255, 255, 255)
black = (0, 0, 0)
gray = (180, 180, 180)
green = (0, 200, 0)
red = (200, 0, 0)
BACKGROUND_COLOR = black


secret_number = random.randint(1, 100)
max_attempts = 10
attempts_used = 0
input_text = ""
msg = ""
title_text = "Guess the Number (1-100)"
answers = []
msg_answers_title = "Your guesses: "
msg_answers = ""
game_over = False

running = True


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.TEXTINPUT:
            input_text += event.text
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                input_text = input_text[:-1]  # Remove last character

            if event.key == pg.K_RETURN and not game_over:
                if input_text.isdigit():
                    guess = int(input_text)
                    if 0 < guess < 100:
                        attempts_used += 1
                        if guess < secret_number:
                            msg = f"'{guess}' - too low! Try a higher number."
                            answers.append(guess)
                            input_text = ""  # Clear input after guess
                        elif guess > secret_number:
                            msg = f"'{guess}' - too high! Try a lower number."
                            answers.append(guess)
                            input_text = ""  # Clear input after guess
                        else:
                            msg = f"Congratulations! You guessed the number {secret_number}!"
                            game_over = True

                        if attempts_used >= max_attempts and not game_over:
                            msg = (
                                f"Out of attempts. The number was " f"{secret_number}."
                            )
                            game_over = True
                    else:
                        msg = "Your guess must be between 1 and 100."
                        input_text = ""
                else:
                    msg = "Please enter a number."
                    input_text = ""
                if len(answers) > 0:
                    msg_answers = f" {', '.join(map(str, answers))}"

    screen.fill(BACKGROUND_COLOR)

    title = big_font.render(title_text, True, white)
    info_msg = big_font.render(msg, True, gray if not game_over else red)
    text_answers = font_obj.render(msg_answers_title + msg_answers, 1, green)
    text_surface = font_obj.render(input_text, 1, white)
    text_attempts = big_font.render(
        f"Attempts: {attempts_used} / {max_attempts}", 1, white
    )

    screen.blit(title, (20, 20))
    screen.blit(text_attempts, (title.get_width() + 30, 20))
    screen.blit(info_msg, (20, title.get_height() + text_surface.get_height() + 50))
    screen.blit(
        text_answers,
        (
            20,
            title.get_height() + text_surface.get_height() + info_msg.get_height() + 60,
        ),
    )

    if not game_over:
        input_box = pg.draw.rect(
            screen,
            white if input_text else gray,
            (
                20,
                title.get_height() + 30,
                max(text_surface.get_width() + 10, 50),
                max(text_surface.get_height(), 30),
            ),
            1,
        )
        screen.blit(text_surface, (25, title.get_height() + 35))

    pg.display.update()
    clock.tick(fps)
