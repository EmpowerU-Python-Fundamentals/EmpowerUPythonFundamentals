import pygame
import colors
pygame.init()

width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("My first game")
font = pygame.font.SysFont('Calibri', 25, True, False)

clock = pygame.time.Clock()
FPS = 30

done = False

POINTS = []

while not done:
# --- Main event loop
    # print("="*60)
    for event in pygame.event.get(): # User did something\
        # print(event)
        if event.type == pygame.QUIT:
            done = True # Flag that we are done so we exit this loop
            # print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            pass
            # print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            # print("User let go of a key.")
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print("User pressed a mouse button")
            print(event)
            mouse_event = event.dict
            if mouse_event["button"] == 1 :
                if not POINTS:
                    POINTS.append(mouse_event["pos"]) 
                else:
                    if POINTS[-1] != mouse_event["pos"]:
                        POINTS.append(mouse_event["pos"])
            if mouse_event["button"] == 3 :
                POINTS.pop()
                        




# --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    gameDisplay.fill(colors.White)
    # --- Go ahead and update the screen with what we've drawn.
    if len(POINTS) > 2:
        pygame.draw.polygon(gameDisplay, ((len(POINTS)*20)%255,(len(POINTS)*10)%255,(len(POINTS)*30)%255), POINTS, width=0)
    for point in POINTS:
        pygame.draw.circle(gameDisplay, colors.Red, point, 5, width=0)
        text = font.render(f"{point}",True,colors.Black)
        gameDisplay.blit(text, (point[0]-45, point[1]-30))



    pygame.display.update()
    # print(POINTS)
# --- Limit to 60 frames per second
    clock.tick(FPS)


print("end game")