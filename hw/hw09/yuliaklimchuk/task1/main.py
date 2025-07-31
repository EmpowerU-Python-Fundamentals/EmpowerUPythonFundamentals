import pygame
import random
import colors

pygame.init()

WIDTH = 800
HEIGHT = 600

done = False
draw = True
random_number = random.randint(1, 100)
attempts = 10

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT)) 
font = pygame.font.SysFont('Calibri', 25, True, False)
font_in_box = pygame.font.SysFont('Calibri', 15, True, False)

clock = pygame.time.Clock()
FPS = 60

input_box = pygame.Rect(WIDTH/7, 100, WIDTH/10+500, 40)
color = colors.Gray 
active = False
text = ''
text_condition = "Enter your number"
text_message=''

def split_the_line(text):
    lines = text.split('\n')
    x, y = WIDTH/6, 15
    for line in lines:
        rendered_line = font.render(line, True, colors.Maroon)
        gameDisplay.blit(rendered_line, (x, y))
        y += rendered_line.get_height() + 5 



pygame.display.set_caption("Game `Guess the number`") 

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
                if draw and input_box.collidepoint(event.pos):
                    active = not active
                    text_condition=''
                    text_message=''
                else:
                    active = False
                color = colors.Black if active else colors.Gray
        if event.type == pygame.KEYDOWN:
            text_message=''
            if active and draw:
                if event.key == pygame.K_RETURN:
                    customer_number = int(text)
                    attempts -=1
                    if customer_number < random_number:
                        text_message = "The entered number is less than the specified number."
                    elif customer_number > random_number:
                        text_message = "The entered number is greater than the specified number."
                    elif customer_number == random_number:
                        text_message = "Congratulations! You guessed the number!"
                        draw = False
                    if attempts == 0 and customer_number != random_number:
                        text_message = "Game over! The number was " + str(random_number)
                        draw = False
                    text = ''  # Очищення після Enter
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    gameDisplay.fill((colors.White))
    split_the_line("You are given an integer between 1 and 100 (inclusive). \n        You have 10 attempts to guess it.")
    txt_surface = font.render(text, True, colors.Black)
    text_condition_print = font_in_box.render(text_condition,True, colors.Gray)
    text_message_print = font.render(text_message, True, colors.Red)
    gameDisplay.blit(text_condition_print, (input_box.x + 10, input_box.y + 10))
    gameDisplay.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    gameDisplay.blit(text_message_print, (WIDTH/7, HEIGHT-100))
    pygame.draw.rect(gameDisplay, color, input_box, 2)
    pygame.display.update()
    clock.tick(FPS)

