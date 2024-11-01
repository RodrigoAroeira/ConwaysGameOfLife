from dataclasses import dataclass

import pygame

from constants import BLACK, HEIGHT, SQUARE_SIZE, WHITE, WIDTH
from helpers import genRandomGrid


@dataclass
class ConwayGrid:

    rows: int
    cols: int

    def __post_init__(self) -> None:
        self.make_new_grid()

    def make_new_grid(self) -> None:
        self.grid = genRandomGrid(self.rows, self.cols)

    def countNeighbors(self, x: int, y: int) -> int:
        count = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                if (i, j) == (0, 0):
                    continue
                nx, ny = x + i, y + j

                if nx in range(self.rows) and ny in range(self.cols):
                    count += self.grid[nx][ny]

        return count

    def update_grid(self) -> None:
        new_grid = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):

                neighbours = self.countNeighbors(i, j)
                alive = self.grid[i][j]

                if not alive and neighbours == 3:
                    new_grid[i][j] = True
                elif alive and (neighbours < 2 or neighbours >= 4):
                    new_grid[i][j] = False
                else:
                    new_grid[i][j] = alive

        self.grid = new_grid

    @staticmethod
    def draw_grid(win: pygame.Surface) -> None:
        for x in range(0, WIDTH, SQUARE_SIZE):
            pygame.draw.line(win, BLACK, (x, 0), (x, HEIGHT))  # Vertical lines
        for y in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.line(win, BLACK, (0, y), (WIDTH, y))  # Horizontal lines

    def draw(self, win: pygame.Surface) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                alive = self.grid[i][j]
                color = WHITE if alive else BLACK
                pygame.draw.rect(
                    win,
                    color,
                    (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )
        self.draw_grid(win)

    def invert(self, x: int, y: int) -> None:
        x //= SQUARE_SIZE
        y //= SQUARE_SIZE
        self.grid[x][y] = not self.grid[x][y]
