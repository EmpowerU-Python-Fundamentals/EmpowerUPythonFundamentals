import pygame
import sys
from core import GuessGame

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 640, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎯 Guess the Number (Meme Edition)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 24)

# --- Game state ---
game = GuessGame()
input_text = ""

# --- Helpers ---
def draw_centered_text(text, y, color=(255, 255, 255)):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        render = font.render(line, True, color)
        rect = render.get_rect(center=(WIDTH // 2, y + i * 30))
        screen.blit(render, rect)

# --- Main loop ---
running = True
while running:
    screen.fill((20, 20, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif not game.over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    game.guess(int(input_text))
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.unicode.isdigit():
                input_text += event.unicode

        elif game.over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()
                input_text = ""

    # --- Draw ---
    draw_centered_text("🕹 Guess the Number Game", 40)
    draw_centered_text(game.message, 120)

    if not game.over:
        draw_centered_text(f"👉 Your guess: {input_text}", 200)
    else:
        draw_centered_text("🔁 Press R to play again", 300)
        draw_centered_text("🛑 Press ESC to exit", 330)

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
