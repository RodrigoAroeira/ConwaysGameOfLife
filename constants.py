import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = HEIGHT = 1000

ROWS = COLS = WIDTH // 20 if not sys.argv[1:] else int(sys.argv[1])


SQUARE_SIZE = WIDTH // COLS
