import random
import pygame as pg
import module as m
pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600




gameDisplay = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Guess the number')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ACTIVE_COLOR = (173, 215, 235)
INACTIVE_COLOR = (200, 200, 200)
BLUE = (0,0,255)

font_large = pg.font.SysFont('Calibri', 40, True, False)
font_medium = pg.font.SysFont('Calibri', 25, True, False)
font_small = pg.font.SysFont('Calibri', 20, True, False)

secret_number = 0
attempts = 0
max_attempts = 10

game_state = 'playing'
feedback_text  = "Guess the number from 1 to 100"
user_guess = None


input_box = m.InputBox(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 16, 200, 32)

play_again_button_rect = pg.Rect(SCREEN_WIDTH // 2 -75, SCREEN_HEIGHT - 80, 150, 50)
play_again_button_color = BLUE
play_again_button_text = font_medium.render("Try again", True, WHITE)
play_again_button_text_rect = play_again_button_text.get_rect(center=play_again_button_rect.center)

def reset_game():
    global secret_number, attempts, feedback_text, user_guess
    secret_number = random.randint(1,100)
    attempts = 0
    game_state = 'playing'
    feedback_text = "Guess a number between 1 and 100!"
    user_guess = None
    input_box.clear_text()
    reset_game()


clock = pg.time.Clock()
Done = False


while not Done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Done = True
        

        if game_state == 'playing':
            submitted_text = input_box.handle_event(event)
            if submitted_text is not None:
                try:
                    guess = int(submitted_text)
                    if 1 <= guess <= 100:
                        user_guess = guess
                        attempts += 1 
                        if user_guess < secret_number:
                            feedback_text = f"Too low. Try again. attempts left {max_attempts - attempts}"
                        elif user_guess > secret_number:
                            feedback_text = f"Too hi. Try again. attempts left {max_attempts - attempts}"
                        else:
                            feedback_text = f"Congratulations! You WIN!! from {attempts} attempt(s)"
                    else:
                        feedback_text = "Please enter a number between 1 and 100."
                except ValueError:
                    feedback_text = "Invalid input. Please enter a whole number."
                if game_state == 'playing' and attempts >= max_attempts:
                    feedback_text = f"You run out of attempts. The sicret number was {secret_number}"
                    game_state = 'lost'
        

        if event.type == pg.MOUSEBUTTONDOWN:
            if game_state in ['won', 'lost'] and play_again_button_rect.collidepoint(event.pos):
                reset_game()

        

    input_box.update()

    gameDisplay.fill(WHITE)
                
    instruction_text_surface = font_medium.render("Guess the Number (1-100)", True, BLACK)
    instruction_text_rect = instruction_text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    gameDisplay.blit(instruction_text_surface, instruction_text_rect)    

    feedback_text_surface = font_large.render(feedback_text, True, BLACK)
    feedback_text_rect = feedback_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
    gameDisplay.blit(feedback_text_surface, feedback_text_rect)


    if game_state == 'playing':
        attempts_text_surface = font_medium.render(f"Attempts: {attempts}/{max_attempts}", True, BLACK)
        attempts_text_rect = attempts_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        gameDisplay.blit(attempts_text_surface, attempts_text_rect)

        input_box.draw(gameDisplay)
    else:
        pg.draw.rect(gameDisplay, play_again_button_color, play_again_button_rect, border_radius=10)
        gameDisplay.blit(play_again_button_text, play_again_button_text_rect)
    
    pg.display.update()


    clock.tick(60)



if __name__ == "__main__":
    pg.quit()
    exit(0)