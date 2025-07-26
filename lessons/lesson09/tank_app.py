import pygame
import colors
pygame.init()

width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Tank game")
font = pygame.font.SysFont('Calibri', 100, True, False)

clock = pygame.time.Clock()
FPS = 60

done = False
draw = True
TANK = {
    "pos": [width/10, height/2],
    "width":40,
    "height":30,
    "shots": [],
    "shots_step": 20
}

TARGET = {
    "pos": [width - width/10, height/2],
    "radius": 30,
    "step": 5
}

def calculate_distance(point1, point2):

    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    
while not done:
# --- Main event loop
    # print("="*60)
    for event in pygame.event.get(): # User did something\
        # print(event)
        if event.type == pygame.QUIT:
            done = True # Flag that we are done so we exit this loop
            # print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:

            match event.dict["key"]:
                case 1073741906:
                    TANK["pos"][1] -= 5
                case 1073741903:
                    TANK["pos"][0] += 5
                case 1073741905:
                    TANK["pos"][1] += 5
                case 1073741904:
                    TANK["pos"][0] -= 5
                case 32:
                    TANK["shots"].append([TANK["pos"][0]+TANK["width"],
                                                  TANK["pos"][1]+TANK["height"]/2-3])
            # print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            # print("User let go of a key.")
            pass
   
                        




# --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # --- Go ahead and update the screen with what we've drawn.
    
    if draw:
        gameDisplay.fill(colors.White)
        pygame.draw.rect(gameDisplay, colors.Olive, [*TANK["pos"],TANK["width"],TANK["height"]])
        pygame.draw.rect(gameDisplay, colors.Olive, [TANK["pos"][0]+TANK["width"],
                                                    TANK["pos"][1]+TANK["height"]/2-3,
                                                    10, 5])

        if TARGET["pos"][1]+ TARGET["radius"] > height:
            TARGET["step"] *= -1
        elif TARGET["pos"][1]- TARGET["radius"] < 0:
            TARGET["step"] *= -1
        TARGET["pos"][1] += TARGET["step"] 
        for shot in TANK["shots"]:
            shot[0] += TANK["shots_step"]
            pygame.draw.circle(gameDisplay, colors.Black, shot, 3)

        pygame.draw.circle(gameDisplay, colors.Red, TARGET["pos"], TARGET["radius"])

        for shot in TANK["shots"]:
            d = calculate_distance(shot, TARGET["pos"])
            if d < TARGET["radius"]:
                text = font.render(f"WIN!!!",True,colors.Fuchsia)
                gameDisplay.blit(text, ( width/2, height/2))
                draw = False
                break
        

    pygame.display.update()
    # print(POINTS)
# --- Limit to 60 frames per second
    clock.tick(FPS)


print("end game")