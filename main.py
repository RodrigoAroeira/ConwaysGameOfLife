from constants import WIDTH, HEIGHT, ROWS, COLS
import pygame

from grid import ConwayGrid

ROOT = pygame.display.set_mode((WIDTH, HEIGHT))


def loop():

    grid = ConwayGrid(ROWS, COLS)
    running = True
    clock = pygame.time.Clock()

    fps = 30

    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

                case pygame.KEYDOWN:

                    match event.key:
                        case pygame.K_r:
                            grid.make_new_grid()
                        case pygame.K_q:
                            running = False

                case pygame.MOUSEWHEEL:
                    fps = max((1, fps + event.y))  # ensures min of 1 fps

                case pygame.MOUSEBUTTONDOWN:
                    if event.button != 1:
                        continue
                    x, y = map(int, pygame.mouse.get_pos())
                    grid.invert(x, y)

        grid.draw(ROOT)
        grid.update_grid()
        pygame.display.update()


if __name__ == "__main__":
    loop()
