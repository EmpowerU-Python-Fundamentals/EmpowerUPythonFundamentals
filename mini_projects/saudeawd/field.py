"""functional"""
import random
import pygame

def is_valid(board, row, col, num):
    """checks if board is valid"""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    """solves the board by placing numbers"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1,10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    """generates the full board"""
    board = [[0]*9 for _ in range(9)]
    solve(board)
    return board

class Field:
    """class field"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = self.width/3
        self.font = pygame.font.SysFont(None, 60)

    def draw_field(self, screen):
        """draw the skeleton of the field"""
        text1 = self.font.render('Sudoku', True, (22, 33, 128))
        screen.blit(text1, (self.x+170, self.y-70))
        for i in range(9):
            pos_x = self.x + (self.gap/3) * (i+1)
            pos_y = self.y + (self.gap/3) * (i+1)
            pygame.draw.line(screen, (192,192,192), (pos_x, self.y), (pos_x, self.y + self.width), 3)
            pygame.draw.line(screen, (192,192,192), (self.x, pos_y), (self.x + self.width, pos_y), 3)
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        for i in range(2):
            pos_x = self.x + self.gap * (i+1)
            pos_y = self.y + self.gap * (i+1)
            pygame.draw.line(screen, (0, 0, 0), (pos_x, self.y), (pos_x, self.y + self.width), 3)
            pygame.draw.line(screen, (0, 0, 0), (self.x, pos_y), (self.x + self.width, pos_y), 3)

class FilledField:
    """class filling the field"""
    def __init__(self, board, x, y, width, height):
        self.board = board
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_size = width // 9
        self.font = pygame.font.SysFont(None, self.cell_size)
        self.original_numbers = [[num != 0 for num in row] for row in board]
        self.user_numbers = [[0]*9 for _ in range(9)]  # track user-placed numbers separately
        self.mistakes = 0

    def draw_numbers(self, screen):
        """drawing numbers in each cell"""
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                if num != 0:
                    if self.original_numbers[row][col]:
                        color = (0, 0, 0)
                    elif self.user_numbers[row][col] == num and\
                          self.is_correct_placement(row, col, num):
                        color = (22, 33, 128)
                    else:
                        color = (255, 0, 0)

                    text = self.font.render(str(num), True, color)
                    pos_x = (self.x + col * self.cell_size + self.cell_size // 3)+4
                    pos_y = (self.y + row * self.cell_size + self.cell_size // 6)+6
                    screen.blit(text, (pos_x, pos_y))

    def is_correct_placement(self, row, col, num):
        """checks if number`s placement is correct"""
        for i in range(9):
            if i != col and self.board[row][i] == num:
                return False
        for i in range(9):
            if i != row and self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if (start_row + i != row or start_col + j != col) and\
                      self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def random_pop(self, num):
        """pops random numbers to create the puzzle of sudoku"""
        for row in range(9):
            for col in range(9):
                if random.choice([True, False]):
                    self.board[row][col] = 0
        self.original_numbers = [[num != 0 for num in row] for row in self.board]

    def handle_click(self, pos, selected_number):
        """handling click"""
        if (self.x <= pos[0] <= self.x + self.width and
            self.y <= pos[1] <= self.y + self.height):
            col = int((pos[0] - self.x) // self.cell_size)
            row = int((pos[1] - self.y) // self.cell_size)

            if not self.original_numbers[row][col]:
                if selected_number is not None:
                    prev_num = self.board[row][col]
                    self.board[row][col] = selected_number
                    self.user_numbers[row][col] = selected_number

                    if not self.is_correct_placement(row, col, selected_number):
                        self.mistakes += 1
                        return False
                    return True
                else:
                    self.board[row][col] = 0
                    self.user_numbers[row][col] = 0
                    return True
        return False

    def is_board_full(self):
        """checks if the board is full"""
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True


class NumbersBelow:
    """class for numbers buttons below"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = 60
        self.font = pygame.font.SysFont(None, int(self.height * 0.9))
        self.eraser_width = 25
        self.eraser_height = 12
        self.selected_number = None
        self.rects = []
        self.eraser_rect = None
        self.eraser_selected = False

    def draw_rectangles(self, screen):
        """drawing buttons rectangles for numbers in it,
          and hendling if button is selected or not"""
        self.rects = []
        for i in range(1, 10):
            pos_x = self.x + self.gap * (i+1)
            rect = pygame.Rect(pos_x, self.y, self.width, self.height)
            self.rects.append((i, rect))

            #draw with blue border if selected
            border_color = (0, 183, 255) if self.selected_number == i else (0, 0, 0)
            pygame.draw.rect(screen, border_color, rect, 3)

            text = self.font.render(str(i), True, (22, 33, 128))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

            if i == 3:
                position_x = pos_x-10
                position_y = self.y- 80
                self.eraser_rect = pygame.Rect(position_x, position_y, self.width, self.height)

                #draw eraser with blue border if selected
                eraser_border = (0, 183, 255) if self.eraser_selected else (0, 0, 0)
                pygame.draw.rect(screen, eraser_border, self.eraser_rect, 3)

                eraser_x = position_x + (self.width - self.eraser_width) / 2
                eraser_y = position_y + (self.height - self.eraser_height) / 2
                pygame.draw.rect(screen, (22, 33, 128),\
                                  (eraser_x, eraser_y, self.eraser_width, self.eraser_height), 2)
                pygame.draw.line(screen, (22, 33, 128), (eraser_x+7, eraser_y),\
                                  (eraser_x+7, eraser_y+10), 2)

    def handle_click(self, pos):
        """handling click"""
        if self.eraser_rect and self.eraser_rect.collidepoint(pos):
            self.selected_number = None
            self.eraser_selected = True
            return None

        for num, rect in self.rects:
            if rect.collidepoint(pos):
                self.selected_number = num
                self.eraser_selected = False
                return num
        return None


class MistakeErase:
    """class for erasing mistakes"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gap = 100
        self.font = pygame.font.SysFont(None, 40)

    def draw_erase(self, screen):
        """drawing the eraser"""
        text = self.font.render('Erase: ', True, (22, 33, 128))
        screen.blit(text, (self.x, self.y))

    def draw_mistakes(self, screen, mistakes):
        """drawing counter for mistakes"""
        text1 = self.font.render(f'Mistakes: {mistakes}/3', True,\
                                  (255, 0, 0) if mistakes > 0 else (22, 33, 128))
        screen.blit(text1, (self.x+self.gap, self.y+self.gap))
