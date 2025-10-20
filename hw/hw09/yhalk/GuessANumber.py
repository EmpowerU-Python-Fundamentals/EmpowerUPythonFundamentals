import pygame
import pygame_gui
import Colors
import random

pygame.init()

width=600
height=600
screen = pygame.display.set_mode((width, height))
manager = pygame_gui.UIManager((width, height))

font = pygame.font.SysFont('Calibri', 14, True, False)
font1 = pygame.font.SysFont('Calibri', 20, True, False)

input_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((height/4, width/3), (width/2, 40)),
                                                  manager=manager)
6
user_text=""
message=""

attempts = 0

i = random.randint(1,100)
print(i)
input_field.get_text() #"""щоб встановити —""" 
print(input_field.get_text())

clock = pygame.time.Clock()
running = True
running1= True
while running:
    time_delta = clock.tick(60) / 1000.0
    manager.update(time_delta)
    screen.fill((Colors.Yellow))
    text1 = font.render(f"Відгадайте число від 1 до 100) У вас 10 спроб)",True,Colors.Blue)
    text2 = font.render(f"Введіть його та натисніть кнопку Enter!",True,Colors.Blue)
    screen.blit(text1,(height/4,width/6))
    screen.blit(text2,(height/4,width/5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == input_field:
                    try:
                        user_text = int(input_field.get_text())
                    except ValueError:
                        message = "Курва йоп твою мать, це не число"
                        continue
                    if user_text == i:
                        message = f"Вітаємо!!! Це число {i}"
                        pygame.time.delay(1000)
                        running = False
                    elif user_text < i:
                        message = "Ваше число менше за загадане"
                        attempts+=1
                    elif user_text > i:
                        message = "Ваше число більше за загадане"
                        attempts+=1
                    if attempts == 9:
                        message = "Нажаль Ви невідгадали((("
                    elif attempts > 9:
                        running = False
                    print(f"attempt {attempts}")
                input_field.set_text("")
                        
    text3 = font.render(f"{user_text}",True,Colors.Blue)
    screen.blit(text3,(height/4,width/4))
    text4 = font1.render(f"{message}",True,Colors.Red)
    screen.blit(text4,(height/4,width/2))
    manager.draw_ui(screen)
    pygame.display.update()

while running1:
    time_delta = clock.tick(60) / 1000.0
    manager.update(time_delta)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running1 = False

pygame.quit()
