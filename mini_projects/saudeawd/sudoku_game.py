"""main game"""
import pygame
from field import Field, generate_full_board, FilledField, NumbersBelow, MistakeErase

pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 183, 255)

START_X = 50
START_Y = 100
FILED_WIDTH = 500
FIELD_HEIGHT = 500
GAP = FILED_WIDTH/3

field = Field(START_X, START_Y, FILED_WIDTH, FIELD_HEIGHT)
board = generate_full_board()
filled_field = FilledField(board, START_X, START_Y, FILED_WIDTH, FIELD_HEIGHT)
filled_field.random_pop(40)

numbers_below = NumbersBelow(-85, 700, FILED_WIDTH/10, FIELD_HEIGHT/10)
ers = MistakeErase(50, 630)
mistk = MistakeErase(285, 530)

GAME_OVER = False
WIN = False
RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER and not WIN:
            pos = event.pos
            selected_num = numbers_below.handle_click(pos)

            if selected_num is None and not numbers_below.eraser_selected:
                filled_field.handle_click(pos, numbers_below.selected_number)
            elif numbers_below.eraser_selected:
                filled_field.handle_click(pos, None)

            #check if board is full and correct after each move
            if filled_field.is_board_full() and filled_field.mistakes < 3:
                ALL_CORRECT = True
                for row in range(9):
                    for col in range(9):
                        if not filled_field.original_numbers[row][col]:
                            num = filled_field.board[row][col]
                            if not filled_field.is_correct_placement(row, col, num):
                                ALL_CORRECT = False
                                break
                    if not ALL_CORRECT:
                        break
                if ALL_CORRECT:
                    WIN = True
    screen.fill(WHITE)

    field.draw_field(screen)
    filled_field.draw_numbers(screen)
    numbers_below.draw_rectangles(screen)
    ers.draw_erase(screen)
    mistk.draw_mistakes(screen, filled_field.mistakes)

    if filled_field.mistakes >= 3:
        font = pygame.font.SysFont(None, 72)
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        RUN = False
    if WIN:
        font = pygame.font.SysFont(None, 72)
        text = font.render("Congratulations!", True, (2, 89, 6))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        RUN = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
