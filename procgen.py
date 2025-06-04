"""
Very simple procgen plant sim
June 2025
"""
import pygame
import random

# Grid and window settings
WIDTH, HEIGHT = 600, 600
GRID_SPACING = 50
LINE_COLOR = (0, 0, 0)  # Black
BG_COLOR = (255, 255, 255)  # White


#
# Logic
#

def neighbours(x, y):
    result = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            coord = (x + i, y + j)
            if not coord == (x, y):
                result.append(coord)
    return result


class World:
    def __init__(self, x_size, y_size):
        self.grid = [[None for x in range(x_size)] for y in range(y_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.base = 0

    def iter_world(self):
        for i in range(x_size):
            for j in range(y_size):
                yield(i, j, self.grid[i][j])

    def is_empty(self, x, y):
        return not self.grid[i][j]

    def add_plant(self, plant):
        """Make sure all cells of plant are reg'd in grid"""
        for x, y in plant.cells:
            self.grid[x][y] = 1


class Plant:
    def __init__(self, init_x):
        self.cells = [(init_x, 0)]

    def get_neighbouring_cells(self, world):
        for x, y in self.cells:
            if grid[x][y]:
                pass


def make_world(x_size, y_size):
    return [[0 for x in range(x_size)] for y in range(y_size)]


def populate(world, n):
    """Place some random cells"""
    wx = len(world)
    wy = len(world[0])
    coords = [(random.randint(0, wy - 1), random.randint(0, wx - 1)) for i in range(n)]
    for x, y in coords:
        world[x][y] = 1

def plant(world):
    """Place 1st cell at base"""
    world[6][11] = 1

def iter_world(world):
    wx = len(world)
    wy = len(world[0])
    for row in range(wy):
        for col in range(wx):
            yield (row, col, world[row][col])

def grow_step(world):
    # get potential growth posns by filtering
    pass

#
# Display
#

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame 2D Grid")

    world = make_world(int(WIDTH / GRID_SPACING), int(HEIGHT / GRID_SPACING))
    plant(world)
    print(world)

    print(neighbours(1,1))
    
    # Main loop
    running = True
    while running:
        screen.fill(BG_COLOR)

        # Draw vertical lines
        for x in range(0, WIDTH + 1, GRID_SPACING):
            pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, HEIGHT), 1)

        # Draw horizontal lines
        for y in range(0, HEIGHT + 1, GRID_SPACING):
            pygame.draw.line(screen, LINE_COLOR, (0, y), (WIDTH, y), 1)

        # Draw cells
        for x, y, el in iter_world(world):
            if el == 1:
                pygame.draw.rect(screen, (255, 0, 0), (x * GRID_SPACING, y * GRID_SPACING, GRID_SPACING, GRID_SPACING))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
