"""
Tetris (pygame)
----------------
Керування:
  ← →  : рух фігури
  ↓    : м'яке падіння (soft drop)
  ↑ / X: обертати за год. стрілкою (CW)
  Z    : обертати проти год. стрілки (CCW)
  Пробіл: жорстке падіння (hard drop)
  C    : утримання (hold)
  P    : пауза
  Esc  : вихід
"""
from __future__ import annotations

import sys
import random
import pygame
from typing import List, Tuple, Optional

# === Константи гри ===
GRID_W, GRID_H = 10, 20
TILE = 30
MARGIN = 20
SIDE_PANEL = 220
WIN_W = GRID_W * TILE + SIDE_PANEL + MARGIN * 3
WIN_H = GRID_H * TILE + MARGIN * 2

FPS = 60
BASE_FALL_MS = 800  # базовий інтервал падіння на 1 рівні
MIN_FALL_MS = 80
SOFT_DROP_MS = 50

# Очки за лінії (на рівень множиться)
LINE_SCORES = {1: 100, 2: 300, 3: 500, 4: 800}

# Кольори (R,G,B)
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
GREY = (50, 50, 60)
GRID_LINE = (35, 35, 45)

COLORS = {
    'I': (0, 255, 255),    # бірюзовий
    'J': (0, 0, 255),      # синій
    'L': (255, 165, 0),    # помаранчевий
    'O': (255, 255, 0),    # жовтий
    'S': (0, 255, 0),      # зелений
    'T': (160, 32, 240),   # фіолетовий
    'Z': (255, 0, 0),      # червоний
}

# Визначення фігур як 4x4 матриць для кожної ротації (SRS-сумісні форми; спрощені кікси)
SHAPES = {
    'I': [
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
        ],
    ],
    'J': [
        [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0],
        ],
    ],
    'L': [
        [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
        ],
        [
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
    ],
    'O': [
        [
            [1, 1],
            [1, 1],
        ],  # квадрат, ротація не змінює
    ],
    'S': [
        [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 0, 1],
        ],
    ],
    'T': [
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
        ],
    ],
    'Z': [
        [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 0, 1],
            [0, 1, 1],
            [0, 1, 0],
        ],
    ],
}

# Для 'O' фігури ротаційна матриця одна; для інших — циклічна


class Tetromino:
    def __init__(self, kind: str):
        self.kind = kind
        self.rot = 0
        self.shape_set = SHAPES[kind]
        self.color = COLORS[kind]
        # Початкова позиція — зверху по центру (з урахуванням ширини форми)
        w = self.width
        self.x = GRID_W // 2 - w // 2
        self.y = 0
        self.has_held = False  # прапорець, щоб не дозволити подвійний hold в одному ході

    @property
    def matrix(self) -> List[List[int]]:
        return self.shape_set[self.rot]

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        return len(self.matrix)

    def cells(self) -> List[Tuple[int, int]]:
        coords = []
        for j, row in enumerate(self.matrix):
            for i, v in enumerate(row):
                if v:
                    coords.append((self.x + i, self.y + j))
        return coords

    def rotate(self, cw: bool = True):
        if self.kind == 'O':
            return  # квадрат не змінюється
        if cw:
            self.rot = (self.rot + 1) % len(self.shape_set)
        else:
            self.rot = (self.rot - 1) % len(self.shape_set)

    def clone(self) -> 'Tetromino':
        t = Tetromino(self.kind)
        t.rot = self.rot
        t.x = self.x
        t.y = self.y
        return t


class Bag7:
    """Генерує мішок з 7 різних фігур у випадковому порядку."""

    KINDS = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']

    def __init__(self):
        self.queue: List[str] = []
        self._refill()

    def _refill(self):
        bag = self.KINDS[:]
        random.shuffle(bag)
        self.queue.extend(bag)

    def next(self) -> Tetromino:
        if len(self.queue) <= 7:
            self._refill()
        return Tetromino(self.queue.pop(0))

    def peek(self, n: int = 5) -> List[str]:
        while len(self.queue) < n:
            self._refill()
        return self.queue[:
]


class Board:
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
        self.grid: List[List[Optional[Tuple[int, int, int]]]] = [
            [None for _ in range(w)] for _ in range(h)
        ]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.w and 0 <= y < self.h

    def collides(self, tet: Tetromino) -> bool:
        for x, y in tet.cells():
            if not self.in_bounds(x, y) or self.grid[y][x] is not None:
                return True
        return False

    def lock(self, tet: Tetromino):
        for x, y in tet.cells():
            if 0 <= y < self.h:
                self.grid[y][x] = tet.color

    def clear_lines(self) -> int:
        new_rows = [row for row in self.grid if any(cell is None for cell in row)]
        cleared = self.h - len(new_rows)
        while len(new_rows) < self.h:
            new_rows.insert(0, [None for _ in range(self.w)])
        self.grid = new_rows
        return cleared


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris (pygame)")
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 22)
        self.font_big = pygame.font.SysFont("consolas", 28, bold=True)

        self.board = Board(GRID_W, GRID_H)
        self.bag = Bag7()
        self.current = self.bag.next()
        self.next_preview = self.bag.peek(5)
        self.hold_piece: Optional[Tetromino] = None
        self.can_hold = True

        self.score = 0
        self.level = 1
        self.lines = 0

        self.fall_timer = 0
        self.fall_interval = BASE_FALL_MS
        self.soft_drop = False
        self.paused = False
        self.game_over = False

    # === Ігрова логіка ===
    def level_from_lines(self) -> int:
        # Кожні 10 ліній — новий рівень
        return 1 + self.lines // 10

    def update_fall_interval(self):
        self.level = self.level_from_lines()
        self.fall_interval = max(BASE_FALL_MS - (self.level - 1) * 60, MIN_FALL_MS)

    def try_move(self, dx: int, dy: int) -> bool:
        if self.game_over or self.paused:
            return False
        clone = self.current.clone()
        clone.x += dx
        clone.y += dy
        if not self.board.collides(clone):
            self.current = clone
            return True
        return False

    def try_rotate(self, cw: bool = True) -> bool:
        if self.game_over or self.paused:
            return False
        clone = self.current.clone()
        clone.rotate(cw)
        # Простий набір кіксів (спроби зсуву)
        kicks = [(0, 0), (-1, 0), (1, 0), (-2, 0), (2, 0), (0, -1)]
        if clone.kind == 'I':
            kicks = [(0, 0), (-2, 0), (2, 0), (-1, 0), (1, 0), (0, -1)]
        for dx, dy in kicks:
            test = clone.clone()
            test.x += dx
            test.y += dy
            if not self.board.collides(test):
                self.current = test
                return True
        return False

    def hard_drop(self):
        if self.game_over or self.paused:
            return
        dist = 0
        while self.try_move(0, 1):
            dist += 1
        self.score += dist * 2  # очки за hard drop
        self.lock_current()

    def soft_step(self):
        # один крок м'якого падіння: якщо можемо — рух вниз і +1 бал
        moved = self.try_move(0, 1)
        if moved:
            self.score += 1
        else:
            self.lock_current()

    def lock_current(self):
        self.board.lock(self.current)
        cleared = self.board.clear_lines()
        if cleared:
            self.lines += cleared
            self.score += LINE_SCORES.get(cleared, 0) * self.level
            self.update_fall_interval()
        self.spawn_next()

    def spawn_next(self):
        self.current = self.bag.next()
        self.next_preview = self.bag.peek(5)
        self.can_hold = True
        # Якщо одразу колізія — програш
        if self.board.collides(self.current):
            self.game_over = True

    def hold(self):
        if not self.can_hold or self.game_over or self.paused:
            return
        self.can_hold = False
        if self.hold_piece is None:
            self.hold_piece = Tetromino(self.current.kind)
            self.current = self.bag.next()
            self.next_preview = self.bag.peek(5)
        else:
            self.hold_piece, self.current = Tetromino(self.current.kind), Tetromino(self.hold_piece.kind)
        # Скидаємо позицію поточної фігури після hold
        w = self.current.width
        self.current.x = GRID_W // 2 - w // 2
        self.current.y = 0
        if self.board.collides(self.current):
            self.game_over = True

    # === Рендер ===
    def draw_cell(self, x: int, y: int, color: Tuple[int, int, int]):
        ox = MARGIN
        oy = MARGIN
        rect = pygame.Rect(ox + x * TILE, oy + y * TILE, TILE, TILE)
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, GRID_LINE, rect, 2)

    def draw_grid(self):
        # фон і сітка
        self.screen.fill(GREY)
        # Область ігрового поля
        field_rect = pygame.Rect(MARGIN, MARGIN, GRID_W * TILE, GRID_H * TILE)
        pygame.draw.rect(self.screen, (20, 20, 28), field_rect)
        for y in range(GRID_H):
            for x in range(GRID_W):
                if self.board.grid[y][x] is not None:
                    self.draw_cell(x, y, self.board.grid[y][x])
        # Поточна фігура
        if not self.game_over:
            for x, y in self.current.cells():
                if y >= 0:
                    self.draw_cell(x, y, self.current.color)
        # Сітка ліній
        for x in range(GRID_W + 1):
            X = MARGIN + x * TILE
            pygame.draw.line(self.screen, GRID_LINE, (X, MARGIN), (X, MARGIN + GRID_H * TILE), 1)
        for y in range(GRID_H + 1):
            Y = MARGIN + y * TILE
            pygame.draw.line(self.screen, GRID_LINE, (MARGIN, Y), (MARGIN + GRID_W * TILE, Y), 1)

    def draw_panel(self):
        panel_x = MARGIN * 2 + GRID_W * TILE
        # Текстова інформація
        def blit_text(text: str, y: int, big: bool = False):
            surf = (self.font_big if big else self.font).render(text, True, WHITE)
            self.screen.blit(surf, (panel_x, y))

        blit_text("TETRIS", MARGIN, big=True)
        blit_text(f"Рівень: {self.level}", MARGIN + 50)
        blit_text(f"Рахунок: {self.score}", MARGIN + 80)
        blit_text(f"Лінії: {self.lines}", MARGIN + 110)

        # Попередній перегляд наступних
        y0 = MARGIN + 160
        blit_text("Далі:", y0)
        self.draw_preview(self.next_preview, panel_x, y0 + 25)

        # Hold
        y1 = y0 + 25 + 5 * TILE + 30
        blit_text("Hold:", y1)
        self.draw_hold(panel_x, y1 + 25)

        # Підказки
        y2 = y1 + 25 + 5 * TILE + 40
        tips = [
            "←/→: рух",
            "↓: soft drop",
            "↑/X: обертати",
            "Z: обертати CCW",
            "Space: hard drop",
            "C: hold",
            "P: пауза",
        ]
        for i, tip in enumerate(tips):
            blit_text(tip, y2 + i * 22)

    def draw_preview(self, kinds: List[str], px: int, py: int):
        box = pygame.Rect(px, py, 5 * TILE, 5 * TILE)
        pygame.draw.rect(self.screen, (25, 25, 35), box)
        pygame.draw.rect(self.screen, GRID_LINE, box, 2)
        # малюємо перших 5 у стопчик
        for idx, kind in enumerate(kinds[:5]):
            self.draw_mini_piece(kind, px + TILE // 2, py + TILE // 2 + idx * (TILE + 10))

    def draw_hold(self, px: int, py: int):
        box = pygame.Rect(px, py, 5 * TILE, 5 * TILE)
        pygame.draw.rect(self.screen, (25, 25, 35), box)
        pygame.draw.rect(self.screen, GRID_LINE, box, 2)
        if self.hold_piece:
            self.draw_mini_piece(self.hold_piece.kind, px + TILE // 2, py + TILE // 2)

    def draw_mini_piece(self, kind: str, px: int, py: int):
        mat = SHAPES[kind][0]
        color = COLORS[kind]
        # центруємо в 4x4 області
        mat_h = len(mat)
        mat_w = len(mat[0])
        for j in range(mat_h):
            for i in range(mat_w):
                if mat[j][i]:
                    rx = px + i * (TILE // 2)
                    ry = py + j * (TILE // 2)
                    rect = pygame.Rect(rx, ry, TILE // 2, TILE // 2)
                    pygame.draw.rect(self.screen, color, rect)
                    pygame.draw.rect(self.screen, GRID_LINE, rect, 1)

    # === Головний цикл ===
    def run(self):
        while True:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)
                    if event.key == pygame.K_p:
                        if not self.game_over:
                            self.paused = not self.paused
                    if self.game_over:
                        continue
                    if not self.paused:
                        if event.key in (pygame.K_UP, pygame.K_x):
                            self.try_rotate(cw=True)
                        elif event.key == pygame.K_z:
                            self.try_rotate(cw=False)
                        elif event.key == pygame.K_LEFT:
                            self.try_move(-1, 0)
                        elif event.key == pygame.K_RIGHT:
                            self.try_move(1, 0)
                        elif event.key == pygame.K_DOWN:
                            self.soft_step()
                        elif event.key == pygame.K_SPACE:
                            self.hard_drop()
                        elif event.key == pygame.K_c:
                            self.hold()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.soft_drop = False

            keys = pygame.key.get_pressed()
            # Безперервний soft drop при утриманні ↓
            if not self.paused and not self.game_over and keys[pygame.K_DOWN]:
                self.soft_drop = True
            else:
                self.soft_drop = False

            if not self.paused and not self.game_over:
                self.fall_timer += dt
                interval = SOFT_DROP_MS if self.soft_drop else self.fall_interval
                if self.fall_timer >= interval:
                    self.fall_timer = 0
                    if not self.try_move(0, 1):
                        # якщо не можемо падати — фіксуємо
                        self.lock_current()

            # Рендер
            self.draw_grid()
            self.draw_panel()

            if self.paused:
                self.draw_center_message("Пауза (P)")
            if self.game_over:
                self.draw_center_message("Гру завершено. Esc — вихід")

            pygame.display.flip()

    def draw_center_message(self, text: str):
        overlay = pygame.Surface((GRID_W * TILE, GRID_H * TILE), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        self.screen.blit(overlay, (MARGIN, MARGIN))
        surf = self.font_big.render(text, True, WHITE)
        rect = surf.get_rect(center=(MARGIN + GRID_W * TILE // 2, MARGIN + GRID_H * TILE // 2))
        self.screen.blit(surf, rect)


def main():
    try:
        Game().run()
    except Exception as e:
        # Безпечне завершення з виводом помилки в консоль
        print("[FATAL]", e, file=sys.stderr)
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()
