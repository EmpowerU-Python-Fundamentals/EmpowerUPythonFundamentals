import pygame
import random
import colors
import time
pygame.init()

player1 = input("What's the first players name ")
player2 = input("What's the second players name ")

width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("tennis")
clock = pygame.time.Clock()

done = False

square1 = pygame.Surface((35, 100))
square1.fill(colors.Black)
square2 = pygame.Surface((35, 100))
square2.fill(colors.Black)

g = 400  
h = 300  
speed_g, speed_h = 5, 5

Font = pygame.font.Font("Fonts/RobotoMono-MediumItalic.ttf", 25)
first_name = Font.render(player1, True, colors.Teal)
second_name = Font.render(player2, True, colors.Teal)
win1 = Font.render(player1 + " Win", True, colors.Silver)
win2 = Font.render(player2 + " Win", True, colors.Silver)
Start=Font.render("Game start in 3 2 1 " , True, colors.White)
stook_sound = pygame.mixer.Sound("Sounds/mixkit-game-ball-tap-2073.wav")

gameDisplay.blit(Start, (300, 300))
pygame.display.update()

circle_speed = 5



y = 0      
a = 0      

time.sleep(3)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            
            match event.key:
                case 1073741906:
                    y -= 70
                    if y < 0:
                        y = 0
                case 1073741905:
                    y += 70
                    if y > height - 100:
                        y = height - 100
                case 119:
                    a -= 70
                    if a < 0:
                        a = 0
                case 115:
                    a += 70
                    if a > height - 100:
                        a = height - 100

    g += speed_g
    h += speed_h

    
    if h <= 0 or h >= height - 35:
        speed_h = -speed_h

   
    if g <= 55 and a <= h <= a + 100:
        speed_g = -speed_g
        pygame.mixer.Sound.play(stook_sound)
        g = 55

    
    if g >= width - 55 - 35 and y <= h <= y + 100:
        speed_g = -speed_g
        pygame.mixer.Sound.play(stook_sound)
        g = width - 55 - 35

    
    if g < 0 :
        gameDisplay.fill(colors.White)
        gameDisplay.blit(win2, (300, 300))
        pygame.display.update()
        pygame.time.delay(3000)
        done = True
        
    if g > width:
        gameDisplay.fill(colors.White)
        gameDisplay.blit(win1, (300, 300))
        pygame.display.update()
        pygame.time.delay(3000)
        done = True
        



    gameDisplay.fill(colors.White)
    gameDisplay.blit(square1, (20, a))
    gameDisplay.blit(square2, (width - 55, y))

    gameDisplay.blit(first_name, (100, 540))
    gameDisplay.blit(second_name, (630, 540))

    pygame.draw.circle(gameDisplay, colors.Red, (g, h), 35)

    pygame.display.update()
    clock.tick(60)
#g, h = width // 2, height // 2
        #speed_g = random.choice([-circle_speed, circle_speed])
        #speed_h = random.choice([-circle_speed, circle_speed])